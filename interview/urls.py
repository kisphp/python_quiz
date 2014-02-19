from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'questions.views.homepage', name='homepage'),
    url(r'^start$', 'questions.views.startquiz', name='startquiz'),
    url(r'^quiz/(?P<id>\d+)', 'questions.views.question', name='question'),

    url(r'^admin/', include(admin.site.urls)),
)
