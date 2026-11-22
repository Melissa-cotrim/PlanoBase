
# PlanoBase — Aplicação de Planeamento de Estudos

## 1. Descrição do Projeto

O PlanoBase é uma aplicação de consola desenvolvida em Python, destinada a ajudar estudantes a organizar as suas atividades académicas.

A aplicação permite gerir perfis, disciplinas, tópicos, tarefas e sessões de estudo, reunindo num único local as principais informações necessárias ao planeamento das atividades escolares.

O projeto foi desenvolvido no âmbito da unidade curricular de Ambientes de Desenvolvimento Colaborativo, do CTeSP em Sistemas e Tecnologias de Informação da Universidade do Algarve.

## 2. Objetivos

Os principais objetivos do PlanoBase são:

- Facilitar a organização das atividades académicas.
- Permitir a gestão de disciplinas e respetivos tópicos.
- Organizar tarefas com diferentes níveis de prioridade.
- Acompanhar a conclusão das tarefas.
- Agendar e gerir sessões de estudo.
- Guardar os dados para utilização posterior.
- Aplicar práticas de desenvolvimento colaborativo com Git e GitHub.

## 3. Funcionalidades Implementadas

### 3.1. Gestão de Perfil

O estudante pode:

- Criar um perfil com nome e curso.
- Consultar os dados do perfil.
- Editar as informações registadas.
- Validar os campos obrigatórios.

### 3.2. Gestão de Disciplinas

A aplicação permite:

- Adicionar disciplinas.
- Consultar as disciplinas existentes.
- Editar informações de uma disciplina.
- Eliminar disciplinas sem registos dependentes.
- Associar tópicos de estudo às disciplinas.

### 3.3. Gestão de Tópicos

Cada disciplina pode conter vários tópicos.

As operações disponíveis incluem:

- Adicionar tópicos.
- Consultar tópicos.
- Editar tópicos.
- Marcar tópicos como concluídos ou pendentes.
- Eliminar tópicos.

### 3.4. Gestão de Tarefas

O PlanoBase permite organizar tarefas académicas através das seguintes funcionalidades:

- Criar tarefas associadas a disciplinas.
- Consultar tarefas registadas.
- Editar tarefas.
- Definir prioridades: Alta, Média ou Baixa.
- Estabelecer prazos.
- Marcar tarefas como concluídas.
- Eliminar tarefas.

### 3.5. Gestão de Sessões de Estudo

O estudante pode:

- Agendar sessões de estudo.
- Associar sessões a disciplinas.
- Definir datas, horas e duração.
- Consultar sessões agendadas.
- Editar sessões existentes.
- Marcar sessões como concluídas.
- Cancelar sessões.
- Eliminar sessões.

### 3.6. Persistência de Dados

Os dados da aplicação são armazenados num ficheiro JSON.

Este mecanismo permite manter as informações registadas entre diferentes execuções do programa.

O carregamento e a gravação dos dados são geridos pelo módulo `dados.py`.

## 4. Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias:

| Tecnologia | Utilização |
|---|---|
| Python 3 | Desenvolvimento da aplicação |
| JSON | Armazenamento de dados |
| Git | Controlo de versões |
| GitHub | Repositório remoto e colaboração |
| Visual Studio Code | Ambiente de desenvolvimento |
| Markdown | Documentação do projeto |

A aplicação utiliza bibliotecas da instalação padrão do Python, não sendo necessária a instalação de dependências externas.

## 5. Estrutura do Projeto

A estrutura principal do PlanoBase é a seguinte:

    PlanoBase/
    |
    |-- main.py
    |-- dados.py
    |-- utilizadores.py
    |-- disciplinas.py
    |-- tarefas.py
    |-- sessoes.py
    |-- README.md
    |-- .gitignore

### Descrição dos ficheiros

| Ficheiro | Descrição |
|---|---|
| `main.py` | Menu principal e navegação entre funcionalidades |
| `dados.py` | Carregamento e gravação dos dados em JSON |
| `utilizadores.py` | Gestão do perfil do estudante |
| `disciplinas.py` | Gestão de disciplinas e tópicos |
| `tarefas.py` | Gestão de tarefas e prioridades |
| `sessoes.py` | Gestão de sessões de estudo |
| `README.md` | Documentação principal do projeto |
| `.gitignore` | Definição dos ficheiros ignorados pelo Git |

Durante a utilização, a aplicação guarda os dados no ficheiro `planobase_dados.json`.

Este ficheiro não é incluído no repositório, pois contém dados locais do utilizador.

## 6. Requisitos

Para executar a aplicação é necessário:

- Python 3 instalado.
- Um terminal ou ambiente de desenvolvimento.
- Os ficheiros do projeto.

Não é necessário instalar bibliotecas adicionais.

## 7. Instalação e Execução

### 7.1. Clonar o repositório

Abrir um terminal e executar:

    git clone https://github.com/Melissa-cotrim/PlanoBase.git

### 7.2. Aceder à pasta

    cd PlanoBase

### 7.3. Executar a aplicação

    python main.py

Em alguns sistemas, poderá ser necessário utilizar:

    python3 main.py

## 8. Como Utilizar

Ao iniciar a aplicação, é apresentado um menu principal com as funcionalidades disponíveis.

O utilizador deve introduzir o número correspondente à opção pretendida.

### Exemplo de utilização

1. Executar o programa.
2. Criar um perfil de estudante.
3. Adicionar uma disciplina.
4. Registar tópicos associados à disciplina.
5. Criar uma tarefa e definir a sua prioridade.
6. Agendar uma sessão de estudo.
7. Consultar ou atualizar os registos.
8. Guardar os dados e sair.

A aplicação utiliza menus interativos para facilitar a navegação.

## 9. Organização do Desenvolvimento

O desenvolvimento do PlanoBase foi organizado em etapas, utilizando Git e GitHub para controlar as alterações ao código.

### 9.1. Controlo de versões

O Git foi utilizado para:

- Registar alterações através de commits.
- Criar branches para diferentes funcionalidades.
- Manter um histórico do desenvolvimento.
- Integrar alterações na branch principal.

### 9.2. Organização das branches

Foram utilizadas branches para separar as diferentes fases de desenvolvimento.

Entre elas:

- `main` — versão principal da aplicação.
- `feature/utilizadores` — desenvolvimento da gestão de perfis.
- `feature/disciplinas` — desenvolvimento da gestão de disciplinas e tópicos.
- `feature/planeamento` — desenvolvimento de tarefas e sessões de estudo.
- `docs/readme` — atualização da documentação.

### 9.3. Pull Requests

Os Pull Requests foram utilizados para apresentar e acompanhar alterações desenvolvidas em branches separadas.

As alterações foram posteriormente integradas na branch principal, preservando o histórico de desenvolvimento.

### 9.4. Issues

As Issues do GitHub foram utilizadas para organizar e acompanhar tarefas relacionadas com o desenvolvimento da aplicação.

## 10. Testes

Foram previstos testes manuais para verificar o funcionamento das principais funcionalidades.

### Gestão de Perfil

- Criar um perfil.
- Consultar as informações registadas.
- Editar os dados.
- Verificar a validação de campos obrigatórios.

### Disciplinas e Tópicos

- Adicionar disciplinas e tópicos.
- Consultar os registos.
- Editar informações.
- Eliminar registos permitidos.
- Verificar associações entre disciplinas e tópicos.

### Tarefas

- Criar tarefas.
- Definir prioridades.
- Alterar o estado de conclusão.
- Editar e eliminar tarefas.

### Sessões de Estudo

- Agendar sessões.
- Alterar datas, horas e duração.
- Concluir ou cancelar sessões.
- Eliminar sessões.

### Persistência

- Guardar os dados.
- Encerrar a aplicação.
- Reiniciar o programa.
- Confirmar que os registos continuam disponíveis.

## 11. Funcionalidades Futuras

O desenvolvimento concentrou-se nas funcionalidades essenciais de organização e planeamento de estudos.

Algumas funcionalidades previstas inicialmente ficaram reservadas para possíveis versões futuras:

- Temporizador Pomodoro.
- Registo e análise de horas estudadas.
- Estatísticas de produtividade.
- Exportação de relatórios.

Estas funcionalidades poderão ser adicionadas em futuras atualizações.

## 12. Contexto Académico

**Instituição:** Universidade do Algarve

**Curso:** CTeSP em Sistemas e Tecnologias de Informação

**Unidade Curricular:** Ambientes de Desenvolvimento Colaborativo

**Ano Letivo:** 2026/2027

**Trabalho:** Trabalho Prático 2

## 13. Autores

Projeto desenvolvido pelos elementos do grupo:

- [Nome do elemento 1]
- [Nome do elemento 2]
- [Nome do elemento 3]

## 14. Repositório

O código-fonte e o histórico de desenvolvimento encontram-se disponíveis no GitHub:

https://github.com/Melissa-cotrim/PlanoBase