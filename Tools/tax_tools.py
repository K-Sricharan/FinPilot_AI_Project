"""
tax_tools.py

Production-ready tax calculation tools for the Tax Planning AI Agent.
FY 2024-25 implementation.
"""

from dataclasses import dataclass, asdict
from typing import Optional
from langchain_core.tools import tool

CESS_RATE = 0.04
STANDARD_DEDUCTION = 50_000


@dataclass
class TaxResult:
    regime: str
    gross_income: float
    total_deductions: float
    taxable_income: float
    tax_before_cess: float
    cess: float
    rebate_87a: float
    final_tax: float


def _apply_slabs(taxable_income: float, slabs):
    tax = 0.0
    for lower, upper, rate in slabs:
        if taxable_income <= lower:
            break
        top = taxable_income if upper is None else min(taxable_income, upper)
        tax += max(0, top - lower) * rate
    return tax

def calculate_80c_deduction(investments: dict) -> float:
    return min(sum(investments.values()) if investments else 0, 150000)


def calculate_80d_deduction(
    self_and_family: float = 0,
    parents: float = 0,
    self_senior: bool = False,
    parents_senior: bool = False,
):
    self_cap = 50000 if self_senior else 25000
    parent_cap = 50000 if parents_senior else 25000
    return min(self_and_family, self_cap) + min(parents, parent_cap)


def calculate_hra(
    basic_salary: float,
    hra_received: float,
    rent_paid: float,
    is_metro: bool = True,
):
    if rent_paid <= 0 or hra_received <= 0:
        return 0.0

    return max(
        0,
        min(
            hra_received,
            max(0, rent_paid - (0.10 * basic_salary)),
            (0.50 if is_metro else 0.40) * basic_salary,
        ),
    )


def calculate_tax_old_regime(
    gross_income: float,
    deduction_80c: float = 0,
    deduction_80d: float = 0,
    hra_exemption: float = 0,
    home_loan_interest: float = 0,
    other_deductions: float = 0,
):
    total_deductions = (
        STANDARD_DEDUCTION
        + min(deduction_80c, 150000)
        + deduction_80d
        + hra_exemption
        + min(home_loan_interest, 200000)
        + other_deductions
    )

    taxable_income = max(0, gross_income - total_deductions)

    slabs = [
        (0, 250000, 0.00),
        (250000, 500000, 0.05),
        (500000, 1000000, 0.20),
        (1000000, None, 0.30),
    ]

    tax = _apply_slabs(taxable_income, slabs)

    rebate = min(tax, 12500) if taxable_income <= 500000 else 0

    tax_after_rebate = max(0, tax - rebate)

    cess = tax_after_rebate * CESS_RATE

    return TaxResult(
        regime="Old Regime",
        gross_income=gross_income,
        total_deductions=round(total_deductions),
        taxable_income=round(taxable_income),
        tax_before_cess=round(tax_after_rebate),
        cess=round(cess),
        rebate_87a=round(rebate),
        final_tax=round(tax_after_rebate + cess),
    )


def calculate_tax_new_regime(
    gross_income: float,
    nps_80ccd2: float = 0,
):
    total_deductions = STANDARD_DEDUCTION + nps_80ccd2

    taxable_income = max(0, gross_income - total_deductions)

    slabs = [
        (0, 300000, 0.00),
        (300000, 600000, 0.05),
        (600000, 900000, 0.10),
        (900000, 1200000, 0.15),
        (1200000, 1500000, 0.20),
        (1500000, None, 0.30),
    ]

    tax = _apply_slabs(taxable_income, slabs)

    rebate = min(tax, 25000) if taxable_income <= 700000 else 0

    tax_after_rebate = max(0, tax - rebate)

    cess = tax_after_rebate * CESS_RATE

    return TaxResult(
        regime="New Regime",
        gross_income=gross_income,
        total_deductions=round(total_deductions),
        taxable_income=round(taxable_income),
        tax_before_cess=round(tax_after_rebate),
        cess=round(cess),
        rebate_87a=round(rebate),
        final_tax=round(tax_after_rebate + cess),
    )


@tool
def compare_tax_regimes(profile: dict) -> dict:
    """
    Compare Old vs New tax regime.

    profile example:
    {
        "gross_income":1800000,
        "basic_salary":900000,
        "hra_received":300000,
        "rent_paid":240000,
        "is_metro":True,
        "investments":{"PPF":50000,"ELSS":100000},
        "medical_self":25000,
        "medical_parents":0,
        "home_loan_interest":200000,
        "other_deductions":0,
        "nps_80ccd2":0
    }
    """

    deduction_80c = calculate_80c_deduction(
        profile.get("investments", {})
    )

    deduction_80d = calculate_80d_deduction(
        self_and_family=profile.get("medical_self", 0),
        parents=profile.get("medical_parents", 0),
        self_senior=profile.get("self_senior", False),
        parents_senior=profile.get("parents_senior", False),
    )

    hra = calculate_hra(
        basic_salary=profile.get("basic_salary", 0),
        hra_received=profile.get("hra_received", 0),
        rent_paid=profile.get("rent_paid", 0),
        is_metro=profile.get("is_metro", True),
    )

    old = calculate_tax_old_regime(
        gross_income=profile["gross_income"],
        deduction_80c=deduction_80c,
        deduction_80d=deduction_80d,
        hra_exemption=hra,
        home_loan_interest=profile.get("home_loan_interest", 0),
        other_deductions=profile.get("other_deductions", 0),
    )

    new = calculate_tax_new_regime(
        gross_income=profile["gross_income"],
        nps_80ccd2=profile.get("nps_80ccd2", 0),
    )

    difference = abs(old.final_tax - new.final_tax)

    if old.final_tax < new.final_tax:
        better = "Old Regime"
    elif new.final_tax < old.final_tax:
        better = "New Regime"
    else:
        better = "Either"

    return {
        "old_regime": asdict(old),
        "new_regime": asdict(new),
        "difference": difference,
        "better_regime": better,
    }


if __name__ == "__main__":
    sample = {
        "gross_income": 1800000,
        "basic_salary": 900000,
        "hra_received": 300000,
        "rent_paid": 240000,
        "is_metro": True,
        "investments": {
            "PPF": 50000,
            "ELSS": 100000,
        },
        "medical_self": 25000,
        "medical_parents": 0,
        "home_loan_interest": 200000,
    }

    from pprint import pprint

    pprint(compare_tax_regimes.invoke({"profile": sample}))
