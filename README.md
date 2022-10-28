# Bienvenido a mi Crud de projects

- creo el projecto en git y lo clono en mis directorios
`git clone direccionSshDeGit`


* crear entorno python
`python3 -m venv venv`


* activar entorno python
`source venv/bin/activate`


* seleccionar el interprete en VSCode
abrimos el editor y oprimimos f1 luego escribimos "python: select interpreter" y escogemos el que diga venv


* instalamos Django
`pip install django`


* instalar Django Rest Framework
`pip install djangorestframework`


* crear proyecto django
`django-admin startproject "nombre_proyecto" .`


* correr el servidor
`python3 manage.py runserver`


* crear app
`python3 manage.py startapp "nombre_app"`


* agregamos la aplicacion a settings
en la carpeta del proyecto vamos a
vamos al archivo settings.py y donde diga INSTALLEDS_APPS agregamos al final el nombre de la app creada 


* agregamos REST FRAMEWORK A LAS APPS
vamos al archivo settings.py y donde diga INSTALLEDS_APPS agregamos al final "rest_framework"


# CREANDO MODELOS 

###creando primer modelo
* Entramos a la carpeta de nuestra app y entramos al archivo models.py

```python
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
```

#### Creando MIGRACIONES
`python3 manage.py makemigrations`


* Ejecutando las MIGRACIONES
`python3 manage.py migrate`


#### creando Serialize
dentro de la carpeta de la app creamos un archivo llamada "serializers.py"


* ABRIMOS serializers.py y ponemos el siguiente codigo

```python
from rest_framework import serializers
from .models import Project
    class ProjectSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = ("id", "title", "description", "technology", "create_at")
			#la coma es para que se convierta en tupla
            read_only_fields = ("create_at",)
```

#### creando archivo Api
dentro de la carpeta de la app creamos un archivo llamada "api.py"


* ABRIMOS api.py y escribimos lo siguiente

```python
from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    # con esta configuracion cualquier cliente podra solicitar datos al server
    # se puede reemplazar por IsAuthenticated
    permission_classes = [permissions.AllowAny]
    serializer_class =  ProjectSerializer
```


#### creando archivo Urls
dentro de la carpeta de la app creamos un archivo llamado "urls.py"

* ABRIMOS urls.py y escribimos lo siguiente

```python
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register("api/projects" , ProjectViewSet , "projects")

urlpatterns = router.urls
```


* agregamos las URLS al proyecto 

vamos a la carpeta del proyecto y abrimos el archivo "url.py" y ponemos el siguiente codigo

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("projects.urls"))
]
```
