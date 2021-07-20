
from django.contrib import admin
from django.urls import path, include
from geekShop.views import index,contacts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('mainapp.urls', namespace='products'),name='products'),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts')

]
