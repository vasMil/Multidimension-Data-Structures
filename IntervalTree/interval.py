# Augmented interval tree
# the nodes when i print them will be presented like that [intervalStart, intervalEnd, Max].
class Node:
    def __init__(self, interval):
        self.interval = interval
        self.left_child = None
        self.right_child = None
        self.Max = interval[1]

    # def has_child(self):
    #     if self.left_child or self.right_child:
    #         return True
    #     return False


class IntervalTree:
    def __init__(self, root):
        self.root = root

    # Builds the tree and matches the correct Max in each node--->

    def addition(self, new_node):
        node = self.root

        while node is not None:
            if new_node.interval[1] > node.Max:
                node.Max = new_node.interval[1]

            if new_node.interval[0] <= node.interval[0]:
                if node.left_child is None:
                    node.left_child = new_node
                    return
                node = node.left_child
            else:
                if node.right_child is None:
                    node.right_child = new_node
                    return
                node = node.right_child

    def search_for_overlaps(self, c_node, query_interval):
        overlapping_nodes = []

        if query_interval is None:
            return

        if self.overlapping(c_node.interval, query_interval):
            overlapping_nodes.append(c_node.interval)

        if (c_node.left_child is not None) and (c_node.left_child.Max >= query_interval[0]):
            self.search_for_overlaps(c_node.left_child, query_interval)

        self.search_for_overlaps(c_node.right.child, query_interval)

    def overlapping(self, interval1, interval2):
        if interval1[0] <= interval2[1] and interval2[0] <= interval1[1]:
            return True

        return False

    # in-order traversal

    def print_tree(self, node):
        if node is None:
            return
        if node.left_child is not None:
            self.print_tree(node.left_child)

        print(node.interval)

        if node.right_child is not None:
            self.print_tree(node.right_child)


t_root = Node([5, 10])
It = IntervalTree(t_root)
It.addition(Node([15, 25]))
It.addition(Node([1, 12]))
It.addition(Node([8, 16]))
It.addition(Node([14, 20]))
It.addition(Node([18, 21]))
It.addition(Node([2, 8]))
It.print_tree(t_root)
