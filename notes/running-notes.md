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

```
# default
                # line_overlap=0.5, -> If two characters have more overlap than this they are considered to be on the same line. The overlap is specified relative to the minimum height of both characters.
                # char_margin = 2.0, -> If two characters are closer together than this margin they are considered part of the same line. The margin is specified relative to the width of the character.
                # line_margin = 0.5, -> If two lines are are close together they are considered to be part of the same paragraph. The margin is specified relative to the height of a line.
                # word_margin = 0.1 -> If two characters on the same line are further apart than this margin then they are considered to be two separate words, and an intermediate space will be added for readability. The margin is specified relative to the width of the character.
                # boxes_flow=0.5, -> -1.0 only horizontal position matters to +1.0 only vertical position matters
                # detect_vertical=False,
                # all_texts=False
                horizontal_textbox_layout_params = LAParams(
                    line_overlap=10,
                    char_margin=0.5,
                    line_margin=0.5,
                    boxes_flow=None, # disable advanced layout analysis
                    detect_vertical=True,
                    all_texts=False
                )
```



```
# LTTextBoxHorizontal -> LTTextBox -> LTTextContainer -> LTExpandableContainer + LTText
#                                        |
#                                       get_text
```




------

# Fixtures 
- minimal_pdf_file.pdf
    - taken from PDF32000_2008_specification.pdf file H.2


<table>
    <thead>
        <th>Object Number</th>
        <th>Object type</th>
    </thead>
    <tbody>
    <tr>
        <td>1</td>
        <td>Catalog (document catalog)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Outlines (outline dictionary)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Pages (page tree node)</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Page (page object)</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Content stream</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Procedure set array</td>
    </tr>
    </tbody>
</table>


## 14.2 Procedure Sets -> this is where the danger comes in
<table>
    <thead>
        <th>Name</th>
        <th>Category of operators</th>
    </thead>
    <tbody>
        <tr>
            <td>Name</td>
            <td>Painting and graphics state</td>
        </tr>
        <tr>
            <td>Text</td>
            <td>Text</td>
        </tr>
        <tr>
            <td>ImageB</td>
            <td>GrayScale images or image masks</td>
        </tr>
        <tr>
            <td>ImageC</td>
            <td>Colour images</td>
        </tr>
        <tr>
            <td>ImageI</td>
            <td>Indexed (colour-table) images</td>
        </tr>
    </tbody>
</table>



## Workflow
    - Implement
        - pre-commit (local)
        - pipeline itself should commit and ultimately tag
        - Optimize the diff'ing/fsmonitor query for handling dependency monitoring

## Git diff
- Possibly `#TODO implement custom fsmonitor to accomodate diff's in Pipfile.lock`




# pre-commit hooks generate_requirements.py
- Purpose: separate changes to underlying dependencies from changes to codes
    - Why?: Think about automated vulnerability checks. One can decouple the "uh, what's this?" from "uh, what's this feature do?"

- Real purpose: I didn't want to forget to chedck if I actually had the dependencies listed somewhere.



- really a terrible way of doing it by page because it has to load the entire document to figure out where page 9 is


LTTextBoxHorizontal -> LTTextLineHorizontal


- Interesting
So whatever way I have it now,
it's going:
1,2,3,4,5,6,7,8,9,10,11,12,13 
then breaking into 
so like the second column
541\n



```

+-----------------------+
|           TITLE
| V       ACTUAL TABLE
| E
| R
| T
| I
| C
| A
| L
| H
| E
| A
| D
| E
| R
+------------------------+
```


describe("Page getting", function() {
    it should:
        return a Page with 3 groups
})



## Tests setup
- I was tearing my hair out about the layout analysis
    - So I'm just going to take a step back and try to get three groups
- [Based the testing structure on pytest good practices](https://docs.pytest.org/en/stable/goodpractices.html)


This is problematic if you are using a tool like tox to test your package in a virtual environment, because you want to test the installed version of your package, not the local code from the repository.

In this situation, it is strongly suggested to use a src layout where application root package resides in a sub-directory of your root:
```
setup.py
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py
```



>  `rootdir` is NOT used to modify sys.path/PYTHONPATH or influence how modules are imported. See pytest import mechanisms and sys.path/PYTHONPATH for more details.


```
Tests as part of application code
Inlining test directories into your application package is useful if you have direct relation between tests and application modules and want to distribute them along with your application:

setup.py
mypkg/
    __init__.py
    app.py
    view.py
    test/
        __init__.py
        test_app.py
        test_view.py
        ...
In this scheme, it is easy to run your tests using the --pyargs option:

pytest --pyargs mypkg
pytest will discover where mypkg is installed and collect tests from there.
```
pytest execute
- `pytest --pyargs primenumbers`

# virtual environment setup because I always forget and have to double look
0. which python
1. virtualenv -p ${USE THE OUTPUT FROM STEP 0} venv
    - create virtual environment using the specified python executable
2. source ./venv/Scripts/activate
    - run the activation script
3. pipenv install .
    - use pipenv to install the dependencies



LTTextLineHorizozntal
|
LTChar +  LTAnno + LTAnno

```
table_cell_header_row_la_params = LAParams(
    line_overlap=2,
    char_margin=2,
    line_margin=0.1,
    word_margin=0.01,
    boxes_flow=0 # vertical and horizontal position
)
```
^ Memory error lol
boxes_flow is horizontal and vertical positioning


```
exception MemoryError
Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects). The associated value is a string indicating what kind of (internal) operation ran out of memory. Note that because of the underlying memory management architecture (C’s malloc() function), the interpreter may not always be able to completely recover from this situation; it nevertheless raises an exception so that a stack traceback can be printed, in case a run-away program was the cause
```


fixture_table_header_row = ["\n", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","2","3","3","3","3","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49", "50" ]



"""

"""

```
self.page = get_page() # a miracle occurs with handling the file path and such and knowing which page to get
```


`class PageWithTable extends LTPage` might be more appropriate
since the core logic of what defines this particular Page is more about an item (a table) on the page.

class Page:
    def __init__(self):


"""
Some class...
"""
def test_get_table_header_row(self):
    table_header_row = self.page["table"]["header"]
    self.assertEqual(
        table_header_row,
        fixture_table_header_row,
        "Mismatch in the table header row."
    )


test_get_table = ["\n", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","2","3","3","3","3","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49", "50" ]

## [traceback - Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)



```
try:
    while True:
        # thing that throws conditional
except MemoryError:
    print("Oh no! MemoryError.")
    from traceback import print_exc
    from sys import stdout
    # print the exception to standard out.
    print_exc(
        file=stdout
    )
```
```
Oh no! MemoryError.
Traceback (most recent call last):
  File "prime-numbers/src/main.py", line 186, in <module>
    page = next(pages_with_primes)
  File "pdfminer/high_level.py", line 149, in extract_pages
    interpreter.process_page(page)
  File "pdfminer/pdfinterp.py", line 897, in process_page
    self.device.end_page(page)
  File "pdfminer/converter.py", line 52, in end_page
    self.cur_item.analyze(self.laparams)
  File "pdfminer/layout.py", line 811, in analyze
    self.groups = self.group_textboxes(laparams, textboxes)
  File "pdfminer/layout.py", line 758, in group_textboxes
    obj1, obj2))
MemoryError
 ```

 Ah, so it's up and dying when it has to do math. Kind of.