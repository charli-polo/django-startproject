from django.conf.urls.defaults import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # project urls here
    (r'^$', TemplateView.as_view(template_name="fresh_start/start.html")),
)
