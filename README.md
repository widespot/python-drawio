# 🚧 WIP draw.io using Python

Create [Draw.io (diagrams.net)](https://app.diagrams.net/) drawings, with Python. **Without dependency !**

## Features

* Rectangles
* Lines
    * stroke type, thickness, color
    * rounded, curved
    * Connected ends, intermediate points

## Usage

```
from xml.etree.ElementTree import tostring

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
    (r, 0.5, 0),
    (200, 50),
    (200, 100),
], stroke_thickness=4, stroke_color="#FF000",
    content="bonjour", curved=True))

with open('widespot.drawio', 'w') as f:
    f.write(tostring(d.to_xml()).decode())
```
