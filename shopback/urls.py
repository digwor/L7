from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/', include('products.urls')),
    path('', include('orders.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
