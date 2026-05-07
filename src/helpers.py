import re

from blocktype import BlockType, block_to_block_type, markdown_to_blocks
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    if delimeter is None:
        raise Exception("delimeter is empty")

    if text_type is None:
        raise Exception("text type is empty")

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        splitted = node.text.split(delimeter)

        if len(splitted) == 1:
            new_nodes.append(node)
            continue

        if len(splitted) % 2 == 0:
            raise Exception("Invalid markdown syntax")

        for i in range(len(splitted)):
            if splitted[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(splitted[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(splitted[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text == "":
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted_images = extract_markdown_images(node.text)

        if len(extracted_images) == 0:
            new_nodes.append(node)
            continue

        splitted = []

        rest_message = None

        for i in range(len(extracted_images)):
            alt_text, image_src = extracted_images[i]

            if rest_message is not None:
                sections = rest_message.split(f"![{alt_text}]({image_src})", 1)
            else:
                sections = node.text.split(f"![{alt_text}]({image_src})", 1)

            if len(sections) != 2:
                raise ValueError("invalid image format")

            if i == len(extracted_images) - 1:
                if sections[0] != "":
                    splitted.append(TextNode(sections[0], TextType.TEXT))

                splitted.append(TextNode(alt_text, TextType.IMAGE, image_src))
                if len(sections) > 0 and sections[1] != "":
                    splitted.append(TextNode(sections[1], TextType.TEXT))
            else:
                splitted.append(TextNode(sections[0], TextType.TEXT))
                splitted.append(TextNode(alt_text, TextType.IMAGE, image_src))
                rest_message = sections[1]

        new_nodes.extend(splitted)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text == "":
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted_links = extract_markdown_links(node.text)

        if len(extracted_links) == 0:
            new_nodes.append(node)
            continue

        splitted = []

        rest_message = None

        for i in range(len(extracted_links)):
            alt_text, link = extracted_links[i]

            if rest_message is not None:
                sections = rest_message.split(f"[{alt_text}]({link})", 1)
            else:
                sections = node.text.split(f"[{alt_text}]({link})", 1)

            if len(sections) != 2:
                raise ValueError("invalid link format")

            if i == len(extracted_links) - 1:
                if sections[0] != "":
                    splitted.append(TextNode(sections[0], TextType.TEXT))

                splitted.append(TextNode(alt_text, TextType.LINK, link))

                if len(sections) > 0 and sections[1] != "":
                    splitted.append(TextNode(sections[1], TextType.TEXT))

            else:
                splitted.append(TextNode(sections[0], TextType.TEXT))
                splitted.append(TextNode(alt_text, TextType.LINK, link))

                rest_message = sections[1]

        new_nodes.extend(splitted)

    return new_nodes


def text_to_textnodes(text):
    textnode = TextNode(text, TextType.TEXT)

    splitted_bold = split_nodes_delimeter([textnode], "**", TextType.BOLD)
    splitted_italic = split_nodes_delimeter(splitted_bold, "_", TextType.ITALIC)
    splitted_code = split_nodes_delimeter(splitted_italic, "`", TextType.CODE)
    splitted_images = split_nodes_image(splitted_code)
    splitted_full = split_nodes_link(splitted_images)

    return splitted_full


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Unknown text type")


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)

    html_nodes = []

    for md_block in markdown_blocks:
        block_type = block_to_block_type(md_block)

        match block_type:
            case BlockType.HEADING:
                text_nodes = text_to_textnodes(md_block)

                children = []

                hlevel = text_nodes[0].text.count("#")

                for node in text_nodes:
                    if node.text_type != TextType.TEXT or not node.text.startswith("#"):
                        children.append(text_node_to_html_node(node))
                    else:
                        children.append(LeafNode(None, node.text.lstrip("# ")))

                html_nodes.append(ParentNode(f"h{hlevel}", children))

            case BlockType.PARAGRAPH:
                lines = md_block.split("\n")

                text_nodes = text_to_textnodes(" ".join(lines))

                children = []

                for node in text_nodes:
                    children.append(text_node_to_html_node(node))

                html_nodes.append(ParentNode("p", children))

            case BlockType.CODE:
                text_node = TextNode(md_block[4:-3], TextType.CODE)

                html_nodes.append(
                    ParentNode("pre", [text_node_to_html_node(text_node)])
                )

            case BlockType.QUOTE:
                block_parts = md_block.split("\n")

                children = []

                for part in block_parts:
                    part_text_nodes = text_to_textnodes(part)

                    for i in range(len(part_text_nodes)):
                        node = part_text_nodes[i]

                        if node.text.lstrip(">") == "":
                            continue

                        if i == len(part_text_nodes) - 1:
                            if node.text.startswith("> "):
                                node.text = node.text[2:] + " "
                            else:
                                node.text += " "
                            children.append(text_node_to_html_node(node))
                        elif (
                            node.text_type != TextType.TEXT
                            or not node.text.startswith("> ")
                        ):
                            children.append(text_node_to_html_node(node))
                        else:
                            children.append(LeafNode(None, node.text.replace("> ", "")))

                html_nodes.append(ParentNode("blockquote", children))

            case BlockType.ULIST:
                block_parts = md_block.split("\n")

                children = []

                for part in block_parts:
                    part_text_nodes = text_to_textnodes(part.lstrip("-").strip())

                    node_parts = []

                    for i in range(len(part_text_nodes)):
                        node = part_text_nodes[i]
                        node_parts.append(text_node_to_html_node(node))

                    children.append(ParentNode("li", node_parts))

                html_nodes.append(ParentNode("ul", children))
            case BlockType.OLIST:
                block_parts = md_block.split("\n")

                children = []

                for part in block_parts:
                    part_text_nodes = text_to_textnodes(part.split(". ")[1])

                    node_parts = []

                    for i in range(len(part_text_nodes)):
                        node = part_text_nodes[i]
                        node_parts.append(text_node_to_html_node(node))

                    children.append(ParentNode("li", node_parts))

                html_nodes.append(ParentNode("ol", children))

    parent = ParentNode("div", html_nodes)

    return parent.to_html()


def extract_title(markdown):
    blocks = markdown.split("\n")

    for block in blocks:
        if block.startswith("# "):
            title = block.lstrip("#").strip()

            return title

    raise Exception("no title found")
