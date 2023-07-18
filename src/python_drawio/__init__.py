from xml.etree.ElementTree import Element as XmlElement, SubElement

from .line import Line, LineStrokeStyle
from .rectangle import RoundedRectangle
from .group import Group
from .element import Element


class Document:
    def __init__(self):
        self.version = "20.5.3"
        self.host = "drawio-plugin"
        self.type = "embed"
        self.pages: list[Page] = []

    def add_page(self, page):
        self.pages += [page]

    def to_xml(self) -> XmlElement:
        root = XmlElement('mxfile', attrib={
            'host': self.host,
            "version": self.version,
            "type": self.type,
            "modified": "2023-07-12T22:58:17.826Z",
            "agent": "5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
            "etag": "MRPZM84XNlerVt0PT8O2",
        })

        for page in self.pages:
            root.append(page.to_xml())

        return root


class Page:

    def __init__(self, title: str):
        self.title = title
        self.content = []
        self.count = 0

    def add_content(self, content):
        # +2 because each root always start with two mxCells taking id 0 and 1
        added_elements = content.set_id(self.count + 2)
        self.count += added_elements
        self.content += [content]

    def to_xml(self):
        page = XmlElement("diagram", attrib={
            "id": "blabetiblou",
            "name": self.title,
        })

        graph_model = SubElement(page, "mxGraphModel", attrib={
            "dx": "535",
            "dy": "212",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": "850",
            "pageHeight": "1100",
            "math": "0",
            "shadow": "0",
        })

        root = SubElement(graph_model, "root")

        SubElement(root, "mxCell", attrib={"id": "0"})
        SubElement(root, "mxCell", attrib={"id": "1", "parent": "0"})

        content: Element
        for content in self.content:
            for xml_element in content.to_xml(parent_id="1"):
                root.append(xml_element)

        return page
