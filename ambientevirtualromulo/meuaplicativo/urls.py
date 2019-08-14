from django.conf.urls import url
from .views import *

urlpatterns = [

url(r'^cliente_form', cadastrar_cliente, name='cadastrar_cliente'),

]
