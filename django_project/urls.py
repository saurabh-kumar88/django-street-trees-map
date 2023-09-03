"""django_project URL Configuration

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
from django.urls import path, include
from street_trees_app import views as tree_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

handler404 = "street_trees_app.views.page_not_found_handler"
handler500 = "street_trees_app.views.server_error_handler"
handler403 = "street_trees_app.views.permission_denied_handler"
handler400 = "street_trees_app.views.bad_request_handler"

urlpatterns = [
    path("", include("street_trees_app.urls")),
    path("404/", tree_views.page_not_found_handler),
    path("500/", tree_views.server_error_handler),
    path("403/", tree_views.permission_denied_handler),
    path("400/", tree_views.bad_request_handler),
    path("shaasan-prabandhan-page/", admin.site.urls),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
