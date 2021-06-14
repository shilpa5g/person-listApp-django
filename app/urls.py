from django.urls import path
from . import views
urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('person/new/', views.person_new, name='person_new'),
    path('person/<int:pk>/edit/', views.person_edit, name='person_edit'),
    path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
    path('person/<int:pk>/detail/', views.person_detail, name='person_detail'),
    
]