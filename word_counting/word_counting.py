"""
  This module contains all the necesary methods for word counting and co-word visualization
"""

import os
import json
import re
from collections import Counter
from itertools import combinations

import matplotlib.pyplot as plt
import networkx as nx
from wordcloud import WordCloud


def execute_wordcounting(articles):

    project_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))

    # Create the path to the output_files directory
    category_file = os.path.join(
        project_dir, "word_counting/category_variables.json")
    synonym_map = os.path.join(project_dir, "word_counting/synonym_map.json")
    # Carga categorías
    with open(category_file, "r", encoding="utf-8") as f:
        category_keywords = json.load(f)

    # Carga sinónimos (si lo usas)
    with open(synonym_map, "r", encoding="utf-8") as f:
        synonym_map = json.load(f)

    category_freq, total_freq = count_keywords_by_category(
        articles, category_keywords, synonym_map
    )

    generate_wordclouds(category_freq, total_freq, output_dir="wordclouds")

    all_keywords = [kw for kws in category_keywords.values() for kw in kws]
    generate_co_occurrence_network(
        articles, all_keywords, output_path="co_word_network.png")


def count_keywords_by_category(articles, category_keywords, synonym_map):
    category_freq = {cat: Counter() for cat in category_keywords}
    total_freq = Counter()
    abstract = ''
    for article in articles:
        if 'abstract' in article:
            abstract = article['abstract'].lower()

        for category, keywords in category_keywords.items():
            for keyword in keywords:
                main_keyword = synonym_map.get(keyword, keyword).lower()
                pattern = r'\b' + re.escape(main_keyword) + r'\b'
                count = len(re.findall(pattern, abstract))
                if count > 0:
                    category_freq[category][main_keyword] += count
                    total_freq[main_keyword] += count

    return category_freq, total_freq


def generate_wordclouds(category_freq, total_freq, output_dir="wordclouds"):
    os.makedirs(output_dir, exist_ok=True)

    for category, freq in category_freq.items():
        wc = WordCloud(width=800, height=400, background_color='white')
        wc.generate_from_frequencies(freq)
        wc.to_file(f"{output_dir}/{category.replace(' ', '_')}.png")

    wc = WordCloud(width=1000, height=500, background_color='white')
    wc.generate_from_frequencies(total_freq)
    wc.to_file(f"{output_dir}/total.png")


def generate_co_occurrence_network(articles, all_keywords, output_path="word_counting/co_word_network.png"):
    G = nx.Graph()
    for article in articles:
        abstract = article.get("abstract", "").lower()
        found_keywords = set()

        for kw in all_keywords:
            if re.search(r'\b' + re.escape(kw.lower()) + r'\b', abstract):
                found_keywords.add(kw)

        for a, b in combinations(found_keywords, 2):
            if G.has_edge(a, b):
                G[a][b]['weight'] += 1
            else:
                G.add_edge(a, b, weight=1)

    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, k=0.5)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue",
            edge_color="gray", font_size=10)
    plt.title("Co-word Network")
    plt.savefig(output_path)
    plt.close()
