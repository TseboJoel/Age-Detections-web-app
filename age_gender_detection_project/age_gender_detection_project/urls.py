from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('age_gender_detection_app.urls')),  # Homepage URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
