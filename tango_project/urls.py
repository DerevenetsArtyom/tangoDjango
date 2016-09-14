from django.conf.urls import include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

from rest_framework import routers

from rango import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'pages', views.PageViewSet)


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):

    def get_success_url(self, request, user):
        return '/rango/'

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
