from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from backend.views import *
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'service_companies', ServiceCompanyViewset)
router.register(r'technical_models', TechnicalModelViewset)
router.register(r'transmission_models', TransmissionModelViewset)
router.register(r'engine_models', EngineModelViewset)
router.register(r'driving_bridge_models', DrivingBridgeModelViewset)
router.register(r'controlled_bridge_models', ControlledBridgeModelViewset)
router.register(r'types_of_maintenance', TypeOfMaintenanceViewset)
router.register(r'recovery_methods', RecoveryMethodViewset)
router.register(r'machines', MachineViewset)
router.register(r'maintenances', MaintenanceViewset)
router.register(r'claim', ClaimViewset)
router.register(r'clients', ClientViewset)
router.register(r'organizations', OrganizationViewset)
router.register(r'failure_nodes', FailureNodeViewset)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
