# pages/urls.py
from django.urls import path, include
from .views import (homePageView, aboutPageView, studentPageView, results, homePost, todo, register,
                    message, logoutView, secret_area, todos)

urlpatterns = [
    path('', homePageView, name='home'),
    path("about/", aboutPageView, name='about'),
    path("xinli/", studentPageView, name='xinli'),
    path("homePost/", homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
    path('todo/', todo, name='todo'),
    path("register/", register, name="register"),
    path('message/<str:msg>/<str:title>/', message, name="message"),  # <-- added
    path('', include("django.contrib.auth.urls")),  # <-- added
    path("logout/", logoutView, name="logout"),
    path('secret/', secret_area, name='secret'),
    path('todos/', todos, name='todos')
]
