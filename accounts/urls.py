from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [

    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),


    path('', home, name="home"),
    path('user/', userPage, name="user-page"),

    path('account/', userSettings, name="account"),

    path('products/', products, name="products"),
    path('customer/<str:pk>/', customer, name="customer"),

    path('create_order/<str:pk>/', create_order, name="create_order"),
    path('update_order/<str:pk>/', update_order, name="update_order"),
    path('delete_order/<str:pk>/', delete_order, name="delete_order"),

    path('create_customer/', create_customer, name="create_customer"),
    path('update_customer/<str:pk>/', update_customer, name="update_customer"),
    path('delete_customer/<str:pk>/', delete_customer, name="delete_customer"),

    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html'),
        name='password_reset',
    ),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_sent.html'),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_form.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_done.html'),
        name='password_reset_complete',
    ),

]
