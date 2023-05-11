from django.urls import path
from . import views

app_name="vendor"
urlpatterns = [
    path("", views.index, name="home"),
    path("user", views.UserListView.as_view(), name="user"),
    path("user/create", views.create_user, name="create_user"),
    path("user/update/<int:user_id>", views.update_user, name="update_user"),
    path("user/delete/<int:user_id>", views.delete_user, name="delete_user"),
    path("desig", views.DesigListView.as_view(), name="desig"),
    path("desig/create", views.create_desig, name="create_desig"),
    path("desig/update/<int:desig_id>", views.update_desig, name="update_desig"),
    path("desig/delete/<int:desig_id>", views.delete_desig, name="delete_desig"),
    path("vendor", views.vendor, name="vendor"),
    path("vendor/<int:vendor_id>", views.vendor_detail, name="detail")
]
