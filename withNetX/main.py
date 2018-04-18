from networkx.drawing.nx_pydot import read_dot
from networkx import all_simple_paths
from itertools import chain
import sys

def main():
    try:
        graph = read_dot(sys.argv[1])
        root = next(filter(lambda R: graph.in_degree(R)==0, graph.nodes()))

        paths = list(map(
            lambda P: list(all_simple_paths(graph, source=root, target=P)),
            list((filter(lambda L: graph.out_degree(L)==0, graph.nodes)))
        ))

        list(map(lambda R: print("".join(R)), list(chain.from_iterable(paths))))

    except:
        print("Unexpected error")

if __name__ == '__main__':
    main()