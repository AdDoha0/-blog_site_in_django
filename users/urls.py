from django.urls import path, reverse_lazy

from. import views

app_name = "users"


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
]