# 📘 Madaniy Hayot — API Documentation

**Base URL:** `http://localhost:8000/api/`

**Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
**ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
**Admin Panel:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 🌐 Til qo'llab-quvvatlash (Multi-language)

Barcha GET endpointlar `lang` query parametrini qabul qiladi:

| Parametr | Qiymat | Natija |
|----------|--------|--------|
| `?lang=uz` | O'zbek tili | Standart til |
| `?lang=ru` | Rus tili | Русский |
| `?lang=en` | Ingliz tili | English |

**Misol:** `GET /api/services/?lang=ru`

> Agar so'ralgan tilda tarjima bo'lmasa, o'zbek tiliga fallback qiladi.

---

## 📋 API Endpoints

### 1. 🔧 Xizmatlar (Services)

**`GET /api/services/`**

Kompaniya xizmatlarini qaytaradi.

**Query Parameters:**
| Parametr | Tur | Tavsif |
|----------|-----|--------|
| `lang` | string | Til kodi: `uz`, `ru`, `en` |

**Response (200 OK):**
```json
[
    {
        "id": 1,
        "title": "Veb-sayt ishlab chiqish",
        "description": "",
        "icon": "laptop",
        "order": 1
    },
    {
        "id": 2,
        "title": "Mobil ilovalar",
        "description": "",
        "icon": "smartphone",
        "order": 2
    }
]
```

---

### 2. 📂 Loyihalar (Projects)

**`GET /api/projects/`**

Kompaniya loyihalari / portfolio.

**Query Parameters:**
| Parametr | Tur | Tavsif |
|----------|-----|--------|
| `lang` | string | Til kodi: `uz`, `ru`, `en` |
| `category` | string | Filtr: `web`, `mobile`, `crm`, `video`, `ai`, `cloud`, `other` |

**Response (200 OK):**
```json
[
    {
        "id": 1,
        "title": "IT-Commerce-Platforma",
        "description": "Veb sayt imkoniyatlarini yanada kengaytirish va sotuvlarni avtomatlashtirish.",
        "image": null,
        "video": null,
        "category": "web",
        "url": "",
        "order": 1
    }
]
```

**Filtr misoli:** `GET /api/projects/?category=mobile&lang=en`

---

### 3. 👥 Jamoa (Team)

**`GET /api/team/`**

Jamoa a'zolarini qaytaradi.

**Query Parameters:**
| Parametr | Tur | Tavsif |
|----------|-----|--------|
| `lang` | string | Til kodi: `uz`, `ru`, `en` |

**Response (200 OK):**
```json
[
    {
        "id": 1,
        "name": "Jasur Jumanov",
        "position": "Asoschi / CEO",
        "image": null,
        "linkedin": "",
        "twitter": "",
        "email": "",
        "order": 1
    }
]
```

---

### 4. 📰 Yangiliklar (News)

#### Ro'yxat

**`GET /api/news/`**

Yangiliklar ro'yxati (sahifalash bilan, 20 tadan).

**Query Parameters:**
| Parametr | Tur | Tavsif |
|----------|-----|--------|
| `lang` | string | Til kodi: `uz`, `ru`, `en` |
| `page` | integer | Sahifa raqami |

**Response (200 OK):**
```json
{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "title": "Zamonaviy Dizayn Trendlari: UX/UI ning Biznesdagi O'rni",
            "image": null,
            "date": "2025-10-12"
        }
    ]
}
```

#### Tafsilot

**`GET /api/news/{id}/`**

Yangilik to'liq ma'lumotlari (matn bilan).

**Response (200 OK):**
```json
{
    "id": 4,
    "title": "Zamonaviy Dizayn Trendlari: UX/UI ning Biznesdagi O'rni",
    "content": "...",
    "image": null,
    "date": "2025-10-12",
    "created_at": "2026-04-10T16:50:16.483000+05:00"
}
```

---

### 5. ✉️ Kontakt xabar yuborish (Contact)

**`POST /api/contact/`**

Sayt kontakt formasidan xabar yuborish.

**Request Body:**
```json
{
    "name": "Jasur Jumanov",
    "email": "jasur@example.com",
    "message": "Sayt yaratish narxi qancha?"
}
```

**Response (201 Created):**
```json
{
    "status": "success",
    "message": "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz.",
    "data": {
        "id": 1,
        "name": "Jasur Jumanov",
        "email": "jasur@example.com",
        "message": "Sayt yaratish narxi qancha?"
    }
}
```

**Xatolar (400 Bad Request):**
```json
{
    "name": ["This field is required."],
    "email": ["Enter a valid email address."]
}
```

> 📌 Yuborilgan xabarlar Admin panelda **Kontakt xabarlar** bo'limida ko'rinadi.

---

### 6. 🏢 Kompaniya ma'lumotlari (Company Info)

**`GET /api/company-info/`**

Kompaniya aloqa ma'lumotlari (singleton).

**Query Parameters:**
| Parametr | Tur | Tavsif |
|----------|-----|--------|
| `lang` | string | Til kodi: `uz`, `ru`, `en` |

**Response (200 OK):**
```json
{
    "phone": "+998 90 123 45 67",
    "email": "info@madaniyhayot.uz",
    "address": "Toshkent shahri, Bodomzor metrosi yaqinida, Amir Temur ko'chasi",
    "telegram": "",
    "instagram": "",
    "facebook": "",
    "linkedin": "",
    "map_embed_url": "https://www.google.com/maps/embed?pb=..."
}
```

---

### 7. 🖼️ Hero Bannerlar (Banners)

**`GET /api/banners/`**

Bosh sahifa banner ma'lumotlari.

**Query Parameters:**
| Parametr | Tur | Tavsif |
|----------|-----|--------|
| `lang` | string | Til kodi: `uz`, `ru`, `en` |

**Response (200 OK):**
```json
[
    {
        "id": 1,
        "title1": "Innovatsion",
        "title2": "IT Yechimlar",
        "subtitle": "Biznesingiz uchun zamonaviy IT yechimlar va raqamli texnologiyalar.",
        "button_text": "Xizmatlarimiz",
        "button_url": "#services",
        "background_image": null,
        "order": 1
    }
]
```

---

## 🔐 Admin Panel

**URL:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

**Login:**
| Maydon | Qiymat |
|--------|--------|
| Username | `admin` |
| Password | `admin123` |

### Admin Panel imkoniyatlari:

- ✅ **Jazzmin** zamonaviy dark tema
- ✅ Barcha modellar uchun CRUD
- ✅ Ko'p tilli (UZ/RU/EN) maydonlar
- ✅ Rasm va video yuklash
- ✅ Kontakt xabarlarni boshqarish
- ✅ Xizmatlar tartibini o'zgartirish (drag & order)
- ✅ Qidiruv va filtrlar

---

## 📊 Response Format

### Muvaffaqiyatli javob:
```
HTTP 200 OK — Ma'lumotlar (list yoki detail)
HTTP 201 Created — Yangi ob'ekt yaratildi
```

### Xato javoblar:
```
HTTP 400 Bad Request — Validatsiya xatosi
HTTP 404 Not Found — Ob'ekt topilmadi
HTTP 500 Server Error — Server xatosi
```

---

## ⚙️ Texnik ma'lumotlar

| Texnologiya | Versiya |
|-------------|---------|
| Python | 3.14+ |
| Django | 6.0 |
| Django REST Framework | 3.17 |
| drf-yasg (Swagger) | 1.21 |
| django-jazzmin | 3.0 |
| Database | SQLite3 (development) |

---

## 🚀 Ishga tushirish

```bash
# Virtual environment yaratish
python -m venv venv
.\venv\Scripts\activate

# Paketlarni o'rnatish
pip install -r requirements.txt

# Migratsiyalar
python manage.py migrate

# Boshlang'ich ma'lumotlarni yuklash
python seed_data.py

# Serverni ishga tushirish
python manage.py runserver 8000
```

---

*© 2026 Madaniy Hayot Media Marketing Markazi*
