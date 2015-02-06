""" Create a shuffeled list of candidates for an event.  """

from django.core.management.base import BaseCommand
from random import shuffle
from dice import models


def make_shuffeled_order(count):
    """Return random list of integers."""

    items = range(1, count + 1)
    shuffle(items)
    return items


class Command(BaseCommand):
    """This gives every candidate a position on the list."""

    help = 'Roll the dice for all Events that passed the deadline'

    def handle(self, *args, **options):
        """Map random position to all candidates."""
        events = models.Event.objects.filter(diced=False)
        for event in events:
            if event.past_deadline:
                position = make_shuffeled_order(event.candidates.count())
                for counter, candidate in enumerate(event.candidates.all()):
                    candidate.position = position[counter]
                event.diced = True
