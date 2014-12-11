import logging
from django.http import HttpResponse
import json
from card_server.views.rest_dispatch import RESTDispatch, data_not_found
from datetime import datetime, timedelta


class CardManifest(RESTDispatch):
    def GET(self, request):
        response = {'cards': [
            {'id': 1,
             'name': "Library Card",
             'type': 'library',
             'position': 2,
             'last_updated': datetime_to_string(datetime.now() - timedelta(days=1)),
             'is_urgent': False
             },
            {'id': 2,
             'name': "HFS Card",
             'type': 'housing_and_food',
             'position': 1,
             'last_updated': datetime_to_string(datetime.now() - timedelta(days=3)),
             'is_urgent': False
             },
            {'id': 3,
             'name': "Tuition DUE TOMORROW",
             'type': 'tuition',
             'position': 3,
             'last_updated': datetime_to_string(datetime.now()),
             'is_urgent': True
             }
        ]}

        return HttpResponse(json.dumps(response))


def datetime_to_string(dt_obj):
    return dt_obj.strftime("%c")
