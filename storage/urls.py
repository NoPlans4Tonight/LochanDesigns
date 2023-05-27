from django.urls import path
from storage import views
from django.conf.urls.static import static
from django.conf import settings

app_name='storage'

urlpatterns = [
    path('', views.products, name='products'),
    path('edit/', views.edit_products, name='edit'),
    path('upload/', views.upload_product, name='upload'),
    path('edit-record/<int:record_id>/', views.edit_record, name='edit_record'),
    path('delete-record/<int:record_id>/', views.delete_record, name='delete_record'),
]