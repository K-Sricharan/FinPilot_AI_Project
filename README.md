# 🤖 FinPilot AI – Tax Planning AI Agent

An end-to-end **AI-powered Tax Planning Assistant** built using **LangGraph, Retrieval-Augmented Generation (RAG), NVIDIA AI Endpoints, FAISS, LangChain, and Streamlit**.

FinPilot AI helps users understand Indian income tax regulations, compare tax regimes, calculate taxes accurately, and explain tax concepts in simple language by combining the reasoning capabilities of Large Language Models with deterministic Python tools and Retrieval-Augmented Generation (RAG).

The primary goal of this project is to understand and implement every core component involved in building a production-ready AI Agent from scratch.

---

# 🚀 Features

FinPilot AI can:

- 🤖 Answer Indian Income Tax questions
- 📚 Retrieve tax regulations using RAG
- 🔎 Search tax documents using FAISS Vector Database
- 🧮 Calculate income tax accurately using deterministic Python tools
- 💰 Compare Old vs New Tax Regime
- 🏠 Calculate HRA Exemption
- 📄 Explain Sections 80C and 80D
- 📊 Apply tax deductions and exemptions
- 💬 Generate human-friendly responses using NVIDIA-hosted LLMs
- 🧠 Use LangGraph ReAct Agent for intelligent tool selection
- 💻 Interactive chat interface built with Streamlit

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
              Streamlit Frontend
                      │
                      ▼
             LangGraph ReAct Agent
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
    RAG Search Tool        Tax Calculator Tool
          │                       │
          ▼                       ▼
   FAISS Vector Store      Python Business Logic
          │                       │
          └───────────┬───────────┘
                      ▼
              NVIDIA Hosted LLM
                      │
                      ▼
         Natural Language Response
```

---

# ⚙️ Tech Stack

### AI Frameworks

- LangGraph
- LangChain

### Large Language Model

- NVIDIA AI Endpoints
- Google DiffusionGemma *(Current Model)*
- *(Can be replaced with Llama, Nemotron, Mistral, etc.)*

### RAG Pipeline

- NVIDIA Embeddings
- FAISS Vector Database
- PyPDF Loader
- Recursive Character Text Splitter

### Backend

- Python

### Frontend

- Streamlit

### Utilities

- python-dotenv
- Dataclasses

---

# 📂 Project Structure

```
Tax Agent
│
├── app.py
├── streamlit_app.py
├── requirements.txt
│
├── Data/
│      hra_rules.pdf
│      section_80c.pdf
│      section_80d.pdf
│      regime_comparison.pdf
│
├── Models/
│      nvidia_llm.py
│
├── Prompts/
│      system_prompt.py
│
├── Rag/
│      retriever.py
│      rag_tool.py
│      LangGraph_agent.py
│
├── Tools/
│      tax_tools.py
│
└── vectorstore/
```

---

# 🔄 Workflow

```
User Question
      │
      ▼
LangGraph ReAct Agent
      │
      ▼
Reasoning by LLM
      │
      ├───────────────┐
      │               │
      ▼               ▼
Need RAG?       Need Calculation?
      │               │
      ▼               ▼
RAG Tool      Tax Calculator Tool
      │               │
      └───────┬───────┘
              ▼
      Tool Results
              │
              ▼
      NVIDIA LLM
              │
              ▼
      Final Response
```

---

# 📌 Current Capabilities

### ✅ Tax Knowledge Retrieval

- Section 80C
- Section 80D
- HRA Rules
- Old Tax Regime
- New Tax Regime

### ✅ Tax Calculations

- Income Tax Calculation
- Old Regime Tax
- New Regime Tax
- HRA Exemption
- Standard Deduction
- Home Loan Interest
- Section 80C Deduction
- Section 80D Deduction
- Health & Education Cess
- Better Tax Regime Recommendation

### ✅ AI Agent

- LangGraph ReAct Agent
- Tool Calling
- Conversation Memory
- RAG Integration
- Multi-turn Conversations

---

# 📅 Development Progress

| Phase | Status |
|--------|--------|
| Phase 0 – Environment Setup | ✅ Completed |
| Phase 1 – NVIDIA LLM Integration | ✅ Completed |
| Phase 2 – Tax Calculation Engine | ✅ Completed |
| Phase 3 – RAG Implementation | ✅ Completed |
| Phase 4 – LangGraph ReAct Agent | ✅ Completed |
| Phase 5 – Tool Calling | ✅ Completed |
| Phase 6 – Streamlit Chat Interface | ✅ Completed |
| Phase 7 – End-to-End Testing | ✅ Completed |
| Phase 8 – Docker Deployment | ⏳ Planned |
| Phase 9 – Cloud Deployment | ⏳ Planned |
| Phase 10 – Production Enhancements | ⏳ Planned |

---

# 🎯 Future Improvements

- Authentication
- User Profiles
- Tax Report Generation (PDF)
- Chat History
- Voice Support
- Multi-Agent Architecture
- MCP Integration
- Cloud Deployment
- Docker Support
- API Version
- Latest Budget Knowledge Base
- Database Integration
- Observability & Logging

---

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

- LangGraph
- LangChain
- AI Agents
- ReAct Agents
- Tool Calling
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embeddings
- Prompt Engineering
- Streamlit
- FAISS
- NVIDIA AI Endpoints
- Production-ready AI Application Architecture

---

# ⭐ Project Vision

FinPilot AI is being developed as a hands-on learning project to understand how modern AI Agents are designed, built, and deployed. Instead of relying solely on Large Language Models, the system combines reasoning, retrieval, and deterministic tools to provide accurate, explainable, and reliable tax assistance.
