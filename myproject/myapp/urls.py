from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'myapp'  # Ustaw nazwę aplikacji

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_view, name='login'),
    path('login/', LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('register/', views.registration_view, name='registration_view'),
    path('logout/', views.logout_view, name='logout'),
    path('panel/', views.panel_view, name='panel'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path("reorder_images/", views.reorder_images, name="reorder_images"),

]
