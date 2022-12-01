"""Tree Building

https://exercism.org/tracks/python/exercises/tree-building

Thanks to @rvandam for the idea to use a dict as a kind of "pointer" map.
https://exercism.org/tracks/python/exercises/tree-building/solutions/rvandam
"""

class Record:
    """Representation of a record with integer self and parent ID's.

    Parameters:
    :param record_id: int - ID of the `Record`.
    :param parent_id: int - ID of the parent `Record`.
    
    Attributes:
    :param record_id: - ID of the `Record`.
    :param parent_id: - ID of the parent `Record`.

    Methods:
    None

    Raises:
    None
    """
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id

class Node:
    """A node in a `BuildTree` object.

    Parameters:
    :param node_id: int - The ID of the `Node`.
    
    Attributes:
    :node_id: int - The ID of the node.
    :children: list["Node"] - A list of `Node` objects which are children 
                              of the current node.

    Methods:
    None

    Raises:
    None
    """
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []

def BuildTree(records: list["Record"]) -> "Node":
    """Build a tree representation of hierarchical records.
    
    :records: - A list of `Record` objects with record and parent ID's.
    :return: Node - The root `Node` contains all lineage information 
                    necesarry to build the full tree.
    """
    records.sort(key=lambda x: x.record_id)
    
    if not records:
        return None
    if records[-1].record_id is not len(records)-1:
        raise ValueError("Record id is invalid or out of order.")

    nodes = dict()
    for r in records:
        if r.record_id is r.parent_id and r is not records[0]:
            raise ValueError("Only root should have equal record and parent id.")
        if r.parent_id > r.record_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
            
        node = Node(r.record_id) # create new node
        nodes[r.record_id] = node  # create a "pointer" to the node
        if not r.record_id: continue # root node has no parent; don't attach to self
        nodes[r.parent_id].children.append(node) # attach any children to their  parent
        
    return nodes[0] # the root node
