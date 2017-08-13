from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf import settings

def main(_):
    return HttpResponseRedirect("/pics")

urlpatterns = [
    url(r'^pics/', include('pics.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
]


DEBUG=True
if DEBUG:
    from django.conf.urls.static import  static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
