from django.conf.urls import url
from django.contrib.auth.views import login
from django.views.generic.base import TemplateView

from . import views

app_name = 'front'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^auth/login/$', login, {'template_name': 'front/login.html'}, name='login'),
    url(r'^auth/logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^members/$', views.MembersView.as_view(), name='members'),
    url(r'^projects/$', TemplateView.as_view(template_name='front/projects.html'),
        name='projects'),
    url(r'^coupons/$', views.CouponsView.as_view(), name='coupons'),
    url(r'^wishlist/$', TemplateView.as_view(template_name='front/wishlist.html'),
        name='wishlist'),
]
