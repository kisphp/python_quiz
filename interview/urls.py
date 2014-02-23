from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'questions.views.homepage', name='homepage'),
    url(r'^start$', 'questions.views.startquiz', name='startquiz'),
    url(r'^quiz/(?P<id>\d+)', 'questions.views.question', name='question'),
    url(r'^finish', 'questions.views.finish', name='finish'),
    url(r'^logout', 'users.views.user_logout', name='logout'),
    url(r'^login', 'users.views.user_login', name='login'),

    url(r'^admin/', include(admin.site.urls)),
)
