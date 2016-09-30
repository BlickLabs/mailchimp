#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urlparse

import requests
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.conf import settings


class CosmeticsNewsletterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CosmeticsNewsletterView, self)\
            .dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        endpoint = urlparse.urljoin(
            settings.MAILCHIMP_API_ROOT,
            'lists/%s/members/' % settings.MAILCHIMP_NEWSLETTER_LIST
        )
        data = {
            "email_address": email,
            "status": "subscribed",
        }
        data = json.dumps(data)
        response = requests.post(
            endpoint, auth=('apikey', settings.MAILCHIMP_API_KEY), data=data)
        return JsonResponse(response.json())
