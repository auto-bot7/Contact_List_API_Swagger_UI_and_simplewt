
from django.contrib import admin
from django.urls import path, include


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Contact List",
      default_version='v1',
      description="Swagger UI",
      terms_of_service="https://harsh.co/terms/",
      contact=openapi.Contact(email="harsh@harsh"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

''' 
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
       ---  swagger/.json for json format | swagger/.yanl for yaml
 '''
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/auth/',include('authenti_cation.urls')),
    path('api/contact/',include('contactdb.urls')),
    path('lout',include('rest_framework.urls'))
]
