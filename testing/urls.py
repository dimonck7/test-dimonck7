from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^requests/$', 'testing.views.requests', name='requests'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'testassignment.views.logout', name='logout'),
    url(r'^accounts/profile/$', redirect_to, {'url': '/edit/'}), #after logging go to edit-page
    url(r'^accounts/login/$', redirect_to, {'url': '/login/'}),
)