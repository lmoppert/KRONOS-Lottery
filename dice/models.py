"""Define Models for the dice app."""

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Employee(models.Model):

    """This extends the built in user model with extra data."""

    user = models.OneToOneField(User)
    phone = models.CharField(max_length="50", blank=True)
    department = models.CharField(max_length=200, blank=True)


class Event(models.Model):

    """Class for the event schedules."""

    name = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    responsible = models.ForeignKey(User, related_name="event_manager")
    participant_number = models.IntegerField()
    schedule = models.DateField()
    deadline = models.DateField()
    diced = models.BooleanField(default=False)
    candidates = models.ManyToManyField(User, through='Candidate')

    @property
    def past_deadline(self):
        """Return True if the deadline has been passed."""

        return self.deadline > datetime.now()


class Candidate(models.Model):

    """Class for the Users that want to subscripe to scheduled events."""

    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    position = models.IntegerField(blank=True)
