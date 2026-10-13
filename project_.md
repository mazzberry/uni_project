# project16_onlineshop_uniproject

## What is this project about?

This is a **Persian (Farsi) online mobile-phone shop** built with Django. It is a
university/learning project (the code and git history contain many Persian
teaching comments and video-lesson references) that implements a small but
complete e-commerce flow for selling mobile phones.

The site is fully localized in Persian:
- Default language is `fa-ir` with `Asia/Tehran` timezone.
- Prices are rendered with a comma helper and numbers are converted to Persian
  digits via custom template filters.
- Jalali (Shamsi) date support is enabled for the Django admin.
- The marketing copy ("درباره ما" / About Us) describes a mobile-phone store.

### Core features
- **Landing / home page**: hero sections, featured products (latest 8) and
  newest products (latest 4), store services and testimonials.
- **Product catalog**: list view with filtering by `status`, pagination
  (elided page range), and a product detail page.
- **Product comments / reviews**: authenticated users can post a 1–5 star
  comment on a product; only "active" comments are shown.
- **Shopping cart**: session-based cart (no DB model) supporting add, remove,
  quantity update, total price, item count, and a sidebar counter via a
  context processor.
- **User accounts**: custom user model + authentication and signup via
  `django-allauth` (email-based login, signup, logout, email confirmation).
- **About Us** page.
- **Internationalization**: English/Persian translation files (`.po`/`.mo`)
  and the `rosetta` web UI for managing translations.
- **Admin panel**: product management with inline comments and Jalali dates.

## Stack & Technologies

### Backend
- **Python 3.12**
- **Django 5.0.2** (main framework)
- **PostgreSQL 16** (production/DB, `psycopg2-binary`)
- **WSGI / ASGI** entry points (`config/wsgi.py`, `config/asgi.py`)

### Django packages
- **django-allauth** – authentication / signup / email confirmation
- **django-crispy-forms + crispy-bootstrap4** – form rendering
- **django-rosetta** – in-browser translation management (i18n)
- **django-i18n** – internationalization helpers
- **django-jalali-date / jalali_core / jdatetime** – Jalali calendar dates
- **django-humanize** – number formatting
- (ckeditor is referenced/commented out in settings)

### Configuration / environment
- **environs** / **python-dotenv** – reads `.env` (`DJANGO_SECRET_KEY`,
  `DJANGO_DEBUG`)
- **dj-database-url / dj-email-url / dj-cache-url** – URL-based settings for DB,
  email and cache

### Frontend
- Django Templates (server-rendered HTML)
- **Bootstrap 4** (via crispy-bootstrap4) + custom CSS
- Custom CSS/JS assets under `static/` (home, aboutus, main, vendor)
- Vendored icon fonts: FontAwesome, Themify, Flaticon, LineIcons, IranSansX
- Product/banner/slider imagery under `static/img/`

### Other libraries
- **Pillow** – `ImageField` image handling
- **requests / requests-oauthlib / oauthlib / PyJWT** – OAuth/social auth deps
- **paramiko / cryptography / cffi / pycparser** – transitive security deps

### Tooling / deployment
- **Docker** (`Dockerfile` on `python:3.12`) and **Docker Compose** with a
  `web` service and a `postgres:16` `db` service
- **git** version control, **PyCharm** (`.idea/`) and **VS Code** (`.vscode/`)

## Project tree

```
project16_onlineshop_uniproject/
├── manage.py                     # Django CLI entry point
├── requirements.txt              # Python dependencies (UTF-16 encoded)
├── Dockerfile                    # python:3.12 image
├── docker-compose.yml            # web + postgres:16 db services
├── .dockerignore
├── .gitignore
├── r2.txt / rr2.txt              # scratch files (gitignored)
├── project_.md                   # this file
│
├── config/                       # project package (settings & routing)
│   ├── __init__.py
│   ├── settings.py               # apps, DB, i18n, allauth, jalali, crispy
│   ├── urls.py                   # root URLconf (admin, allauth, rosetta, apps)
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/                     # custom user & auth
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                  # CustomUserCreation/ChangeForm
│   ├── models.py                 # CustomUser(AbstractUser)
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
├── pages/                        # static / marketing pages
│   ├── __init__.py
│   ├── admin.py / apps.py / models.py / tests.py
│   ├── urls.py                   # home, aboutUs
│   ├── views.py                  # HomePageView, AboutUsPageView
│   ├── migrations/
│   │   └── __init__.py
│   └── templates/pages/
│       └── aboutus.html
│
├── products/                     # catalog, products, comments
│   ├── __init__.py
│   ├── admin.py                  # ProductAdmin + CommentsInline (Jalali)
│   ├── apps.py
│   ├── forms.py                  # CommentForm
│   ├── models.py                 # Product, Comment, ActiveCommentsManager
│   ├── urls.py                   # list, detail, comment_create, test_translation
│   ├── views.py                  # ProductListView, ProductDetailView, ...
│   ├── tests.py
│   ├── locale/fa/LC_MESSAGES/    # django.po / django.mo (Persian)
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_comment.py
│   │   ├── 0003_rename_datetime_created_comment_datetime_created.py
│   │   ├── 0004_product_cover_alter_comment_stars_alter_comment_text.py
│   │   └── 0005_alter_product_datetime_created.py
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── comment_tags.py        # only_active_comments filter
│   └── templates/products/
│       ├── product_list.html
│       ├── product_detail.html
│       └── test_hello.html
│
├── cart/                         # session-based shopping cart
│   ├── __init__.py
│   ├── admin.py / apps.py / models.py / tests.py
│   ├── cart.py                   # Cart class (session-backed)
│   ├── context_processors.py     # injects `cart` into templates
│   ├── forms.py                  # AddToCartProductForm
│   ├── urls.py                   # cart_detail, cart_add, cart_remove
│   ├── views.py
│   ├── locale/fa/LC_MESSAGES/    # django.po / django.mo (Persian)
│   ├── migrations/
│   │   └── __init__.py
│   └── templates/cart/
│       ├── cart_detail.html
│       └── cart_sidebar.html
│
├── persian_translate/            # Persian number/price template helpers
│   ├── __init__.py
│   ├── admin.py / apps.py / models.py / tests.py / views.py
│   ├── migrations/
│   │   └── __init__.py
│   └── templatetags/
│       ├── __init__.py
│       └── persian_translation_tags.py   # translate_number, price_comma
│
├── templates/                    # project-wide templates
│   ├── _base.html                # base layout (header/nav)
│   ├── _footer.html
│   ├── topheader.html
│   ├── home.html                 # landing page
│   └── account/                  # allauth overrides
│       ├── email_confirm.html
│       ├── login.html
│       ├── logout.html
│       ├── signup.html
│       └── email/
│           ├── email_confirmation_message.txt
│           └── email_confirmation_subject.txt
│
├── static/                       # source static assets
│   ├── css/                      # aboutus, _base, home, main, vendor
│   ├── js/                       # main.js, vendor.js
│   ├── fonts/                    # FontAwesome, Themify, Flaticon, IranSansX, ...
│   └── img/                      # banner, bg, blog, brand, icons, logo,
│                                 #   products, slider, team, testmonial, ...
│
├── staticfiles/                  # collectstatic output (admin, ckeditor, css,
│                                 #   fonts, img, js)
│
├── media/                        # user-uploaded files
│   ├── media/product/product_cover/
│   └── product/product_cover/    # product cover images
│
├── a_doc /                       # docs (note: folder name has a trailing space)
│   └── about-us.md               # Persian "About Us" copy
│
├── .idea/                        # PyCharm project settings
│   └── ... (misc.xml, modules.xml, workspace.xml, inspectionProfiles/, ...)
├── .vscode/
│   └── settings.json
└── venv/                         # local virtual environment (gitignored)
```

## Apps summary

| App | Responsibility |
|-----|----------------|
| `config` | Project settings, root URLconf, WSGI/ASGI |
| `accounts` | Custom user model + auth forms |
| `pages` | Home page and About Us page |
| `products` | Product catalog, detail, comments/reviews |
| `cart` | Session-based cart and its UI |
| `persian_translate` | Persian digit and price formatting template filters |

## How to run (from the config present)

With Docker Compose:

```bash
docker compose up --build
# app: http://localhost:8000
```

Or locally (requires env vars and a PostgreSQL DB):

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

> Note: `requirements.txt` is UTF-16 encoded, which some tools read as binary.
> Required env vars: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG` (see `config/settings.py`).
