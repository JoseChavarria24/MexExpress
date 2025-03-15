from django.urls import path
from shopApp.views import index
from shopApp.views import about

urlpatterns = [
    path('', index, name = "index"),
    path('about/', about, name = "about"),
]
