"""TestTools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from tools import views

router = routers.SimpleRouter()
# router = routers.DefaultRouter()
router.register(r'tools', views.ProjectsViewSet)

urlpatterns = [
    # path('', IndexView.as_view()),
    # path('projects', views.ProjectsList.as_view()),
    # path('projects/<int:pk>', views.ProjectsDetail.as_view()),
    # path("projects", views.ProjectsViewSet.as_view({
    #     "get": "list",
    #     "post": "create"
    # }), name="projects-list"),
    # path('projects/<int:pk>', views.ProjectsViewSet.as_view(
    #     {
    #         "get": "retrieve",
    #         "put": "update",
    #         "delete": "destroy"
    #     })),
    # path("projects/names", views.ProjectsViewSet.as_view({
    #     "get": "names"
    # }), name="projects-name"),
    # path('projects/<int:pk>/interfaces', views.ProjectsViewSet.as_view({
    #     "get": "interfaces",
    # })),
    path("", include(router.urls))
]
