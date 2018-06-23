# 참조 : https://www.youtube.com/watch?v=i1SW4q9yUEs
import threading, random


def splitter(words):
    mylist = words.split()
    newList = []
    while(mylist):
        newList.append(mylist.pop(random.randrange(0, len(mylist))))
        print(' '.join(newList))


if __name__ == '__main__':
    sentence = 'I am a handsome beast. Word.'
    numOfThreads = 5
    threadList = []

    print("STARTING...\n")
    for i in range(numOfThreads):
        t = threading.Thread(target=splitter, args=(sentence,))
        t.start()
        threadList.append(t)

    print("\nThread Count: " + str(threading.activeCount()) + "\n")
    print("EXITING...\n")