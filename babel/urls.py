"""babel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import index, about, newsroom, publication
from catalog.viewscat import PublicationByDewey, PublicationDetail


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("newsroom/", newsroom, name="newsroom"),
        path("about/", about, name="about"),
        path("", index, name="index"),
        path("catalog/", publication, name="publication"),
        path(
            "catalog/dewey_<str:deweynumber>/",
            PublicationByDewey.as_view(),
            name="publication-dewey",
        ),
        path(
            "catalog/<int:deweynumber>_<str:authorref>_<pk>/",
            PublicationDetail.as_view(),
            name="publication-detail",
        ),
        path(
            "catalog/<pk>/", PublicationDetail.as_view(), name="publication-detail-pk",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
