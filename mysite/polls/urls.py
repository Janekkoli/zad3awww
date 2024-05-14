from django.conf.urls.static import static
from django.urls import path

from mysite import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("login/", views.login_page, name="login"),
    path("artist/<int:svg_id>/", views.artist, name="artist"),
    path("svg/<int:svg_id>/", views.show_svg, name="show_svg"),
    path('delete_square/<int:square_id>/', views.delete_square, name='delete_square'),
    path('add_square/<int:svg_id>/', views.add_square, name='add_square'),
    path('logout/', views.logout_view, name='logout'),
]
