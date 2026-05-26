# Plano de Testes Automatizados
## Parte 1 - Documentação Casos de teste

ID | Cenário de Teste | Entrada (CEP) | Comportamento Esperado | Status Esperado (HTTP) |
|---|---|---|---|---|
**CT-01** | CEP Válido (Caminho Feliz) | 01001000 | Retorna endereço correto | 200 OK
**CT-02** | CEP Inexistente (Formato Válido) | 99999999 | Retorna um JSON contendo a chave "erro": true | 200 OK
**CT-03** | CEP com Formato Inválido (Letras) | ABCDEXYZ | Servidor rejeita a requisição malformada |400 Bad Request
**CT-04** | CEP com Má Formatação (Espaços) | 01001 000 | Espaço quebra a URL da requisição | 400 Bad Request
**CT-05** | CEP com Hífen (Formato Válido) | 01001-000 | API trata o hífen e retorna o endereço com sucesso | 200 OK
**CT-06** | CEP Incompleto (Menos dígitos) | 123 | Tamanho insuficiente gera erro na rota da API | 400 Bad Request

## Como executar

```bash
pytest -s -v test_cep.py
```

## Exibição no terminal

```
test_cep.py::test_cep_valido PASSED
test_cep.py::test_cep_inexistente PASSED
test_cep.py::test_formato_invalido PASSED
test_cep.py::test_cep_com_espacos PASSED
test_cep.py::test_cep_com_hifen PASSED
test_cep.py::test_cep_incompleto PASSED
```

