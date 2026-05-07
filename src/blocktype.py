from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []

    lines = markdown.split("\n\n")

    for line in lines:
        stripped_line = line.strip()

        if stripped_line != "":
            blocks.append(stripped_line)

    return blocks


def block_to_block_type(markdown_block):
    lines = markdown_block.split("\n")

    if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH

        return BlockType.QUOTE

    if markdown_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH

        return BlockType.ULIST

    if markdown_block.startswith("1. "):
        i = 1

        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1

        return BlockType.OLIST

    return BlockType.PARAGRAPH
