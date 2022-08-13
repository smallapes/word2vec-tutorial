import gensim
import jieba
import warnings
warnings.filterwarnings('ignore')

name=['峨眉派','倚天剑','屠龙刀','金毛狮王','青翼蝠王',\
      '谢逊','杨逍','冷谦','赵敏','乾坤大挪移','明教',\
      '郭襄','昆仑派','六大派','少林派','九阳真经','紫衫龙王','韦一笑']
for col in name:
    jieba.suggest_freq(col,True)

#分词
fin=open(filename_novel,'r')
fou=open(filename_segment,'w')
for line in fin.readlines():
    newline=jieba.cut(line,cut_all=False)
    str_out=' '.join(newline)\
        .replace('，','').replace('。','')\
        .replace(',','').replace('.','')\
        .replace('?','').replace('？','')\
        .replace('!','').replace('！','')\
        .replace('（','').replace('(','')\
        .replace('）','').replace(')','')\
        .replace('“','').replace('”','').replace('"','')\
        .replace('’','').replace('‘','').replace('\'','')\
        .replace('、','').replace('：','').replace(':','')\
        .replace('[','').replace(']','')\
        .replace('{','').replace('}','')\
        .replace('<','').replace('>','')\
        .replace('《','').replace('》','')\
        .replace(';','').replace('；','')\
        .replace('-','').replace('_','')\
        .replace('·','').replace('+','')\
        .replace('…','')\
        .replace('〗','').replace('〖','')
    fou.write(str_out)
fou.close()

sentences=gensim.models.word2vec.LineSentence(filename_segment)
model=gensim.models.word2vec.Word2Vec(sentences,size=20,window=5,min_count=10,workers=4)
model.save(filename_model)


def getSimilarity(s):
  print('similarity by word of :' + s)
  for k in model.similar_by_vector(s, 5):
    print(k[0], k[1])


getSimilarity('张无忌')