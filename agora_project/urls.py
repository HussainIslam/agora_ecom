from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from allauth.account.views import confirm_email
from django.conf.urls import url

schema_view = get_schema_view(
   openapi.Info(
      title="Agora Ecom API",
      default_version='v1',
      description="API Documentation for Agora Ecom",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('', include('accounts.urls')),
   path('', include('pages.urls')),
   path('', include('products.urls')),
   path('', include('orders.urls')),
   path('carts/',include('carts.urls')),
   path('admin/', admin.site.urls),
   path('rest-auth/', include('rest_auth.urls')),
   path('rest-auth/registration/', include('rest_auth.registration.urls')),
   path('accounts-rest/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
   from django.conf.urls.static import static
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)