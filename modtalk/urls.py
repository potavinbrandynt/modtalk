"""modtalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required as auth

from django.contrib import admin
admin.autodiscover()

from links.views import LinkListView, UserProfileDetailView, UserProfileEditView
from contact import urls as contact_urls
from .views import redirect_root

urlpatterns = [
    url(r'^$', redirect_root),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', LinkListView.as_view(), name='home'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', include(contact_urls)),
    url(r'^login/$', "django.contrib.auth.views.login",
        {"template_name":"login.html"}, name="login"),
    url(r'^logout/$', "django.contrib.auth.views.logout_then_login",
        name="logout"),
    url(r'^accounts/', include("registration.backends.simple.urls")),
    url(r"^users/(?P<slug>\w+)/$", UserProfileDetailView.as_view(),
        name="profile"),
    url(r"edit_profile/$", auth(UserProfileEditView.as_view()),
        name="edit_profile"),
]
