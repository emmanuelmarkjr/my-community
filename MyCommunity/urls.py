from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin

from activities import views as activities_views
from authentication import views as mycommunity_auth_views
from home import views as home_views
from search import views as search_views
from authentication.views import ResetPasswordRequestView
from authentication.views import PasswordResetConfirmView


admin.autodiscover()

urlpatterns = [
    url(r'^$', home_views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', auth_views.login, {'template_name': 'home/cover.html'},
        name='login'),
    url(r'^password_success/$', mycommunity_auth_views.password_success, name='password_success'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', mycommunity_auth_views.signup, name='signup'),
    url(r'^forgot/$', ResetPasswordRequestView.as_view(), name='forgot'),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
    url(r'^settings/$', home_views.settings, name='settings'),
    url(r'^settings/picture/$', home_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', home_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', home_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^settings/password/$', home_views.password, name='password'),
    url(r'^network/$', home_views.network, name='network'),
    url(r'^feeds/', include('feeds.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^messages/', include('messenger.urls')),
    url(r'^notifications/$', activities_views.notifications,
        name='notifications'),
    url(r'^notifications/last/$', activities_views.last_notifications,
        name='last_notifications'),
    url(r'^notifications/check/$', activities_views.check_notifications,
        name='check_notifications'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^(?P<username>[^/]+)/$', home_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)