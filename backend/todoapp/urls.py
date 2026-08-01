from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health', lambda request: HttpResponse('ok')),
    path('api/todos/', include('todos.urls')),
    path('api/payments/', include('payments.urls')),
]
