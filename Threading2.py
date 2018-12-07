import logging
import threading

# logger 함수선언: 쓰레드 정보상세 출력
def get_logger():
    logger = logging.getLogger("Thread Example")
    logger.setLevel(logging.DEBUG)
    #fh = logging.FileHandler("threading.log") #로그파일출력
    fh = logging.StreamHandler()
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger

# 쓰레드로 실행할 execute 함수선언: logger함수 출력 
def execute(number, logger):
    """
    function thread
    """
    logger.debug('execute fucntion executing')
    result = number * 2
    logger.debug('execute functin ended with: {}'.format(result))
    
if __name__ == '__main__':
    #로거생성
    logger = get_logger()
    for i, name in enumerate(['kim', 'Lee', 'Park', 'Cho', 'Hong']):
        my_thread = threading.Thread(
            #execute함수 할당
            target=execute, name=name, args=(i,logger))
        #start메소드 호출 
        my_thread.start()
