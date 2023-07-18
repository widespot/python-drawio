import enum
from xml.etree.ElementTree import Element as XmlElement, SubElement
from typing import Union

from .element import Element


class LineStrokeStyle(enum.Enum):
    SOLID = 'solid'
    DASHED = 'dashed'
    DOTTED = 'dotted'


class Line(Element):

    def get_y(self) -> int:
        return self.get_min_y()

    def get_x(self) -> int:
        return self.get_min_x()

    def get_min_x(self) -> int:
        return self.get_min_points(0)

    def get_min_y(self) -> int:
        return self.get_min_points(1)

    def get_min_points(self, i) -> int:
        return self.get_minmax_points(min, i)

    def get_max_points(self, i) -> int:
        return self.get_minmax_points(max, i)

    def get_minmax_points(self, fun, i):
        return fun(
            list(filter(lambda p: not isinstance(p, Element) and len(p) == 2,
                        self.points)),
            default=(0, 0),
            key=lambda p: p[i])[i]

    def get_width(self) -> int:
        return self.get_max_points(0) - self.get_min_points(0)

    def get_height(self) -> int:
        return self.get_max_points(1) - self.get_min_points(1)

    def __init__(self, points: list[Union[tuple[int, int], Element, tuple[Element, int, int]]],
                 stroke_thickness: int = 1, stroke_color: str = "#000000",
                 stroke_style: LineStrokeStyle = LineStrokeStyle.SOLID,
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

    def to_xml(self, parent_id: str = "1") -> list[XmlElement]:
        # TODO deal with None id
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
            "edge": "1",
            "parent": parent_id,
        }
        source_point = self.points[0]
        target_point = self.points[len(self.points) - 1]
        if isinstance(source_point, Element) or len(source_point) == 3:
            element = source_point if isinstance(source_point, Element) else source_point[0]
            cell_attrib['source'] = element.id
            if not isinstance(source_point, Element):
                cell_style.update(exitX=str(source_point[1]), exitY=str(source_point[2]), exitDx="0", exitDy="0")
        if isinstance(target_point, Element) or len(target_point) == 3:
            element = target_point if isinstance(target_point, Element) else target_point[0]
            cell_attrib['target'] = element.id
            if not isinstance(target_point, Element):
                cell_style.update(entryX=str(target_point[1]), entryY=str(target_point[2]), entryDx="0",
                                  entryDy="0")

        cell_attrib['style'] = ";".join([f"{key}={val}" for (key, val) in cell_style.items()])

        cell = XmlElement("mxCell", attrib=cell_attrib)

        geometry_attrib = {
            "width": str("50"),
            "height": str("50"),
            "relative": "1",
            "as": "geometry",
        }

        geometry = SubElement(cell, "mxGeometry", attrib=geometry_attrib)

        if not isinstance(source_point, Element) and len(source_point) == 2:
            SubElement(geometry, "mxPoint", attrib={
                "x": str(source_point[0]),
                "y": str(source_point[1]),
                "as": "sourcePoint",
            })

        if not isinstance(target_point, Element) and len(target_point) == 2:
            SubElement(geometry, "mxPoint", attrib={
                "x": str(target_point[0]),
                "y": str(target_point[1]),
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

        return [cell]
