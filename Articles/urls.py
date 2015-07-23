from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('post.urls')),
    url(r'^admin/', include(admin.site.urls), name="admin"),
    url(r'^articles/', include("post.urls")),
]
