"""
Madaniy Hayot — Admin Panel Configuration
Jazzmin orqali chiroyli admin panel
"""

from django.contrib import admin
from .models import (
    Service, Project, TeamMember, News,
    ContactMessage, CompanyInfo, HeroBanner
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SERVICE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'icon', 'order', 'is_active', 'updated_at')
    list_filter = ('is_active', 'icon')
    list_editable = ('order', 'is_active')
    search_fields = ('title_uz', 'title_ru', 'title_en')
    ordering = ('order',)

    fieldsets = (
        ("🇺🇿 O'zbek tili", {
            'fields': ('title_uz', 'description_uz'),
        }),
        ("🇷🇺 Rus tili", {
            'classes': ('collapse',),
            'fields': ('title_ru', 'description_ru'),
        }),
        ("🇬🇧 Ingliz tili", {
            'classes': ('collapse',),
            'fields': ('title_en', 'description_en'),
        }),
        ("⚙️ Sozlamalar", {
            'fields': ('icon', 'order', 'is_active'),
        }),
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROJECT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'category', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'category')
    list_editable = ('order', 'is_active')
    search_fields = ('title_uz', 'title_ru', 'title_en')
    ordering = ('order', '-created_at')

    fieldsets = (
        ("🇺🇿 O'zbek tili", {
            'fields': ('title_uz', 'description_uz'),
        }),
        ("🇷🇺 Rus tili", {
            'classes': ('collapse',),
            'fields': ('title_ru', 'description_ru'),
        }),
        ("🇬🇧 Ingliz tili", {
            'classes': ('collapse',),
            'fields': ('title_en', 'description_en'),
        }),
        ("📸 Media", {
            'fields': ('image', 'video'),
        }),
        ("⚙️ Sozlamalar", {
            'fields': ('category', 'url', 'order', 'is_active'),
        }),
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TEAM MEMBER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'position_uz', 'order', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    search_fields = ('name_uz', 'name_ru', 'name_en', 'position_uz')
    ordering = ('order',)

    fieldsets = (
        ("🇺🇿 O'zbek tili", {
            'fields': ('name_uz', 'position_uz'),
        }),
        ("🇷🇺 Rus tili", {
            'classes': ('collapse',),
            'fields': ('name_ru', 'position_ru'),
        }),
        ("🇬🇧 Ingliz tili", {
            'classes': ('collapse',),
            'fields': ('name_en', 'position_en'),
        }),
        ("📸 Rasm", {
            'fields': ('image',),
        }),
        ("🔗 Ijtimoiy tarmoqlar", {
            'classes': ('collapse',),
            'fields': ('linkedin', 'twitter', 'email'),
        }),
        ("⚙️ Sozlamalar", {
            'fields': ('order', 'is_active'),
        }),
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# NEWS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'date', 'is_active', 'created_at')
    list_filter = ('is_active', 'date')
    list_editable = ('is_active',)
    search_fields = ('title_uz', 'title_ru', 'title_en')
    date_hierarchy = 'date'
    ordering = ('-date',)

    fieldsets = (
        ("🇺🇿 O'zbek tili", {
            'fields': ('title_uz', 'content_uz'),
        }),
        ("🇷🇺 Rus tili", {
            'classes': ('collapse',),
            'fields': ('title_ru', 'content_ru'),
        }),
        ("🇬🇧 Ingliz tili", {
            'classes': ('collapse',),
            'fields': ('title_en', 'content_en'),
        }),
        ("📸 Media va Sana", {
            'fields': ('image', 'date'),
        }),
        ("⚙️ Sozlamalar", {
            'fields': ('is_active',),
        }),
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONTACT MESSAGE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    ordering = ('-created_at',)

    def short_message(self, obj):
        return obj.message[:80] + "..." if len(obj.message) > 80 else obj.message
    short_message.short_description = "Xabar"

    def has_add_permission(self, request):
        """Admin paneldan xabar qo'shish taqiqlanadi — faqat sayt orqali"""
        return False


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMPANY INFO (Singleton)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'updated_at')

    fieldsets = (
        ("📞 Aloqa", {
            'fields': ('phone', 'email'),
        }),
        ("🇺🇿 Manzil (UZ)", {
            'fields': ('address_uz',),
        }),
        ("🇷🇺 Manzil (RU)", {
            'classes': ('collapse',),
            'fields': ('address_ru',),
        }),
        ("🇬🇧 Manzil (EN)", {
            'classes': ('collapse',),
            'fields': ('address_en',),
        }),
        ("🔗 Ijtimoiy tarmoqlar", {
            'fields': ('telegram', 'instagram', 'facebook', 'linkedin'),
        }),
        ("🗺️ Xarita", {
            'fields': ('map_embed_url',),
        }),
    )

    def has_add_permission(self, request):
        """Faqat 1 ta ob'ekt bo'lishi mumkin"""
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HERO BANNER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ('title1_uz', 'title2_uz', 'order', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    ordering = ('order',)

    fieldsets = (
        ("🇺🇿 O'zbek tili", {
            'fields': ('title1_uz', 'title2_uz', 'subtitle_uz', 'button_text_uz'),
        }),
        ("🇷🇺 Rus tili", {
            'classes': ('collapse',),
            'fields': ('title1_ru', 'title2_ru', 'subtitle_ru', 'button_text_ru'),
        }),
        ("🇬🇧 Ingliz tili", {
            'classes': ('collapse',),
            'fields': ('title1_en', 'title2_en', 'subtitle_en', 'button_text_en'),
        }),
        ("⚙️ Sozlamalar", {
            'fields': ('button_url', 'background_image', 'order', 'is_active'),
        }),
    )
