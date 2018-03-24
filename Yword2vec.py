#coding:utf-8
from gensim.models import word2vec
import gensim
import logging
import numpy as np

def build_word_dict(model_path):
    """  获取word2vec模型的所有词向量
    :param model_path: 已经训练好的word2vec模型保存路径
    :return:   """
    model = gensim.models.Word2Vec.load(model_path)
    vocab = model.wv.vocab
    word_vector = {}
    for word in vocab:
        word_vector[word] = model[word]
    return word_vector
def readResult():
    fa = open("Data/jiebaOut/2.txt", 'r',encoding='utf-8')
    next(fa)
    key=[]
    value=[]
    for line in fa.readlines():
        # print("line",line)
        lineKey=line.split(" ")[0]
        lineValue=line.split(" ")[1:-1]
        key.append(lineKey)
        value.append(lineValue)
    #write
    file1 = open('data3.txt', 'w',encoding='utf-8')
    file2 = open('data4.txt', 'w')
    for i in key:
        file1.write(i)
        file1.write('\n')
    file1.close()
    for i in value:
        for j in i:
          file2.write(str(j))
          file2.write(' ')
        file2.write('\n')
    file2.close()
    fa.close()


# 主程序
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"Data/jiebaOut/1.txt")  # 加载语料
model = word2vec.Word2Vec(sentences, min_count=1,size=100)  # 训练skip-gram模型，默认window=5

print ("model",model)



#y3=model['']
#print("y3",y3)
# 保存模型，以便重用
model.save('model/word2vec_model')
#new_model=gensim.models.Word2Vec.load('/model/word2vec_model')
#aaa=build_word_dict(model)
model.wv.save_word2vec_format("Data/jiebaOut/2.txt")
readResult()





