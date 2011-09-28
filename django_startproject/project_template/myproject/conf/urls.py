from django.conf.urls.defaults import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # project urls here
    # (r'^$', TemplateView.as_view(template_name="fresh_start/start.html")),
)

# app_name = 'fresh_start'
app_name = 'fresh_start_mag'
app = 'myproject.apps.%s' % app_name

urlpatterns += patterns('',
    (r'', include('%s.urls' % app )),
	# (r'^login/$', 'login'),
	#  (r'^signup/$', 'signup'),
	#  (r'^features/$', 'features'),
	#  (r'^learn/$', 'learn'), 
	#  (r'^plans/$', 'signup'),
	#  (r'^pricing/$', 'signup'),
	#  (r'^faqs/$', 'faqs'),
	#  (r'^support/$', 'support'),
	)