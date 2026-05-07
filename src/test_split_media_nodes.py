import unittest

from helpers import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitMediaNodes(unittest.TestCase):
    def test_split_image_node(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) 123",
            TextType.TEXT,
        )

        splitted = split_nodes_image([node])

        self.assertEqual(
            splitted,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" 123", TextType.TEXT),
            ],
        )

    def test_split_link_node(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) 321",
            TextType.TEXT,
        )

        splitted = split_nodes_link([node])

        self.assertEqual(
            splitted,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
                TextNode(" 321", TextType.TEXT),
            ],
        )

    def test_split_image_nodes(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) 123",
            TextType.TEXT,
        )

        node2 = TextNode(
            "This is text with an ![second image](https://i.imgur.com/3elNhQu.png) and another ![image](https://i.imgur.com/zjjcJKZ.png) 123",
            TextType.TEXT,
        )

        splitted = split_nodes_image([node, node2])

        self.assertEqual(
            splitted,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" 123", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" 123", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
