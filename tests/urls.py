# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.urls import path, include


urlpatterns = [
    path('', include('kradmin.urls', namespace='kradmin')),
]
