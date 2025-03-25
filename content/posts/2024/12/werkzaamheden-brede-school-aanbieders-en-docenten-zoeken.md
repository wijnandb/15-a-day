--- 
draft: true
title: "Werkzaamheden Brede School: aanbieders en docenten zoeken"
date: "2024-12-03T11:43:05+0100"
layout: post
tags: ["brede school", "TODO","development"]
slug: "werkzaamheden-brede-school-aanbieders-en-docenten-zoeken"
---

We willen voor alle overeenkomsten waar we nog geen akkoord op hebben ontvangen of waarvoor nog geen docent is aangewezen of zelfs waarvan de docent nog geen geldig VOG heeft, de optie bieden voor andere aanbieders om zich hiervoor in te schrijven/aan te melden.

Hoe pakken we dit aan?

- [x] uitdraai maken van alle overeenkomsten uit blok 2 waar geen akkoord voor is
- [x] pagina waar deze overeenkomsten getoond worden
    - [x] view aanmaken
    - [x] url aanmaken
    - [x] template aanmaken
- [x] nieuwe tabel aanmaken, waarin de aanbieders zich kunnen aanbieden om de Schedule te verzorgen
- [x] pagina waar we per Schedule de mogelijkheid bieden om als aanbieder aan te melden, inclusief toewijzen aan docent
- [x] pagina waar we per Schedule tonen welke aanbieders zich hebben aangemeld, mogelijkheid om 1 te kiezen
- [x] op voorgaande pagina, bij aanbieders die aan voorwaarden voldoen, na druk op knop "akkoord", aanbieder en docent in overeenkomst opnemen
- [x] na click en toevoegen aanbieder en docent, overeenkomst op akkoord zetten.


Eerste stap, filteren van Schedules.
```Python
from activity.models import Schedule

filtered_schedules = Schedule.objects.filter(
    period_id=77,
    agreement__in=[Schedule.Agreement.TO_AGREE, Schedule.Agreement.DISAGREED]
```

De volgende stap is het aanmaken van de tabel om mogelijk te maken dat een aanbieder aangeeft dat ze de activiteit willen verzorgen:

```Python
from django.db import models
from django.utils.translation import gettext_lazy as _

class ScheduleApplication(TimestampedModel):
    """
    Model to store applications from companies to handle schedules.
    A company can apply to a schedule and must provide a teacher if they want to proceed.
    """

    schedule = models.ForeignKey(
        'Schedule',
        on_delete=models.CASCADE,
        related_name='applications',
        verbose_name=_("Schedule"),
        help_text=_("The schedule this application is for."),
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        related_name='schedule_applications',
        verbose_name=_("Company"),
        help_text=_("The company applying to handle the schedule."),
    )
    teacher = models.ForeignKey(
        'userprofile.Profile',
        on_delete=models.CASCADE,
        verbose_name=_("Teacher"),
        related_name='schedule_applications',
        help_text=_("The teacher the company proposes to handle the schedule."),
        limit_choices_to={'is_teacher': True},
    )
    comment = models.TextField(
        blank=True,
        default="",
        verbose_name=_("Comment"),
        help_text=_("Optional comments or additional details provided by the company."),
    )

    class Meta:
        verbose_name = _("Schedule Application")
        verbose_name_plural = _("Schedule Applications")
        unique_together = ('schedule', 'company')
        ordering = ['schedule__day']

    def __str__(self):
        return f"Aanmelding van {self.company} voor {self.schedule}"

```






- [ ] Ook nog oplossen: optie F ingevoerd, zowel in view als in pagina. Dit is het geval als een docent niet is verbonden aan een aanbieder. Nu staat daar een tekst: bel Wijnand, met mijn telefoonnummer.



