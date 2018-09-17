# pdfReader

How to use
==========

1. Create a folder named `pdf` in `pdfReader/` and put pdf documents in `./pdf/`
2. Run `Python pdfReader.py`
3. pdf documents will be converted into txt files in `./txt/`

Dependence: Install pdfminer
================

* Webpage: https://euske.github.io/pdfminer/
* Download (PyPI): https://pypi.python.org/pypi/pdfminer/
* Demo WebApp: http://pdf2html.tabesugi.net:8080/

How to Install
--------------

* Install Python 2.6 or newer. (**For Python 3 support have a look at [pdfminer.six](https://github.com/goulu/pdfminer)**).
* Download the source code.
* Unpack it.
* Run `setup.py`:

$ python setup.py install

* Do the following test:

$ pdf2txt.py samples/simple1.pdf