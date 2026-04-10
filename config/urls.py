"""
Madaniy Hayot — Main URL Configuration
Admin + Swagger + API
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SWAGGER / OpenAPI SCHEMA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
schema_view = get_schema_view(
    openapi.Info(
        title="Madaniy Hayot API",
        default_version='v1',
        description="""
## 🚀 Madaniy Hayot Media Marketing Markazi — REST API

Bu API orqali **Madaniy Hayot** saytining barcha ma'lumotlarini boshqarish mumkin.

### 🌐 Til qo'llab-quvvatlash
Barcha endpointlar `?lang=uz|ru|en` query parametrini qabul qiladi.
Standart til: **O'zbek (uz)**

### 📋 Mavjud bo'limlar:
- **Xizmatlar** — Kompaniya xizmatlari ro'yxati
- **Loyihalar** — Portfolio va bajarilgan ishlar
- **Jamoa** — Jamoa a'zolari
- **Yangiliklar** — Blog va yangiliklar
- **Kontakt** — Sayt orqali xabar yuborish
- **Kompaniya** — Aloqa ma'lumotlari
- **Banner** — Bosh sahifa bannerlari
        """,
        terms_of_service="https://madaniyhayot.uz/terms/",
        contact=openapi.Contact(email="info@madaniyhayot.uz"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # Admin Panel (Jazzmin)
    path('admin/', admin.site.urls),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API
    path('api/', include('core.urls')),
]

# Media fayllarni development serverda ko'rsatish
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
