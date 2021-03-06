from django.conf.urls import url
from rango import views


urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Category Actions
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),

    # About Page
    url(r'^about/$', views.about, name='about'),

    # Search
    url(r'^search/$', views.search, name='search'),

    # Go to page
    url(r'^goto/$', views.track_url, name='goto'),

    # Like category
    url(r'^like_category/$', views.like_category, name='like_category'),


    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),


    # Custom accounts
    url(r'^restricted/', views.restricted, name='restricted'),

    # url(r'^register/$', views.register, name='register'),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$', views.user_logout, name='logout'),


    ]
