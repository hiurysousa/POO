import pytest
import json
from unittest.mock import MagicMock
from src.perguntadiscursiva import PerguntaDiscursiva
from src.llmservice import LLMService
from src.correcao import Correcao

def test_criar_prompt_correcao():
    """Garante que o prompt está sendo montado com os dados corretos da questão."""
    pergunta = PerguntaDiscursiva(
        texto="O que é encapsulamento em POO?", 
        resposta_esperada="Proteger os atributos internos de uma classe usando métodos públicos."
    )
    resposta_aluno = "É esconder as variáveis e usar getters e setters."
    
    prompt = Correcao.criar_prompt_correcao(pergunta, resposta_aluno)
    
    # Valida se as informações cruciais foram injetadas na string do prompt
    assert "O que é encapsulamento em POO?" in prompt
    assert "Proteger os atributos internos" in prompt
    assert "É esconder as variáveis" in prompt


def test_corrigir_discursiva_com_sucesso_via_mock():
    """Testa o fluxo feliz: a API responde um JSON válido e a classe Correcao o decodifica."""
    pergunta = PerguntaDiscursiva(texto="O que é uma classe?", resposta_esperada="Um molde para objetos.")
    resposta_aluno = "É a estrutura que define um objeto."
    
    # 1. Cria um mock do LLMService
    mock_service = MagicMock(spec=LLMService)
    
    # Simula a string JSON que o modelo retornaria na vida real
    json_retorno_llm = json.dumps({
        "correta": True,
        "pontuacao": 1.0,
        "feedback": "Resposta muito boa e direta.",
        "explicacao": "O aluno compreendeu que a classe funciona como a definição estrutural."
    })
    
    # Configura o método público para retornar essa string
    mock_service.fazer_chamada_api.return_value = json_retorno_llm

    # 2. Executa a correção injetando o nosso mock
    resultado = Correcao.corrigir_discursiva(pergunta, resposta_aluno, service=mock_service)

    # 3. Asserts
    assert resultado["correta"] is True
    assert resultado["pontuacao"] == 1.0
    assert resultado["feedback"] == "Resposta muito boa e direta."
    
    # Garante que a classe Correcao chamou o método exato que sobrou no diagrama do professor
    mock_service.fazer_chamada_api.assert_called_once()


def test_fallback_quando_api_retorna_erro():
    """Testa se o sistema lida com falhas de rede/API sem quebrar o programa."""
    pergunta = PerguntaDiscursiva(texto="O que é polimorfismo?", resposta_esperada="Métodos com mesma assinatura e comportamentos diferentes.")
    
    mock_service = MagicMock(spec=LLMService)
    # Simula o método disparando um erro de conexão/timeout
    mock_service.fazer_chamada_api.side_effect = Exception("Erro de conexão com o servidor do Groq")

    # Executa a correção que vai falhar internamente na chamada da API
    resultado = Correcao.corrigir_discursiva(pergunta, "Não lembro", service=mock_service)

    # Verifica se o bloco 'except' capturou a falha e retornou o dicionário padrão de erro
    assert resultado["correta"] is False
    assert resultado["pontuacao"] == 0.0
    assert "Erro na comunicação" in resultado["feedback"]