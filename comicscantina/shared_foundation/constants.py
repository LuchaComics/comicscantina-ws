# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# The domain of our application.
#

COMICSCANTINA_APP_HTTP_PROTOCOL = settings.COMICSCANTINA_APP_HTTP_PROTOCOL
COMICSCANTINA_APP_HTTP_DOMAIN = settings.COMICSCANTINA_APP_HTTP_DOMAIN


# The groups of our application.
#

EXECUTIVE_GROUP_ID = 1
MANAGEMENT_GROUP_ID = 2
FRONTLINE_GROUP_ID = 3
ASSOCIATE_GROUP_ID = 4
CUSTOMER_GROUP_ID = 5


# The default currency of our application.
#

COMICSCANTINA_APP_DEFAULT_MONEY_CURRENCY = settings.COMICSCANTINA_APP_DEFAULT_MONEY_CURRENCY


# The following constants are used by the "contant_point" models.
#

TELEPHONE_CONTACT_POINT_TYPE_OF_ID = 1
MOBILE_CONTACT_POINT_TYPE_OF_ID = 2
WORK_CONTACT_POINT_TYPE_OF_ID = 3

TELEPHONE_CONTACT_POINT_TYPE_OF_CHOICES = (
    (TELEPHONE_CONTACT_POINT_TYPE_OF_ID, _('Telephone')),
    (MOBILE_CONTACT_POINT_TYPE_OF_ID, _('Mobile')),
    (WORK_CONTACT_POINT_TYPE_OF_ID, _('Work Telephone'))
)
