from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

from .views import index, report, collect

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    # path("", index, name="index"),
    path("", report, name="report"),
    path("report/", report, name="report"),
    path("report/<str:page_name>", report, name="report"),
    path("collect/<str:page_name>", collect, name="collect"),
    path("admin/", admin.site.urls),
]
