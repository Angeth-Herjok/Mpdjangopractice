from .views import *
from django.urls import path

urlpatterns = [
    path('', admin.site.urls),
]