#!/usr/bin/env python3
from pdfminer.high_level import extract_text_to_fp, extract_pages
from pdfminer.layout import LAParams, LTTextContainer, LTTextBoxHorizontal, LTTextLine, LTTextBoxVertical, LTChar
from pdfminer.converter import XMLConverter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve_all
from sys import version_info
from io import StringIO
PATH_TO_PDF = "./references/a_reconstruction_of_lehmers_table_of_primes_roegel_1914.pdf"

if version_info > (3,0):
    from io import StringIO
    print("io came in as StringIO")
else:
    from io import BytesIO as StringIO


"""
@name get_specific_pages
@description - get specific pages within a pdf -> made it its own function because extract_pages behaves differently
@param {list} page_numbers - example: want page 9? pass in [8]
@param {int} maxpages - maximum number of pages to parse; default of 1 page
@return {LTPage}
"""
def get_specific_pages(pdf_path_as_string, page_numbers=[0], max_pages=1):
    pages = extract_pages(
        PATH_TO_PDF,
        page_numbers=page_numbers,
        maxpages=max_pages
    )
    return pages

# # returns a generator
# def get_specific_pages_without_interpreting(file_handle, password, page_numbers: List[int]=[0], laparams: LAParams):
    
#     yield uninterpreted_page


resource_manager = PDFResourceManager(
    caching=False
)
output_string = StringIO()
# hmm...
# self, resource_manager, output targe
device = XMLConverter(
    resource_manager,
    output_string,
    codec=None

)
# seems wasteful
# with open(PATH_TO_PDF, 'rb') as fh:
#     parser = PDFParser(fh)
#     pdf_document = PDFDocument(parser)
#     print("\n pdf_document")
#     print(pdf_document)

# do not decode the 

def create_device():
    type_converter = TypeConverter
    return type_converter


def get_pdf_document():

    return
    

from inspect import getmembers, isroutine
"""
@name get_document_properties 
@description - get the properties of a loaded document rather than just guessing
"""
def get_document_properties(pdf_document):
    # scrub the methods/routines
    document_properties = getmembers(pdf_document, lambda attribute: not(isroutine(attribute)))
    # scrub the prefixed __thingy__ default stuff
    filtered_attributes = [attribute for attribute in document_properties if not(attribute[0].startswith('__') and attribute[0].endswith('__'))]
    return filtered_attributes

# one of type in lttypes
def get_element_type(element):
    element_type = type(element)
    # element_type.split('pdfminer.layout.') # maybe
    return element_type



pages_with_primes = get_specific_pages(PATH_TO_PDF, [8], 1)
element_types = []
text_elements = []



"""
@name is_primes_section
@description - a very flimsy (why? because in an ideal world there'd be a stronger relationship between the actual vertical slices
of primes and isolating the headers and sidebars) means of accumulating the primes
"""

# maybe the more appropriate relationship is the positioning within the page since 
# it seems like the bottom footer that is smaller does not quite get picked up

# gross structure
def is_primes_section(horizontal_textbox: LTTextBoxHorizontal) -> {bool, list}:
    is_primes_section = {
        "is_primes": False,
        "primes": []
    }
    text_content_as_string = horizontal_textbox.get_text()
    text_content = text_content_as_string.split('\n')
    # a simple pass showed that the primes series had a trailing '' but the column names did not.
    # like I said flimsy.
    filtered_text_content = filter(lambda item: True if item else False, text_content)
    if (len(filtered_text_content) == 100):
        is_primes_section = {
            "is_primes": True,
            "primes": filtered_text_content
        }
    else:
        is_primes_section = {
            "is_primes": False,
            "primes": []
        }

    return is_primes_section

# kind of feels like I'm missing the point at the orientation/decode level
# ')\n1\n1\n0\n2\n' => 2011
# but I don't want to read too much into that right now since I'd be basing any generalization on literally a single section of a single page.

primes = []
# tuning the horizontal textbox layout
horizontal_textbox_layout_params = LAParams(
    line_overlap=0.1,
    char_margin=0.2,
    line_margin=1,
    word_margin=0.1,
    boxes_flow=0.5
)
# 58.748 - y1
# 536.136 - y2
KNOWN_Y1_COORDINATE = 58.748
KNOWN_Y2_COORDINATE = 536.136
# if isinstance(element, LTTextBoxHorizontal):
#     element_bounding_box = element.bbox
#     if ()

# # 161.327,542.988,163.258,546.933
# KNOWN_START_OF_TABLE_COORDINATES = {
#     x1: 161.327,
#     x2: 1
# }

"""
"1 - 48 583 \n" title
{
    x0:427.49863,
    x1:465.4567273915,
    y0:559.4267198580001,
    y1:567.606462858,
}
"""
"""
')\n1\n1\n0\n2\n'
{
    x0: 105.925, 
    y0: 443.960, 
    x1: 117.880, 
    y1: 471.907
}
"""
"""
{
    x0: 161.327,
    y0: 542.988,
    x1: 163.258,
    y1: 546.933
}
"""
table_coordinates = {
    "x0": 160,
    "y0": 546,
    "x1": 840,
    "y1": 595
}

def is_sequential(list_of_values: list):
    is_sequential = False
    return is_sequential

# very crude logic for identifying the headers
SIZE_OF_HEADER_CELLS = {
    # "height": 3.9452159999999594
    # "width": 1.931183231999995 # sincerely doubt the precision
    "height": 3.9,
    "width": 1.4
}
# something, something euler's method or newton's method for approximating error 
# would probably be relevant if I were elegant.
try: 
    while True:
        # LTPage
        page = next(pages_with_primes)
        # really iterating over the table itself. 
        for element in page:
            # x0, y0, x1, y1
            element_position = element.bbox
            # had to manually get the rough coordinates
            if element.x0 > table_coordinates["x0"]:
                if isinstance(element, LTTextBoxHorizontal):
                    element_text = element.get_text()
                    print("element_text\n")
                    print(element_text)
                    if element_text == '1\n':
                        print("first element of the header row")
                        print(element_text)
                    # if element_text == '50\n':
                    #     print("end of the header row")
                    #     print(element_text)
except StopIteration:
    print("StopIteration reached")
finally:
    print("Finally block")

print("\n primes: \n")
print(primes)