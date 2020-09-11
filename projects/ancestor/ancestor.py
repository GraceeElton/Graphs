from util import Stack, Queue  # These may come in handy



def earliest_ancestor(ancestors, starting_node):
    # no parents means earliest

    # use DTS to find the destinating or starting node
    # once we have located we the person follow their line to find
    # the earliest ancestor

    # [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    # starting_node = 6
    #(3, 6)
    #(5, 6)
    # starting_node = 3
    #(2, 3)
    #(1, 3)
    # starting_node = 5
    #(4, 5)
    # starting_node = 4
    # reached no more parents but still need to check 3 & 5
