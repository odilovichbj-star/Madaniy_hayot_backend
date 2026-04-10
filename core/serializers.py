"""
Madaniy Hayot — DRF Serializers
Til parametri orqali ma'lumotlar filtrlanadi.
"""

from rest_framework import serializers
from .models import (
    Service, Project, TeamMember, News,
    ContactMessage, CompanyInfo, HeroBanner
)


class MultiLanguageMixin:
    """
    Tilga qarab maydonlarni qaytaradi.
    Query param: ?lang=uz|ru|en
    """

    def get_localized_field(self, obj, field_name, lang=None):
        """Tilga mos maydon qiymatini qaytaradi, fallback uz"""
        if not lang:
            request = self.context.get('request')
            lang = request.query_params.get('lang', 'uz') if request else 'uz'

        # Avval so'ralgan tildagi qiymatni olish
        value = getattr(obj, f'{field_name}_{lang}', '')
        # Agar bo'sh bo'lsa, uz ga fallback
        if not value and lang != 'uz':
            value = getattr(obj, f'{field_name}_uz', '')
        return value or ''


class ServiceSerializer(MultiLanguageMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'icon', 'order']

    def get_title(self, obj):
        return self.get_localized_field(obj, 'title')

    def get_description(self, obj):
        return self.get_localized_field(obj, 'description')


class ProjectSerializer(MultiLanguageMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'video', 'category', 'url', 'order']

    def get_title(self, obj):
        return self.get_localized_field(obj, 'title')

    def get_description(self, obj):
        return self.get_localized_field(obj, 'description')


class TeamMemberSerializer(MultiLanguageMixin, serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'position', 'image', 'linkedin', 'twitter', 'email', 'order']

    def get_name(self, obj):
        return self.get_localized_field(obj, 'name')

    def get_position(self, obj):
        return self.get_localized_field(obj, 'position')


class NewsListSerializer(MultiLanguageMixin, serializers.ModelSerializer):
    """Yangiliklar ro'yxati (qisqa)"""
    title = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'image', 'date']

    def get_title(self, obj):
        return self.get_localized_field(obj, 'title')


class NewsDetailSerializer(MultiLanguageMixin, serializers.ModelSerializer):
    """Yangilik tafsilotlari (to'liq)"""
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'image', 'date', 'created_at']

    def get_title(self, obj):
        return self.get_localized_field(obj, 'title')

    def get_content(self, obj):
        return self.get_localized_field(obj, 'content')


class ContactMessageSerializer(serializers.ModelSerializer):
    """Kontakt xabar yuborish"""

    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message']
        read_only_fields = ['id']


class CompanyInfoSerializer(MultiLanguageMixin, serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = CompanyInfo
        fields = [
            'phone', 'email', 'address',
            'telegram', 'instagram', 'facebook', 'linkedin',
            'map_embed_url'
        ]

    def get_address(self, obj):
        return self.get_localized_field(obj, 'address')


class HeroBannerSerializer(MultiLanguageMixin, serializers.ModelSerializer):
    title1 = serializers.SerializerMethodField()
    title2 = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()
    button_text = serializers.SerializerMethodField()

    class Meta:
        model = HeroBanner
        fields = [
            'id', 'title1', 'title2', 'subtitle',
            'button_text', 'button_url', 'background_image', 'order'
        ]

    def get_title1(self, obj):
        return self.get_localized_field(obj, 'title1')

    def get_title2(self, obj):
        return self.get_localized_field(obj, 'title2')

    def get_subtitle(self, obj):
        return self.get_localized_field(obj, 'subtitle')

    def get_button_text(self, obj):
        return self.get_localized_field(obj, 'button_text')
