from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest

@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo='Java',
        data_do_curso = date.today(),
        carga_horaria = '40'
    )
    return curso
    
        
@pytest.mark.django_db
def test_str_deve_retornar_string(curso):
    assert str(curso) =='Java:2024-03-04-40'
    
    
# # Retorno da string 
# def __str__(self):
#     return f'{self.titulo}:{self.data_do_curso} - {self.carga_horaria}'