from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dos-and-donts/", views.DosAndDonts, name="DosAndDonts"),
    path("whyStreetTrees/", views.whyStreetTrees, name="whyStreetTrees"),
    path("developer/", views.developer, name="developer"),
    path("get_tree_info/", views.get_tree_info, name="get_tree_info"),
    path("map/", views.render_map, name="render_map"),
    path("search_tree/", views.search_tree, name="search_tree"),
]
