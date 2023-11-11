from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('users', views.users, name='users'),
    path('report', views.report, name='report'),
    path('change', views.change, name='change'),
    path('complete/<int:pk>', views.complete, name='complete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('assign_task', views.assign_task, name='assign_task'),
    path('add_user', views.add_user, name='add_user'),
]