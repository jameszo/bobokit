# -*- coding: utf-8 -*-

from wordcloud import WordCloud
from PIL import Image
import codecs
import numpy as np
import jieba
import matplotlib.pyplot as plt


def draw_wordcloud():
    comment_text = open('/Volumes/iserv-data/data/word_count/gushici_new/cloud_words.txt','r').read()
    cut_text = " ".join(jieba.cut(comment_text))
    image = Image.open(r'./cloud_bg.png')
    graph = np.array(image)
    cloud = WordCloud(
        font_path="ameisimple.ttf",
        background_color='white',
        mask=graph,
        max_words=2000,
        max_font_size=40
    )
    word_cloud = cloud.generate(cut_text) 
    word_cloud.to_file("word_cloud.jpg") 
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    draw_wordcloud()

