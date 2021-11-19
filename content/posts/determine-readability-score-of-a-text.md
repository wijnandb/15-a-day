--- 
draft: true
title: "Determine readability score of a text"
date: "2021-09-03T09:17:00+0200"
layout: post
tags: ["reading", "readability", "leestmeer"]
slug: "determine-readability-score-of-a-text"
---


To determine the [readability] score of a text (how easy or difficult is the text), there are different methods.
Factors on which te readability is calculated are:
- Average sentence length
- Number of different hard words
- Number of personal pronouns
- Percentage of unique words
- Number of prepositional phrases 

Losse associaties om niet nu al te verdwalen in diverse zoektochten op het web:

- ugent, wordfrequencies and age of acquisition
- kaggle, competitie om readabilty score te berekenen

## Kaggle competition
The [kaggle competition]() on rating the complexity of literary passages for grades 3-12 mentions some important research and background information about readability:
- [Why Children Should be Taught to Read with More Challenging Texts]()
- [The Percentage of Words Known in a Text and Reading Comprehension]()
- [Previous research on developing text readability algorithms]()



## Dutch research on readability
Suzanne Kleijn: Clozing in on readability: How linguistic features affect and predict text comprehension and on-line processing. Proefschrift Universiteit Utrecht, verdediging op 6 april 2018. Onderzoek gefinancierd door NWO.

De 5 voorspellers uit het [onderzoek] zijn:

- woordfrequentie: hoe vaker een woord voorkomt in het dagelijks taalgebruik, hoe beter;
- concreetheid van woorden: hoe concreter de woorden, hoe beter;
- informatie per deelzin: hoe minder informatie per deelzin, hoe beter;
- de afstand tussen grammaticale eenheden: hoe korter de afstand, hoe beter – dus geen tangconstructies;
- het voorkomen van bijvoeglijk gebruikte voltooid deelwoorden zoals ‘overeengekomen niveaus’: hoe minder, hoe beter.

[readability]: https://en.wikipedia.org/wiki/Readability
[onderzoek]: https://www.nemokennislink.nl/publicaties/nieuwe-leesbaarheidsformule-voor-begrijpelijke-teksten/
[kaggle competition]:https://www.kaggle.com/c/commonlitreadabilityprize/discussion/236463
[Why Children Should be Taught to Read with More Challenging Texts]:
[The Percentage of Words Known in a Text and Reading Comprehension]:https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-4781.2011.01146.x
[Previous research on developing text readability algorithms]:https://www.researchgate.net/publication/335801547_Moving_beyond_classic_readability_formulas_new_methods_and_new_models