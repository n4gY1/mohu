from django.contrib import admin
from django.urls import path

from repont.views import index_view, get_reponts, repont_view, info_view, add_repont_view

urlpatterns = [
    path('', index_view,name="index"),
    path('reponts', get_reponts,name="get_reponts"),
    path('view/<int:pk>', repont_view,name="repont_view"),
    path('info',info_view,name="info"),
    path('add',add_repont_view,name="add_repont")
]
