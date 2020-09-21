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



"""
Input:
pages = extract_pages(...)
Output:
pages:
<generator object extract_pages at 0x034D2270>
"""


I have no idea why people use pdfminer.

Maybe more guesstimate-ing with the input.




So it pulls it out in vertical slices.
```
 element is of type text; element.get_text():
50
4
7527
33
43
63
69
81
91
99
609
23
29
39
53
57
59
81
99
701
11
13
17
37
41
43
77
79
91
97
807
09
19
37
43
57
69
81
903
11
17
33
39
47
51
63
69
77
81
8017
23
29
49
73
79
91
109
19
21
31
57
63
79
87
93
97
221
39
47
59
71
81
99
311
13
37
41
53
71
83
97
407
09
13
37
49
63
73
79
81
87
91
97
523
27
33
39
41
63
71
89
93


 element is of type text; element.get_text():
4


 element is of type text; element.get_text():
25
2
1383
91
97
401
07
19
33
67
81
87
91
93
99
503
17
21
23
29
57
59
63
69
77
87
89
99
601
11
13
17
47
49
61
73
83
701
13
27
37
39
51
57
67
73
87
99
803
17
21
39
41
51
59
63
71
81
93
911
29
37
43
61
77
91
97
2003
13
27
31
37
39
51
63
67
73
79
91
93
109
11
23
29
33
47
53
57
59
71
89
93
229
47
59
71
73
77
79
83
91
303
2
```