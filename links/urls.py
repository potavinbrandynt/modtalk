from django.conf.urls import url
from .views import LinkListView


urlpatterns = [
    url(r'^$',
        LinkListView.as_view(), 
        name='home'),
]