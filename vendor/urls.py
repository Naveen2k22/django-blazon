from django.urls import path
from . import views

app_name="vendor"
urlpatterns = [
    path("", views.index, name="home"),
    path("user/", views.UserListView.as_view(), name="user"),
    path("user/create", views.create_user, name="create_user"),
    path("user/update/<int:user_id>/", views.update_user, name="update_user"),
    path("user/delete/<int:user_id>/", views.delete_user, name="delete_user"),
    path("vendor/", views.vendor, name="vendor"),
    path("vendor/<int:vendor_id>/", views.vendor_detail, name="detail")
]
