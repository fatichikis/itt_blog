/*Consultas*/

Blog.objects.create(name='Beatles Blog', tagline='All the latest Beatles news.')
from blog.models import Blog
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()

