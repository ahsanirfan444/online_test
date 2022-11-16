
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user_management/', include('user_management.urls')),
    path('task/', include('task.urls')),
]
