def TopologicalSort(graph, results):
    # Base case
    if len(graph) == 0:
        return results

    current_semester = []
    for key in graph.keys():
        if len(graph[key]) == 0:
            current_semester.append(key)

    # Decrease the graph
    for subject in current_semester:
        for key in graph.keys():
            if subject in graph[key]:
                graph[key].remove(subject)
        del graph[subject]
    
    # Recursive
    results.append(current_semester)
    return TopologicalSort(graph,results)