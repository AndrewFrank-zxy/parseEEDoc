# -*- coding: utf-8 -*-

"""Python implementation of the TextRank algoritm.

From this paper:
    https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf

Based on:
    https://gist.github.com/voidfiles/1646117
    https://github.com/davidadamojr/TextRank
"""
from config import path_config
import util

import matplotlib.pyplot as plt
import networkx as nx
import editdistance
import itertools
import nltk

import io
import os
import re
pc = path_config()
match_filter = re.compile(r'^\W+$')

def setup_environment():
    """Download required resources."""
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    print('Completed resource downloads.')


# filter out nouns, and proper nouns
def filter_for_tags(tagged, tags=['NN', 'NNS', 'NNP', 'NNPS']):
    """Apply syntactic filters based on POS tags."""
    return [item for item in tagged if item[1] in tags and not re.match(match_filter, item[0])]


def normalize(tagged):
    """Return a list of tuples with the first item's periods removed."""
    return [(item[0].replace('.', ''), item[1]) for item in tagged]


def unique_everseen(iterable, key=None):
    """List unique elements in order of appearance.

    Examples:
        unique_everseen('AAAABBBCCDAABBB') --> A B C D
        unique_everseen('ABBCcAD', str.lower) --> A B C D
    """
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in [x for x in iterable if x not in seen]:
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def build_graph(nodes):
    """Return a networkx graph instance.

    :param nodes: List of hashables that represent the nodes of a graph.
    """
    gr = nx.Graph()  # initialize an undirected graph
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))

    # add edges to the graph (weighted by Levenshtein distance)
    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = editdistance.eval(firstString, secondString)
        gr.add_edge(firstString, secondString, weight=levDistance)

    return gr


def draw_graph(graph):
    layout = nx.spring_layout(graph)
    plt.figure(1)
    nx.draw(graph, pos=layout, node_color='y')
    plt.show()


def extract_key_phrases(text, nums=-1, comb=False):
    """Return a set of key phrases.

    :param text: A string.
    """
    # tokenize the text using nltk
    word_tokens = nltk.word_tokenize(text)

    # assign POS tags to the words in the text
    tagged = nltk.pos_tag(word_tokens)
    textlist = [x[0] for x in tagged]
    # print(textlist)

    tagged = filter_for_tags(tagged)
    tagged = normalize(tagged)

    unique_word_set = unique_everseen([x[0] for x in tagged])
    word_set_list = list(unique_word_set)

    # this will be used to determine adjacent words in order to construct
    # keyphrases with two words

    graph = build_graph(word_set_list)

    # pageRank - initial value of 1.0, error tolerance of 0,0001,
    calculated_page_rank = nx.pagerank(graph, weight='weight')

    # most important words in ascending order of importance
    # keyphrases = sorted(calculated_page_rank, key=lambda x: x.get,
    #                     reverse=True)
    keyphrases = sorted(calculated_page_rank.items(), key=lambda x: x[1],
                        reverse=True)

    # the number of keyphrases returned will be relative to the size of the
    # text (a third of the number of vertices)
    nums = (min(int(nums), len(word_set_list)) if int(nums) > -1
            else len(word_set_list) // 3 + 1)
    keyphrases = keyphrases[0:nums]
    keyphrases_search = [i[0] for i in keyphrases]

    # take keyphrases with multiple words into consideration as done in the
    # paper - if two words are adjacent in the text and are selected as
    # keywords, join them together
    modified_key_phrases = set([])
    # keeps track of individual keywords that have been joined to form a
    # keyphrase
    dealt_with = set([])
    i = 0
    j = 1
    while j < len(textlist):
        first = textlist[i]
        second = textlist[j]
        if first in keyphrases_search and second in keyphrases_search:
            keyphrase = first + ' ' + second
            modified_key_phrases.add(keyphrase)
            dealt_with.add(first)
            dealt_with.add(second)
        else:
            if first in keyphrases_search and first not in dealt_with:
                modified_key_phrases.add(first)

            # if this is the last word in the text, and it is a keyword, it
            # definitely has no chance of being a keyphrase at this point
            if j == len(textlist) - 1 and second in keyphrases_search and \
                    second not in dealt_with:
                modified_key_phrases.add(second)

        i = i + 1
        j = j + 1

    return modified_key_phrases, keyphrases, graph


def extract_sentences(text, summary_length=100, clean_sentences=False, language='english'):
    """Return a paragraph formatted summary of the source text.

    :param text: A string.
    """
    sent_detector = nltk.data.load('tokenizers/punkt/'+language+'.pickle')
    sentence_tokens = sent_detector.tokenize(text.strip())
    graph = build_graph(sentence_tokens)

    calculated_page_rank = nx.pagerank(graph, weight='weight')

    # most important sentences in ascending order of importance
    sentences = sorted(calculated_page_rank, key=calculated_page_rank.get,
                       reverse=True)

    # return a 100 word summary
    summary = ' '.join(sentences)
    summary_words = summary.split()
    summary_words = summary_words[0:summary_length]
    dot_indices = [idx for idx, word in enumerate(
        summary_words) if word.find('.') != -1]
    if clean_sentences and dot_indices:
        last_dot = max(dot_indices) + 1
        summary = ' '.join(summary_words[0:last_dot])
    else:
        summary = ' '.join(summary_words)

    return summary


def gen_key_phrases(para_content, key_phrases, para_num):
    """Generate key phrases to write."""
    kpp = 'Key phrases in paragraph%d:\n' % para_num
    kpp = kpp + para_content + '\n\n'
    for key_phrase in key_phrases:
        kpp = kpp + key_phrase + ' '
    kpp = kpp + '\n===========\n'
    return kpp

def write_key_phrases(filename, key_phrases):
    """Write key phrases to a file."""
    print("Generating output to " + pc.trkp + '/' + filename)
    key_phrase_file = io.open(
        pc.trkp + '/' + filename, 'w', encoding='UTF-8')
    key_phrase_file.write(key_phrases)
    key_phrase_file.close()

    print("-")


def write_summary(filename, summary):
    """Write summaries to a file."""
    print("Generating output to " + pc.trsp + '/' + filename)
    summary_file = io.open(pc.trsp + '/' + filename, 'w', encoding='UTF-8')
    summary_file.write(summary)
    summary_file.close()

    print("-")


def summarize_all():
    # retrieve each of the articles
    articles, dp = util.retrieve_input_path(pc.tap, 'txt')

    for article in articles:
        article_path = util.full_local_path(pc.tap, article)
        print('Reading \"' + article_path + '\"')
        article_file = io.open(article_path,
                               'r', encoding='UTF-8')
        text = article_file.read()
        text_list = text.split('\n')
        n = 0
        kpa = ''
        for prgh in text_list:
            n += 1
            m_keyphrases, keyphrases, graph = extract_key_phrases(prgh, 10)
            kpa = kpa + gen_key_phrases(prgh, m_keyphrases, n)
        write_key_phrases(article, kpa)

        # keyphrases, graph = extract_key_phrases(text)
        # summary = extract_sentences(text)
        # draw_graph(graph)
if __name__ == '__main__':
    summarize_all()
