from django.urls import path

from . import views

app_name = 'gucc_app'   

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('committee/', views.committee, name='committee'),
    path('welfare', views.welfare, name='welfare'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('main-shed/', views.main_shed, name='main_shed'),
    path('macpherson-shed/', views.macpherson_shed, name='macpherson_shed'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('koalas/', views.koalas, name='koalas'),
    path('basekit/', views.basekit, name='basekit'),
    path('kayakkit/', views.kayakkit, name='kayakkit'),
    path('baseinventory/', views.baseinventory, name='baseinventory'),
    path('test/', views.test, name='test'),
    path('pool/', views.pool, name='pool'),
    path('garscube/', views.garscube, name='garscube'),
    path('macpherson/', views.macpherson, name='macpherson'),
]