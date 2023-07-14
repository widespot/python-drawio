from xml.etree.ElementTree import Element, SubElement

from .content import Content


class RoundedRectangle(Content):
    def __init__(self, x: int, y: int, width: int, height: int, border_width: int = 1, arc_size: int = 5,
                 content: str = "", text_align: str = "center", text_valign: str = "middle"):
        super().__init__()
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

    def to_xml(self):
        # TODO deal with None id
        cell = Element("mxCell", attrib={
            "id": str(self.id),
            "value": self.content,
            "style": f"rounded={1 if self.rounded else 0};whiteSpace=wrap;html=1;arcSize={self.arc_size};align={self.text_align};verticalAlign={self.text_valign};",
            "vertex": str(self.border_width),
            "parent": "1",
        })

        SubElement(cell, "mxGeometry", attrib={
            "x": str(self.x),
            "y": str(self.y),
            "width": str(self.width),
            "height": str(self.height),
            "as": "geometry",
        })

        return cell
