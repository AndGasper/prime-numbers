- Why ~`pypdf`~ ~`pyPdf2`~ ? 
- Because I googled python pdf parser, and the pip page for `pdfreader` was the first result. Some data science article mentioned `pdfminer`. 
Shout out to the [pdfreader people](https://github.com/maxpmaxp/pdfreader#related-projects) for mentioning the other projects/libraries. 
```
Related Projects
 - pdfminer (cool stuff)
 - pyPdf
 - xpdf
 - pdfbox
 - mupdf

Source: https://github.com/maxpmaxp/pdfreader#related-projects
```


I picked [`pyPdf`](https://pypi.org/project/pyPdf/) because it sounded the simplest. 
- But it turns out `pyPdf` is now `pyPDF2` since the OP doesn't maintain it anymore.

- But when I tried to find the github/homepage for `pypdf2` it seems like the project has been abandoned...so let's pick the 

- Why ~`pdfminer`~ `pdfminer.six`
- Because when `pyPdf` went bust I was just like fuggit, I guess I'll just pick the first one on the list (which makes more sense than picking pyPdf because it _sounded_ simpler)
- But then it turned out that `pdfminer` is at the end of its lifecycle...

>  PDFMiner
PDFMiner is a text extraction tool for PDF documents.  
...  
Warning: As of 2020, PDFMiner is not actively maintained. The code still works, but this project is largely dormant. For the active project, check out its fork pdfminer.six.  
Source: https://github.com/euske/pdfminer#pdfminer

- So I picked `pdfminer.six` because jesus christ, let's move on.