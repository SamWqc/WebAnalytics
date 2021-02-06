""" Running the model."""

from edmot import EdMot
from param_parser import parameter_parser
from utils import tab_printer, graph_reader, membership_saver

def main():
    """
    Parsing command line parameters, reading data, fitting EdMot and scoring the model.
    """
    args = parameter_parser()
    tab_printer(args)
    graph = graph_reader(args.edge_path)
    graph.remove_nodes_from([node for node in graph.nodes() if graph.degree()[node]<=1])

    model = EdMot(graph, args.components, args.cutoff)
    memberships = model.fit()
    membership_saver(args.membership_path, memberships)

if __name__ == "__main__":
    main()
