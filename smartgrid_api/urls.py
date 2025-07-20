"""
URL configuration for smartgrid_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from smartgrid_api.views import AuditViewSet, NonConformiteViewSet, RegisterView, LoginView, GridSchemaView, AuditExportView, AuditStatsView, ExportAuditCSVView
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from smartgrid_api.models import Audit
from django.http import HttpResponse
import pandas as pd
import io
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

router = DefaultRouter()
router.register(r'audits', AuditViewSet, basename='audit')
router.register(r'nonconformites', NonConformiteViewSet, basename='nonconformite')

def debug_catchall(request, *args, **kwargs):
    print(f"DEBUG CATCHALL: {request.method} {request.path} -- ARGS: {args}, KWARGS: {kwargs}")
    return JsonResponse({'detail': f'No match for {request.path}', 'args': args, 'kwargs': kwargs}, status=404)

def test_export(request):
    print('TEST EXPORT ROUTE HIT')
    return JsonResponse({'result': 'test export route works'})

def test_export_pk(request, pk):
    print(f'TEST EXPORT ROUTE HIT FOR PK={pk}')
    return JsonResponse({'result': f'test export route works for pk={pk}'})

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/export-audit/<int:pk>/', ExportAuditCSVView.as_view(), name='audit-export'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/grid-schema/', GridSchemaView.as_view(), name='grid-schema'),
    path('api/audit-stats/', AuditStatsView.as_view(), name='audit-stats'),
    
   
    path('api/debug-catchall/', debug_catchall),
    path('api/test-export/', test_export),
    path('api/audits-export-test/<str:pk>/', test_export_pk, name='audit-export-test'),
  
    path('api/', include(router.urls)),
    
  
    path('api/<path:unmatched>/', debug_catchall),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import get_resolver
print("Registered URL patterns:")
for url_pattern in get_resolver().url_patterns:
    print(url_pattern)