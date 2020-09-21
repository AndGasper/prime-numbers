import pdfminer
PDFMINER_VERSION = pdfminer.__version__

print("pdfminer version:${VERSION}".format(
    VERSION=PDFMINER_VERSION
))

import pprint

pprint.pprint(pdfminer)