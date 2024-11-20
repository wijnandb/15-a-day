---
draft: true
title: "Bredeschool stand van zaken spreadsheet georganiseerde activiteiten"
date: "2024-11-19T11:09:24+0200"
layout: post
tags: ["project", "brede-school"]
slug: "bredeschool-stand-van-zaken-spreadsheet-georganiseerde-activiteiten"
---

Omdat we scholen willen stimuleren om zo snel mogelijk het programma rond te maken, zodat aanbieders en docenten vastgelegd kunnen worden, willen we inzichtelijk maken hoe ver een school staat met het organiseren van activiteiten.

Omdat de Talentmakelaars en IC-ers geen toegang hebben tot het overzicht met de stand van zakne van alle scholen, maken we een spreadsheet dat we delen met alle Talentmakelaars. Het spreadsheet wordt elke nacht bijgewerkt en bevat de volgende velden:

- school
- aantal aangevraagde activiteiten
- aantal aanbieder gekoppeld (dus zonder "geen aanbieder")
- aantal op "ter goedkeuring"
- aantal aanbieder akkoord
- aantal docent aangewezen
- aantal docent VOG akkoord
- aantal inschrijving open
- aantal minimaal aantal inschrijvingen bereikt (dus gelijk of groter dan max_participants)
- aantal maximaal aantal leerlingen geplaatst

Hoe ziet de query er uit?

We queryen Schedule en filteren op Period.

Zie beschrijving hieronder, dit is antwoord van Chad: https://chatgpt.com/c/673c8caa-1f00-800a-ae20-acba2aa51888 
"Geen aanbieder" heeft id = 312

Ask ChatGPT:
- We want to create a Google spreadsheet and update it every night, from a Django application. I already have code that updates a Google document, so let's focus on the query first.

We want to filter the Schedule model, see below, we filter on the last Period.
We then want to create a list of all Schools and the number of Schedules in that last Period.
In the third column, we want to show the number of Schedules that have a Company attached which is not the "geen aanbieder" (so look up that id)
The next column shows the number of Schedules that have any status except "CONCEPT"
Then we want to show the number of Schedules that have status "AGREED"
Following column lists the number of Schedules that have a Teacher assigned.
Next up, the number of ASchedules that have a Teacher assigned with a valid VOG (Eligibility document, see below for the Model). SO the status has to be "verified".

That's it for now.

What I forgot to mention, is that this way of counting Schedules means that we always look for the number of Schedules that ALSO apply to the next filter, so we limit the number of Schedules in every step.

That also means that the first column has the highest number of Schedules, and it either stays the same or the amount gets lower.


```Python
class Schedule(TimestampedModel):
    """
    A schedule takes an activity and a company providing that activity.
    It is scheduled for a maximum number of participants of several schools
    and several groups. It is scheduled for a number of dates (roughly between
    10 and 13) and is held weekly on the same day at the same time.
    """

    def get_available_schooldates():
        """Used to store an empty default value in the arrayfield for dates"""
        return list()

    class Day(models.TextChoices):
        MONDAY = 1, _("Monday")
        TUESDAY = 2, _("Tuesday")
        WEDNESDAY = 3, _("Wednesday")
        THURSDAY = 4, _("Thursday")
        FRIDAY = 5, _("Friday")
        SATURDAY = 6, _("Saturday")
        SUNDAY = 7, _("Sunday")

    class Status(models.TextChoices):
        CONCEPT = 0, _("Concept")
        FUTURE = 1, _("Toekomstige")
        CURRENT = 2, _("Huidige")
        PAST = 3, _("Afgelopen")
        ARCHIVED = 4, _("Gearchiveerde")

    class Agreement(models.TextChoices):
        CONCEPT = 0, _("Concept")
        TO_AGREE = 1, _("Ter beoordeling")
        AGREED = 2, _("Akkoord")
        DISAGREED = 3, _("Niet akkoord")
        RECEIVED_INVOICE = 4, _("Factuur ontvangen")
        INVOICE_PAID = 5, _("Factuur voldaan")

    class ScheduleType(models.TextChoices):
        BREDE_SCHOOL = 1, _("Brede School")
        RICH_SCHOOL_DAY = 2, _("Rich School day")
        PO_VO = 3, _("PO/VO")

    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        verbose_name=_("Activity"),
        related_name="schedules",
        null=False,
        blank=False,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name=_("Company Name"),
        blank=False,
        null=False,
    )
    school = models.ManyToManyField(
        School, verbose_name=_("School"), related_name="school"
    )
    group = models.ManyToManyField(
        Yeargroup,
        related_name="yeargroup",
        verbose_name=_("Yeargroups"),
    )
    day = models.CharField(
        max_length=1,
        choices=Day.choices,
        verbose_name=_("Weekday"),
        null=False,
        blank=False,
    )
    starting_time = models.TimeField(
        verbose_name=_("Starting Time"),
        # default="00:00",
        null=True,
        blank=True,
    )
    end_time = models.TimeField(
        verbose_name=_("End Time"),
        # default= 00:00",
        null=True,
        blank=True,
    )
    min_participants = models.PositiveIntegerField(
        verbose_name=_("Min Participants"),
        blank=False,
        null=False,
        default=0,
    )
    max_participants = models.PositiveIntegerField(
        verbose_name=_("Max Participants"),
        blank=False,
        null=False,
        default=15,
    )
    period = models.ForeignKey(
        "Period",
        on_delete=models.CASCADE,
        related_name="period",
        verbose_name="blok",
    )
    dates = ArrayField(
        models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False),
        size=30,
        default=get_available_schooldates,
    )
    teacher = models.ForeignKey(
        to="userprofile.Profile",
        on_delete=models.CASCADE,
        verbose_name=_("Teacher"),
        blank=True,
        null=True,
        limit_choices_to={"is_teacher": True},
    )
    address = models.CharField(
        max_length=100,
        verbose_name=_("Address"),
        blank=True,
        default="",
    )
    location = models.CharField(
        max_length=100,
        verbose_name=_("Location"),
        blank=True,
        default="",
    )
    comment = models.TextField(
        blank=True,
        default="",
        help_text="Extra informatie m.b.t. activiteit",
        verbose_name="Extra informatie m.b.t. activiteit",
    )
    participants = models.ManyToManyField(Student, through="Participation")
    active = models.BooleanField(
        default=False,
        help_text="Aanvinken is openzetten voor inschrijvingen door ouders en IC-ers.",
        verbose_name="Open voor inschrijving",
    )
    internal_activity = models.BooleanField(
        default=False,
        help_text="Interne school-activiteit, ouders kunnen niet inschrijven.",
        verbose_name="Interne activiteit",
    )
    status = models.CharField(
        choices=Status.choices, max_length=1, null=False, blank=False, default=1
    )
    agreement = models.CharField(
        choices=Agreement.choices, max_length=1, null=False, blank=False, default=0
    )
    skills = models.ManyToManyField(Skill, blank=True)
    schedule_type = models.CharField(
        choices=ScheduleType.choices,
        max_length=1,
        null=False,
        blank=False,
        default=ScheduleType.BREDE_SCHOOL,
    )

    class Meta:
        verbose_name = _("Schedule")
        verbose_name_plural = _("Schedules")
        ordering = ["dates", "day", "starting_time", "activity__name"]

```

This is the Eligibility Document model:

```Python
class EligibilityDocument(TimestampedModel):
    """Keep track of document of eligibility uploaded by teacher waiting for approval."""

    TYPE = (
        ("upload file", "VOG indienen"),
        ("waiting to be verified", "Wacht op verificatie VOG"),
        ("verified", "VOG ontvangen en gecontroleerd"),
    )
    teacher = models.OneToOneField(
        "userprofile.Profile",
        on_delete=models.SET_NULL,
        related_name="eligibility_document",
        null=True,
    )
    document = models.FileField(upload_to=UploadHandler.user_upload_path, null=True)
    status = models.CharField(choices=TYPE, max_length=28)
    approved_by = models.ForeignKey(
        to="userprofile.Profile", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ["-created"]

    def get_filename(self):
        name = self.document.name.rsplit("/")[-1]
        return name

    def __str__(self):
        return "{} {}".format(self.teacher, self.status)
```
