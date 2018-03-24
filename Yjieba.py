#coding:utf-8
import jieba
import codecs

#StopWord
def createstoplist(stoppath):
    print('load stopwords...')
    stoplist=[line.strip() for line in codecs.open(stoppath,'r',encoding='utf-8').readlines()]
    stopwords={}.fromkeys(stoplist)
    return stopwords

# read the file by line
def readFileByLine(file):
    fileTrainRead = []
    # fileTestRead = []
    with open(file, "r", encoding="utf-8", errors="ignore") as fileTrainRaw:
        for line in fileTrainRaw:
            fileTrainRead.append(line)
    return fileTrainRead

# segment word with jieba
def segWithJieba(fileRead):
    stopwords = createstoplist(fileStopPath)
    fileTrainSeg = []
    for i in range(len(fileRead)):
        words = jieba.cut(fileRead[i], cut_all=False)
        seg = ''
        for word in words:
            if word not in stopwords:
                if word != '\t'and word != '\n' and word!='\ufeff':
                    fileTrainSeg.append([(word)])
                    #   fileTrainSeg.append([' '.join(list(words))])
                    #  if i % 100 == 0 :
                    #    print (i)
                    print("word", word)
    return fileTrainSeg

# save the result
def saveResult(fileSeg):
    with open(fileSegWordDonePath, 'wb') as fW:
        for i in range(len(fileSeg)):
            fW.write(fileSeg[i][0].encode('utf-8'))
            fW.write('\n'.encode('utf-8'))


#main
filePath='Data/jiebaIn/1.txt'
fileSegWordDonePath ='Data/jiebaOut/1.txt'
fileStopPath='Data/Stop.txt'
fileIn=readFileByLine(filePath)
fileOut=segWithJieba(fileIn)
saveResult(fileOut)





