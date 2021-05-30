import os.path
import timeit

from IOhandling import getResource, ShowResult
from Graph import TopologicalSort

def Planning(filename):
    print("\nFile: \"{}\"".format(filename))
    print("Sorting...")
    start = timeit.default_timer()

    graph = getResource(filename)
    result = TopologicalSort(graph,[])

    stop = timeit.default_timer()
    ShowResult(result)

    print("Time: {} s".format(stop-start))
    

# MAIN PROGRAM
print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("┃       Subject Planning (Decrease and Conquer)       ┃")
print("┃               by: Bintang Fajarianto                ┃")
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

QnA = input("Check all testcase (y/n)?\n>> ")
if QnA == 'y':
    allfiles = [f for f in os.listdir('../testcase/') if os.path.isfile(os.path.join('../testcase/', f)) and f.endswith('.txt')]

    for f in allfiles:
        Planning(f)

    print("┏━━━━━━━━━━━━━┓\n┃     END     ┃\n┗━━━━━━━━━━━━━┛")

elif QnA == 'n':
    while 1:
        print("\nInput filenames (TC1.txt / ... / TC10.txt)")
        filename = input(">> ")
        while not os.path.isfile('../testcase/' + filename):
            print("File not found!\n")
            print("Input filenames (TC1.txt / ... / TC10.txt)")
            filename = input(">> ")
        
        Planning(filename)

        QnA = input("\nCheck other testcase (y/n)?\n>> ")
        if QnA == 'y':
            continue
        elif QnA == 'n':
            print("┏━━━━━━━━━━━━━┓\n┃     END     ┃\n┗━━━━━━━━━━━━━┛")
            break
        else:
            print("Come on! u dumb..\n")
            break
else:
    print("Come on! u dumb..\n")