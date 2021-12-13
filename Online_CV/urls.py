
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from dashboard import views as dashview
from . import views
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

    path('admin/', admin.site.urls),
    # path('', views.homepage),
    path('', dashview.dashboard_view),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('accountss/', include('allauth.urls')),
    path('createpages/', include('createpage.urls')),

    path('', include('django.contrib.auth.urls'))

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)