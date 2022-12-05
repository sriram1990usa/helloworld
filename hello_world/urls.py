from django.urls import path
from .views import homepage
from django.conf.urls.static import static, settings

urlpatterns = [
    path('', homepage, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

