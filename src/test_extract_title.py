import unittest

from helpers import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
# Title #1
## Title #2
### Title #2

some paragraph

- ul
- list
- also
        """

        title_text = extract_title(markdown)

        self.assertEqual(title_text, "Title #1")


if __name__ == "__main__":
    unittest.main()
