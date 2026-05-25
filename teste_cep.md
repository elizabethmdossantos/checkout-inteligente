## Parte 1 - Documentação Casos de teste

ID | Cenário de Teste | Entrada (CEP) | Comportamento Esperado | Status Esperado (HTTP) |
|---|---|---|---|---|
**CT-01** | CEP Válido (Caminho Feliz) | 01001000 | Retorna endereço correto (Praça da Sé, São Paulo) | 200 OK
**CT-02** | CEP Inexistente (Formato Válido) | 99999999 | Retorna um JSON contendo a chave "erro": true | 200 OK
**CT-03** | CEP com Formato Inválido (Letras) | ABCDE-XYZ | Retorna uma página de erro (HTML) ou Bad Request |400 Bad Request
**CT-04** | CEP com Má Formatação (Espaços) | 01001 000 | Retorna Bad Request devido ao caractere inválido | 400 Bad Request
**CT-05** | CEP com Hífen (Formato Válido) | 01001-000A | API deve tratar o hífen e retornar o endereço com sucesso | 200 OK
**CT-06** | CEP Incompleto (Menos dígitos) | 123 | Retorna erro de requisição devido ao tamanho incorreto | 400 Bad Request

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
