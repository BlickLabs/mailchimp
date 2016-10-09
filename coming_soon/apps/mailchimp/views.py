#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urlparse
import json

import requests
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.conf import settings


class BlickNewsletterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BlickNewsletterView, self)\
            .dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        mailchimp_list = request.POST.get('list')
        endpoint = urlparse.urljoin(
            settings.MAILCHIMP_BLICK_API_ROOT, 'lists/%s/members/' % mailchimp_list
        )
        data = {
            "email_address": email,
            "status": "subscribed",
        }
        data = json.dumps(data)
        response = requests.post(
            endpoint, auth=('apikey', settings.MAILCHIMP_BLICK_API_KEY), data=data)
        return JsonResponse(response.json())


class CosmeticsNewsletterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CosmeticsNewsletterView, self)\
            .dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        endpoint = urlparse.urljoin(
            'https://us1.api.mailchimp.com/3.0/',
            'lists/495e6d8931/members/'
        )
        data = {
            "email_address": email,
            "status": "subscribed",
        }
        data = json.dumps(data)
        response = requests.post(
            endpoint, auth=('apikey', '9cade3c4fd50d8ecf2246113a864d60c-us1'), data=data)
        return JsonResponse(response.json())


class VelttNewsletterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VelttNewsletterView, self)\
            .dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        endpoint = urlparse.urljoin(
            'https://us1.api.mailchimp.com/3.0/',
            'lists/1b596219ee/members/'
        )
        data = {
            "email_address": email,
            "status": "subscribed",
        }
        data = json.dumps(data)
        response = requests.post(
            endpoint, auth=('apikey', '9cade3c4fd50d8ecf2246113a864d60c-us1'), data=data)
        return JsonResponse(response.json())