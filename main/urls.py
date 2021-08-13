from django.urls import path
from .views import *

urlpatterns = [
    path('', Index),
    path('about/', About),
    path('service/', Service),
    path('hodim-detail/<int:id>/', HodimDetail),

    path('hodimlar/', Hodim),
    path('ishchi/<int:id>/', IshchiDetail),
    path('hodim-add/', HodimAdd)
]