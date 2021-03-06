"""Django-Admin interface support

Adds support for managing webhook subscriptions in the Django admin.
"""
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from . import models

class SubscriberAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Subscriber, SubscriberAdmin)
