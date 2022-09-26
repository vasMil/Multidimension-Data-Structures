# Augmented segment tree
# (A segment (closed interval) is a set of points between two points
# A and B, where A and B are included)
#
# the nodes when i print them will be presented like that [intervalStart, intervalEnd, Max].
import random
import time


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


class SegmentTree:
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

    def search_for_overlaps(self, c_node, query_integer):
        overlapping_nodes = []

        if query_integer is None:
            return

        if self.overlapping(c_node.interval, query_integer):
            overlapping_nodes.append(c_node.interval)
            print(c_node.interval)

        if (c_node.left_child is not None) and (c_node.left_child.Max > query_integer):
            self.search_for_overlaps(c_node.left_child, query_integer)

        if (c_node.right_child is not None) and (c_node.right_child.Max > query_integer):
            self.search_for_overlaps(c_node.right_child, query_integer)

    def overlapping(self, interval, integer):
        if interval[0] < integer and interval[1] > integer:
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

    def deletion(self, root_node, node_del):
        if root_node is None:
            return None

        if node_del[0] < root_node.interval[0]:
            self.deletion(root_node.left_child, node_del)
        elif node_del[0] > root_node.interval[0]:
            self.deletion(root_node.right_child, node_del)
        else:
            if node_del[1] < root_node.interval[1]:
                self.deletion(root_node.left_child, node_del)
            elif node_del[1] > root_node.interval[1]:
                self.deletion(root_node.right_child, node_del)
            else:
                # the interval for deletion is right here
                if (root_node.right_child is None) and (root_node.left_child is not None):
                    root_node.interval = root_node.left_child.interval
                    root_node.Max = root_node.left_child.Max


# def test():
#     t_root = Node([5, 10])
#     st = SegmentTree(t_root)
#     st.addition(Node([15, 25]))
#     st.addition(Node([1, 12]))
#     st.addition(Node([8, 16]))
#     st.addition(Node([14, 20]))
#     st.addition(Node([18, 21]))
#     st.addition(Node([2, 8]))
#     st.maxes(t_root)
#     st.print_tree(t_root)
#     st.search_for_overlaps(t_root, 2)


def build_tree():
    t_root = Node([5, 10])
    It = SegmentTree(t_root)
    for i in range(10000):
        start_p = random.randint(0, 100)
        end_p = random.randint(start_p + 10, start_p + 100)
        It.addition(Node([start_p, end_p]))
    It.maxes(t_root)
    It.print_tree(t_root)
    print("---overlaps-->")
    ns2 = time.time_ns()
    It.search_for_overlaps(t_root, 2)
    ns3 = time.time_ns()
    print("time for searching", ns3 - ns2)


build_tree()
