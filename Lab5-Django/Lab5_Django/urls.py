
from django.conf.urls import include, url
from django.contrib import admin
import usuario.views
import films.views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', usuario.views.home, name='home'),
    url(r'^register', usuario.views.register_request, name='register'),
    url(r'^login', usuario.views.login, name='login'),
    url(r'^home', films.views.home, name='logeado'),
    url(r'^logout', films.views.logout, name='logout'),
    url(r'^verPelis', films.views.verPelis, name='verPelis'),
    url(r'^votar', films.views.votar, name='votar'),
    url(r'^aficionados', films.views.aficionados, name='aficionados'),
]
