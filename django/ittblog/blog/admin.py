# -*- coding: utf-8 -*-
from blog.models import Entry, Author

from django.contrib import admin

# Register your models here.
admin.site.register(Author, Entry)
