#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 11:11:49 2019

@author: Megha
"""

def syntax_text():
     """Detects syntax in the text."""
    # [START language_syntax_text]
import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

text = 'I was the student body president of my school.'

client = language.LanguageServiceClient()

if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

    # Instantiates a plain text document.
    # [START language_python_migration_syntax_text]
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
tokens = client.analyze_syntax(document).tokens
    
pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
           'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

for token in tokens:
   part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
   print(u'{}: {}'.format(part_of_speech_tag.name,
         token.text.content))
    # [END language_python_migration_syntax_text]
    # [END language_syntax_text]