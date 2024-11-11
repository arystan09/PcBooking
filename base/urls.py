from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    # path('book/', views.book, name="book"),
    path("profile/update",views.update_user_profile,name="update-user-profile"),
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path("profile/",views.user_profile,name="user-profile"),
    path("clubs/", views.list_computer_clubs, name="clubs"),
    path("upload_club_file/", views.upload_club_file, name="upload_club_file"),
    path("clubs/<int:club_id>/",views.detailed_club_view,name="detailed_club_view"),
]
