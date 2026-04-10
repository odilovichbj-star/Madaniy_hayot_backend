"""
Madaniy Hayot — Core Models
Barcha modellar ko'p tilli (uz/ru/en) qo'llab-quvvatlaydi.
"""

from django.db import models


class Service(models.Model):
    """Kompaniya xizmatlari (Web, Mobile, ERP, UI/UX, etc.)"""

    ICON_CHOICES = [
        ('laptop', 'Laptop — Veb-sayt'),
        ('smartphone', 'Smartphone — Mobil ilova'),
        ('database', 'Database — ERP/CRM'),
        ('pen-tool', 'PenTool — UI/UX Dizayn'),
        ('shield-check', 'ShieldCheck — Xavfsizlik'),
        ('video', 'Video — Video Production'),
        ('graduation-cap', 'GraduationCap — Akademiya'),
        ('cloud', 'Cloud — Bulutli texnologiyalar'),
    ]

    title_uz = models.CharField("Nomi (UZ)", max_length=200)
    title_ru = models.CharField("Nomi (RU)", max_length=200, blank=True)
    title_en = models.CharField("Nomi (EN)", max_length=200, blank=True)

    description_uz = models.TextField("Tavsif (UZ)", blank=True)
    description_ru = models.TextField("Tavsif (RU)", blank=True)
    description_en = models.TextField("Tavsif (EN)", blank=True)

    icon = models.CharField(
        "Ikona",
        max_length=50,
        choices=ICON_CHOICES,
        default='laptop',
        help_text="Lucide icon nomi (frontendda ishlatiladi)"
    )

    order = models.PositiveIntegerField("Tartib raqami", default=0)
    is_active = models.BooleanField("Faolmi?", default=True)

    created_at = models.DateTimeField("Yaratilgan", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan", auto_now=True)

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"
        ordering = ['order', 'id']

    def __str__(self):
        return self.title_uz


class Project(models.Model):
    """Kompaniya loyihalari / portfolio"""

    CATEGORY_CHOICES = [
        ('web', 'Veb-sayt'),
        ('mobile', 'Mobil ilova'),
        ('crm', 'CRM/ERP'),
        ('video', 'Video Production'),
        ('ai', 'AI & Akademiya'),
        ('cloud', 'Cloud Computing'),
        ('other', 'Boshqa'),
    ]

    title_uz = models.CharField("Nomi (UZ)", max_length=300)
    title_ru = models.CharField("Nomi (RU)", max_length=300, blank=True)
    title_en = models.CharField("Nomi (EN)", max_length=300, blank=True)

    description_uz = models.TextField("Tavsif (UZ)")
    description_ru = models.TextField("Tavsif (RU)", blank=True)
    description_en = models.TextField("Tavsif (EN)", blank=True)

    image = models.ImageField("Rasm", upload_to='projects/', blank=True, null=True)
    video = models.FileField("Video", upload_to='projects/videos/', blank=True, null=True)

    category = models.CharField(
        "Kategoriya",
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='web'
    )

    url = models.URLField("Loyiha URL", blank=True, help_text="Tashqi havola (agar bo'lsa)")

    order = models.PositiveIntegerField("Tartib raqami", default=0)
    is_active = models.BooleanField("Faolmi?", default=True)

    created_at = models.DateTimeField("Yaratilgan", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan", auto_now=True)

    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title_uz


class TeamMember(models.Model):
    """Jamoa a'zolari"""

    name_uz = models.CharField("Ism (UZ)", max_length=200)
    name_ru = models.CharField("Ism (RU)", max_length=200, blank=True)
    name_en = models.CharField("Ism (EN)", max_length=200, blank=True)

    position_uz = models.CharField("Lavozim (UZ)", max_length=200)
    position_ru = models.CharField("Lavozim (RU)", max_length=200, blank=True)
    position_en = models.CharField("Lavozim (EN)", max_length=200, blank=True)

    image = models.ImageField("Rasm", upload_to='team/', blank=True, null=True)

    linkedin = models.URLField("LinkedIn", blank=True)
    twitter = models.URLField("Twitter / X", blank=True)
    email = models.EmailField("Email", blank=True)

    order = models.PositiveIntegerField("Tartib raqami", default=0)
    is_active = models.BooleanField("Faolmi?", default=True)

    created_at = models.DateTimeField("Yaratilgan", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan", auto_now=True)

    class Meta:
        verbose_name = "Jamoa a'zosi"
        verbose_name_plural = "Jamoa a'zolari"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.name_uz} — {self.position_uz}"


class News(models.Model):
    """Yangiliklar / blog postlar"""

    title_uz = models.CharField("Sarlavha (UZ)", max_length=500)
    title_ru = models.CharField("Sarlavha (RU)", max_length=500, blank=True)
    title_en = models.CharField("Sarlavha (EN)", max_length=500, blank=True)

    content_uz = models.TextField("Matn (UZ)", blank=True)
    content_ru = models.TextField("Matn (RU)", blank=True)
    content_en = models.TextField("Matn (EN)", blank=True)

    image = models.ImageField("Rasm", upload_to='news/', blank=True, null=True)

    date = models.DateField("Sana", help_text="Yangilik sanasi")
    is_active = models.BooleanField("Faolmi?", default=True)

    created_at = models.DateTimeField("Yaratilgan", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan", auto_now=True)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.title_uz} ({self.date})"


class ContactMessage(models.Model):
    """Sayt orqali yuborilgan xabarlar"""

    name = models.CharField("Ism", max_length=200)
    email = models.EmailField("Email")
    message = models.TextField("Xabar")

    is_read = models.BooleanField("O'qildimi?", default=False)

    created_at = models.DateTimeField("Yuborilgan vaqt", auto_now_add=True)

    class Meta:
        verbose_name = "Kontakt xabar"
        verbose_name_plural = "Kontakt xabarlar"
        ordering = ['-created_at']

    def __str__(self):
        read_status = "✅" if self.is_read else "🔴"
        return f"{read_status} {self.name} — {self.email}"


class CompanyInfo(models.Model):
    """
    Kompaniya aloqa ma'lumotlari.
    Faqat 1 ta ob'ekt bo'lishi kerak (Singleton).
    """

    phone = models.CharField("Telefon", max_length=50)
    email = models.EmailField("Email")

    address_uz = models.TextField("Manzil (UZ)")
    address_ru = models.TextField("Manzil (RU)", blank=True)
    address_en = models.TextField("Manzil (EN)", blank=True)

    telegram = models.URLField("Telegram", blank=True)
    instagram = models.URLField("Instagram", blank=True)
    facebook = models.URLField("Facebook", blank=True)
    linkedin = models.URLField("LinkedIn", blank=True)

    map_embed_url = models.TextField(
        "Google Maps Embed URL",
        blank=True,
        help_text="Google Maps iframe src URL"
    )

    updated_at = models.DateTimeField("Yangilangan", auto_now=True)

    class Meta:
        verbose_name = "Kompaniya ma'lumotlari"
        verbose_name_plural = "Kompaniya ma'lumotlari"

    def __str__(self):
        return "Kompaniya ma'lumotlari"

    def save(self, *args, **kwargs):
        """Singleton pattern — faqat 1 ta ob'ekt bo'lishi mumkin"""
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1, defaults={
            'phone': '+998 90 123 45 67',
            'email': 'info@madaniyhayot.uz',
            'address_uz': "Toshkent shahri, Bodomzor metrosi yaqinida, Amir Temur ko'chasi",
        })
        return obj


class HeroBanner(models.Model):
    """Bosh sahifa banner ma'lumotlari"""

    title1_uz = models.CharField("Sarlavha 1 (UZ)", max_length=200)
    title1_ru = models.CharField("Sarlavha 1 (RU)", max_length=200, blank=True)
    title1_en = models.CharField("Sarlavha 1 (EN)", max_length=200, blank=True)

    title2_uz = models.CharField("Sarlavha 2 (UZ)", max_length=200)
    title2_ru = models.CharField("Sarlavha 2 (RU)", max_length=200, blank=True)
    title2_en = models.CharField("Sarlavha 2 (EN)", max_length=200, blank=True)

    subtitle_uz = models.TextField("Qo'shimcha matn (UZ)", blank=True)
    subtitle_ru = models.TextField("Qo'shimcha matn (RU)", blank=True)
    subtitle_en = models.TextField("Qo'shimcha matn (EN)", blank=True)

    button_text_uz = models.CharField("Tugma matni (UZ)", max_length=100, blank=True)
    button_text_ru = models.CharField("Tugma matni (RU)", max_length=100, blank=True)
    button_text_en = models.CharField("Tugma matni (EN)", max_length=100, blank=True)

    button_url = models.CharField("Tugma URL", max_length=300, blank=True, default="#services")

    background_image = models.ImageField("Fon rasmi", upload_to='banners/', blank=True, null=True)

    is_active = models.BooleanField("Faolmi?", default=True)
    order = models.PositiveIntegerField("Tartib raqami", default=0)

    created_at = models.DateTimeField("Yaratilgan", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan", auto_now=True)

    class Meta:
        verbose_name = "Hero Banner"
        verbose_name_plural = "Hero Bannerlar"
        ordering = ['order']

    def __str__(self):
        return f"{self.title1_uz} {self.title2_uz}"
