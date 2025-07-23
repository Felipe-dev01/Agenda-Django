Um sistema completo de gerenciamento de eventos pessoais desenvolvido com Django, criado durante o curso "Desenvolvimento Web com Python e Django" da plataforma [DIO](https://dio.me/).

## 📋 Sobre o Projeto

Este é um sistema web que permite aos usuários criar, gerenciar e organizar seus eventos pessoais de forma intuitiva. O projeto implementa funcionalidades completas de CRUD (Create, Read, Update, Delete) com autenticação de usuários e uma interface responsiva.

## ✨ Funcionalidades

- 🔐 **Sistema de Autenticação Completo**
  - Cadastro de novos usuários
  - Login/Logout seguro
  - Validação de dados únicos (username e email)

- 📅 **Gerenciamento de Eventos**
  - Criação de novos eventos
  - Edição de eventos existentes
  - Exclusão de eventos
  - Visualização organizada da agenda

- 🎨 **Interface Responsiva**
  - Design moderno e intuitivo
  - Totalmente responsivo para dispositivos móveis
  - Indicadores visuais para eventos atrasados

- 🔒 **Segurança**
  - Controle de acesso por usuário
  - Proteção CSRF
  - Validação de permissões

- 📊 **API JSON**
  - Endpoint para listagem de eventos em formato JSON
  - Integração facilitada com outras aplicações

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django 5.2.4
- **Frontend:** HTML5, CSS3
- **Banco de Dados:** SQLite3
- **Linguagem:** Python 3.13
- **Autenticação:** Django Auth System

## 📁 Estrutura do Projeto

```
agenda/
├── agenda/                 # Configurações principais do Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Configurações do projeto
│   ├── urls.py           # URLs principais
│   └── wsgi.py
├── core/                  # App principal
│   ├── migrations/        # Migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py          # Configuração do admin
│   ├── apps.py
│   ├── models.py         # Modelo Evento
│   ├── tests.py
│   └── views.py          # Lógica das views
├── static/               # Arquivos estáticos
│   └── css/
│       └── style.css     # Estilos customizados
├── templates/            # Templates HTML
│   ├── models/           # Templates base
│   ├── agenda.html       # Lista de eventos
│   ├── evento.html       # Formulário de eventos
│   ├── login.html        # Página de login
│   └── user.html         # Cadastro de usuários
├── db.sqlite3           # Banco de dados
└── manage.py            # Script de gerenciamento do Django
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd agenda-django
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install django
```

4. **Execute as migrações:**
```bash
python manage.py migrate
```

5. **Crie um superusuário (opcional):**
```bash
python manage.py createsuperuser
```

6. **Execute o servidor:**
```bash
python manage.py runserver
```

7. **Acesse a aplicação:**
   - Abra seu navegador em: `http://127.0.0.1:8000/`
   - Admin Django: `http://127.0.0.1:8000/admin/`

## 📱 Como Usar

### 1. Primeiro Acesso
- Acesse a aplicação e clique em "Não tem cadastro?"
- Preencha o formulário com username, email e senha
- Faça login com suas credenciais

### 2. Gerenciando Eventos
- **Criar Evento:** Clique em "Novo Evento" e preencha os dados
- **Editar Evento:** Clique em "Editar" ao lado do evento desejado
- **Excluir Evento:** Clique em "Excluir" para remover o evento
- **Eventos Atrasados:** Aparecem destacados em vermelho

### 3. API JSON
- Acesse: `/agenda/lista/<id_usuario>` para obter eventos em JSON

## 🎯 Funcionalidades Técnicas

### Modelo de Dados
O sistema utiliza o modelo `Evento` com os seguintes campos:
- `titulo`: Título do evento (CharField)
- `descricao`: Descrição detalhada (TextField)
- `data_evento`: Data e hora do evento (DateTimeField)
- `data_criacao`: Data de criação automática (DateTimeField)
- `usuario`: Relacionamento com User (ForeignKey)

### Views Principais
- `lista_eventos`: Exibe agenda do usuário logado
- `evento`: Formulário de criação/edição
- `submit_evento`: Processa dados do formulário
- `delete_evento`: Remove eventos com validação de permissão
- `json_lista_evento`: API JSON para listagem

### Sistema de Autenticação
- Cadastro com validação de duplicatas
- Login seguro com Django Auth
- Logout automático
- Controle de acesso com `@login_required`

## 🎨 Interface

A interface foi desenvolvida com foco na experiência do usuário:
- **Design Responsivo:** Adaptável a diferentes tamanhos de tela
- **Cores Intuitivas:** Eventos atrasados em vermelho, ações em azul
- **Animações Suaves:** Transições e hover effects
- **Feedback Visual:** Indicadores de loading e validação

## 🔧 Configurações

O projeto está configurado para:
- **Timezone:** America/Sao_Paulo
- **Linguagem:** Português Brasil (pt-BR)
- **Debug:** Ativado (desenvolvimento)
- **Banco:** SQLite3 (desenvolvimento)

## 📚 Aprendizado

Este projeto foi desenvolvido como parte do curso da DIO e aborda:
- Fundamentos do Django Framework
- Sistema de autenticação e autorização
- Manipulação de modelos e banco de dados
- Desenvolvimento de templates e views
- Criação de APIs simples
- Boas práticas de segurança web

## 🤝 Contribuições

Este é um projeto educacional, mas sugestões e melhorias são sempre bem-vindas!

## 📄 Licença

Projeto desenvolvido para fins educacionais durante o curso da DIO.

---

**Desenvolvido por Felipe Farias** 
*Curso: Desenvolvimento Web com Python e Django - DIO.me*
