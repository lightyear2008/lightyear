'''
此示例演示了日志记录的操作，logging是标准库
'''
import logging

#清空log.log文件
with open('log.log', 'w') as f:
    f.write('')

#配置日志输出格式 asctime:时间，levelname:日志级别，message:日志信息
log_format = '%(asctime)s - %(levelname)s - %(message)s'

'''
配置日志
filename:日志文件名（如果设置了控制台中就没有输出）（也可以直接填路径）
level:输出此级别及以上的日志（DEBUG<INFO<WARNING<ERROR<CRITICAL）
format:日志输出格式（见上）
备注：此函数只有第一次调用时发挥效果
'''
logging.basicConfig(filename = 'log.log',level = logging.DEBUG,format = log_format)

# 记录不同级别的日志信息
logging.debug('这是一条调试信息')
logging.info('这是一条普通信息')
logging.warning('这是一条警告信息')
logging.error('这是一条错误信息')
logging.critical('这是一条严重错误信息')
