"""etcsecure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from etcsecure import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
#    url(r'^$', 'views.index', name='index'),
#    url(r'^index.html', 'views.index', name='index')

    #url(r'^$', 'etcsecure.views.index', name='home'),
    #url(r'^index.html', 'etcsecure.views.index', name='home'),
#    url(r'^keyword-vocab.html','tools.views.kw_vocab'),
#    url(r'^backlinks.html','tools.views.bing_bl'),
#    url(r'^pr_estimate.html','tools.views.pr_est'),
#    url(r'^terms.html','tools.views.wn_lemma'),
#    url(r'^term-dict.html','tools.views.wn_dict'),
#    url(r'^term-verb.html','tools.views.verb_parse'),
#    url(r'^verb/(?P<verb>[\w\-]+)/$', 'tools.views.verb'),
#    url(r'^dict/(?P<term>[\w\-]+)/$', 'tools.views.wn_dict'),
#    url(r'^term/(?P<term>[\w\-]+)/$', 'tools.views.wn_lemma'),
#    url(r'^termj/(?P<term>[\w\-]+)/$', 'tools.views.term_js'),
#    url(r'^termjson/(?P<term>[\w\-]+)/$', 'tools.views.term_json'),


