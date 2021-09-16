import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    # filename='log.log',
    filemode='w'
)  # 自定义设置日志的输出样式

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
