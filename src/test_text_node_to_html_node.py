import unittest

from helpers import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        text = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        bold = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(bold)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a bold text node</b>")

    def test_italic(self):
        italic = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(italic)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>This is a italic text node</i>")

    def test_code(self):
        code = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(code)

        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.to_html(), "<code>This is a code text node</code>")

    def test_link(self):
        link = TextNode("This is a link text node", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(link)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://boot.dev">This is a link text node</a>',
        )

    def test_image(self):
        link = TextNode(
            "This is an image", TextType.IMAGE, "https://test.dev/testimage"
        )
        html_node = text_node_to_html_node(link)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://test.dev/testimage" alt="This is an image" />',
        )


if __name__ == "__main__":
    unittest.main()
