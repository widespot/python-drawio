import os
import unittest
from xml.etree.ElementTree import tostring

from python_drawio import Page, Document, RoundedRectangle, Line, Group


class TestGroup(unittest.TestCase):
    output_dir = "tests/unit/output/test_group/"

    def setUp(self) -> None:
        os.makedirs(TestGroup.output_dir, exist_ok=True)

    def test_connection(self):
        d = Document()
        p = Page("page")
        d.add_page(p)

        g = Group(x=100, y=69)

        r1 = RoundedRectangle(
            x=0, y=0, width=100, height=100,
        )
        g.add_element(r1)
        r2 = RoundedRectangle(
            x=250, y=150, width=100, height=100,
        )
        g.add_element(r2)
        g.add_element(Line(points=[
            r1,
            r2,
        ]))
        p.add_content(g)

        with open(f'{TestGroup.output_dir}/connection.drawio', 'w') as f:
            f.write(tostring(d.to_xml()).decode())
