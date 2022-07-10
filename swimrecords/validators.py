from django.core.exceptions import ValidationError
from django.utils import timezone

def stroke_check(stroke):
    stroke_types = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in stroke_types:
        raise ValidationError(f"{stroke} is not a valid stroke")

def no_future_records(record):
    if record > timezone.now():
        raise ValidationError("Can't set record in the future.")