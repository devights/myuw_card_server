from django.conf.urls import patterns, include, url
from card_server.views.card_view import CardView
from card_server.views.card_manifest import CardManifest

urlpatterns = patterns(
    # Why the hell are you ignoring the first url?!
    url(r'^v1/asdf/$', CardManifest().run),
    url(r'^v1/card/(?P<card_id>[0-9]{1})$', CardView().run),
    url(r'^v1/card/$', CardManifest().run)

)