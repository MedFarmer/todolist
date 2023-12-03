from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('todolist/', TodolistView.as_view(), name='todolist'),
    path('todocreate/', TodoCreateView.as_view(), name='todocreate'),
    path('categorycreate/', CategoryCreateView.as_view(), name='categorycreate'),
    path('detail/<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TodoUpdatelView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', TodoDeleteView.as_view(), name='delete'),
]