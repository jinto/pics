from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_view, name='main'),
    url(r'^scan$', views.scan_view, name='scan'),
    url(r'^show/(?P<id>[\w-]+)$', views.show_view, name='show'),
    url(r'^next/(?P<id>[\w-]+)$', views.next_view, name='next'),
    url(r'^random$', views.random_view, name='random'),
    #$url(r'^accounts$', views.accounts_list_view, name='accounts_list'),
    #$url(r'^accounts/(?P<id>[\w-]+)$', views.accounts_detail_view, name='accounts_detail'),
]
