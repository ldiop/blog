from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='emailusers'),
    path('<int:mpk>', views.email_detail, name='t_email_detail'),
    path('<int:mpk>/edit/', views.t_email_edit, name='t_email_edit'),
    path('<int:mpk>/delete', views.t_email_delete, name='t_email_delete'),
    path('addaccount/', views.t_email_add, name='t_email_add'),
]