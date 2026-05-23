# KANBAN BOARD

Kanban Board é um projeto desktop desenvolvido com Python e PySide6, com o objetivo de organizar tarefas de forma visual utilizando o método Kanban. O software permite gerenciar atividades ao longo de três etapas: **A Fazer**, **Fazendo** e **Feito**.

## TECNOLOGIAS UTILIZADAS

- **Python** || linguagem principal do projeto
- **PySide6** || para construção da interface gráfica 

## ORGANIZAÇÃO DO CÓDIGO

O código é monolítico, onde toda a lógica está dentro do arquivo main.py

## INICIANDO O PROGRAMA

1. Crie e ative o ambiente virtual:
   ```bash
   # Criar o venv
   python -m venv venv

   # Ativar no Windows
   venv\Scripts\activate

   # Ativar no Linux/macOS
   source venv/bin/activate
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt

   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

## FUNCIONALIDADES

- Adição de novas tarefas à lista **A Fazer** via caixa de diálogo
- Movimentação de tarefas de **A Fazer** → **Fazendo**
- Movimentação de tarefas de **Fazendo** → **Feito**
- Numeração automática dos itens em cada lista
- Cores distintas para cada coluna (vermelho, amarelo e verde)
