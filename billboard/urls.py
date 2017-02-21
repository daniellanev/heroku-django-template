from django.conf.urls import url
from . import views

app_name = 'billboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_message$', views.add_message, name='add_message'),
]
    