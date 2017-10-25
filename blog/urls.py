from django.conf.urls import url
from django.contrib import admin

import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^baby/$', views.baby, name='baby'),
    url(r'^main/$', views.homepage, name='homepage'),
    url(r'^edit/$', views.edit_page, name='edit_page'),
    url(r'^edit/over/(?P<page_id>\d*)/$', views.edit_action, name='edit_action'),
    url(r'^article/(?P<page_id>\d+)/$', views.articlepage, name='article'),
    url(r'^rechange/(?P<page_id>\d+)/$', views.rechange, name='rechange'),
]
