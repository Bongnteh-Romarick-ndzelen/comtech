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
    path('topic3/', views.topic3, name='topic3'),
    path('topic4/', views.topic4, name='topic4'),
    path('topic5/', views.topic5, name='topic5'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
]
