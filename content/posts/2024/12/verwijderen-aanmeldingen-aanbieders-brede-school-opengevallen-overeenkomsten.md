--- 
draft: true
title: "Verwijderen aanmeldingen aanbieders Brede School opengevallen overeenkomsten"
date: "2024-12-10T10:03:09+0100"
layout: post
tags: ["brede school", "TODO"]
slug: "verwijderen-aanmeldingen-aanbieders-brede-school-opengevallen-overeenkomsten"
---


We willen de mogelijkheid om aanmeldingen te verwijderen van aanbieders voor het invullen van overeenkomsten die nog op "ter beoordeling" staan.
Om het op de bestaande pagina van de aanbieders te doen is mogelijk, maar ook lastig. Bovendien is de pagina live en willen we niets "stukmaken", dus een nieuwe pagina in het leven roepen lijkt het handigste.

We kunnen een pagina maken voor de aanbieders, waarop ze de eigen aanmeldingen zien. Dit is een betrekkelijk simpele pagina, aangezien het de records uit de tabel ScheduleApplication zijn, gefilterd op ofwel de aanbieder van de ingelogde gebruiker, ofwel de ingelogde docent.

Op die pagina willen we nog meer tonen: kalenderweergave van de activiteiten die de aanbieder/docent gaat verzorgen ofwel waar deze zich voor heeft ingeschreven.

Ook willen we dat de aanmelder (aanbieder of docent) een opmerking achter kan laten, zodat er niet weer een e-malstroom op hgang wordt gebracht.

Ten slotte willen we de status van een aanmelding tonen: als al een andere aanbieder/docent is gekozen, dan tonen we dat.

- [x] view aanmaken "toon aanmeldingen"
Selecteer alles uit ScheduleApplication voor deze periode, filter op company en/of teacher.
- [ ] template aanmaken
- [ ] url aanmaken
- [ ] HTMX view delete application maken
- [ ] url voor HTMX view maken

# Backoffice pagina
Op de pagina van de backoffice willen we ook laten zien welke overlap er is zodat er niet per ongeluk een docent dubbel wordt geboekt.
Een link naar de inzet per aanbieder/docent lijkt een "quick win".