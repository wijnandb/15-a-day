--- 
draft: false
title: "Asking a single agent to assemble a multi-agent crew"
date: "2025-03-25T12:36:12+0100"
layout: post
tags: ["multi-agent", "AI", "productivity"]
slug: "asking-a-single-agent-to-assemble-a-multi-agent-crew"
--- 

I am doing a little experiment and at the moment of writing, I don't know the outcome yet.
First, I ask ChatGPT 4 the follwing (quite elaborate) question:

*I know there are a million different fitness apps out there and hardly any on eof them actually "works" in the sense that it automagically gets people to work out.*

*So before even considering building something, we need to analyze what an app's actual job is.*

*Look up Clayton Christensen's "jobs to be done" (it's an interesting read and moreover: we can learn from it) and get a grasp of what it means to figure out "which job needs to be done".*

*Do research on the reasons why people work out, whta triggers them, what motivates them, what get sthem to actually exercise.*

*Do a similar research on reasons why people stop working out, why don't they do their exercises, why do they stop going to the gym?*

*How do the two outcomes relate to one another?*

*Is there a way to promote or facilitate the reasons to work out?*
*Are there ways to prevent the (underlying) reasons for not working out surface or become a dominant force?*

*Present your findings in a structured way, like it is an academic paper.*

(I don't know why I added the last line, I guess it's just to try and make myself look smart or something. WhadduIknow)

I have gotten an already great answer, you can read it [here](https://chatgpt.com/share/67e2a672-8c88-800a-8774-0c9c771ef647), buit I wanted more: I was curious if a multi-agent approch would get me a better result, so I asked ChatGPT (in another chat):

*Look at the prompt below and determine which crew you would assemble to tackle this task.*
And I pasted the exact same prompt.

[This was the response](https://chatgpt.com/share/67e2a711-faa0-800a-88d1-ed866faab55a).

As you can see in the response, it recommended a crew of people with different roles and different tasks, see below.
It also asked to simulate running it with different roles, which I will do later.

This is the setup it recommended:
  name: FitnessMotivationResearchCrew
  description: A cross-functional team tasked with understanding the real job of fitness apps by analyzing human behavior, motivations, and drop-off triggers.
  agents:
    - BehavioralPsychologist
    - JTBDStrategist
    - UserResearcher
    - AcademicWriter
    - DataAnalyst
    - FitnessCoach
  tasks:
    - ResearchFitnessMotivation
    - ResearchFitnessDropOff
    - ConductUserInterviews
    - AnalyzeQuantitativeTrends
    - GatherTrainerInsights
    - DefineJobsToBeDone
    - SynthesizeFindings
    - WriteFinalReport

