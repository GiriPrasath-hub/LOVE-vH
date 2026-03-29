---
title: LOVE vH AI
emoji: "🤖"
colorFrom: blue
colorTo: green
sdk: docker
---

# LOVE vH — Adaptive AI Assistant Environment (OpenEnv RL System)

A real-world reinforcement learning environment that trains AI assistants to improve response quality using structured reward shaping and simulated human feedback.

---

## 🚨 Problem

Modern AI assistants generate responses, but:

- They do not improve from interaction feedback  
- They lack consistent evaluation metrics  
- They fail to adapt tone, relevance, and accuracy together  

This creates a gap between AI responses and real human expectations.

---

## 💡 Solution — LOVE vH

LOVE vH is an adaptive AI environment where agents learn to:

- Respond accurately to user intent  
- Maintain contextual relevance  
- Adjust tone based on user emotion  
- Improve over time using reward signals  

It simulates real assistant behavior instead of toy problems.

---

## ⚙️ Environment Design

The environment follows the OpenEnv specification:

- `reset()` → initializes user scenario  
- `step(action)` → evaluates agent response  
- `state()` → returns current interaction context  

### Observation Space
- User message  
- Context history  
- User emotion  

### Action Space
- Response text  
- Tone selection (friendly / helpful / formal)  

---

## 🎯 Tasks & Difficulty Levels

### 🟢 Easy
- Direct user requests  
- Goal: correct and clear response  
- Ends after first correct answer  

### 🟡 Medium
- Ambiguous queries  
- Goal: clarification + helpful response  

### 🔴 Hard
- Emotional or frustrated users  
- Goal: de-escalation and resolution  

---

## 🧪 Reward System

The agent is evaluated using multi-dimensional scoring:

- Accuracy → correctness of response  
- Relevance → alignment with user intent  
- Tone → emotional appropriateness  
- Human Feedback → simulated judge scoring  
- Penalties → repetition and weak follow-ups  

This ensures continuous learning instead of binary success/failure.

---

## 🤖 Learning Policy

The agent improves over episodes by:

- Tracking reward outcomes per tone and topic  
- Updating tone-selection strategy  
- Reinforcing high-performing behaviors  

This enables adaptive responses over time.

---

## 📊 Baseline Performance

Example inference run:

Step 1 → Reward: +30  
Step 2 → Reward: +20  
Step 3 → Reward: +22  
Step 4 → Reward: +20  

Final Score: **92.0**

The agent demonstrates consistent performance improvement.

---

## 🚀 Run Locally

```bash
python inference.py