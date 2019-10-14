from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addbook$', views.addbook),
    url(r'^books/(?P<id>\d+)$', views.booksmain),
    url(r'^addauthortobook/(?P<id>\d+)$', views.addauthortobook),
    url(r'^authors$', views.authormain),
    url(r'^addauthor$', views.addauthor),
    url(r'^authors/(?P<id>\d+)$', views.authordes),
    url(r'^addbooktoauthor/(?P<id>\d+)$', views.addbooktoauthor)
]
