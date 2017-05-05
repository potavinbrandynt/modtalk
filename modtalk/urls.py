from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required as auth

from django.contrib import admin
admin.autodiscover()

#from django.contrib import comments as django_comments.urls

from links.views import (LinkListView, UserProfileDetailView,
UserProfileEditView, LinkCreateView, LinkDetailView, LinkUpdateView,
LinkDeleteView, VoteFormView)

from contact import urls as contact_urls
from .views import redirect_root

urlpatterns = [
    url(r'^$', redirect_root),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
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
    url(r"^link/create/$", auth(LinkCreateView.as_view()),
        name="link_create"),
    url(r"^link/(?P<pk>\d+)$", LinkDetailView.as_view(),
        name="link_detail"),
    url(r"^link/update/(?P<pk>\d+)$", auth(LinkUpdateView.as_view()),
        name="link_update"),
    url(r"^link/delete/(?P<pk>\d+)$", auth(LinkDeleteView.as_view()),
        name="link_delete"),
    url(r'^vote/$', auth(VoteFormView.as_view()), name="vote"),
]
