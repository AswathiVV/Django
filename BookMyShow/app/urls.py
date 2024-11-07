from django.urls import path
from . import views
urlpatterns=[
    path('',views.bms),
    path('view_movie/<id>',views.view_movie),
]