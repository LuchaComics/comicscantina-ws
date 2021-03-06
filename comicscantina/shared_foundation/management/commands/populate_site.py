# -*- coding: utf-8 -*-
import os
import sys
from decimal import *
from django.db.models import Sum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext_lazy as _
from django.core.management import call_command
from shared_foundation.models.franchise import SharedFranchise
from shared_foundation.models.franchise import SharedFranchiseDomain


class Command(BaseCommand):
    help = _('Updates site object.')

    def handle(self, *args, **options):
        # First call; current site fetched from database.
        from django.contrib.sites.models import Site # https://docs.djangoproject.com/en/dev/ref/contrib/sites/#caching-the-current-site-object
        current_site = Site.objects.get_current()
        current_site.domain = settings.COMICSCANTINA_APP_HTTP_DOMAIN
        current_site.save()

        self.stdout.write(
            self.style.SUCCESS(_('Successfully updated site object.'))
        )
