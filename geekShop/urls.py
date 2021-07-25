from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from geekShop.views import index,contacts
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('mainapp.urls', namespace='products'),name='products'),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)