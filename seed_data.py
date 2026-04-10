"""
Madaniy Hayot — Boshlang'ich ma'lumotlar
Frontend saytdagi barcha ma'lumotlarni bazaga yuklash
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from datetime import date
from core.models import Service, Project, TeamMember, News, CompanyInfo, HeroBanner


def seed():
    print("🌱 Ma'lumotlar yuklanmoqda...")

    # ━━━━━━━━━━━ SERVICES ━━━━━━━━━━━
    services_data = [
        {
            'title_uz': "Veb-sayt ishlab chiqish", 'title_ru': "Веб-разработка", 'title_en': "Web Development",
            'icon': 'laptop', 'order': 1,
        },
        {
            'title_uz': "Mobil ilovalar", 'title_ru': "Мобильные приложения", 'title_en': "Mobile Apps",
            'icon': 'smartphone', 'order': 2,
        },
        {
            'title_uz': "ERP & CRM Tizimlar", 'title_ru': "ERP и CRM системы", 'title_en': "ERP & CRM Systems",
            'icon': 'database', 'order': 3,
        },
        {
            'title_uz': "UI/UX Dizayn", 'title_ru': "UI/UX Дизайн", 'title_en': "UI/UX Design",
            'icon': 'pen-tool', 'order': 4,
        },
        {
            'title_uz': "Axborot Xavfsizligi", 'title_ru': "Кибербезопасность", 'title_en': "Cybersecurity",
            'icon': 'shield-check', 'order': 5,
        },
        {
            'title_uz': "Video Production", 'title_ru': "Видеопродакшн", 'title_en': "Video Production",
            'icon': 'video', 'order': 6,
        },
        {
            'title_uz': "AI Akademiya", 'title_ru': "AI Академия", 'title_en': "AI Academy",
            'icon': 'graduation-cap', 'order': 7,
        },
        {
            'title_uz': "Bulutli texnologiyalar (Cloud Computing)", 'title_ru': "Облачные технологии (Cloud Computing)", 'title_en': "Cloud Computing",
            'icon': 'cloud', 'order': 8,
        },
    ]
    for s in services_data:
        Service.objects.get_or_create(title_uz=s['title_uz'], defaults=s)
    print(f"  ✅ {len(services_data)} xizmat yuklandi")

    # ━━━━━━━━━━━ PROJECTS ━━━━━━━━━━━
    projects_data = [
        {
            'title_uz': "IT-Commerce-Platforma", 'title_ru': "IT-E-commerce Платформа", 'title_en': "IT-Commerce Platform",
            'description_uz': "Veb sayt imkoniyatlarini yanada kengaytirish va sotuvlarni avtomatlashtirish.",
            'description_ru': "Расширение возможностей сайта и автоматизация продаж.",
            'description_en': "Expanding website capabilities and automating sales.",
            'category': 'web', 'order': 1,
        },
        {
            'title_uz': "Mobil ilova", 'title_ru': "Мобильное приложение", 'title_en': "Mobile Application",
            'description_uz': "Mijozlar uchun qulay hamda ishonchli mobil ilova orqali xizmat ko'rsatish.",
            'description_ru': "Обслуживание клиентов через удобное и надежное мобильное приложение.",
            'description_en': "Serving customers through a convenient and reliable mobile app.",
            'category': 'mobile', 'order': 2,
        },
        {
            'title_uz': "CRM Tizimi", 'title_ru': "CRM Система", 'title_en': "CRM System",
            'description_uz': "Kompaniya ichki boshqaruvini tizimlashtirish va mijozlar bazasini yuritish.",
            'description_ru': "Систематизация внутреннего управления и ведение клиентской базы.",
            'description_en': "Systematizing internal management and maintaining a customer base.",
            'category': 'crm', 'order': 3,
        },
        {
            'title_uz': "Video Production", 'title_ru': "Видеопродакшн", 'title_en': "Video Production",
            'description_uz': "Professional reklama roliklari va biznes uchun yuqori sifatli korporativ videolar yaratish.",
            'description_ru': "Создание профессиональных рекламных роликов и высококачественных корпоративных видео для бизнеса.",
            'description_en': "Creating professional promotional clips and high-quality corporate videos for your business.",
            'category': 'video', 'order': 4,
        },
        {
            'title_uz': "AI Akademiya", 'title_ru': "AI Академия", 'title_en': "AI Academy",
            'description_uz': "Sun'iy intellekt va raqamlashtirish bo'yicha professional o'quv kurslari va mahorat darslari.",
            'description_ru': "Профессиональные учебные курсы и мастер-классы по искусственному интеллекту и цифровизации.",
            'description_en': "Professional training courses and masterclasses on artificial intelligence and digitalization.",
            'category': 'ai', 'order': 5,
        },
        {
            'title_uz': "Cloud Computing", 'title_ru': "Cloud Computing", 'title_en': "Cloud Computing",
            'description_uz': "Biznesni bulutli platformalarga o'tkazish, ma'lumotlarni xavfsiz saqlash va tizim barqarorligini ta'minlash.",
            'description_ru': "Перенос бизнеса на облачные платформы, безопасное хранение данных и обеспечение стабильности системы.",
            'description_en': "Migrating business to cloud platforms, secure data storage and ensuring system stability.",
            'category': 'cloud', 'order': 6,
        },
    ]
    for p in projects_data:
        Project.objects.get_or_create(title_uz=p['title_uz'], defaults=p)
    print(f"  ✅ {len(projects_data)} loyiha yuklandi")

    # ━━━━━━━━━━━ TEAM ━━━━━━━━━━━
    team_data = [
        {
            'name_uz': "Jasur Jumanov", 'name_ru': "Жасур Жуманов", 'name_en': "Jasur Jumanov",
            'position_uz': "Asoschi / CEO", 'position_ru': "Основатель / CEO", 'position_en': "Founder / CEO",
            'order': 1,
        },
        {
            'name_uz': "Azamat Alimov", 'name_ru': "Азамат Алимов", 'name_en': "Azamat Alimov",
            'position_uz': "Texnik Direktor / CTO", 'position_ru': "Технический директор / CTO", 'position_en': "Technical Director / CTO",
            'order': 2,
        },
        {
            'name_uz': "Malika Soliyeva", 'name_ru': "Малика Солиева", 'name_en': "Malika Soliyeva",
            'position_uz': "Art Direktor / Lead Designer", 'position_ru': "Арт-директор / Ведущий дизайнер", 'position_en': "Art Director / Lead Designer",
            'order': 3,
        },
        {
            'name_uz': "Sardor Salimov", 'name_ru': "Сардор Салимов", 'name_en': "Sardor Salimov",
            'position_uz': "Marketing bo'limi boshlig'i", 'position_ru': "Руководитель отдела маркетинга", 'position_en': "Head of Marketing",
            'order': 4,
        },
    ]
    for t in team_data:
        TeamMember.objects.get_or_create(name_uz=t['name_uz'], defaults=t)
    print(f"  ✅ {len(team_data)} jamoa a'zosi yuklandi")

    # ━━━━━━━━━━━ NEWS ━━━━━━━━━━━
    news_data = [
        {'title_uz': "IT Texnologiyalaridagi So'nggi Yangiliklar", 'title_ru': "Последние новости в IT-технологиях", 'title_en': "Latest News in IT Technologies", 'date': date(2023, 1, 21)},
        {'title_uz': "Yangi ERP Loyihamiz Ishga Tushdi", 'title_ru': "Запущен новый ERP-проект", 'title_en': "Our New ERP Project Launched", 'date': date(2022, 12, 15)},
        {'title_uz': "Madaniy Hayot Xodimlari Tadbirda", 'title_ru': "Сотрудники Madaniy Hayot на мероприятии", 'title_en': "Madaniy Hayot Staff at Event", 'date': date(2022, 11, 5)},
        {'title_uz': "Zamonaviy Dizayn Trendlari: UX/UI ning Biznesdagi O'rni", 'title_ru': "Тренды современного дизайна: Роль UX/UI в бизнесе", 'title_en': "Modern Design Trends: The Role of UX/UI in Business", 'date': date(2025, 10, 12)},
        {'title_uz': "Kiberxavfsizlik - Raqamli Dunyoda Ma'lumotlar Himoyasi", 'title_ru': "Кибербезопасность - Защита данных в цифровом мире", 'title_en': "Cybersecurity - Data Protection in the Digital World", 'date': date(2025, 10, 5)},
        {'title_uz': "Video Marketing: Brendingiz Uchun Yuqori Sifatli Roliklar", 'title_ru': "Видеомаркетинг: высококачественные ролики для вашего бренда", 'title_en': "Video Marketing: High-Quality Clips for Your Brand", 'date': date(2025, 9, 28)},
        {'title_uz': "AI Akademiya: Sun'iy Intellekt Dunyosiga Ilk Qadamlar", 'title_ru': "AI Академия: Первые шаги в мир искусственного интеллекта", 'title_en': "AI Academy: First Steps into the World of AI", 'date': date(2025, 9, 15)},
        {'title_uz': "Bulutli Texnologiyalar: Biznesni Masofadan Boshqarish", 'title_ru': "Облачные технологии: удаленное управление бизнесом", 'title_en': "Cloud Technologies: Remote Business Management", 'date': date(2025, 9, 1)},
    ]
    for n in news_data:
        News.objects.get_or_create(title_uz=n['title_uz'], defaults=n)
    print(f"  ✅ {len(news_data)} yangilik yuklandi")

    # ━━━━━━━━━━━ COMPANY INFO ━━━━━━━━━━━
    CompanyInfo.objects.get_or_create(pk=1, defaults={
        'phone': '+998 90 123 45 67',
        'email': 'info@madaniyhayot.uz',
        'address_uz': "Toshkent shahri, Bodomzor metrosi yaqinida, Amir Temur ko'chasi",
        'address_ru': "г. Ташкент, метро Бодомзор, улица Амира Темура",
        'address_en': "Tashkent city, near Bodomzor metro station, Amir Temur Street",
        'map_embed_url': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2995.1764722513476!2d69.28376797672693!3d41.346197471313496!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38ae8b7c7b80a221%3A0x6b44a49c4f74d008!2sBodomzor!5e0!3m2!1sen!2sus!4v1712750000000!5m2!1sen!2sus",
    })
    print("  ✅ Kompaniya ma'lumotlari yuklandi")

    # ━━━━━━━━━━━ HERO BANNER ━━━━━━━━━━━
    HeroBanner.objects.get_or_create(title1_uz="Innovatsion", defaults={
        'title1_uz': "Innovatsion", 'title1_ru': "Инновационные", 'title1_en': "Innovative",
        'title2_uz': "IT Yechimlar", 'title2_ru': "IT Решения", 'title2_en': "IT Solutions",
        'subtitle_uz': "Biznesingiz uchun zamonaviy IT yechimlar va raqamli texnologiyalar.",
        'subtitle_ru': "Современные IT решения и цифровые технологии для вашего бизнеса.",
        'subtitle_en': "Modern IT solutions and digital technologies for your business.",
        'button_text_uz': "Xizmatlarimiz", 'button_text_ru': "Наши услуги", 'button_text_en': "Our Services",
        'button_url': "#services",
        'order': 1,
    })
    print("  ✅ Hero banner yuklandi")

    print("\n🎉 Barcha ma'lumotlar muvaffaqiyatli yuklandi!")


if __name__ == '__main__':
    seed()
