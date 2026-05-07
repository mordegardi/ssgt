import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        node_html_result = "<p>Hello, World!</p>"
        node_html_result_wrong = "<p>Hello World</p>"
        self.assertEqual(node.to_html(), node_html_result)
        self.assertNotEqual(node.to_html(), node_html_result_wrong)

    def test_repr(self):
        node = LeafNode("div", "This is a div node")
        self.assertEqual(repr(node), "LeafNode(div, This is a div node, None)")


if __name__ == "__main__":
    unittest.main()
