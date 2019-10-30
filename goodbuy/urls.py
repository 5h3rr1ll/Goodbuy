from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from accounts import views as acccount_views
from home import views as home_views
from goodbuyDatabase import views as gd_views
from scraper import views as scraper_views
from brandScraper import views as brand_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_views.start_screen, name="home"),
    path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html"),
        name="login"),
    path("logout/", auth_views.LogoutView.as_view(
        template_name="accounts/logout.html"),
        name="logout"),
    path("register/", acccount_views.register, name="register"),
    path('profile/', acccount_views.user_profile, name="user_profile"),
    path("accounts/", include(
        ("accounts.urls","accounts"),
        namespace="accounts")),
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"),
        name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"),
        name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html"),
        name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"),
        name="password_reset_complete"),
    path("home/", include(("home.urls","home"),namespace="home")),
    path('code_scanner/', include(
        ('codeScanner.urls',"codeScanner"),
        namespace="codeScanner")),
    path('goodbuyDatabase/', include(
        ('goodbuyDatabase.urls',"goodbuyDatabase"),
        namespace="goodbuyDatabase")),
    path('scraper/', include(
        ('scraper.urls',"scraper"),
        namespace="scraper")),
    path("lookupBrands/", brand_views.scrape),
    path("isbigten/<str:brandname>/", gd_views.is_big_ten),
    path("lookup/<str:code>/", scraper_views.scrape),
    path("feedback/<str:code>/", gd_views.feedback),
]

if settings.DEBUG == True:
    urlpatterns +=  static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
