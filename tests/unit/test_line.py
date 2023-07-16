import os
import unittest
from xml.etree.ElementTree import tostring

from python_drawio import Page, Document, RoundedRectangle, Line, LineStrokeStyle


class TestLine(unittest.TestCase):
    output_dir = "tests/unit/output/test_line/"

    def setUp(self) -> None:
        os.makedirs(TestLine.output_dir, exist_ok=True)

    def test_connection(self):
        d = Document()
        p = Page("page")
        d.add_page(p)

        r1 = RoundedRectangle(
            x=0, y=0, width=100, height=100,
        )
        p.add_content(r1)
        r2 = RoundedRectangle(
            x=250, y=150, width=100, height=100,
        )
        p.add_content(r2)
        p.add_content(Line(points=[
            r1,
            r2,
        ]))

        with open(f'{TestLine.output_dir}/connection.drawio', 'w') as f:
            f.write(tostring(d.to_xml()).decode())

    def test_connection_with_intermediate(self):
        d = Document()
        p = Page("page")
        d.add_page(p)

        r1 = RoundedRectangle(
            x=0, y=0, width=100, height=100,
        )
        p.add_content(r1)
        r2 = RoundedRectangle(
            x=250, y=150, width=100, height=100,
        )
        p.add_content(r2)
        p.add_content(Line(points=[
            r1,
            (200, 50),
            (50, 200),
            r2,
        ]))

        with open(f'{TestLine.output_dir}/connection_with_intermediate.drawio', 'w') as f:
            f.write(tostring(d.to_xml()).decode())

    def test_relative_connection(self):
        d = Document()
        p = Page("page")
        d.add_page(p)

        r1 = RoundedRectangle(
            x=0, y=0, width=100, height=100,
        )
        p.add_content(r1)
        r2 = RoundedRectangle(
            x=250, y=150, width=100, height=100,
        )
        p.add_content(r2)
        p.add_content(Line(points=[
            (r1, 0.1, 0.2),
            (200, 50),
            (r2, 0.5, 1.1),
        ]))

        with open(f'{TestLine.output_dir}/relative_connection.drawio', 'w') as f:
            f.write(tostring(d.to_xml()).decode())
