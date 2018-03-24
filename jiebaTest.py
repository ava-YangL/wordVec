#coding=utf-8
import jieba,math
import jieba.analyse
from gensim.models import word2vec
'''
jieba.cut主要有三种模式
'''
#随便对一个动物园的评论进行分析
str_text="真是好久好久没来哈皮娜拉野生动物园了，记忆里还是小时候三四年级学校组织春游去的银河系"
#全模式cut_all=True
str_quan1=jieba.cut(str_text,cut_all=True)
print('全模式分词：{ %d}' % len(list(str_quan1)))
str_quan2=jieba.cut(str_text,cut_all=True)
print("/".join(str_quan2))
# print(str(str_1))   #为一个generator 用for循环可以得到分词的结果
# str_1_len=len(list(str_1))  #为什么？这里执行后后面.join 就不执行，求告知

#精准模式cut_all=False，默认即是
str_jing1=jieba.cut(str_text,cut_all=False)
print('精准模式分词：{ %d}' % len(list(str_jing1)))
str_jing2=jieba.cut(str_text,cut_all=False)
print("/".join(str_jing2))

#搜索引擎模式  cut_for_search
str_soso1=jieba.cut_for_search(str_text)
print('搜索引擎分词：{ %d}' % len(list(str_soso1)))
str_soso2=jieba.cut_for_search(str_text)
print("/".join(str_soso2))


# to test the segment result
#PrintListChinese(fileTrainSeg[10])

