from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.myblogs, name='myblogs'),
    path('accounts/', include('django.contrib.auth.urls')),
]