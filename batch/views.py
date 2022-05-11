from django.views.generic import ListView
from . import models

class batchView(ListView):
    model = models.passcode
