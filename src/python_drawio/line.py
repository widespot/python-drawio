import enum
from xml.etree.ElementTree import Element, SubElement, tostring
from typing import Union

from .content import Content


class LineStrokeStyle(enum.Enum):
    SOLID = 'solid'
    DASHED = 'dashed'
    DOTTED = 'dotted'


class Line(Content):

    def __init__(self, points: list[Union[list[int], Content]],
                 stroke_thickness: int = 1, stroke_color: str = "#000000", stroke_style: LineStrokeStyle = LineStrokeStyle.SOLID,
                 rounded: bool = False, curved: bool = False,
                 content: str = "",
                 end_arrow: str = "classic"):
        super().__init__()
        assert len(points) >= 2
        self.points: list[[int, int]] = points
        self.stroke_thickness = stroke_thickness
        self.stroke_color = stroke_color
        self.stroke_style: LineStrokeStyle = stroke_style
        self.content = content
        self.rounded = rounded
        self.curved = curved
        self.end_arrow = end_arrow

    def to_xml(self):
        # TODO deal with None id
        # TODO parent id
        cell_style = {
            'html': 1,
            "strokeWidth": self.stroke_thickness,
            "strokeColor": self.stroke_color,
        }
        if self.end_arrow is not None:
            cell_style['end_arrow'] = self.end_arrow
        if self.stroke_style == LineStrokeStyle.DASHED:
            cell_style['dashed'] = 1
        if self.curved:
            cell_style['curved'] = 1
        elif self.rounded:
            cell_style['rounded'] = 1
        else:
            cell_style['rounded'] = 0

        cell_attrib = {
            "id": str(self.id),
            "value": self.content,
            "style": ";".join([f"{key}={val}" for (key, val) in cell_style.items()]),
            "edge": "1",
            "parent": "1",
        }
        if isinstance(self.points[0], Content):
            cell_attrib['source'] = self.points[0].id
        if isinstance(self.points[len(self.points) - 1], Content):
            cell_attrib['target'] = self.points[len(self.points) - 1].id

        cell = Element("mxCell", attrib=cell_attrib)

        geometry_attrib = {
            "width": str("50"),
            "height": str("50"),
            "relative": "1",
            "as": "geometry",
        }

        geometry = SubElement(cell, "mxGeometry", attrib=geometry_attrib)

        if not isinstance(self.points[0], Content):
            SubElement(geometry, "mxPoint", attrib={
                "x": str(self.points[0][0]),
                "y": str(self.points[0][1]),
                "as": "sourcePoint",
            })

        if not isinstance(self.points[len(self.points) - 1], Content):
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
