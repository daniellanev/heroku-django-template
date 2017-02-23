from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews
from accounts.views import login_view, register_view, logout_view

app_name = 'accounts'
urlpatterns = [
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^register$', register_view, name='register'),
]
  