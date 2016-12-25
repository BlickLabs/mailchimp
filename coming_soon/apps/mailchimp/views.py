#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urlparse
import json

import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.conf import settings
from django.template import loader


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


class SylvieContactView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SylvieContactView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        key = 'key-eb656047b090ea091ef7c5d2fbd83dc5'
        domain = 'mg.balletsylviereynaud.com'
        recipient = 'alan@blick.mx'

        ctx = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'message': request.POST.get('message'),
        }

        body = loader.render_to_string('email/sylvie_contact.html', ctx)

        request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(domain)
        request = requests.post(request_url, auth=('api', key), data={
            'from': 'Ballet Sylviereynaud  <postmaster@{0}>'.format(domain),
            'to': recipient,
            'subject': 'Nuevo contacto desde pagina web',
            'text': body
        })

        if request.status_code != 200:
            value = '0'
        else:
            value = '1'

        return HttpResponse(value)


class BegonaContactView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BegonaContactView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):

        key = 'key-eb656047b090ea091ef7c5d2fbd83dc5'
        domain = 'mg.begonafernandez.com.mx'
        recipient = 'alan@blick.mx'

        ctx = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'message': request.POST.get('message'),
            'address': request.POST.get('address'),
        }

        body = loader.render_to_string('email/begona_contact.html', ctx)

        request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(domain)
        request = requests.post(request_url, auth=('api', key), data={
            'from': 'Begoña <postmaster@{0}>'.format(domain),
            'to': recipient,
            'subject': 'Nuevo contacto desde pagina web',
            'text': body
        })

        if request.status_code != 200:
            value = '0'
        else:
            value = '1'

        return HttpResponse(value)