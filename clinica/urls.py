from django.urls import path, include
from .views import paciente_create, medico_create, registro_create, consulta_create, prescricao_create
from .views import home
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, MedicoViewSet, ConsultaViewSet, RegistroSaudeViewSet, PrescricaoViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'registros', RegistroSaudeViewSet)
router.register(r'prescricoes', PrescricaoViewSet)



urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),     # API com prefixo 'api/'
    path('paciente/create/', paciente_create, name='paciente_create'),
    path('medico/create/', medico_create, name='medico_create'),
    path('registrosaude/create/', registro_create, name='registrosaude_create'),
    path('consulta/create/', consulta_create, name='consulta_create'),  # rota para o form
    path('prescricao/create/', prescricao_create, name='prescricao_create')

]
