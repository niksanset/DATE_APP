
from django.contrib import admin
from django.urls import path
from app.views import profile_list_view, create_profile_view, profile_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_list_view),
    path('create_profile/', create_profile_view),
    path('<slug:human_slug>/', profile_detail_view , name='human'),
]
