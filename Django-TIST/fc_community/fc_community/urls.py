from django.urls import path, include
from django.contrib import admin
from fcuser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcuser/', include('fcuser.urls')),  # login/으로 들어오는 url 연결해준다
    path('board/' , include('board.urls')),
    path('', home),
]
