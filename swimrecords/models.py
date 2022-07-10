from django.db import models
from django.forms import CheckboxInput
from .validators import *
from django.core.validators import MinValueValidator, MaxValueValidator

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=False)
    team_name = models.CharField(max_length=100, blank=False)
    relay = models.BooleanField(null=False)
    stroke = models.CharField(max_length=100, validators=[stroke_check])
    distance = models.IntegerField(validators=[MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[no_future_records])
    record_broken_date = models.DateTimeField()

    def clean(self):
        super().clean()
        if self.record_date and self.record_broken_date and self.record_broken_date and self.record_date and self.record_broken_date < self.record_date:
            raise ValidationError({{"record_broken_date" : "Can't break record before record was set."}})