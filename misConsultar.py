# crear atributo
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()

# crarlo y salvarlo
Blog.objects.create(name='Beatles Blog', tagline='All the latest Beatles news.')

# asi lo creas asignadole su id
b4 = Blog(id=3, name='Not Cheddar', tagline='Anything but cheese.')

/* Su funcion es actualizar de muchos a muchos mediante el metodo add*/
from blog.models import Blog, Author, Entry
joe = Author.objects.create(name="Joe")
joe.save()

/*En esta seccion anexa datos para guardalos,*/
>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> john.save()
>>>paul.save()
>>>george.save()
>>>ringo.save()

/*obtiene una instruccion de seleccion y un filtro, es decir se obtiene uun query  y se llama los objetos*/
>> Blog.objects
<django.db.models.manager.Manager object at ...>
>>> b = Blog(name='Foo', tagline='Bar')
>>> b.objects

/* Obtiene todos los datos guardados en la clase entry*/
>>> all_entries = Entry.objects.all()

/* Es un query de filtro para obtener entradas desde ese año*/
Entry.objects.filter(pub_date__year=2006)
/* nota en mi django no se pudo usar ese comando en su caso se uso:*/
Entry.objects.all()
>>> y2006 = Entry.objects.filter(pub_date__year=2006)
/* este comando te excluye los datos del año que selecciones*/
>>> not2006 = Entry.objects.exclude(pub_date__year=2006)

specific_entries = Entry.objects.exclude(pub_date__gte=datetime.date.today()