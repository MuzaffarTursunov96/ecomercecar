
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/car/', include('newproject.urls')),
    # path('api/v1/car', CarApiView.as_view()),
]
