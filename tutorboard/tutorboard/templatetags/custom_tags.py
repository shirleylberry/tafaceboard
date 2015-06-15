from django import template
from django.forms import Textarea, ClearableFileInput

from datetime import datetime
import re

register = template.Library()

@register.filter(name='is_textarea')
def is_textarea(field):
  return field.field.widget.__class__.__name__ == Textarea().__class__.__name__
  
@register.filter(name='is_upload')
def is_upload(field):
  return field.field.widget.__class__.__name__ == ClearableFileInput().__class__.__name__

@register.filter()
def days_diff(date1):
    # returns only the number of days since an update as an integer
    # date1 is from the django template filter timesince w/ format x day(s), y hour(s), etc
    num_days = re.search('(^\d{1,2})(?= day)', date1)
    # checks if any time has ever been entered if there's < 1day
    sub_one_day = re.search('(\d{1,2})((?= hour)|(?= minute))', date1)
    if num_days is not None:
        num_days = num_days.group()
        return int(num_days)
    elif sub_one_day is not None:
        return 0
    else:
        return -1