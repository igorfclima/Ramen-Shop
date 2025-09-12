# Ramen Shop - Sistema de Pedidos em Python

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)

Um sistema de linha de comando (CLI) para simular o fluxo de pedidos de um restaurante de Lamen (Ramen Shop), desenvolvido em Python com foco em boas práticas de programação e princípios de design SOLID.

## 📜 Sobre o Projeto

Este projeto implementa a lógica de negócio de um restaurante, desde a criação de um pedido customizado pelo cliente, passando por uma fila de preparo na cozinha, até o registro final no caixa para o balanço financeiro. É um exercício prático para aplicar conceitos de Programação Orientada a Objetos (POO) de forma clara e modular.

## ✨ Features

-   **Criação de Pedidos:** Interface para montar um pedido com base em um menu pré-definido (tamanho, proteína, adicionais).
-   **Fila de Processamento:** Os pedidos são enviados para uma fila única, garantindo a ordem de preparo (FIFO - First-In, First-Out).
-   **Atualização de Status:** Acompanhamento do ciclo de vida do pedido ("Recebido", "Em Preparação", "Pronto", "Retirado").
-   **Balanço Financeiro:** Geração de um relatório diário com a quantidade de pedidos, receita total e o ticket médio.

## 🛠️ Arquitetura e Design

A arquitetura do sistema foi projetada seguindo os princípios **SOLID** para garantir um código desacoplado, coeso, testável e de fácil manutenção.

-   **(S) Single Responsibility Principle:** Cada classe (`Order`, `Kitchen`, `CashRegister`, etc.) possui uma única responsabilidade bem definida.
-   **(O) Open/Closed Principle:** A estrutura permite a extensão com novas funcionalidades (ex: novos itens, promoções) sem modificar o código existente.
-   **(L) Liskov Substitution Principle:** O design suporta herança de forma que subtipos possam substituir seus tipos base sem quebrar a lógica.
-   **(I) Interface Segregation Principle:** As interfaces das classes são enxutas e específicas para suas funções, evitando "classes faz-tudo".
-   **(D) Dependency Inversion Principle:** O sistema utiliza injeção de dependência (`RamenShopSystem` recebe `Kitchen` e `CashRegister`), facilitando os testes e a flexibilidade.

## 💻 Tecnologias Utilizadas

-   **Linguagem:** Python 3.10+
-   **Testes:** `unittest` (módulo padrão do Python)
-   **Qualidade de Código:** Aderência ao guia de estilo PEP 8.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

### Pré-requisitos

-   [Python 3.10](https://www.python.org/downloads/) ou superior
-   [Git](https://git-scm.com/)

### Instalação

1.  Clone o repositório:
    ```sh
    git clone [https://github.com/seu-usuario/ramen-shop-project.git](https://github.com/seu-usuario/ramen-shop-project.git)
    ```

2.  Navegue até o diretório do projeto:
    ```sh
    cd ramen-shop-project
    ```

3.  Crie e ative um ambiente virtual:
    ```sh
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  Se houver um arquivo `requirements.txt` ou `requirements-dev.txt`, instale as dependências:
    ```sh
    pip install -r requirements-dev.txt
    ```

## ▶️ Execução

Para iniciar a simulação do restaurante, execute o arquivo principal:

```bash
python main.py
```
## 📌 Como Rodar os Testes

Para garantir a integridade e o correto funcionamento das classes, execute os testes unitários com o seguinte comando a partir da raiz do projeto:

```bash
python -m unittest discover -s tests
```

Para iniciar a simulação do restaurante, execute o arquivo principal:
```sh
python main.py
```

## 📁 Estrutura do Projeto
```
ramen-shop-project/
├── src/
│   ├── menu_item.py
│   ├── order.py
│   ├── kitchen.py
│   ├── cash_register.py
│   └── ramen_shop_system.py
├── tests/
│   ├── test_order.py
│   └── ... (outros arquivos de teste)
├── main.py
└── README.md
```
