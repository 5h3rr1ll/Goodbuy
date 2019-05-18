from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from accounts import views as acccount_views
from . import views as goodbuy_views
from home import views as home_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_views.start_screen, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("register/", acccount_views.register, name="register"),
    path('profile/', acccount_views.view_profile, name="profile"),
    path("accounts/", include(("accounts.urls","accounts"),namespace="accounts")),
    path('code/', include(('codeScanner.urls',"codeScanner"),namespace="codeScanner")),
    path('mvpLogoGrab/', include(('mvpLogoGrab.urls',"logograb"),namespace="logograb")),
    path('goodbuyDatabase/', include(('goodbuyDatabase.urls',"goodbuyDatabase"),namespace="goodbuyDatabase")),
]

if settings.DEBUG == True:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
