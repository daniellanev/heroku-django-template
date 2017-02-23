
from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews
from accounts.views import login_view, register_view, logout_view

app_name = 'billboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_message$', views.add_message, name='add_message'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
]
    
