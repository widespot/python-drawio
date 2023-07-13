from xml.etree.ElementTree import Element, SubElement, tostring


class Document:
    def __init__(self):
        self.version = "20.5.3"
        self.host = "drawio-plugin"
        self.type = "embed"
        self.pages: list[Page] = []

    def add_page(self, page):
        self.pages += [page]

    def to_xml(self) -> Element:
        root = Element('mxfile', attrib={
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
        content.set_id(self.count + 2)
        self.count += 1
        self.content += [content]

    def to_xml(self):
        page = Element("diagram", attrib={
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

        for content in self.content:
            root.append(content.to_xml())

        return page


class Content:

    def __init__(self):
        self.id = None

    def set_id(self, id):
        if self.id is not None:
            raise Exception("Id already set")
        self.id = id


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
