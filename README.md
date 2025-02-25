🌐 Tech Site

🚀 Descrição
Tech Site é uma aplicação web desenvolvida em Django, seguindo a arquitetura Model-View-Template (MVT). O projeto foi estruturado para facilitar a manutenção e escalabilidade, utilizando padrões de desenvolvimento modernos.
📂 Estrutura do Projeto
1. Aplicação Principal (meu_site/)

    asgi.py / wsgi.py → Configuração para servidores ASGI e WSGI.
    settings.py → Configurações gerais do Django, incluindo bancos de dados e apps instalados.
    urls.py → Definição das rotas principais.

2. Aplicação tech_info/

Módulo que contém a lógica do site.

    migrations/ → Scripts para controle de versão do banco de dados.
    static/tech_info/ → Arquivos estáticos (CSS, JS, imagens).
    templates/tech_info/ → Templates HTML para renderização das páginas.
    __init__.py → Inicializador do módulo.
    admin.py → Configuração do Django Admin.
    apps.py → Configuração da aplicação.
    models.py → Definição dos modelos do banco de dados.
    tests.py → Testes automatizados da aplicação.
    urls.py → Rotas específicas da aplicação.
    views.py → Componentes da interface e lógica de requisição/resposta.

🛠 Como Executar

1️⃣ Clone o repositório:

git clone https://github.com/Jose6348/Tech_site.git
cd Tech_site

2️⃣ Crie um ambiente virtual e instale as dependências:

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Execute as migrações do banco de dados:

python manage.py migrate

4️⃣ Inicie o servidor de desenvolvimento:

python manage.py runserver

5️⃣ Acesse o site em:

http://127.0.0.1:8000/

🔧 Tecnologias Utilizadas

    Django 🟢 (Framework backend)
    SQLite/PostgreSQL 🛢 (Banco de dados)
    HTML, CSS, JavaScript 🎨 (Frontend)
    Django ORM 🔗 (Gerenciamento de banco de dados)

📌 Este projeto segue boas práticas para desenvolvimento de aplicações Django.
📜 Licença

Este projeto está licenciado sob a MIT License.
