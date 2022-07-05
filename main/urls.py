from django.contrib import admin
from django.urls import path

from main.views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view()),
]
