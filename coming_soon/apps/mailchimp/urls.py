#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^blick/$',
        view=views.BlickNewsletterView.as_view(),
        name='blick'),

    url(regex='^email/sylvie/$',
        view=views.SylvieContactView.as_view(),
        name='sylvie'),

    url(regex='^email/begona/$',
        view=views.BegonaContactView.as_view(),
        name='sylvie'),

]
