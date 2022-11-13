from django.urls import path
from PriApp.views import mostrar_flia


urlpatterns = [
    path('', mostrar_flia)
]