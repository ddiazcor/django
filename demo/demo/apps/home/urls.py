from django.conf.urls import patterns,url

urlpatterns = patterns('demo.apps.home.views',
                       url(r'^$','index_view',name='vista_principal'),
)