# Augmented interval tree
# the nodes when i print them will be presented like that [intervalStart, intervalEnd, Max].
class Node:
    def __init__(self, interval):
        self.interval = interval
        self.left_child = None
        self.right_child = None
        self.Max = None

    def has_child(self):
        if self.left_child or self.right_child:
            return True
        return False


class IntervalTree:
    def __init__(self, root):
        self.root = root

    # Builds the tree and matches the correct Max in each node-->

    def addition(self, new_node):
        node = self.root

        while node is not None:

            # if new_node.interval[1] > node.Max:
            #     node.interval[2] = new_node.interval[1]

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
            print(c_node.interval)

        if (c_node.left_child is not None) and (c_node.left_child.Max >= query_interval[0]):
            self.search_for_overlaps(c_node.left_child, query_interval)

        if (c_node.right_child is not None) and (c_node.right_child.Max >= query_interval[0]):
            self.search_for_overlaps(c_node.right_child, query_interval)

    def overlapping(self, interval1, interval2):
        if interval1[0] <= interval2[1] and interval2[0] <= interval1[1]:
            return True

        return False

    # in-order traversal-->

    def print_tree(self, node):
        if node is None:
            return
        if node.left_child is not None:
            self.print_tree(node.left_child)

        print(node.interval)

        if node.right_child is not None:
            self.print_tree(node.right_child)

    # finds the max for each node-->

    def maxes(self, root_node):
        if (root_node.Max is None) and (root_node.has_child()):
            max_array = []
            if root_node.left_child:
                self.maxes(root_node.left_child)
                max_array.append(root_node.left_child.Max)
            if root_node.right_child:
                self.maxes(root_node.right_child)
                max_array.append(root_node.right_child.Max)
            max_array.append(root_node.interval[1])
            root_node.Max = max(max_array)
            root_node.interval.append(root_node.Max)
            return

        else:
            root_node.Max = root_node.interval[1]
            root_node.interval.append(root_node.Max)
            return


t_root = Node([5, 10])
It = IntervalTree(t_root)
It.addition(Node([15, 25]))
It.addition(Node([1, 12]))
It.addition(Node([8, 16]))
It.addition(Node([14, 20]))
It.addition(Node([18, 21]))
It.addition(Node([2, 8]))
# It.addition(Node([8, 21]))
It.maxes(t_root)
# It.print_tree(t_root)
It.search_for_overlaps(t_root, [10, 15])
