from django.conf.urls.defaults import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # project urls here
    # (r'^$', TemplateView.as_view(template_name="fresh_start/start.html")),
)

urlpatterns += patterns('daddy.apps.fresh_start.views',
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