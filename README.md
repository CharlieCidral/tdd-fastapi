# Store with FastAPI and TDD

Este repositório contém a implementação de uma loja virtual utilizando FastAPI e práticas de Desenvolvimento Guiado por Testes (TDD).

## Estrutura do Projeto

- **/store**: Contém o código fonte da aplicação da loja.
- **/tests**: Inclui os testes que seguem a metodologia TDD.

## Ferramentas e Configurações

- **.gitignore**: Lista de arquivos e diretórios ignorados pelo Git.
- **.pre-commit-config.yaml**: Configurações para o pre-commit.
- **Makefile**: Define comandos para facilitar a execução de tarefas.
- **docker-compose.yml**: Configuração para rodar a aplicação em containers Docker.
- **poetry.lock** e **pyproject.toml**: Arquivos de configuração para gerenciamento de dependências com Poetry.

## Como Usar

Para executar a aplicação localmente, siga os passos abaixo:

1. Clone o repositório.
    ```bash
    git clone https://github.com/CharlieCidral/tdd-fastapi.git
    ```
2. Instale as dependências usando Poetry.
    ```bash
    poetry install
    ```
3. Execute os testes para garantir que tudo está configurado corretamente.
    ```bash
    make test
    ```
4. Inicie a aplicação com Docker Compose.
    ```bash
    docker-compose up
    ```

## Contribuições

Contribuições são bem-vindas!

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
