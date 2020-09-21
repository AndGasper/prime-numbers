#!/usr/bin/env python3
from pdfminer.high_level import extract_text_to_fp, extract_pages
from pdfminer.layout import LAParams, LTTextContainer, LTTextBoxHorizontal, LTTextLine, LTTextBoxVertical
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

# output_string = StringIO()
# with open(PATH_TO_PDF, 'rb') as fh:
#     extract_text_to_fp(
#         fh, 
#         output_string,
#         page_numbers=8,
#         maxpages=1,
#         output_type="xml",
#         laparams=LAParams(),
#         # output_type='html',
#         codec=None,
#         debug=True
#     )

# get pages
# with open(PATH_TO_PDF, 'rb') as fh:
#     print("\n should be file handle object:")
#     print(fh)
#     # pages = extract_pages(
#     #     fh,
#     #     page_numbers=8,
#     #     maxpages=9
#     # )
#     pages = extract_pages(
#         fh,
#         maxpages=3
#     )

# get_pages
# extract_pages is "special" in that it handles the open call...



"""
@name get_specific_pages
@description - get specific pages within a pdf -> made it its own function because extract_pages behaves differently
@param {list} page_numbers - example: want page 9? pass in [8]
@param {int} maxpages - maximum number of pages to parse; default of 1 page
@return {LTPage}
"""
def get_specific_pages(pdf_path_as_string, page_numbers=[0], maxpages=1):
    pages = extract_pages(
        PATH_TO_PDF,
        page_numbers=page_numbers,
        maxpages=1
    )
    return pages



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
with open(PATH_TO_PDF, 'rb') as fh:
    parser = PDFParser(fh)
    pdf_document = PDFDocument(parser)
    print("\n pdf_document")
    print(pdf_document)

    # ? -> PDFObjRef
    # document_pages = pdf_document.catalog['Pages']
    # resolved_objects = document_pages.resolve()
    # print("\n document_pages")
    # print(document_pages)

    # print("\n resolved_objects")
    # print(resolved_objects)
    # for resolved_object in resolved_objects['Kids']:
    #     print("\n resolve resolve")
    #     print(resolved_object.resolve())

    

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



# LTTextBoxHorizontal -> LTTextBox -> LTTextContainer -> LTExpandableContainer + LTText
#                                        |
#                                       get_text

"""
@name is_primes_section
@description - a very flimsy (why? because in an ideal world there'd be a stronger relationship between the actual vertical slices
of primes and isolating the headers and sidebars) means of accumulating the primes
"""

# maybe the more appropriate relationship is the positioning within the page since 
# it seems like the bottom footer that is smaller does not quite get picked up

# gross structure
def is_primes_section(horizontal_textbox: LTTextBoxHorizontal) -> {bool, List}:
    is_primes_section = {
        is_primes_section: False,
        primes: []
    }
    text_content_as_string = horizontal_textbox.get_text()
    text_content = text_content.split('\n')
    # a simple pass showed that the primes series had a trailing '' but the column names did not.
    # like I said flimsy.
    filtered_text_content = filter(lambda item: True if item else False, text_content)
    if (len(filtered_text_content) == 100):
        is_primes_section = {
            is_primes_section: True,
            primes = filtered_text_content
        }
    else:
        is_primes_section = {
            is_primes_section: False,
            primes: []
        }

    return is_primes_section

# kind of feels like I'm missing the point at the orientation/decode level
# ')\n1\n1\n0\n2\n' => 2011
# but I don't want to read too much into that right now since I'd be basing any generalization on literally a single section of a single page.

primes = []
try: 
    while True:
        # so this is really the page_layout
        page = next(pages_with_primes)
        print("\n what is page again?")
        print(page)
        divisions_of_page = page.group
        # really iterating over the table itself. 
        for element in page:
            element_type = get_element_type(element)
            element_types.append(element_type)
            # very flimsy
            is_primes_section = is_primes_section(element)
            if (is_primes_section.is_primes_section):
                # do prime logic
                # there's a version of this somewhere that can kind of leverage the headers
                # but the relationship is not obvious to me at this time. 
                # (so like 547 gets truncated to 47, but only after 541 appears to make it clear the values have "rolled over")
                primes.append(is_primes_section.primes) 
            # it is bothering me that it using the term "horizontal"
            # when it is correctly slicing "vertically"
                
except StopIteration:
    print("StopIteration reached")
finally:
    print("Finally block")

print("\n primes: \n")
print(primes)