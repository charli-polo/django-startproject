from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('myproject.apps.fresh_start.views',
    (r'^$', 'index'),
	(r'^login/$', 'login'),
	(r'^signup/$', 'signup'),
	(r'^features/$', 'features'),
	(r'^learn/$', 'learn'),	
	(r'^plans/$', 'signup'),
	(r'^pricing/$', 'signup'),
	(r'^faqs/$', 'faqs'),
	(r'^support/$', 'support'),
)