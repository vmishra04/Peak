#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:00:58 2019

@author: Megha
"""

def classify_text():
    """CLassifies text."""
    # [START language_classify_text]
import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

text = 'I have taken Wed Development classes, coding in HTML, CSS, and JavaScript. ' \
        'I am also taking an introduction to Data Science class and learning to' \
        'analyze data sets using python.'

client = language.LanguageServiceClient()

if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

categories = client.classify_text(document).categories

for category in categories:
    print(u'=' * 20)
    print(u'{:<16}: {}'.format('name', category.name))
    print(u'{:<16}: {}'.format('confidence', category.confidence))
    # [END language_classify_text]