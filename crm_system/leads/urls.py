from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),

    path('update-status/<int:id>/', views.update_status, name='update_status'),
    path('edit/<int:id>/', views.edit_lead, name='edit_lead'),
    path('delete/<int:id>/', views.delete_lead, name='delete_lead'),
]