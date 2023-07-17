# Todo List App - Reis567
- Django project
  
Portuguese version at the end

This is a Todo List application built with Django. It allows users to create, update, and delete tasks in their task list. The application provides user authentication and registration functionality.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Credits](#credits)

## Installation

1. Clone the repository:

git clone https://github.com/Reis567/django_todo_list/

2. Navigate to the project directory:

cd todo_list

3. Create a virtual environment:
   python -m venv env

4. Activate the virtual environment:

- On macOS and Linux:

 source env/bin/activate

-  On Windows:
  env\Scripts\activate


5. Install the dependencies:
pip install -r requirements.txt


6. Run the migrations:
python manage.py migrate

7. Start the development server:

   python manage.py runserver



8. Access the application in your browser at `http://localhost:8000`.

## Usage

- Register a new account by clicking on the "Register" link on the login page.
- Login using your registered account credentials.
- Once logged in, you will be redirected to the task list page.
- On the task list page, you can view all your tasks, search for tasks, and perform actions such as marking a task as complete or deleting a task.
- To create a new task, click on the "Add" link on the task list page.
- To update the details of a task, click on the task title and edit the form.
- To delete a task, click on the delete icon next to the task.
- To logout, click on the "Logout" link on the task list page.

## Features

- User authentication: Users can register, login, and logout.
- Task list: Users can view a list of their tasks.
- Task search: Users can search for specific tasks by title.
- Task creation: Users can create new tasks.
- Task update: Users can update the details of their tasks.
- Task deletion: Users can delete their tasks.

## Credits

This Todo List application was developed by Reis567.

# Português

# Aplicativo Lista de Tarefas - Reis567
Projeto Django


Este é um aplicativo de Lista de Tarefas construído com Django. Ele permite que os usuários criem, atualizem e excluam tarefas em sua lista de tarefas. O aplicativo oferece funcionalidade de autenticação e registro de usuários.

## Sumário

- [Instalação](#instalação)
- [Uso](#uso)
- [Recursos](#recursos)
- [Créditos](#créditos)

## Instalação

1. Clone o repositório:

```
git clone https://github.com/Reis567/django_todo_list/
```

2. Navegue até o diretório do projeto:

```
cd todo_list
```

3. Crie um ambiente virtual:

```
python -m venv env
```

4. Ative o ambiente virtual:

- No macOS e Linux:

```
source env/bin/activate
```

- No Windows:

```
env\Scripts\activate
```

5. Instale as dependências:

```
pip install -r requirements.txt
```

6. Execute as migrações:

```
python manage.py migrate
```

7. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

8. Acesse o aplicativo em seu navegador em `http://localhost:8000`.

## Uso

- Registre uma nova conta clicando no link "Registrar" na página de login.
- Faça login usando as credenciais de sua conta registrada.
- Depois de fazer o login, você será redirecionado para a página da lista de tarefas.
- Na página da lista de tarefas, você pode visualizar todas as suas tarefas, pesquisar tarefas e executar ações como marcar uma tarefa como concluída ou excluir uma tarefa.
- Para criar uma nova tarefa, clique no link "Adicionar" na página da lista de tarefas.
- Para atualizar os detalhes de uma tarefa, clique no título da tarefa e edite o formulário.
- Para excluir uma tarefa, clique no ícone de exclusão ao lado da tarefa.
- Para fazer logout, clique no link "Logout" na página da lista de tarefas.

## Recursos

- Autenticação de usuário: os usuários podem se registrar, fazer login e fazer logout.
- Lista de tarefas: os usuários podem visualizar uma lista de suas tarefas.
- Pesquisa de tarefas: os usuários podem pesquisar tarefas específicas por título.
- Criação de tarefas: os usuários podem criar novas tarefas.
- Atualização de tarefas: os usuários podem atualizar os detalhes de suas tarefas.
- Exclusão de tarefas: os usuários podem excluir suas tarefas.

## Créditos

Este aplicativo Lista de Tarefas foi desenvolvido por Reis567.
