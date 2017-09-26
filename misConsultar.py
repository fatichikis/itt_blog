# crear atributo
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()

# crarlo y salvarlo
Blog.objects.create(name='Beatles Blog', tagline='All the latest Beatles news.')

# asi lo creas asignadole su id
b4 = Blog(id=3, name='Not Cheddar', tagline='Anything but cheese.')

#Su funcion es actualizar de muchos a muchos mediante el metodo add
from blog.models import Blog, Author, Entry
joe = Author.objects.create(name="Joe")
joe.save()

#aqui anexamos y trabajamos con la llave foranea
from blog.models import Entry
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
entry.blog = cheese_blog
entry.save()

#multiples objectos para actualizar
#actualizacion y filtros mediante alguna fecha
Entry.objects
    .filter(pub_date__year=2007)
    .update(headline='Everything is the same')

# actualizacion de la llave foranea
b = Blog.objects.get(pk=1)
Entry.objects
    .all()
    .update(blog=b)

# Actualizacion de los headlines en el blog
Entry.objects
    .select_related()
    .filter(blog=b)
    .update(headline='Everything is the same')

# guardar cada dato en el queryset 
for item in my_queryset:
    item.save()

#En esta seccion anexa datos para guardalos,
>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> john.save()
>>>paul.save()
>>>george.save()
>>>ringo.save()

#obtiene una instruccion de seleccion y un filtro, es decir se obtiene uun query  y se llama los objetos
>> Blog.objects
<django.db.models.manager.Manager object at ...>
>>> b = Blog(name='Foo', tagline='Bar')
>>> b.objects

/#Obtiene todos los datos guardados en la clase entry
>>> all_entries = Entry.objects.all()

# Es un query de filtro para obtener entradas desde ese año
Entry.objects.filter(pub_date__year=2006)
#nota en mi django no se pudo usar ese comando en su caso se uso:
Entry.objects.all()
>>> y2006 = Entry.objects.filter(pub_date__year=2006)
# este comando te excluye los datos del año que selecciones*/
>>> not2006 = Entry.objects.exclude(pub_date__year=2006)

specific_entries = Entry.objects.exclude(pub_date__gte=datetime.date.today()

# aqui comenzamos con los limites de los queryset
# slice te muestra todas las consultas devolviendote 5
Entry.objects.all()[:5]  # sql  LIMIT 5
										 
# LIMIT 5
Entry.objects.all()[:5]

# OFFSET 5 LIMIT 5
Entry.objects.all()[5:10]

# te regresa por cada 2 un objecto que empieze con 10
Entry.objects.all()[:10:2]

# te muestra las consultas (entradas) del dato con id# 4 es decir el dato cuarto que se anexo es el que se va mostrar
Entry.objects.filter(blog_id=4)
Entry.objects.filter(blog__name='Beatles Blog')

# F expressions  este codigo te muestra los comentarios mediante el filtro que seleccionas
from django.db.models import F
Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)

# 
Blog.objects.get(id=14) # __exact is implied
Blog.objects.get(pk=14) # pk implies id__exact

# Q object  and  or   es una pregunta de donde y una busqueda exacta con que?...
Q(question__startswith='Who') | Q(question__startswith='What') # WHERE question LIKE 'Who%' OR question LIKE 'What%'
Q(question__startswith='Who') & Q(name='leslie')

# order_by te ordena los filtros mediante la fecha
Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')

# Manager.raw()  raw sql
for p in Person.objects.raw('SELECT * FROM myapp_person'):
    print(p)
										 
# te devuleve la informacion de blogs mediante la opcion fred
a = get_object_or_404(e.authors, name='Fred')

										 
#Join
#Para abarcar una relación, basta con utilizar el nombre de campo de campos relacionados entre modelos,  hasta que obtenga el campo que desee.
# Use a custom manager 'recent_entries' in the search for an
# entry con una llave primaria de id3
e = get_object_or_404(Entry.recent_entries, pk=3)
										 
 # odbtiene una entrada cion una llave primaria  de 3
e = get_object_or_404(Entry, pk=3)
										 
Entry.objects.filter(blog__name='Beatles Blog')
Blog.objects.filter(entry__headline__contains='Lennon')

# entry con una condicion
Blog.objects.filter(
    entry__headline__contains='Lennon',
    entry__pub_date__year=2008
)

Blog.objects.exclude(
    entry__in=Entry.objects.filter(
        headline__contains='Lennon',
        pub_date___year=2008,
    ),
)

# 
Blog.objects
    .filter(entry__headline__contains='Lennon')
    .filter(entry__pub_date__year=2008)

Blog.objects.exclude(
    entry__headline__contains='Lennon',
    entry__pub_date__year=2008,
)
										 
#eliminar objectos
e.delete()

# eliminar objectos 
Entry.objects.filter(pub_date__year=2005).delete() 
										 
#Copiando las instancias 
blog = Blog(name='My blog', tagline='Blogging is easy')
blog.save()

blog.pk = None
blog.save()

#una a muchas la relacion
										 # Forward relationship
e = Entry.objects.get(id=2)
e.blog = some_blog
e.save()

# Backward relationship
b = Blog.objects.get(id=1)

# By default
b.entry_set.all()
b.entry_set.filter(headline__contains='Lennon')
b.entry_set.count()

# blog = ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries')
b.entries.all()
b.entries.filter(headline__contains='Lennon')
b.entries.count()
 
#Relacion de uno a uno en django
class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    details = models.TextField()

ed = EntryDetail.objects.get(id=2)
ed.entry

e = Entry.objects.get(id=2)
e.entrydetail = ed									
			
**/***************************************/************************/**************************
#ultimas lineas del codijo
										 
The pk Lookup Shortcut

Blog.objects.get(id=14)
Blog.objects.get(pk=14)

# te devuelve de la app blog los datos guardados el id 1,4y7
Blog.objects.filter(pk__in=[1,4,7])

# Gte devuelve los datos guardados con el id 14
Blog.objects.filter(pk__gt=14)

# Te crea filtros de busqueda con el id o llave foranea indicada
Entry.objects.filter(blog__id=3)
Entry.objects.filter(blog__pk=3)
Entry.objects.filter(blog=b) 
Entry.objects.filter(blog=b.id) 
Entry.objects.filter(blog=5) 