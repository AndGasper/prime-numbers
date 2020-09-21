#!/usr/bin/env python3
from pdfminer.high_level import extract_text_to_fp, extract_pages
from pdfminer.layout import LAParams, LTTextContainer
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


def get_pdf_document():
    pdf_document = ""



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
    document_pages = pdf_document.catalog['Pages']
    resolved_objects = document_pages.resolve()
    print("\n document_pages")
    print(document_pages)

    print("\n resolved_objects")
    print(resolved_objects)
    for resolved_object in resolved_objects['Kids']:
        print("\n resolve resolve")
        print(resolved_object.resolve())

    

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




document_properties = get_document_properties(pdf_document)
print("\n document_properties")
print(document_properties)


pages_with_primes = get_specific_pages(PATH_TO_PDF, [8], 1)
try: 
    while True:
        # so this is really the page_layout
        page = next(pages_with_primes)
        print('\n page inside of while')
        print(page)
        for element in page:
            if isinstance(element, LTTextContainer):
                print("\n element is of type text; element.get_text():")
                text_container = element
                print(element.get_text())
except StopIteration:
    print("StopIteration reached")
finally:
    print("Finally block")


# try:
#     page_with_prime = next(pages_with_primes)


# print("output_string:\n")
# print(output_string)