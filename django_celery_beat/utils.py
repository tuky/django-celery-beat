"""Utilities."""
# -- XXX This module must not use translation as that causes
# -- a recursive loader import!
from __future__ import absolute_import, unicode_literals
import datetime

from django.conf import settings
from django.utils import timezone

is_aware = timezone.is_aware

# see Issue #222
now_localtime = getattr(timezone, 'template_localtime', timezone.localtime)


def make_aware(value):
    """Force datatime to have timezone information."""
    if getattr(settings, 'USE_TZ', False):
        # naive datetimes are assumed to be in UTC.
        if timezone.is_naive(value):
            value = timezone.make_aware(value, timezone.utc)
        # then convert to the Django configured timezone.
        default_tz = timezone.get_default_timezone()
        value = timezone.localtime(value, default_tz)
    return value


def now():
    """Return the current date and time."""
    if getattr(settings, 'USE_TZ', False):
        _now = now_localtime(timezone.now())
        if not getattr(settings, 'DJANGO_CELERY_BEAT_TZ_AWARE', True):
            _now = datetime.datetime.now()
        return _now
    else:
        return timezone.now()


def is_database_scheduler(scheduler):
    """Return true if Celery is configured to use the db scheduler."""
    if not scheduler:
        return False
    from kombu.utils import symbol_by_name
    from .schedulers import DatabaseScheduler
    return (
        scheduler == 'django'
        or issubclass(symbol_by_name(scheduler), DatabaseScheduler)
    )
