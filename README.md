# Assignment-2-CSCN8020

# 🚖 Q-Learning Agent — Taxi-v3 Environment

This project implements and evaluates a **Q-Learning agent** using the **OpenAI Gymnasium Taxi-v3** environment.  
The goal is to train the agent to efficiently pick up and drop off passengers while minimizing penalties and optimizing rewards.

---

## 🧩 Project Overview

The notebook walks through the full **Q-learning workflow**, including:
1. **Implementing the Q-learning algorithm** (agent, config, and training loop).  
2. **Training and evaluating** the agent in the Taxi-v3 environment.  
3. **Hyperparameter tuning** using learning rate (α) and exploration rate (ε) sweeps.  
4. **Selecting the best configuration** and retraining the optimal agent.  
5. **Evaluating and visualizing performance** using both text-based and real-time render modes.

---

## ⚙️ Setup and Requirements

### Prerequisites
Make sure you have Python 3.8+ and the following libraries installed:

```bash
pip install gymnasium numpy matplotlib pandas
