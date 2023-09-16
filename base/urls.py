from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('topic1/', views.topic1, name='topic1'),
    path('topic2/', views.topic2, name='topic2'),
]