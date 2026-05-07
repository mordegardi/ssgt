import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("p", "Hello World!")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p>Hello World!</p></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("span", "I'm a span!")
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(), "<div><p><span>I'm a span!</span></p></div>"
        )

    def test_no_children(self):
        parent_node = ParentNode("div", [])

        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_multiple_children(self):
        child_node_1 = LeafNode("p", "Lorem")
        child_node_2 = LeafNode("p", "Lorem 2")
        child_node_3 = LeafNode(None, " dolor met")

        parent_node = ParentNode("div", [child_node_1, child_node_2, child_node_3])

        self.assertEqual(
            parent_node.to_html(), "<div><p>Lorem</p><p>Lorem 2</p> dolor met</div>"
        )


if __name__ == "__main__":
    unittest.main()
