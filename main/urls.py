from django.urls import path

from main import views


app_name = "main"

urlpatterns = [
    path("all/", views.IndexView.as_view(), name="all_posts"),
    path("category/", views.IndexView.as_view(), name="category"),
]
