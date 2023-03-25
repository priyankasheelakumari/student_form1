from django.urls import path
from .import views


urlpatterns=[
    path('form',views.first),
    path('tabview',views.tab),
    path('view <str:v_id>',views.viewbtn,name='viewbtn1'),
    path('update <str:u_id>',views.updates,name='updatebtn'),
    path('erase <str:d_id>',views.dele,name='deletebtn'),
    path('index',views.index),
    path('search',views.search),
    path('registration',views.register)
]