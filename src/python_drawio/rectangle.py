from xml.etree.ElementTree import Element as XmlElement, SubElement

from .element import Element


class RoundedRectangle(Element):
    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def __init__(self, x: int, y: int, width: int, height: int, border_width: int = 1, arc_size: int = 5,
                 content: str = "", text_align: str = "center", text_valign: str = "middle"):
        super().__init__()

        assert isinstance(x, int)
        assert isinstance(y, int)
        assert isinstance(width, int) and width > 0
        assert isinstance(height, int) and height > 0
        assert isinstance(border_width, int) and border_width > 0
        assert isinstance(content, str)

        self.border_width = border_width
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.arc_size = arc_size
        self.rounded: bool = True
        self.content: str = content
        self.text_align: str = text_align
        self.text_valign: str = text_valign

    def to_xml(self, parent_id: str = "1") -> list[XmlElement]:
        # TODO deal with None id
        cell = XmlElement("mxCell", attrib={
            "id": str(self.id),
            "value": self.content,
            "style": f"rounded={1 if self.rounded else 0};whiteSpace=wrap;html=1;arcSize={self.arc_size};align={self.text_align};verticalAlign={self.text_valign};",
            "vertex": str(self.border_width),
            "parent": parent_id,
        })

        SubElement(cell, "mxGeometry", attrib={
            "x": str(self.x),
            "y": str(self.y),
            "width": str(self.width),
            "height": str(self.height),
            "as": "geometry",
        })

        return [cell]
