# Checklist de Instalação — Python (Windows / macOS / Linux)

Use este checklist ao preparar máquinas dos alunos.

## Pré-requisitos
- Acesso administrador (para instalar software) — nem sempre necessário (use ambiente virtual)
- Conexão com internet
- Editor recomendado: VS Code (https://code.visualstudio.com/)

---

## Windows (passo a passo)
1. Baixar Python
   - Acesse https://python.org > Downloads > Windows > selecione latest Python 3.x
   - Execute o instalador e marque "Add Python to PATH" e "Install launcher for all users".
2. Verificar instalação
   - Abra PowerShell e execute: `python --version`
3. Criar ambiente virtual
   ```powershell
   python -m venv env
   .\env\Scripts\activate
   python -m pip install --upgrade pip
   ```
4. Instalar VS Code (opcional)
   - Baixe e instale; instale as extensões: Python (Microsoft), Pylance.
5. Problemas comuns
   - "python não é reconhecido" — verifique PATH; reinicie o terminal.
   - Permissões — rodar instalador como Administrador.

---

## macOS (passo a passo)
1. Recomendado: Homebrew
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install python
   ```
2. Verificar e criar venv
   ```bash
   python3 --version
   python3 -m venv env
   source env/bin/activate
   pip install --upgrade pip
   ```
3. VS Code: instalar e configurar extensão Python.
4. Problemas comuns
   - PATH com múltiplas versões de Python — use `python3` e `python3 -m venv`.

---

## Linux (Debian/Ubuntu)
1. Instalar pacotes base
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-venv python3-pip
   ```
2. Criar venv
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install --upgrade pip
   ```
3. systemd (para deploy)
   - Copiar unit file para `/etc/systemd/system/` e executar reload/enable/start.

---

## Verificações finais para todos os SO
- `python --version` ou `python3 --version` mostra a versão correta.
- `pip list` não retorna erros.
- O editor (VS Code) reconhece o interpretador do ambiente virtual.

---

## Atividades pós-instalação
- Criar e executar `ola_mundo.py` com: `print("Olá, mundo")`.
- Executar o script de exemplo do `projeto_backup`.
