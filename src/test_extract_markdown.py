import unittest

from helpers import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_markdown_images(self):
        regex_result = extract_markdown_images(
            "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )

        self.assertEqual(
            regex_result,
            [
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_markdown_links(self):
        regex_result = extract_markdown_links(
            "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )

        self.assertEqual(
            regex_result,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ],
        )

    def test_markdown_wrong_images(self):
        regex_result = extract_markdown_images(
            "This is text with a [rick roll] (https://i.imgur.com/aKaOqIh.gif) and ![obi wan] (https://i.imgur.com/fJRm4Vk.jpeg)"
        )

        self.assertNotEqual(
            regex_result,
            [
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_markdown_wrong_links(self):
        regex_result = extract_markdown_links(
            "This is text with a [rick roll] (https://i.imgur.com/aKaOqIh.gif) and ![obi wan] (https://i.imgur.com/fJRm4Vk.jpeg)"
        )

        self.assertNotEqual(
            regex_result,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
