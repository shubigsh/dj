from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path("diff_exa/",views.diff_exa,name='diff_exa'),
    path("www/",views.www,name='www'),
    path("pakages/",views.pakages,name='pakages'),
    path("dij/",views.dij,name='dij'),
    path("boot/",views.boot,name='boot'),


   #project 1 urls
    path('index/',views.index,name='index'),
    path('Nykaa/',views.nykaa,name='Nykaa'),
    path('kylie/',views.Kylie,name='kylie'),
    path('Lakme/',views.lakme,name='Lakme'),
    path('MAC/',views.mac,name='MAC'),
    path('beauty_tips/',views.beauty_tips,name='beauty_tips'),
    path('cart/',views.cart,name='cart')



    #project 2 urls
    
]