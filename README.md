# Blog proyecto académico sobre Python & Django

Blog con Python & Django.

## Comenzando con Python & Django

Este proyecto fue inicializado con Python [https://www.python.org/] y Django [https://www.djangoproject.com/].

## Sobre el proyecto

Este proyecto fue llevado a cabo con fines académicos, tratando de respetar las mejores prácticas obtenidas en clase, en el marco del curso de Python brindado por CoderHouse.

El proyecto consiste en la realización de un blog, a través de la cual se podrán probar las principales funcionalidades aprendidas.

Para la realización del proyecto, se instalaron las siguientes dependencias:

- landing page modelo basada en Bootstrap [https://startbootstrap.com/theme/agency]
- "Django Crispy Forms" para implementar estilos basados en Bootstrap a los formularios Django [https://django-crispy-forms.readthedocs.io/en/latest/index.html]

### Modelo

- Author: se registra el nombre, apellido, email y especialidad del autor.
- Post: se registra el título, subtítulo, contenido y fecha de creación del post.
- Topic: se registra el nombre del tema.

### Templates

- layout.html: pantalla "padre", de donde heredan el resto de los templates.
- index.html: pantalla principal. Hereda de layout.html.
- register.html: pantalla para formularios "POST" y "GET". Hereda de layout.html.
- result.html: pantalla para mostrar el resultado de la búsqueda de los formularios y "GET". Hereda de layout.html.

### Vistas

- index: pantalla principal que invoca el contenido de la landing page: autores, posts y temas. Utiliza el template "index.html".
- register: pantalla
- create_author: crea un nuevo autor. Es invocado desde un formulario POST.
- create_post: crea un nuevo post. Es invocado desde un formulario POST.
- create_topic: crea un nuevo tema. Es invocado desde un formulario POST.
- get_author: obtiene un autor por ID. Es invocado desde un formulario GET.
- get_post: obtiene un autor por ID. Es invocado desde un formulario GET.
- get_topic: obtiene un autor por ID. Es invocado desde un formulario GET.

### Estructura

- /App: se encuentra la página "landing" del blog, donde se listan los temas, posts y autores.
- /App/register - POST forms: incluye tres formularios para el ingreso de los datos de cada clase del modelo: autores, posts o temas. Se utiliza el método "POST". En cada formulario se registra el nuevo contenido del blog, que se visualiza en "/app".
- /App/register - GET forms: incluye tres formularios para buscar los autores, posts o temas por ID. Se utiliza el método "GET".
- /App/result: se visualiza el resultado de la búsqueda realizada mediante los formularios "GET". Si no encuentra el registro, muestra un mensaje indicando tal situación.

### Samples

Se dejan a disposición tres imágenes con las pantallas del sistema.

- /App/samples/20220511_app_.png
- /App/samples/20220511_app_register_.png
- /App/samples/20220511_app_result_.png

