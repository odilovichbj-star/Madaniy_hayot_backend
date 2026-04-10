"""
Madaniy Hayot — API Views
Barcha endpointlar uchun ViewSet va APIView'lar
"""

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import (
    Service, Project, TeamMember, News,
    ContactMessage, CompanyInfo, HeroBanner
)
from .serializers import (
    ServiceSerializer, ProjectSerializer, TeamMemberSerializer,
    NewsListSerializer, NewsDetailSerializer,
    ContactMessageSerializer, CompanyInfoSerializer, HeroBannerSerializer
)


# Swagger uchun umumiy til parametri
lang_param = openapi.Parameter(
    'lang',
    openapi.IN_QUERY,
    description="Til kodi: uz, ru, en (default: uz)",
    type=openapi.TYPE_STRING,
    enum=['uz', 'ru', 'en'],
    default='uz'
)


class ServiceListView(generics.ListAPIView):
    """
    Barcha faol xizmatlarni qaytaradi.

    `?lang=uz|ru|en` — tilga qarab tarjima qilingan ma'lumotlar qaytadi.
    """
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Xizmatlar ro'yxati",
        operation_description="Barcha faol xizmatlarni qaytaradi. `lang` parametri orqali tarjima olinadi.",
        manual_parameters=[lang_param],
        tags=['Xizmatlar'],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProjectListView(generics.ListAPIView):
    """
    Barcha faol loyihalarni qaytaradi.

    `?lang=uz|ru|en` — tilga qarab tarjima qilingan ma'lumotlar qaytadi.
    `?category=web|mobile|crm|video|ai|cloud|other` — kategoriya bo'yicha filtr.
    """
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    pagination_class = None

    def get_queryset(self):
        qs = Project.objects.filter(is_active=True)
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(category=category)
        return qs

    @swagger_auto_schema(
        operation_summary="Loyihalar ro'yxati",
        operation_description="Barcha faol loyihalarni qaytaradi. `category` va `lang` parametrlari bilan filtrlanadi.",
        manual_parameters=[
            lang_param,
            openapi.Parameter(
                'category', openapi.IN_QUERY,
                description="Kategoriya filtr: web, mobile, crm, video, ai, cloud, other",
                type=openapi.TYPE_STRING,
            ),
        ],
        tags=['Loyihalar'],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TeamMemberListView(generics.ListAPIView):
    """
    Barcha faol jamoa a'zolarini qaytaradi.
    """
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Jamoa a'zolari",
        operation_description="Barcha faol jamoa a'zolarini qaytaradi.",
        manual_parameters=[lang_param],
        tags=['Jamoa'],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NewsListView(generics.ListAPIView):
    """
    Barcha faol yangiliklar ro'yxati (qisqa format).
    """
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsListSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Yangiliklar ro'yxati",
        operation_description="Barcha faol yangiliklar ro'yxati. Sahifalash mavjud.",
        manual_parameters=[lang_param],
        tags=['Yangiliklar'],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NewsDetailView(generics.RetrieveAPIView):
    """
    Yangilik tafsilotlari (to'liq matn bilan).
    """
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsDetailSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Yangilik tafsilotlari",
        operation_description="Yangilik ID bo'yicha to'liq ma'lumotlarni qaytaradi.",
        manual_parameters=[lang_param],
        tags=['Yangiliklar'],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ContactMessageCreateView(generics.CreateAPIView):
    """
    Sayt orqali kontakt xabar yuborish.
    POST: { "name": "...", "email": "...", "message": "..." }
    """
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Kontakt xabar yuborish",
        operation_description="Sayt kontakt formasidan xabar yuborish. Yuborilgan xabarlar admin panelda ko'rinadi.",
        tags=['Kontakt'],
        responses={
            201: openapi.Response(
                description="Xabar muvaffaqiyatli yuborildi",
                examples={
                    "application/json": {
                        "id": 1,
                        "name": "Jasur",
                        "email": "jasur@example.com",
                        "message": "Sayt yaratish narxi qancha?"
                    }
                }
            ),
            400: "Validatsiya xatosi",
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "status": "success",
                "message": "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class CompanyInfoView(APIView):
    """
    Kompaniya aloqa ma'lumotlari (singleton).
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Kompaniya ma'lumotlari",
        operation_description="Kompaniya telefon, email, manzil va ijtimoiy tarmoq ma'lumotlarini qaytaradi.",
        manual_parameters=[lang_param],
        tags=['Kompaniya'],
        responses={200: CompanyInfoSerializer()},
    )
    def get(self, request):
        info = CompanyInfo.load()
        serializer = CompanyInfoSerializer(info, context={'request': request})
        return Response(serializer.data)


class HeroBannerListView(generics.ListAPIView):
    """
    Bosh sahifa hero bannerlarini qaytaradi.
    """
    queryset = HeroBanner.objects.filter(is_active=True)
    serializer_class = HeroBannerSerializer
    permission_classes = [AllowAny]
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Hero Bannerlar",
        operation_description="Bosh sahifadagi faol bannerlarni qaytaradi.",
        manual_parameters=[lang_param],
        tags=['Banner'],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
