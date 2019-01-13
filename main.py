# -*- coding: utf-8 -*-
import os
from textrank.TextRank4Keyword import TextRank4Keyword
from textrank.TextRank4Sentence import TextRank4Sentence
from document.document import get_document
from document.utils.util import ModefyPath
from document.result import save_result
from pyecharts import Graph
current_path = os.path.dirname(__file__)
mp = ModefyPath()

# def extract_summary(filename):
#     """Print summary text to stdout."""
#     with open(filename) as f:
#         summary = textrank.extract_sentences(f.read())
#         print(summary)


# def extract_phrases(filename):
#     """Print key-phrases to stdout."""
#     with open(filename) as f:
#         phrases = textrank.extract_key_phrases(f.read())
#         print(phrases)
def form_graph(para_msg, **args):
    store_msg = para_msg.split('_')
    link_source = args['graph']
    node_source = args['word']
    links = []
    nodes = []
    for i in node_source:
        nodes.append({'name': node_source[i]})
        j = 0
        for item in link_source[i]:
            if item == 1:
                links.append({"source": node_source[i], "target": node_source[j]})
            j += 1
    graph = Graph("段落关系图", width=1200, height=600)
    graph.add(
        "",
        nodes,
        links,
        repulsion=8000,
        # label_pos="right",
        # graph_repulsion=50,
        # is_legend_show=False,
        # line_curve=0.2,
        # label_text_color=None,
    )
    html_folder = mp.join_path(current_path, 'graph',
                     'doc' + store_msg[0])
    mp.create_folder(html_folder)
    graph.render(mp.join_path(html_folder, store_msg[1] + '.html'))
    return {'nodes': nodes, 'links': links}


def extract_key_phrases(paragraph, para_msg, num=5):
    result = 'paragraph:\n'
    result = result + paragraph + '\n\n'
    # print(paragraph)
    # print()

    tr4w = TextRank4Keyword()

    # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
    graph_msg = tr4w.analyze(text=paragraph, lower=False, window=2)
    print(graph_msg)
    form_graph(para_msg, **graph_msg)

    result = result + 'keywords:\n'
    # print('keywords:')
    for item in tr4w.get_keywords(num, word_min_len=1):
        # print(item.word, item.weight)
        result = result + item.word + '\n'
        # print(item.word)

    # result = result + '\nkeyphrases:\n' 
    # print()
    # print('keyphrases:')
    # for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=0):
    #     result = result + phrase + '\n'
        # print(phrase)

    tr4s = TextRank4Sentence()
    tr4s.analyze(text=paragraph, lower=False, source='all_filters')

    result = result + '\nabstract:\n'
    # print()
    # print('abstract:')
    for item in tr4s.get_key_sentences(num=1):
        result = result + item.sentence + '\n'
        # print(item.sentence)

    # print()
    # print(item.index, item.weight, item.sentence)
    return result + '====================================\n'


if __name__ == '__main__':
    # save_result('1', '1')
    result_all = ''
    docs = get_document('byTXT', './document/articles/txt/00466776.txt')
    # print(docs)
    doc_num = 0
    for doc in docs:
        paragraphs = docs[doc].split('\n')
        # print(paragraphs)
        para_num = 0
        for paragraph in paragraphs:
            para_num += 1
            para_msg = str(doc_num) + '_' + str(para_num)
            result_all = result_all + extract_key_phrases(paragraph, para_msg)
        save_result(doc, result_all)
