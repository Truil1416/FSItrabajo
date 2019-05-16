# Search methods

import search

ab = search.GPSProblem('D', 'F'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.my_gestor(ab).path())
print(search.my_best_gestor(ab).path())

# Result:
#20
#[<Node F>, <Node S>, <Node R>, <Node C>, <Node D>] : 99 + 80 + 146 + 120 = 445
#6
#[<Node F>, <Node B>, <Node P>, <Node C>, <Node D>] : 211 + 101 + 138 + 120 = 570
#21
#[<Node F>, <Node S>, <Node R>, <Node C>, <Node D>] : 99 + 80 + 146 + 120 = 445
#13
#[<Node F>, <Node S>, <Node R>, <Node C>, <Node D>] : 99 + 80 + 146 + 120 = 445