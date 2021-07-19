from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import home, register

 

urlpatterns = [
    path('person/list/', views.person_list, name='person_list'),
    path('person/new/', views.person_new, name='person_new'),
    path('person/<int:pk>/edit/', views.person_edit, name='person_edit'),
    path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
    path('person/<int:pk>/detail/', views.person_detail, name='person_detail'),
    path('login/',auth_views.LoginView.as_view(), {'template_name': 'app/registration/login.html'}, name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name = 'logout'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),

    path('password_reset/', auth_views.PasswordResetView.as_view(),{'template_name': 'app/registration/password_reset.html'}, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), {'template_name': 'app/registration/password_reset_done.html'}, name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), {'template_name': 'app/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), {'template_name': 'app/registration/password_reset_complete.html'}, name='password_reset_complete'),

    path('password_reset_request/', views.password_reset_request, name="password_reset_request"),
    #path('password_reset_form/', views.password_reset_form, name="password_reset_form"),


    path('list/', views.PersonListAPI.as_view(), name = 'list'),
    path('create/', views.PersonCreateAPI.as_view(), name = 'create'),
    path('update/<int:pk>/', views.PersonUpdateAPI.as_view(), name = 'update'),
    path('destroy/<int:pk>/', views.PersonDestroyAPI.as_view(), name = 'destroy'),

]