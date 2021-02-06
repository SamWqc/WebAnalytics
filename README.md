# WebAnalytics
*********************************************************************************************************

## crawling_main.ipynb

1.根据Pro_list.xlsx爬取每个Porf的信息

2.将爬取的数据放入prof_info.csv中；爬取失败的名单存入failure.csv

## add_google_scholarName.ipynb

将Pro_list.xlsx中的名字统一成GoogleScholar上的名字


## adding_info_ofFailing.ipynb
往prof_info.csv中追加数据


## data_convertion.ipynb
1.对prof_info.csv中的数据进行转换处理：

a)统一名字的格式(保证同一个人的名字只有一种格式)

b)将Prof的名字编码为数字;

2.生成name-num对应的字典；train.csv数据保存在EdMot/input/cora_edges.csv; 更新后的数据保存在converted.csv中

## Node_Content_Embedding.ipynb
1.对每个Researcher的PaperTitle以及Description进行Doc2Vec,作为Node的Atrribute

2.用SINE--Node2vec对node进行embedding

3.k-means算法进行聚类，将Reseacher分为3类;

4.SpectralEmbedding对vector进行降维; 展示聚类效果
