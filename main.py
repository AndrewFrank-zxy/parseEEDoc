# -*- coding: utf-8 -*-

import os
import io
import textrank

def initialize():
    """Download required nltk libraries."""
    textrank.setup_environment()

def extract_summary(filename):
    """Print summary text to stdout."""
    with open(filename) as f:
        summary = textrank.extract_sentences(f.read())
        print(summary)

def extract_phrases(filename):
    """Print key-phrases to stdout."""
    with open(filename) as f:
        phrases = textrank.extract_key_phrases(f.read())
        print(phrases)


if __name__ == '__main__':
    # extract_summary("./pdfReader/txt/Debtholders' Demand for Conservatism Evidence from Changes in Directors' Fiduciary Duties.txt")
    # extract_phrases("./pdfReader/txt/Debtholders' Demand for Conservatism Evidence from Changes in Directors' Fiduciary Duties.txt")
    textrank.summarize_all()
