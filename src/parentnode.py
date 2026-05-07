from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required")

        if self.children is None:
            raise ValueError("children are required")

        html = f"<{self.tag}>{self.props_to_html()}"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
