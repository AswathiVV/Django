from django.urls import path
from . import views

urlpatterns = [
    path('z',views.fun1),
    path('x',views.disp_std),
    path('g',views.fun),
    path('p',views.form2)
]