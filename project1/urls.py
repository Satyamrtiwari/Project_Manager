from django.contrib import admin
from django.urls import path , include
from django.http import JsonResponse

urlpatterns = [
    path("", lambda request: JsonResponse({"status": "Backend is running"})),
    path('admin/', admin.site.urls),
    path('api/',include('app2.urls')),
]
