import logging
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
from card_server.views.rest_dispatch import RESTDispatch, data_not_found


class CardView(RESTDispatch):
    def GET(self, request, card_id):
        card_id = int(card_id)
        template = None
        if card_id == 1:
            template = 'library.html'
        if card_id == 2:
            template = 'hfs.html'
        if card_id == 3:
            template = 'tuition.html'

        return render_to_response(template, {})
