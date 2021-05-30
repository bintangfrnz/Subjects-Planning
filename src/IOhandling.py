def getResource(filename):
    graph = {}
    with open('../testcase/' + filename) as f:
        line = f.readline()
        while line:
            nodes = ''.join([c for c in line if c not in " .\n"]).split(',')
            graph[nodes[0]] = nodes[1:]
            line = f.readline()
    return graph

