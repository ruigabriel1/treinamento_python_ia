# Projeto: Backup Simples

## Objetivo
Script de exemplo para demonstrar leitura de argumentos, manipulação de arquivos e deploy como serviço.

## Execução local
1. Criar venv: `python3 -m venv env && source env/bin/activate`
2. (Opcional) instalar dependências: `pip install -r requirements.txt`
3. Testar:
   ```bash
   python main.py --source /caminho/origem --dest /caminho/destino --keep 3
   ```

## Deploy com systemd (Linux)
1. Ajuste caminhos e usuário no `meuapp.service`.
2. Copie o unit file:
   ```bash
   sudo cp meuapp.service /etc/systemd/system/meuapp.service
   sudo systemctl daemon-reload
   sudo systemctl enable meuapp.service
   sudo systemctl start meuapp.service
   sudo journalctl -u meuapp.service -f
   ```

## Windows
- Use Agendador de Tarefas para executar o script periodicamente ou empacote com `pyinstaller` para criar um executável.
