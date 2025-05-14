--- 
draft: false
title: "Glossary of LLM related terms"
date: "2025-03-25T15:09:39+0100"
layout: post
tags: ["glossary","AI","LLM"]
slug: "glossary-of-llm-related-terms"
---


# 📚 Glossary

---

## 🧠 General Terms

- **LLM (Large Language Model)**  
  A machine learning model trained on vast amounts of text data to understand and generate human-like language. Examples include ChatGPT, Claude, Gemini, and Mistral.

- **Token**  
  A unit of text (word, part of a word, or symbol) used by LLMs for processing language.

- **Prompt**  
  A textual input given to an LLM to instruct or query it.

- **Context Window**  
  The amount of text (in tokens) an LLM can consider at once.

- **Fine-tuning**  
  Customizing a pre-trained LLM on specific data to specialize it for a task or domain.

- **Embedding**  
  A numerical representation of text used for semantic understanding, clustering, and retrieval tasks.

- **RAG (Retrieval-Augmented Generation)**  
  A technique where external data is fetched and combined with a prompt to help the LLM generate more accurate responses.

- **Chain-of-Thought Reasoning**  
  A prompting technique that encourages the model to "think step by step" before answering.

- **Hallucination**  
  When an LLM generates factually incorrect or fabricated information with confidence.

- **Agent**  
  A software entity that uses an LLM and tools to perform a task autonomously or semi-autonomously.

- **Memory**  
  Persistent storage of past interactions or user-specific data, allowing an agent or LLM to build continuity.

- **Tool Use**  
  The ability of an LLM or agent to use external APIs or tools (e.g., calculator, browser) to complete a task.

- **Multi-agent System**  
  A setup where multiple AI agents collaborate, often using LLMs, each with different roles or goals.

---

## 🚀 Mainstream LLMs (as of 2025)

- **GPT-4 / GPT-4 Turbo** – *OpenAI*  
  GPT-4 Turbo is faster and cheaper than GPT-4 with a 128k token context window. Powers ChatGPT.

- **Claude 3** – *Anthropic*  
  Known for long context windows and safety features.

- **Gemini 1.5** – *Google DeepMind*  
  Formerly Bard. Integrates with Google apps. Very large context support.

- **Mistral** – *Mistral AI*  
  Open-weight models such as Mistral 7B and Mixtral.

- **LLaMA** – *Meta*  
  Series of open-weight models, including LLaMA 2 and upcoming LLaMA 3.

- **Command R** – *Cohere*  
  RAG-optimized models, popular in enterprise use.

- **Grok** – *xAI (Elon Musk)*  
  Integrated with X (formerly Twitter). Focused on reasoning and open-source.

---

## 🛠️ CrewAI-Specific Terms

**[CrewAI](https://www.crewai.com)** is a Python framework for building collaborative LLM agents.

- **Crew**  
  A team of agents that work together to accomplish a task.

- **Agent (in CrewAI)**  
  An LLM-based worker with a defined role, goal, tools, and behavior.

- **Role**  
  Describes the function of the agent, e.g., "Researcher" or "Writer."

- **Goal**  
  The specific objective assigned to the agent.

- **Backstory**  
  Optional narrative that gives personality or behavioral context to an agent.

- **Tools**  
  External functions or utilities agents can use (e.g., search, code execution).

- **Process**  
  The workflow strategy — sequential (agents act one after another) or collaborative.

- **Task**  
  A work item assigned to an agent with instructions and output expectations.

- **Output File**  
  Where the agent or crew stores results for reuse or review.

- **Memory**  
  Stores past outputs or steps to inform current and future agent reasoning.

---

## 🤖 AutoGPT / AgentGPT Providers and Frameworks

Frameworks that support autonomous or collaborative AI agents using LLMs and tools.

| Provider / Project | Description |
|---------------------|-------------|
| **CrewAI** | Python framework for defining structured agent teams with goals, memory, tools, and collaboration. [🔗](https://www.crewai.com) |
| **AutoGPT** | One of the original autonomous agents. Generates subgoals, uses tools, and stores memory. [🔗](https://github.com/Torantulino/Auto-GPT) |
| **AgentGPT** | Web-based UI for autonomous agents that think and act in the browser. [🔗](https://agentgpt.reworkd.ai) |
| **SuperAGI** | Full-featured open-source platform with GUI, memory, and marketplace for agents. [🔗](https://superagi.com) |
| **OpenAgents (Microsoft)** | Research-oriented agent platform with planning and tool use. [🔗](https://openagents.github.io) |
| **LangGraph** | Graph-based multi-agent coordination framework built on LangChain. [🔗](https://langgraph.langchain.com) |
| **MetaGPT** | Simulates a software dev team (PM, Engineer, QA) using role-based agents. [🔗](https://github.com/geekan/MetaGPT) |
| **ChatDev** | Simulates a virtual software company with agents playing different roles. |
| **BabyAGI** | Lightweight agent framework that continuously generates and prioritizes tasks. [🔗](https://github.com/yoheinakajima/babyagi) |
| **Camel-AI** | Agent communication framework focused on negotiation and collaboration. [🔗](https://github.com/camel-ai/camel) |

---

## ⚙️ Related Ecosystem Tools

- **LangChain**  
  Framework for chaining prompts, memory, and tools together. Widely used in agent systems.

- **LlamaIndex**  
  Data indexing layer to connect LLMs with custom or private datasets.

- **Toolformer**  
  A fine-tuning technique to teach LLMs how and when to use tools.

- **OpenFunction Calling**  
  Technique that enables LLMs to invoke external APIs via structured JSON outputs (e.g., OpenAI’s function calling, Anthropic’s tool use).
