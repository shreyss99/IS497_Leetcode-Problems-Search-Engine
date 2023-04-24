from django.urls import path

from LC_SearchEngine import views

urlpatterns = [
    path("", views.home, name="LC_SearchEngine_Home"),
    path("about/", views.about_us, name="LC_SearchEngine_About"),
    path("data/", views.data_view, name="LC_SearchEngine_Data")
]
