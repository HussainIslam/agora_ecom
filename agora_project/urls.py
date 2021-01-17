from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from allauth.account.views import confirm_email
from django.conf.urls import url

urlpatterns = [
    path('', include('pages.urls')),
    path('', include('products.urls')),
    path('carts/',include('carts.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts-rest/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
