from . import views
from django.urls import re_path

urlpatterns = (
    re_path(r'^$', views.home, name='home'),
    re_path(r'^profile/(?P<id>[0-9]+)$', views.profile, name='profile'),
)
