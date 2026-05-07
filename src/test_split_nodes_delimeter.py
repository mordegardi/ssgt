import unittest

from helpers import split_nodes_delimeter
from textnode import TextNode, TextType


class TestSplitNodesDelimeter(unittest.TestCase):
    def test_split_text_node(self):
        node = TextNode("This is a simple text", TextType.TEXT)
        splitted = split_nodes_delimeter([node], "`", TextType.TEXT)

        self.assertEqual(splitted[0].text, "This is a simple text")

    def test_split_bold_node(self):
        node = TextNode("This is a text with **bold** word", TextType.TEXT)
        splitted = split_nodes_delimeter([node], "**", TextType.BOLD)

        self.assertEqual(splitted[0].text, "This is a text with ")
        self.assertEqual(splitted[1].text, "bold")
        self.assertEqual(splitted[2].text, " word")

    def test_split_italic_node(self):
        node = TextNode("This is a text with _italic_ word", TextType.TEXT)
        splitted = split_nodes_delimeter([node], "_", TextType.ITALIC)

        self.assertEqual(splitted[0].text, "This is a text with ")
        self.assertEqual(splitted[1].text, "italic")
        self.assertEqual(splitted[2].text, " word")

    def test_split_code_node(self):
        node = TextNode("This is a `code` within text", TextType.TEXT)
        splitted = split_nodes_delimeter([node], "`", TextType.CODE)

        self.assertEqual(splitted[0].text, "This is a ")
        self.assertEqual(splitted[1].text, "code")
        self.assertEqual(splitted[2].text, " within text")

    def test_split_wrong_inputs(self):
        node = TextNode("This is a `code` within text", TextType.TEXT)
        splitted = split_nodes_delimeter([node], "**", TextType.CODE)

        self.assertEqual(splitted[0].text, "This is a `code` within text")

    def test_split_bold_multiple(self):
        node = TextNode(
            "This is a **bold** word in the bold **sentence**!", TextType.TEXT
        )
        splitted = split_nodes_delimeter([node], "**", TextType.BOLD)

        self.assertEqual(splitted[0].text, "This is a ")
        self.assertEqual(splitted[1].text, "bold")
        self.assertEqual(splitted[2].text, " word in the bold ")
        self.assertEqual(splitted[3].text, "sentence")
        self.assertEqual(splitted[4].text, "!")

        self.assertEqual(splitted[0].text_type, TextType.TEXT)
        self.assertEqual(splitted[1].text_type, TextType.BOLD)
        self.assertEqual(splitted[2].text_type, TextType.TEXT)
        self.assertEqual(splitted[3].text_type, TextType.BOLD)
        self.assertEqual(splitted[4].text_type, TextType.TEXT)

        node = TextNode(
            "This is a **bold** word in the bold **sentence**", TextType.TEXT
        )
        splitted = split_nodes_delimeter([node], "**", TextType.BOLD)

        self.assertEqual(splitted[0].text, "This is a ")
        self.assertEqual(splitted[1].text, "bold")
        self.assertEqual(splitted[2].text, " word in the bold ")
        self.assertEqual(splitted[3].text, "sentence")

    def test_split_multiple_nodes(self):
        node_1 = TextNode("This is a `code` within text", TextType.TEXT)
        node_2 = TextNode("This is a text with _italic_ word", TextType.TEXT)
        node_3 = TextNode("This is a text with **bold** word", TextType.TEXT)
        node_4 = TextNode("This is a simple text", TextType.TEXT)

        splitted = split_nodes_delimeter(
            [node_1, node_2, node_3, node_4], "**", TextType.BOLD
        )

        self.assertEqual(splitted[0].text, "This is a `code` within text")
        self.assertEqual(splitted[1].text, "This is a text with _italic_ word")
        self.assertEqual(splitted[2].text, "This is a text with ")
        self.assertEqual(splitted[3].text, "bold")
        self.assertEqual(splitted[4].text, " word")
        self.assertEqual(splitted[5].text, "This is a simple text")

        self.assertEqual(splitted[0].text_type, TextType.TEXT)
        self.assertEqual(splitted[1].text_type, TextType.TEXT)
        self.assertEqual(splitted[2].text_type, TextType.TEXT)
        self.assertEqual(splitted[3].text_type, TextType.BOLD)
        self.assertEqual(splitted[4].text_type, TextType.TEXT)
        self.assertEqual(splitted[5].text_type, TextType.TEXT)

        splitted_2 = split_nodes_delimeter(splitted, "_", TextType.ITALIC)

        self.assertEqual(splitted_2[0].text, "This is a `code` within text")
        self.assertEqual(splitted_2[1].text, "This is a text with ")
        self.assertEqual(splitted_2[2].text, "italic")
        self.assertEqual(splitted_2[3].text, " word")
        self.assertEqual(splitted_2[4].text, "This is a text with ")
        self.assertEqual(splitted_2[5].text, "bold")
        self.assertEqual(splitted_2[6].text, " word")
        self.assertEqual(splitted_2[7].text, "This is a simple text")

        self.assertEqual(splitted_2[0].text_type, TextType.TEXT)
        self.assertEqual(splitted_2[1].text_type, TextType.TEXT)
        self.assertEqual(splitted_2[2].text_type, TextType.ITALIC)
        self.assertEqual(splitted_2[3].text_type, TextType.TEXT)
        self.assertEqual(splitted_2[4].text_type, TextType.TEXT)
        self.assertEqual(splitted_2[5].text_type, TextType.BOLD)
        self.assertEqual(splitted_2[6].text_type, TextType.TEXT)
        self.assertEqual(splitted_2[7].text_type, TextType.TEXT)

        splitted_3 = split_nodes_delimeter(splitted_2, "`", TextType.CODE)

        self.assertEqual(splitted_3[0].text, "This is a ")
        self.assertEqual(splitted_3[1].text, "code")
        self.assertEqual(splitted_3[2].text, " within text")
        self.assertEqual(splitted_3[3].text, "This is a text with ")
        self.assertEqual(splitted_3[4].text, "italic")
        self.assertEqual(splitted_3[5].text, " word")
        self.assertEqual(splitted_3[6].text, "This is a text with ")
        self.assertEqual(splitted_3[7].text, "bold")
        self.assertEqual(splitted_3[8].text, " word")
        self.assertEqual(splitted_3[9].text, "This is a simple text")

        self.assertEqual(splitted_3[0].text_type, TextType.TEXT)
        self.assertEqual(splitted_3[1].text_type, TextType.CODE)
        self.assertEqual(splitted_3[2].text_type, TextType.TEXT)
        self.assertEqual(splitted_3[3].text_type, TextType.TEXT)
        self.assertEqual(splitted_3[4].text_type, TextType.ITALIC)
        self.assertEqual(splitted_3[5].text_type, TextType.TEXT)
        self.assertEqual(splitted_3[6].text_type, TextType.TEXT)
        self.assertEqual(splitted_3[7].text_type, TextType.BOLD)
        self.assertEqual(splitted_3[8].text_type, TextType.TEXT)
        self.assertEqual(splitted_3[9].text_type, TextType.TEXT)


if __name__ == "__main__":
    unittest.main()
