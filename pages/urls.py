# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, studentPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path("about/",aboutPageView, name='about'),
    path("xinli/", studentPageView, name='xinli'),
    path("homePost/", homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
