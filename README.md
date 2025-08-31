# Curso: Python do Zero com Assistente de IA

**Visão geral**
Curso prático que leva um iniciante da instalação do Python até a execução de um projeto real em uma máquina (PC, VM ou Raspberry Pi), com a ajuda de uma IA como tutor e debugger.

**Formato**: 8 módulos (presencial ou remoto), ~16–24 horas no total.

## Conteúdo resumido
- Instalação e setup (Windows / macOS / Linux)
- Fundamentos: tipos, controle de fluxo, estruturas de dados
- Funções, módulos, I/O e manipulação de arquivos
- Ambientes virtuais, pip, `requirements.txt`
- Depuração com `pdb` e ferramentas do editor
- Projeto prático (backup simples / API / automação)
- Deploy em máquina: systemd, Agendador de Tarefas (Windows) e Docker

## Instalação rápida (comandos)
### Windows
1. Baixe e instale Python (https://python.org) — marque **Add Python to PATH**.
2. Abra PowerShell e verifique:
```powershell
python --version
python -m venv env
# Ativar o venv no PowerShell (ex.: env/Scripts/activate)
python -m pip install --upgrade pip
```

### macOS (Homebrew)
```bash
brew install python
python3 --version
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
```

### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
```

## Como usar este repositório
- `checklist_instalacao.md` — passo-a-passo de instalação por SO.
- `projeto_backup/` — exemplo pronto com `main.py`, `requirements.txt` e `systemd` unit file.
- `exercicios/` — exercícios por módulo (sugestão de organização).

## Deploy rápido (exemplo systemd)
1. Clone o repositório na máquina alvo.
2. Crie e ative o ambiente virtual: `python3 -m venv env && source env/bin/activate`.
3. Instale dependências: `pip install -r requirements.txt`.
4. Copie o unit file para `/etc/systemd/system/meuapp.service` e execute:
```bash
sudo systemctl daemon-reload
sudo systemctl enable meuapp.service
sudo systemctl start meuapp.service
sudo journalctl -u meuapp.service -f
```

## Banco de prompts úteis
- "Explique em termos leigos o que faz esse código: <cole código>"
- "Encontre bugs neste código e sugira correções: <cole>"
- "Escreva 3 testes pytest para a função X: <cole função>"

## Contato do instrutor
- Instrutor: __
- Repositório do curso: link aqui
