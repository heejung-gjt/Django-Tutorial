from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),  # login/으로 들어오는 url 연결해준다
    path('logout/',views.logout)
]
