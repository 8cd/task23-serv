from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from ask.views import found, not_found

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$',found),
	url(r'^login/$',found),
	url(r'^signup/$', found),
	url(r'^ask/$', found),
	url(r'^ask//popular/$',found),
	url(r'^new/$', found),
	url(r'^question/(?P<qid>\d+)/$',found),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^',not_found),
)
