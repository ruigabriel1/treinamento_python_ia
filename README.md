# Curso: Python do Zero com Assistente de IA

**Descrição curta**  
Repositório com material para um treinamento prático que usa inteligência artificial (ex.: ChatGPT) como assistente didático e debugger, levando um iniciante desde a instalação do Python até a execução e deploy de um projeto em uma máquina (PC, VM ou Raspberry Pi).

---

# Índice
1. [Visão geral](#visão-geral)  
2. [Estrutura do repositório](#estrutura-do-repositório)  
3. [Como começar, instalação rápida](#como-começar,-instalação-rápida)  
4. [Projeto-exemplo: `projeto_backup`](#projeto-exemplo-projeto_backup)  
5. [Deploy como serviço (systemd) — passos rápidos](#deploy-como-serviço-systemd---passos-rápidos)  
6. [Checklist de instalação (resumo)](#checklist-de-instalação-resumo)  
7. [Plano completo do treinamento (incluído)](#plano-completo-do-treinamento-incluído)  
8. [Banco de prompts para usar com IA](#banco-de-prompts-para-usar-com-ia)  
9. [Avaliação, dicas do instrutor e próximos passos](#avaliação-dicas-do-instrutor-e-próximos-passos)  
10. [Licença / Contato](#licença--contato)

---

# Visão geral

Este repositório reúne:

- Um **README.md** (este arquivo) com todas as instruções e o plano de treinamento integrado.  
- Um **checklist de instalação** (arquivo `checklist_instalacao.md`).  
- Um **projeto-exemplo** minimalista chamado `projeto_backup/` com:
  - `main.py` — script de backup simples (exemplo prático).
  - `requirements.txt`.
  - `meuapp.service` — exemplo de unit file systemd.
  - `README_PROJECT.md` — instruções do projeto.

O objetivo é que um aluno leigo consiga, com orientação e uso de um assistente de IA:
- Instalar Python e ferramentas básicas,
- Aprender fundamentos de Python (sintaxe, estruturas, I/O, módulos),
- Criar, testar e versionar um pequeno projeto,
- Colocar o projeto para rodar automaticamente em uma máquina.

---

# Estrutura do repositório

```
/ (root)
├─ README.md                      # (este arquivo)
├─ checklist_instalacao.md        # checklist de instalação por SO
└─ projeto_backup/
   ├─ main.py
   ├─ requirements.txt
   ├─ meuapp.service
   └─ README_PROJECT.md
```

---

# Como começar, instalação rápida

**Windows**
1. Baixe Python em https://python.org e marque **Add Python to PATH** no instalador.  
2. Abra PowerShell:
   ```powershell
   python --version
   python -m venv env
   .\env\Scripts\activate
   python -m pip install --upgrade pip
   ```
3. Instale VS Code e extensão Python (Microsoft), Pylance (opcional).

**macOS**
```bash
brew install python
python3 --version
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
```

**Linux (Debian/Ubuntu)**
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
```

Após ativar o `venv`, você pode rodar o projeto de exemplo:
```bash
cd projeto_backup
python main.py --source /caminho/origem --dest /caminho/destino --keep 3
```

---

# Projeto-exemplo: `projeto_backup`

**Objetivo**: demonstrar leitura de argumentos, manipulação de arquivos, logging, retenção de backups e deploy como serviço.

**Resumo dos arquivos**
- `main.py` — realiza `copytree` da pasta origem para um diretório destino com timestamp; remove backups antigos para manter apenas N últimos; grava logs.
- `requirements.txt` — vazio no exemplo (usa somente stdlib), mas pronto para adicionar dependências.
- `meuapp.service` — exemplo de unit file para systemd (ajuste `User`, `WorkingDirectory`, `ExecStart` conforme seu ambiente).
- `README_PROJECT.md` — como executar localmente e como instalar com systemd.

**Como testar localmente**
1. Ative seu ambiente virtual.
2. Execute:
   ```bash
   python projeto_backup/main.py --source /tmp/origem --dest /tmp/backups --keep 5
   ```
3. Verifique logs (`backup.log` por padrão) e a criação da pasta `backup_YYYYMMDD_HHMMSS`.

---

# Deploy como serviço (systemd) — passos rápidos

1. Ajuste os caminhos em `meuapp.service` (usuário, workingdir, caminho do venv e do script).  
2. Copie para `/etc/systemd/system/meuapp.service`:
   ```bash
   sudo cp meuapp.service /etc/systemd/system/meuapp.service
   sudo systemctl daemon-reload
   sudo systemctl enable meuapp.service
   sudo systemctl start meuapp.service
   sudo journalctl -u meuapp.service -f
   ```
3. Para Windows, use Agendador de Tarefas ou empacote com `pyinstaller` para criar um executável e agende-o.

---

# Checklist de instalação (resumo)

- Verificar versão do Python: `python --version` / `python3 --version`.
- Criar e ativar ambiente virtual: `python -m venv env` + ativação adequada por SO.
- Atualizar pip: `python -m pip install --upgrade pip`.
- Instalar editor (VS Code) e extensões recomendadas.
- Executar `ola_mundo.py` como teste rápido (`print("Olá, mundo")`).
- Testar execução do `projeto_backup`.

(Um arquivo mais detalhado `checklist_instalacao.md` está incluído no ZIP.)

---

# Plano completo do treinamento (incluído)

> Abaixo está o conteúdo completo do plano de treinamento — objetivo do curso, público, estrutura por módulos, atividades, prompts e orientações para o instrutor. Use-o como material do curso ou copie diretamente para slides/manual.

## 1. Objetivos do treinamento
- Instalar e configurar ambiente Python (Windows/macOS/Linux).
- Ensinar fundamentos: sintaxe, tipos, controle de fluxo, funções, módulos, pacotes.
- Capacitar o aluno a desenvolver, testar e executar um programa útil em uma máquina real.
- Mostrar como usar IA como tutor: pedir explicações, gerar exemplos, depurar e melhorar código.

## 2. Público-alvo
Leigos com pouca ou nenhuma experiência em programação que sabem usar um computador e abrir um terminal/linha de comando.

## 3. Duração sugerida
- Formato leve: 8 módulos — 2–3 horas por módulo (16–24 horas no total).  
- Bootcamp intensivo: 3 dias (8h/dia) com exercícios guiados.

## 4. Pré-requisitos
- Computador com internet.
- Conta em serviço de IA (opcional).
- Vontade de experimentar e errar; digitar código.

## 5. Ferramentas e materiais
- Python 3.10+.
- Editor: VS Code (recomendado) ou Thonny.
- Terminal/PowerShell.
- Git (opcional).
- Acesso a ChatGPT ou similar — incluir prompts (abaixo).

---

## 6. Estrutura do curso (módulo por módulo)

### Módulo 0 — Setup & primeiros passos
**Objetivo:** instalar Python, configurar editor e criar primeiro script.
- Instalação (Windows/macOS/Linux).
- Verificar `python --version`.
- Criar venv e ativar.
- Primeiro arquivo `ola_mundo.py` e execução.
**Atividade prática:** script que pede nome ao usuário e imprime saudação. Usar IA para revisar.

### Módulo 1 — Fundamentos: variáveis, tipos e operações
- Números, strings, booleanos, conversões, formatação.
**Atividade:** calculadora simples.

### Módulo 2 — Controle de fluxo
- `if/elif/else`, loops `for`/`while`, `break/continue`, comprehensions.
**Atividade:** jogo adivinhe o número.

### Módulo 3 — Estruturas de dados
- Listas, tuplas, dicionários, sets; iteração e métodos.
**Atividade:** gerenciador simples de contatos (buscar/ordenar/filtrar).

### Módulo 4 — Funções e módulos
- Definir funções, parâmetros, retorno, escopo.
**Atividade:** criar módulo utilitário e importá-lo.

### Módulo 5 — I/O e manipulação de arquivos
- Ler/escrever `.txt` e `.csv`, usar `with`.
**Atividade:** ler CSV e gerar relatório simples.

### Módulo 6 — Ambiente de pacotes e depuração
- `pip`, `requirements.txt`, virtualenv, `pdb` e debugger do VS Code.
**Atividade:** instalar `requests` e fazer uma chamada HTTP; depurar erro proposital.

### Módulo 7 — Projeto prático
- Escolher entre: automação (backup), API simples com Flask, bot leve.
**Atividades:** escrever, testar, documentar e versionar com Git.

### Módulo 8 — Colocar em produção / executar em máquina
- Instalar Python na máquina alvo, clonar repositório, criar venv, instalar deps.
- Transformar script em serviço/daemon (systemd/Windows Scheduler) ou empacotar com `pyinstaller`/Docker.

---

## 7. Avaliação e entrega
- Tarefas por módulo (checks).
- Projeto final (demo 3–5 min).
- Rubrica: funcionalidade mínima, boas práticas, documentação.

---

## 8. Banco de prompts (exemplos para usar com IA)

- **Explicação simples:**  
  `"Explique em termos leigos o que faz esse código: <cole código>"`
- **Gerar exemplo:**  
  `"Mostre 3 exemplos simples de como somar dois números em Python, com comentários explicativos."`
- **Gerar testes:**  
  `"Crie 5 testes unitários pytest para essa função: <cole função>"`
- **Refatorar:**  
  `"Refatore este código para ser mais legível e com tratamento de erros: <cole código>"`
- **Checklist de deploy:**  
  `"Liste passo a passo como colocar este script para rodar como serviço em Linux, assumindo que o código está em /home/user/app."`
- **Depuração:**  
  `"Tenho este erro: <mensagem de erro>. Aqui está o trecho de código: <cole>. O que está causando e como conserto?"`

---

# Avaliação, dicas do instrutor e próximos passos

**Dicas do instrutor**
- Incentive o aluno a tentar antes de pedir ajuda à IA. Errar é parte do aprendizado.
- Ensine como escrever bons prompts: contexto + objetivo + código (quando aplicável).
- Use pair programming com a IA: IA sugere; aluno revisa e aprova.
- Comece com pequenas vitórias (ex.: primeiro "Olá, Mundo" em 10 minutos).

**Próximos passos sugeridos**
- Expandir o projeto-exemplo (adicionar compressão, upload para nuvem, etc.).
- Criar exercícios de código e testes automatizados (pytest).
- Versionar o repositório e adicionar CI simples (GitHub Actions) para rodar testes.

---

# Licença e contato

Sinta-se livre para usar e adaptar este material para aulas, bootcamps ou estudo pessoal. Se quiser, posso:
- Gravar os arquivos no repositório remoto (se você fornecer acesso),
- Ajustar `meuapp.service` para caminhos/usuário do seu ambiente,
- Gerar instruções detalhadas para Agendador de Tarefas do Windows (XML/PowerShell),
- Criar um ZIP atualizado com o README já substituído no pacote.
