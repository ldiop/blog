from django.urls import path, include

from .views import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ftp/<int:pk>', views.t_user_detail, name='t_user_detail'),
    path('ftp/<int:pk>/edit/', views.t_user_edit, name='t_user_edit'),
    path('ftp/<int:pk>/delete', views.t_user_delete, name='t_user_delete'),
    path('ftp/addaccount/', views.t_user_add, name='t_user_add'),
    path(r'^search/$', views.index, name='t_user_search'),

]
