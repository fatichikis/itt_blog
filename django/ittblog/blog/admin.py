# -*- coding: utf-8 -*-
from blog.models import Entry, Author

from django.contrib import admin

from django.db.models import F
# Register your models here.
admin.site.register(Author, Entry)

Entry.objects.filter(n_comments__gt=F('n_pingbacks'))

# Can use arithmetic
Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))

# Span relationships in an F() object
Entry.objects.filter(authors__name=F('blog__name'))

# Add/Subtract 'timedelta' objects
from datetime import timedelta
Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))

# Bitwise operations supported
F('somefield').bitand(16)
F('somefield').bitor(8)
