from django.urls import path
from . import views

urlpatterns = [
    path('z',views.fun1),
    path('x',views.disp_std),
    # path('g',views.fun),
    path('add_std',views.add_std),
    path('edit_std/<id>',views.edit_std),
    path('delete_std/<id>',views.delete_std)
]