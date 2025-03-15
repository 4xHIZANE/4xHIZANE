from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('app/', views.homepage, name='app'),  # Yangi yo‘l qo‘shildi
    path('reg/', views.registration, name='reg'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update_post, name='update'),  # ID qo'shildi
    path('create/', views.create_post, name='create'),
]
