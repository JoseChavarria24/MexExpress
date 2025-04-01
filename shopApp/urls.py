from django.urls import path
from shopApp.views import index, about, form_comment, form_contact


urlpatterns = [
    path('', index, name = "index"),
    path('about/', about, name = "about"),
    path('form_comment/', form_comment, name = "comment"),
    path('form_contact/',form_contact, name = "register_contact"),
]
