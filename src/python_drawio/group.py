import enum
from xml.etree.ElementTree import Element as XmlElement, SubElement
from typing import Union

from .element import Element


class Group(Element):

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_width(self) -> int:
        # TODO
        pass

    def get_height(self) -> int:
        # TODO
        pass

    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y
        self.elements: list[Element] = []

    def set_id(self, id: int) -> int:
        added_elements = super().set_id(id)

        for element in self.elements:
            added_elements += element.set_id(id + added_elements)

        return added_elements

    def add_element(self, element: Element):
        self.elements.append(element)

    def to_xml(self, parent_id: str = "1") -> list[XmlElement]:
        cell_attrib = {
            "id": str(self.id),
            "value": "",
            "vertex": "1",
            "connectable": "0",
            "parent": parent_id,
            "style": "group",
        }

        cell = XmlElement("mxCell", attrib=cell_attrib)

        geometry_attrib = {
            "x": str(self.x),
            "y": str(self.y),
            "width": self.get_width(),
            "height": self.get_height(),
            "as": "geometry",
        }

        SubElement(cell, "mxGeometry", attrib=geometry_attrib)

        return [cell] + [xml_element
                         for xml_elements in list(map(lambda e: e.to_xml(parent_id=str(self.id)), self.elements))
                         for xml_element in xml_elements]
