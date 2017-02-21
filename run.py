#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
from collections import Counter

words_list = list()
target_words_list = list()

with open('happiness_seg.txt', encoding="utf-8") as f_read:
    content = f_read.read()
    content = content.replace(" ", "")
    words = jieba.cut(content, cut_all=False)
    for i in words:
        words_list.append(i)

mark = 1
for i in words_list:
    if len(words_list[mark - 1]) >= 2 and len(words_list[mark]) >= 2 and len(words_list[mark + 1]) >= 2:
        word1 = "%s_%s" % (words_list[mark-1], words_list[mark])
        word2 = "%s_%s" % (words_list[mark], words_list[mark + 1])
        target_words_list.append(word1)
        target_words_list.append(word2)
    mark += 1
    
words_counts = Counter(target_words_list)
top_ten = words_counts.most_common(10)
print(top_ten)
