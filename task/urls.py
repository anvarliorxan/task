
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from service import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('user/',include("user.urls")),
    path('service/',include('service.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
