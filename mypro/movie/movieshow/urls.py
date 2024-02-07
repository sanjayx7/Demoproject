from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from movieshow import views
app_name="movieshow"

urlpatterns = [
    path('',views.home,name="home"),
    path('addmovie',views.addmovie,name="addmovie"),
    path('viewmovie',views.viewmovie,name="viewmovie"),
    path('edit/<int:p>', views.edit, name="edit"),
    path('delete/<int:p>', views.delete, name='delete'),




]