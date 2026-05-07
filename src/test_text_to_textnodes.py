import unittest

from helpers import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text_md = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        textnodes = text_to_textnodes(text_md)

        self.assertEqual(
            textnodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_text_to_textnodes_reverse(self):
        text_md = "This is [link](https://boot.dev) with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) image and a `code block` and an _italic_ and a **text** word"

        textnodes = text_to_textnodes(text_md)

        self.assertEqual(
            textnodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" with an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" image and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and a ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
