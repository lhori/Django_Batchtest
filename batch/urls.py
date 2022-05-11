from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'passcode'
urlpatterns = [
    path('', views.batchView.as_view())
]
