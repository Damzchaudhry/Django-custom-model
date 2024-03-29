
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from accounts.views import *


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/',include("accounts.urls")),
    path('api', include('api.urls')),
    path('', TemplateView.as_view(template_name="homepage.html")),






]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
