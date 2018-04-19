from django.conf.urls import patterns, include, url
from django.contrib import admin
from webapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'obapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#JODER ESTATE ATENTA PORQUE TIENES QUE PONER UN ARGUMENTO ABSOLUTO E INCLUIR EN EL NOMBRE DONDE ESTA
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',"webapp.views.index", name = 'index'),
)
