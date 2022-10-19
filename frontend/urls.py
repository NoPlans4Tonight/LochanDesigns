from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('products/', views.products, name='products'),
    # path("", views.inventory, name='inventory')
    path("", views.home_page)
]
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)