# -*- coding: utf-8 -*-
from textrank.TextRank4Keyword import TextRank4Keyword
from textrank.TextRank4Sentence import TextRank4Sentence
from document.document import get_document

# def initialize():
#     """Download required nltk libraries."""
#     textrank.setup_environment()


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


def extract_key_phrases(pragh, num=5):
    print(pragh)
    print()

    tr4w = TextRank4Keyword()

    # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
    tr4w.analyze(text=pragh, lower=False, window=2)

    print('keywords:')
    for item in tr4w.get_keywords(num, word_min_len=1):
        # print(item.word, item.weight)
        print(item.word)

    print()
    print('keyphrases:')
    for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=0):
        print(phrase)

    tr4s = TextRank4Sentence()
    tr4s.analyze(text=pragh, lower=False, source='all_filters')

    print()
    print('abstract:')
    for item in tr4s.get_key_sentences(num=1):
        print(item.sentence)
    print()
    # print(item.index, item.weight, item.sentence)


if __name__ == '__main__':
    docs = get_document()
    for doc in docs:
        paragraphs = docs[doc].split('\n')
        print(paragraphs)
        n = 0
        kpa = ''
        for prgh in paragraphs:
            n += 1
            extract_key_phrases(prgh)

#             m_keyphrases, keyphrases, graph = extract_key_phrases(prgh, 10)
#             kpa = kpa + gen_key_phrases(prgh, m_keyphrases, n)
#         write_key_phrases(article, kpa)

#         keyphrases, graph = extract_key_phrases(text)
#         summary = extract_sentences(text)
#         draw_graph(graph)

#     # retrieve each of the articles
# #     articles, dp = util.retrieve_input_path(pc.tap, 'txt')

# #     for article in articles:
# #         article_path = util.full_local_path(pc.tap, article)
# #         print('Reading \"' + article_path + '\"')
# #         article_file = io.open(article_path,
# #                                'r', encoding='UTF-8')
# #         text = article_file.read()
# #         text_list = text.split('\n')
# #         n = 0
# #         kpa = ''
# #         for prgh in text_list:
# #             n += 1
# #             extract_key_phrases(prgh)

#         #     m_keyphrases, keyphrases, graph = extract_key_phrases(prgh, 10)
#         #     kpa = kpa + gen_key_phrases(prgh, m_keyphrases, n)
#         # write_key_phrases(article, kpa)

#         # keyphrases, graph = extract_key_phrases(text)
#         # summary = extract_sentences(text)
#         # draw_graph(graph)

#     # extract_summary("./pdfReader/txt/Debtholders' Demand for Conservatism Evidence from Changes in Directors' Fiduciary Duties.txt")
#     # extract_phrases("./pdfReader/txt/Debtholders' Demand for Conservatism Evidence from Changes in Directors' Fiduciary Duties.txt")
#     # textrank.summarize_all()
#     # text = codecs.open("articles-txt/Debtholders' Demand for Conservatism Evidence from Changes in Directors' Fiduciary Duties.txt", 'r', 'utf-8').read()
#     # tr4w = TextRank4Keyword()

#     # tr4w.analyze(text=text, lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

#     # print( 'keywords:' )
#     # for item in tr4w.get_keywords(5, word_min_len=1):
#     # # print(item.word, item.weight)
#     #     print(item.word)

#     # print()
#     # print( 'keyphrases:' )
#     # for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 0):
#     #     print(phrase)

#     # tr4s = TextRank4Sentence()
#     # tr4s.analyze(text=text, lower=True, source = 'all_filters')

#     # print()
#     # print( 'abstract:' )
#     # for item in tr4s.get_key_sentences(num=1):
#     #     print(item.sentence)
#     # # print(item.index, item.weight, item.sentence)
