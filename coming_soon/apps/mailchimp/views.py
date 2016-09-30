#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urlparse
import json

import requests
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


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