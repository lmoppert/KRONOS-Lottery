"""Define the admin interface."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from dice import models


class EmployeeInline(admin.StackedInline):

    """Extends the built in user model."""

    model = models.Employee
    can_delete = False
    verbose_name_plural = 'Mitarbeiter'


class EmployeeAdmin(UserAdmin):

    """Add the inline to the existing admin."""

    inlines = (EmployeeInline, )


class CandidateInline(admin.TabularInline):

    """Manage the candidates that have subsriped so far."""

    model = models.Candidate
    extra = 0


class EventAdmin(admin.ModelAdmin):

    """Admin of the events in the dice app."""

    model = models.Event
    inlines = (CandidateInline, )


admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
admin.site.register(models.Event, EventAdmin)
