from django.urls import path
from . import views
from .views import HomePagueView, ContactPagueView, AboutPagueView

urlpatterns = [
    path('', HomePagueView.as_view(), name="home"),
