#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^mccosmeticsmx/$',
    view=views.CosmeticsNewsletterView.as_view(),
    name='mccosmeticsmx'),

    url(regex='^veltt/$',
    view=views.VelttNewsletterView.as_view(),
    name='veltt'),

]
