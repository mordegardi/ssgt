import unittest

from helpers import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_paragraphs(self):
        markdown_text = """
This is the first paragraph

This is the second paragraph

This is the third paragraph
        """

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            "<div><p>This is the first paragraph</p><p>This is the second paragraph</p><p>This is the third paragraph</p></div>",
        )

    def test_markdown_to_html_paragraphs_with_inline(self):
        markdown_text = """
This is the **first** paragraph

This is the _second_ paragraph

This is the `third` paragraph
        """

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            "<div><p>This is the <b>first</b> paragraph</p><p>This is the <i>second</i> paragraph</p><p>This is the <code>third</code> paragraph</p></div>",
        )

    def test_markdown_to_html_paragraphs_with_links_and_images(self):
        markdown_text = """
This is the **first** paragraph with a simple [link](https://boot.dev)!

This is the _second_ paragraph with an example ![image](https://i.imgur.com/zjjcJKZ.png) and also some text after

This is the `third` paragraph
"""

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            '<div><p>This is the <b>first</b> paragraph with a simple <a href="https://boot.dev">link</a>!</p><p>This is the <i>second</i> paragraph with an example <img src="https://i.imgur.com/zjjcJKZ.png" alt="image" /> and also some text after</p><p>This is the <code>third</code> paragraph</p></div>',
        )

    def test_markdown_to_html_paragraphs_with_headers(self):
        markdown_text = """
# Header **L1** bold

## Header _L2_ italic

### Header `L3` code

###### Header [L6](https://boot.dev)

This is the first paragraph

This is the second paragraph with an example

This is the third paragraph
"""

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            '<div><h1>Header <b>L1</b> bold</h1><h2>Header <i>L2</i> italic</h2><h3>Header <code>L3</code> code</h3><h6>Header <a href="https://boot.dev">L6</a></h6><p>This is the first paragraph</p><p>This is the second paragraph with an example</p><p>This is the third paragraph</p></div>',
        )

    def test_markdown_to_html_paragraphs_with_codeblock(self):
        markdown_text = """
This is the first paragraph

This is the second paragraph with an example

This is the third paragraph

```
{
    an example
    of a code
    block
}
```
"""

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            "<div><p>This is the first paragraph</p><p>This is the second paragraph with an example</p><p>This is the third paragraph</p><pre><code>{\n    an example\n    of a code\n    block\n}\n</code></pre></div>",
        )

    def test_markdown_to_html_paragraphs_with_blockquote(self):
        self.maxDiff = None
        markdown_text = """
This is the first paragraph

This is the second paragraph with an example

This is the third paragraph

> multiline quote
> with some **bold** and _italic_ words
>
> and also some `code` as well
"""

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            "<div><p>This is the first paragraph</p><p>This is the second paragraph with an example</p><p>This is the third paragraph</p><blockquote>multiline quote with some <b>bold</b> and <i>italic</i> words and also some <code>code</code> as well </blockquote></div>",
        )

    def test_markdown_to_html_paragraphs_with_unordered_list(self):
        markdown_text = """
This is the first paragraph

This is the second paragraph with an example

This is the third paragraph

- unordered **item** 1
- unordered _item_ 2
- unordered `item` 3
- [a simple link](https://boot.dev)
"""

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            '<div><p>This is the first paragraph</p><p>This is the second paragraph with an example</p><p>This is the third paragraph</p><ul><li>unordered <b>item</b> 1</li><li>unordered <i>item</i> 2</li><li>unordered <code>item</code> 3</li><li><a href="https://boot.dev">a simple link</a></li></ul></div>',
        )

    def test_markdown_to_html_paragraphs_with_ordered_list(self):
        markdown_text = """
This is the first paragraph

This is the second paragraph with an example

This is the third paragraph

1. ordered **item** 1
2. ordered _item_ 2
3. ordered `item` 3
"""

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            "<div><p>This is the first paragraph</p><p>This is the second paragraph with an example</p><p>This is the third paragraph</p><ol><li>ordered <b>item</b> 1</li><li>ordered <i>item</i> 2</li><li>ordered <code>item</code> 3</li></ol></div>",
        )

    def test_markdown_to_html_complete(self):
        self.maxDiff = None
        markdown_text = """
# Header **level** 1

## Header _level_ 2

#### Header `level` 4

This is the **first** paragraph

This is the _second_ paragraph with an example

This is the `third` paragraph

> multiline quote
> with some **bold** and _italic_ words
> and also some `code` as well

```
{
    we have some code as well!
}
```

1. ordered **item** 1
2. ordered _item_ 2
3. ordered `item` 3

- unordered **item** 1
- unordered _item_ 2
- unordered `item` 3
"""

        html = markdown_to_html_node(markdown_text)

        self.assertEqual(
            html,
            "<div><h1>Header <b>level</b> 1</h1><h2>Header <i>level</i> 2</h2><h4>Header <code>level</code> 4</h4><p>This is the <b>first</b> paragraph</p><p>This is the <i>second</i> paragraph with an example</p><p>This is the <code>third</code> paragraph</p><blockquote>multiline quote with some <b>bold</b> and <i>italic</i> words and also some <code>code</code> as well </blockquote><pre><code>{\n    we have some code as well!\n}\n</code></pre><ol><li>ordered <b>item</b> 1</li><li>ordered <i>item</i> 2</li><li>ordered <code>item</code> 3</li></ol><ul><li>unordered <b>item</b> 1</li><li>unordered <i>item</i> 2</li><li>unordered <code>item</code> 3</li></ul></div>",
        )


if __name__ == "__main__":
    unittest.main()
