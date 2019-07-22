from django.contrib import admin
from . import views


from django.urls import include, path

from . import views
app_name = "accounts"

urlpatterns = [
    path('', views.signup,name="signup"),

    path('list', views.UserListView.as_view(),name="list"),
]
