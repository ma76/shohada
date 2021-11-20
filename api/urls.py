from django.urls import path
from .views import *

urlpatterns = [
    path('shahids', ShahidView.as_view()),
]
