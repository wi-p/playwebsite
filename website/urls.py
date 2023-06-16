from django.urls import path
from website import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('post/<str:post>/', views.post, name = 'post')
]