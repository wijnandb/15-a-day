--- 
draft: true
title: "Working smart with LLM's"
date: "2025-02-14T10:28:03+0100"
layout: post
tags: ["AI", "productivity", "LLM", "ChatGPT"]
slug: "working-smart-with-llm-s"
---

How can I work smarter, achieve more, be less stressed, by utilising AI?

When creating an application, using Saas Pegasus so I have the basic functionality covered, I want to create a workflow which is fast, reliable, scalable and high-quality.

The idea I have around this, is using both (remote) developers and AI.

The code will be on Github, where we can use the Wiki, the discussions and the issues.

I'm thinking of creating an agent (or several), that take an idea, a description of a feature, or app, and break it down in smaller pieces so it can create requirements and mockups and maybe even code to realise that feature or app.

1. Idea, description as input
2. Ask additional, clarifying questions as long as needed (loop)
3. Create discussion in Github repo



"I want to create AI-agents that work together to create software, specifically for (existing) Django applications. Help me break down the steps to get there. I am interested in creating a hybrid model first, which works with Github discussions, Github issues, Github Wiki and (remote) developers. By reducing the steps or actually the time it takes to explain things to a developer, we are already making progress, so that's the first goal. From there on out, we can improve and move tasks to the AI agent."

### Planner agent
The Planner Agent's task is to:
- Understand the user's request
- Analyze the existing Django application to determine the necessary changes
- Break the request into discrete, executable tasks
- Assign tasks to the appropriate AI agent or human developer

(
    - Track progress and ensure tasks are completed in the right order
    - Verify dependencies between tasks to avoid inconsistencies
)

### Testing agent
Start with a testing agent?
Write tests for existing code

"I want to create an AI agent that writes tests for existing Django code.
I will be using ChatGPT.
Code will be living in Github.
Break down the steps needed to create such an AI agent."

"What are useful tests that are generally being written for Django applications?"


I think I can do more with AI agents.
I have several ideas that keep lingering in the back of my mind.
I could use AI to help me go from idea to existing application.

"I want to create AI agents that work together to go from idea to live and deployed web-application.
It doesn't have to do it in one fell swoop, what it does is, it takes an idea and breaks it down in steps that need to be taken.
This can be:
- asking questions until the idea is clearly ironed out
- thinks of the steps needed to take, to go from idea to MVP
- helps with the realisation of any of the steps, which could be the creation of an AI agent for a specific task

Phase 1: Core Agent (The Orchestrator)
- **Input**: the user provides an idea
- **Step 1 - Clarification**: The agent asks structured questions to refine the idea.
- **Step 2 - Breakdown**: The agent determines the necessary steps to turn the idea into an MVP.
- **Step 3 - Execution Support**: The agent identifies tasks that can be automated and suggests specialized agents to handle them.
- **Step 4 - Create agents**: Creates the agents suggested in step 3.

Script for streamlit 












"Please create a Github Wiki for the IkTel platform."
Use either Levi or an agemt that creates the actual files.
