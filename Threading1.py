import threading

#쓰레드에서 실행할 Execute 함수선언
def execute(number):
    """
    function thread
    """
    print(threading.currentThread().getName(), number)

if __name__ == '__main__':
    #execute 함수 할당 
    for i in range(1,8):
        my_thread = threading.Thread(target=execute, args=(i,))
        my_thread.start()
