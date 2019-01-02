import logging

'''
5 níveis de mensagens de saída
INFO
DEBUG
WARNING
ERROR
CRITICALx
'''


def execute():
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='hello.log', level=logging.INFO, filemode='w', format=format, datefmt='%d/%m/%y %I:%M:%S %p')
    logger = logging.getLogger(__file__)

    logger.info('Mensagem informativa')
    logger.debug('Mensagem de debug')
    logger.error('Um erro aconteceu')


if __name__ == '__main__':
    execute()
