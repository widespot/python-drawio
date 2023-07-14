from xml.etree.ElementTree import Element, SubElement, tostring

from .content import Content


class Line(Content):

    def __init__(self, points: list[[int, int]],
                 stroke_thickness: int = 1, stroke_color: str = "#000000",
                 rounded: bool = False, curved: bool = False,
                 content: str = "",
                 end_arrow: str = "classic"):
        super().__init__()
        assert len(points) >= 2
        self.points: list[[int, int]] = points
        self.stroke_thickness = stroke_thickness
        self.stroke_color = stroke_color
        self.content = content
        self.rounded = rounded
        self.curved = curved
        self.end_arrow = end_arrow

    def to_xml(self):
        # TODO deal with None id
        # TODO parent id
        cell = Element("mxCell", attrib={
            "id": str(self.id),
            "value": self.content,
            "style": f"endArrow={self.end_arrow};html=1;{'curved' if self.curved else 'rounded'}={1 if self.rounded or self.curved else 0};strokeWidth={self.stroke_thickness};strokeColor={self.stroke_color};",
            "edge": "1",
            "parent": "1",
        })

        geometry_attrib = {
            "width": str("50"),
            "height": str("50"),
            "relative": "1",
            "as": "geometry",
        }

        geometry = SubElement(cell, "mxGeometry", attrib=geometry_attrib)

        SubElement(geometry, "mxPoint", attrib={
            "x": str(self.points[0][0]),
            "y": str(self.points[0][1]),
            "as": "sourcePoint",
        })

        SubElement(geometry, "mxPoint", attrib={
            "x": str(self.points[len(self.points) - 1][0]),
            "y": str(self.points[len(self.points) - 1][1]),
            "as": "targetPoint",
        })

        if len(self.points) > 2:
            array = SubElement(geometry, "Array", attrib={
                "as": "points",
            })
            for p in self.points[1:-1]:
                SubElement(array, "mxPoint", attrib={
                    "x": str(p[0]),
                    "y": str(p[1]),
                })

        return cell
