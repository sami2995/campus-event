from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from test2.views import home, detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home_url"),
    path("detail/<int:pk>/", detail, name="detail_url"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
