
from django.conf.urls import include, url
from django.contrib import admin
import usuario.views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', usuario.views.home, name='home'),
    url(r'^register', usuario.views.register_request, name='register'),
    url(r'^login', usuario.views.login, name='login'),

]
