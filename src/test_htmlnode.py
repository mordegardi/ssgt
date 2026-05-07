import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", None, None, {"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')
        node = HTMLNode("a", "Click me", None, {"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')
        node = HTMLNode("div", None, None, {"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')

    def test_eq(self):
        node1 = HTMLNode("div", "Hello, world!", None, None)
        node2 = HTMLNode("div", "Hello, world!", None, None)
        self.assertEqual(node1, node2)
        node3 = HTMLNode("p", "Hello, world!", None, None)
        self.assertNotEqual(node1, node3)
        node4 = HTMLNode("div", "Hello, world!", None, {"class": "container"})
        self.assertNotEqual(node1, node4)


if __name__ == "__main__":
    unittest.main()
