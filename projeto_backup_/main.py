#!/usr/bin/env python3
"""
Backup simples de uma pasta para outra com compressão mínima e logging.
Uso: python main.py --source /caminho/origem --dest /caminho/destino [--keep N]
"""
import argparse  # Módulo para analisar argumentos da linha de comando
import os  # Módulo para interagir com o sistema de arquivos
import shutil  # Módulo para operações de cópia e remoção de arquivos/diretórios
import datetime  # Módulo para trabalhar com datas e horas
import logging  # Módulo para registrar mensagens de log
import errno  # Módulo para códigos de erro do sistema


def setup_logging(logfile_path):
    # Configura o sistema de logging para registrar mensagens em arquivo e no console
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(logfile_path),
            logging.StreamHandler()
        ]
    )


def ensure_dir(path):
    # Garante que o diretório especificado exista, criando-o se necessário
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def timestamp():
    # Retorna a data e hora atual formatada como string para uso em nomes de arquivos
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')


def perform_backup(source, dest, keep=5):
    # Realiza o backup da pasta source para a pasta dest, mantendo no máximo 'keep' backups antigos
    if not os.path.exists(source):
        logging.error('Source path does not exist: %s', source)
        return 1

    ensure_dir(dest)
    name = f"backup_{timestamp()}"
    dest_path = os.path.join(dest, name)

    logging.info('Starting backup from %s to %s', source, dest_path)
    try:
        shutil.copytree(source, dest_path)
    except Exception as e:
        logging.exception('Backup failed: %s', e)
        return 1

    # Remove backups antigos, mantendo apenas os mais recentes conforme o parâmetro 'keep'
    backups = sorted([d for d in os.listdir(dest) if d.startswith('backup_')])
    if len(backups) > keep:
        to_delete = backups[:len(backups)-keep]
        for d in to_delete:
            path_del = os.path.join(dest, d)
            logging.info('Removing old backup: %s', path_del)
            shutil.rmtree(path_del, ignore_errors=True)

    logging.info('Backup completed successfully.')
    return 0


if __name__ == '__main__':
    # Configuração do parser de argumentos para receber parâmetros da linha de comando
    parser = argparse.ArgumentParser(description='Backup simples de pasta')
    parser.add_argument('--source', '-s', required=True, help='Pasta origem')
    parser.add_argument('--dest', '-d', required=True, help='Pasta destino onde os backups serão gravados')
    parser.add_argument('--keep', '-k', type=int, default=5, help='Quantidade de backups a manter')
    parser.add_argument('--log', default='backup.log', help='Arquivo de log')

    args = parser.parse_args()
    setup_logging(args.log)
    code = perform_backup(args.source, args.dest, keep=args.keep)
    raise SystemExit(code)
