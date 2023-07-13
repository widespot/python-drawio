import unittest
from xml.etree.ElementTree import tostring

from python_drawio import Page, Document, RoundedRectangle, Line


class TestContext(unittest.TestCase):

    def test_get(self):
        d = Document()
        p1 = Page("Page-1")
        p2 = Page("Page-2")
        d.add_page(p1)
        d.add_page(p2)

        r = RoundedRectangle(
            x=200, y=100, width=100, height=100,
            content="blabetiblou",
            text_align="left", text_valign="top",
        )
        p1.add_content(r)
        p1.add_content(Line(points=[
            [20, 50],
            [200, 50],
            [200, 100],
        ], stroke_thickness=4, stroke_color="#FF000",
            content="bonjour", curved=True))

        with open('tests/unit/test.drawio', 'w') as f:
            f.write(tostring(d.to_xml()).decode())
