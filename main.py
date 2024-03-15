from decimal import Decimal
from pathlib import Path

from borb.pdf import Document
from borb.pdf import FixedColumnWidthTable
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayoutWithOverflow
from borb.pdf import Image
from borb.pdf.page.page_size import PageSize

doc = Document()

page = Page(PageSize.A4_LANDSCAPE.value[0], PageSize.A4_LANDSCAPE.value[1])  # A4 Landscape
doc.add_page(page)

# with 2 it works, with 3 it doesn't
# number_of_samples = 2
number_of_samples = 3
layout = SingleColumnLayoutWithOverflow(page)
# add the header, maybe
table = FixedColumnWidthTable(
    number_of_columns=7,
    number_of_rows=number_of_samples + 1,
    column_widths=[Decimal(2), Decimal(6), Decimal(1), Decimal(2), Decimal(1), Decimal(2), Decimal(1)],
)
# add the table header
table.add(Paragraph("Sample ID", font="Helvetica-Bold"))
table.add(Paragraph("Image", font="Helvetica-Bold"))
table.add(Paragraph("Valid", font="Helvetica-Bold"))
table.add(Paragraph("Data Mode", font="Helvetica-Bold"))
table.add(Paragraph("Other Mode", font="Helvetica-Bold"))
table.add(Paragraph("Some float", font="Helvetica-Bold"))
table.add(Paragraph("Done", font="Helvetica-Bold"))

for i in range(number_of_samples):
    table.add(Paragraph(f"Sample_{i}"))
    table.add(Image(Path("./sample.png"), width=Decimal(250), height=Decimal(156)))
    table.add(Paragraph("yes"))
    table.add(Paragraph("increasing"))
    table.add(Paragraph("="))
    table.add(Paragraph("4.342E+00"))
    table.add(Paragraph("no"))

table.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
layout.add(table)

with open("/Users/si/Desktop/output.pdf", "wb") as out_file_handle:
    PDF.dumps(out_file_handle, doc)

