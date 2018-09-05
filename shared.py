import json
from IPython.display import display, Markdown, HTML
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

'''
List of common packages
Uncomment any number of these and replace import
statements with "from shared import *
'''
# import os
# import sys
# import pickle
# import requests
# from glob import glob
# from datetime import datetime
# import numpy as np
# import pandas as pd
# from scipy import stats
# import matplotlib.pyplot as plt
# import statsmodels.api as sm
# import sklearn
# import keras


def make_link(filename, section, link_within_doc=True, link_type='ipynb'):

    if not filename.endswith(link_type) and not link_within_doc:
        filename = filename.replace('ipynb', link_type)
    prefix = '' if link_within_doc else filename
    return prefix + '#' + section


def display_master_toc(link_type='html'):
    display(Markdown('# Table of Contents'))

    # TODO: Add acknowledgements?
    '''
    Book structure, particularly Table of Contents, based on slides by Jim Arlow
    https://www.slideshare.net/jimarlow/want-to-write-a-book-in-jupyter-heres-how

    Reference handling adapted from code by Valerio Basile
    http://valeriobasile.github.io/Managing-my-own-bibliography/

    '''
    # display(Markdown('* [Acknowledgements](acknowledgements.{})'.format(link_type)))

    num_units = 9
    for n in range(num_units):
        display_unit_toc('unit{}/notebook.ipynb'.format(n + 1), toc_head=False, link_within_doc=False, link_type=link_type)
        lab_link = '* [Unit {} Lab](unit{}/lab.ipynb)'.format(n + 1, n + 1)
        display(Markdown(lab_link))

    display(Markdown('* [References](refs.{})'.format(link_type)))


def display_unit_toc(filename=__name__, toc_head=True, link_within_doc=True, link_type='ipynb'):
    with open(filename) as data_file:
        data = json.load(data_file)
    contents = []
    for c in data['cells']:
        s = c['source']
        if not any(s):
            continue
        line1 = s[0].strip()
        if line1.startswith('#') and line1.endswith('#'):
            line1 = line1[:-1]  # remove trailing #
            count = line1.count('#') - 1 # count indent level based on leading #
            plaintext = line1[count + 1:].strip()
            section = plaintext.replace(' ', '-')
            link = make_link(filename, section, link_within_doc=link_within_doc, link_type=link_type)
            list_item = ' ' * count + '* [{}]({})'.format(plaintext, link)
            contents.append(list_item)
    # display(HTML("<a id='table_of_contents'></a>"))
    if toc_head:
        display(Markdown('# Table of Contents'))
    display(Markdown('\n'.join(contents)))


# Adapted from code by Valerio Basile
# http://valeriobasile.github.io/Managing-my-own-bibliography/
def display_refs():

    with open('refs.bib') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    md = []
    for bib_item in bib_database.entries:

        if 'booktitle' in bib_item.keys():
            venue = u', {}'.format(bib_item['booktitle']).replace('{', '').replace('}', '')
        elif 'journal' in bib_item.keys():
            venue = u', {}'.format(bib_item['journal'])
        else:
            venue = u''

        if 'pages' in bib_item.keys():
            pages = u', {}'.format(bib_item['pages'])
        else:
            pages = u''

        if 'file' in bib_item.keys():
            pdf_link = u' [PDF]({})'.format(bib_item['file'].split(':')[1])
        else:
            pdf_link = u''

        md.append(u"- {0} *{1}* ({2}){3}{4} {5} \n".format(bib_item['author'],
                                                           bib_item['title'].replace('{', '').replace('}', ''),
                                                           bib_item['year'],
                                                           venue,
                                                           pages,
                                                           pdf_link))

    display(Markdown('# References'))
    display(Markdown('\n'.join(sorted(md))))
