from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^profile/(\d+)',views.profile, name='profile'),
    url(r'^profile',views.own_profile, name='myprofile'),
    url(r'^edit_profile/(?P<username>\w{0,50})',views.edit_profile,name='edit_profile'),
    url(r'^like/(\d+)$',views.like,name='like'),
    url(r'^image/(?P<image_id>\d+)', views.single_image, name='single_image'),
    url(r'^search/', views.search, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)