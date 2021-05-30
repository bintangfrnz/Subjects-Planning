def getResource(filename):
    graph = {}
    with open('../testcase/' + filename) as f:
        line = f.readline()
        while line:
            nodes = ''.join([c for c in line if c not in " .\n"]).split(',')
            graph[nodes[0]] = nodes[1:]
            line = f.readline()
    return graph

def SwitchToRoman(num):
    semester = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII"
    }
    return semester.get(num, "Only handle 8 semesters")

def ShowResult(results):
    print("--- Result ---")
    for i in range(len(results)):
        if i > 7:
            break
        
        subject = ', '.join(results[i])
        print(f'Semester {SwitchToRoman(i+1)}\t: {subject}')