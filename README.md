# Django 4 by Example

[<img src="https://djangobyexample.com/static/v4/img/django_by_example_4_cover.png" style="width:200px;"  align="left">](https://djangobyexample.com/)

## About the Book

**Django 4 by Example** (4th edition) will guide you through the entire process of developing professional web applications with Django. The book not only covers the most relevant aspects of the framework, but it will also teach you how to integrate other popular technologies into your Django projects.

The book will walk you through the creation of four real-world applications, solving common problems, and implementing best practices, using a step-by-step approach that is easy to follow.

After reading this book, you will have a good understanding of how Django works and how to build practical, advanced web applications.

## Django Projects

The book covers a wide range of web app development topics divided into four different Django projects:

- **Blog Application** (chapters 1-3): Create a complete blog application
  - Build data models, views, and URLs
  - Implement an administration site for your blog
  - Use canonical URLs for modles and implement SEO-friendly URLs for posts
  - Build post pagination and learn how to create class-based views
  - Use forms to allow readers to share posts via email and implement a comment system using model forms
  - Add tags to posts using [django-taggit](https://github.com/jazzband/django-taggit) and recommend similar posts based on shared tags
  - Implement custom template tags to display latest posts and most commented posts
  - Implement a custom template filter to render [Markdown](https://github.com/Python-Markdown/markdown)
  - Create a sitemap and a RSS feed for your blog
  - Implement a full-text search engine using PostgreSQL

- **Social Website** (chapters 4-7): Create a website to bookmark and share images
  - Implement authentication using the Django authentication framework
  - Extend the user model with a custom profile model
  - Use the Diango messages framework
  - Build a custom authentication backend
  - Implement social authentication (OAuth2) with Facebook, Twitter, and Google using [Python Social Auth](https://github.com/python-social-auth/social-app-django)
  - Use [django-extensions](https://github.com/django-extensions/django-extensions) to run the development server through HTTPS
  - Generate image thumbnails with [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails)
  - Implement many-to-many relationships in models
  - Build a JavaScript bookmarklet with JavaScript and Django
  - Add asynchronous HTTP requests with the JavaScript Fetch API and Django
  - Implement infinite scroll pagination
  - Build a user follow system
  - Create a user activity stream and optimize QuerySets
  - Learn to use Django signals
  - Use [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) to obtain relevant debug information
  - Count image views with [Redis](https://redis.io/)
  - Build an image ranking with Redis

- **Ecommerce Application** (chapters 8-11): Create a fully-featured on-line shop
  - Build the models of the product catalog
  - Create a shopping cart using Django sessions
  - Create custom context processors
  - Manage customer orders
  - Send asynchronous notifications using [Celery](https://docs.celeryq.dev/) and [RabbitMQ](https://www.rabbitmq.com/)
  - Monitory Celery using [Flower](https://github.com/mher/flower)
  - Integrate [Stripe](https://stripe.com/) to process payments
  - Implement a webhook to receive payment notifications from Stripe
  - Build custom views in the Django administration site
  - Create admin actions and generate CSV files
  - Generate PDF invoices dynamically using [Weasyprint](https://weasyprint.org/)
  - Create a coupon system to apply disconts to orders
  - Integrate discounts with Stripe payments
  - Build a product recommendation engine using Redis
  - Add internationalization to the shop
  - Generate and manage translation files
  - Use [Rosetta](https://github.com/mbi/django-rosetta) to manage translations
  - Translate URL patterns and build a language selector
  - Translate models using [django-parler](https://github.com/django-parler/django-parler)
  - Localize forms using [django-localflavor](https://github.com/django/django-localflavor)

- **eLearning Platform** (chapters 12-13): Create an eLearning platform including a CMS
  - Build course models
  - Create and use data fixtures
  - Use model inheritance to create polymorphic Content
  - Create a custom model field to order course contents
  - Implement authentication views
  - Build a content management system using class-based views and mixins
  - Restrict access using groups and permissions
  - Build formsets to manage course contents
  - Create drag-and-drop functionality to reorder content in-place using JavaScript and Django
  - Using generic mixins from [django-braces](https://github.com/brack3t/django-braces)
  - Implement public views and student enrolment views
  - Render different type of contents and use [django-embed-video](https://github.com/jazzband/django-embed-video)
  - Cache content using the cache framework
  - Use the [Memached](https://memcached.org/) and Redis cache backends
  - Monitor Redis using [django-redisboard](https://github.com/ionelmc/django-redisboard)
