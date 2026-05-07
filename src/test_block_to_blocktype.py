import unittest

from blocktype import BlockType, block_to_block_type, markdown_to_blocks


class TestBlockToBlockType(unittest.TestCase):
    def test_markdown_block_to_block_type(self):
        markdown_text = """
# Heading N1

## Heading N2

### Heading N3

```
some code block
```

Just a paragraph

> Some quote for sure (c) me

- finish python basics
- finish the first python project
- finnish

1. finish python OOP course
2. finish asteroids
3. fish
        """

        markdown_blocks = markdown_to_blocks(markdown_text)

        block_types = []

        for block in markdown_blocks:
            block_types.append(block_to_block_type(block))

        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.CODE,
                BlockType.PARAGRAPH,
                BlockType.QUOTE,
                BlockType.ULIST,
                BlockType.OLIST,
            ],
        )


if __name__ == "__main__":
    unittest.main()
