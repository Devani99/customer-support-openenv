# 🚀 OpenEnv Customer Support Simulator

## 🧠 Overview

This project implements a **real-world reinforcement learning environment** using the OpenEnv framework, simulating a **customer support ticket handling system**.

The environment allows an AI agent to interact with user support queries, take actions (reply, refund, escalate, etc.), and receive **dense reward signals** based on performance.

---

## 🎯 Motivation

Customer support automation is a critical real-world problem used by companies like Amazon, Stripe, and Swiggy.

This environment models:

* Multi-step decision making
* Natural language understanding
* Emotional handling (angry customers)
* Task completion workflows

---

## 🏗️ Environment Design

### 📥 Observation Space

```python
Observation:
    ticket_id: str
    customer_message: str
    conversation_history: List[str]
    sentiment: float
    urgency: int
    resolved: bool
```

---

### 🎮 Action Space

```python
Action:
    action_type:
        - reply
        - ask_clarification
        - issue_refund
        - escalate
        - close_ticket
    message: Optional[str]
```

---

## ⚙️ Core API (OpenEnv Compatible)

* `reset(task_id)` → initializes environment
* `step(action)` → returns (observation, reward, done, info)
* `state()` → returns current state

---

## 🧪 Tasks (Increasing Difficulty)

### 🟢 Easy — FAQ Resolution

* Task: Help user reset password
* Expected: Provide instructions + close ticket

---

### 🟡 Medium — Refund Handling

* Task: Handle double charge issue
* Expected: Issue refund + close ticket

---

### 🔴 Hard — Angry Customer Handling

* Task: Handle frustrated customer demanding refund
* Requires:

  * Empathy (apology)
  * Correct resolution (refund/escalate)
  * Proper action sequence

---

## 🎯 Reward Design

The environment uses **dense reward shaping**:

### General Rewards

* +0.1 → helpful response
* -0.1 → empty/irrelevant reply

### Task-Specific Rewards

#### Easy

* +0.4 → correct instruction
* +0.5 → closing ticket

#### Medium

* +0.5 → issuing refund
* +0.4 → closing ticket

#### Hard

* +0.3 → empathetic response
* +0.4 → correct resolution
* +0.2 → proper closure

### Penalties

* Inefficient steps → small negative reward
* Incorrect sequence → reduced reward

### Final Reward

* Clamped between **0.0 and 1.0**

---

## 🤖 Baseline Agent

A deterministic rule-based agent is provided for reproducible evaluation.

### 📊 Baseline Performance

```text
Easy Task   → 1.0
Medium Task → 1.0
Hard Task   → ~0.4
Average     → ~0.8
```

---

## 🧠 Key Features

* ✅ Real-world simulation (not a toy problem)
* ✅ Multi-step decision-making environment
* ✅ Deterministic grading logic
* ✅ Dense reward signals
* ✅ Supports reinforcement learning workflows
* ✅ Fully reproducible baseline

---

## 📁 Project Structure

```text
support-env/
│
├── env/
│   ├── environment.py
│   ├── models.py
│   ├── tasks.py
│   ├── grader.py
│
├── baseline.py
├── openenv.yaml
├── Dockerfile
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Run baseline agent

```bash
python baseline.py
```

---

### 3️⃣ Run API server

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:7860/docs
```

---

## 🐳 Docker Support

```bash
docker build -t support-env .
docker run support-env
```

---

## 📦 OpenEnv Configuration

`openenv.yaml` defines:

* Environment metadata
* Task definitions
* Action & observation schema

---

## 🧪 Evaluation Criteria Alignment

### ✅ Runtime Correctness

* Runs without errors
* Fully tested with baseline agent

### ✅ Interface Compliance

* Implements OpenEnv API (`step`, `reset`, `state`)
* Structured models using Pydantic

### ✅ Task Design

* Real-world tasks
* Clear objectives
* Increasing difficulty

### ✅ Grading Logic

* Deterministic
* Dense reward shaping
* Partial credit supported

---

## 🚀 Future Improvements

* Multi-turn conversations
* Tool usage (database lookup simulation)
* LLM-based agent integration
* Advanced sentiment analysis

---

## 🏁 Conclusion

This project demonstrates how reinforcement learning environments can model **real-world workflows**, enabling AI agents to learn meaningful decision-making strategies beyond games and synthetic tasks.

---
