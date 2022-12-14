from django.urls import path
from storage import views
from django.conf.urls.static import static
from django.conf import settings

app_name='storage'

urlpatterns = [
    path('', views.products, name='products'),
    path('edit/', views.edit_products, name='edit'),
    path('upload/', views.upload_product, name='upload'),
]