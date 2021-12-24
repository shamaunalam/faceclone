from django.urls import path
from minifb import views
urlpatterns = [ 
    path('',views.index,name='login'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.edit_profile,name='editprofile'),
    path('logout',views.Logout,name='logout'),
    path('register',views.register,name='register'),
    path('createpost',views.create_post,name='createpost')
]   