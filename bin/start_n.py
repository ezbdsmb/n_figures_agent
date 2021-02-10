import threading

from client.agent import Agent
from time import sleep

if __name__ == '__main__':
    N = 12
    for i in range(N):
        a = Agent(figure='queen')
        thread = threading.Thread(target=a.run)
        thread.start()

        sleep(0.3)
