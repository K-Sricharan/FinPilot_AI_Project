# 🤖 Tax Planning AI Agent

An end-to-end AI-powered Tax Planning Agent built using **LangGraph, RAG, NVIDIA NIM, FAISS, and Streamlit**.

The goal of this project is to build a production-ready AI Agent capable of answering tax-related questions, retrieving tax regulations using Retrieval-Augmented Generation (RAG), performing accurate tax calculations through Python tools, and generating easy-to-understand responses using NVIDIA-hosted Large Language Models.

> 🚀 This project is being built completely from scratch to understand every component involved in modern AI Agent development.

---

# 📌 Project Goals

The Tax Planning AI Agent can:

- 📚 Search tax documents using RAG
- 🧮 Calculate taxes accurately using Python functions
- 💬 Explain tax rules in natural language
- 📄 Compare tax regimes
- 🏠 Calculate HRA
- 💰 Apply deductions like 80C, 80D, etc.
- 🤖 Use NVIDIA-hosted LLMs for reasoning

---

# 🏗️ High-Level Architecture

```

                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
                LangGraph Agent
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
     RAG Search            Tax Calculator
     (FAISS)              (Python Tools)
          │                       │
          └───────────┬───────────┘
                      ▼
              NVIDIA LLM API
        (Llama / Nemotron / Mistral)
                      │
                      ▼
          Easy-to-Understand Answer


---

### One suggestion

Since you're building this as a **learning journey**, I recommend adding a progress tracker. It makes the repository more engaging and shows continuous development.

For example:

```markdown
## 📅 Project Progress

- [x] Phase 0 – Environment Setup
- [ ] Phase 1 – NVIDIA LLM Integration
- [ ] Phase 2 – AI Agent Fundamentals
- [ ] Phase 3 – Tax Calculator
- [ ] Phase 4 – RAG Implementation
- [ ] Phase 5 – LangGraph Workflow
- [ ] Phase 6 – Streamlit UI
- [ ] Phase 7 – Production Enhancements
