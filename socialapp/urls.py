from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_password_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_password_complete.html'),name='password_reset_complete'),
    path('create_account/',views.UserRegistration,name='create_account'),
    path('register_done/',views.registerdone,name="register_done"),
    path('profile/<str:username>/',views.user_profile,name='profile'),
    #path('profile/<str:pk>/',views.user_profile,name='profile'),
    path('edit/',views.editprofile,name='edit'),
    path('images/',views.imageview,name='images'),
    #path('img/<str:username>/',views.image_on_dashboard,name="img")
    path('search/',views.search,name='search'),
    path('follow/<str:id>/<str:username>/',views.follow,name='follow'),
    path('unfollow/<str:id>/<str:username>/',views.unfollow,name='unfollow'),
    path('likes/<str:id>/',views.users_like,name='users_like'),
    path('comments/<str:id>/',views.commentview,name="comment"),
    path('messages/<str:id>/',views.message,name="message"),
    path('delete_comment/<str:post_id>/<str:comment_id>/',views.delete_comment,name="delete_comment"),

    ]
