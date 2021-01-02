# 有趣的python数据分析及可视化小项目





## 1.  爬取并分析北上广深链家网租房房源全部数据，得出租房建议（北上广深租房图鉴）

   项目主要爬取北上广深链家网全部租房房源数据，并且得出租金分布、租房考虑因素等建议

   主要的文件为：
   - house_data_crawler.py：爬取北上广深租房房源数据的代码（带说明和注释, 需要安装mongodb）
   - info.py：租房类型和各城市各区域的信息，供house_data_crawler.py调用
   - 北上广深租房图鉴.ipynb: Jupyter notebook代码，对北上广深租房数据进行分析
   - data_sample.csv: 租房数据，这里只随机选择了12000条，每城市3000条

   #### 运行环境：
   - python3.7

   #### 需要安装的包：
   - requests
   - pyecharts
   - pandas
   - numpy
   - pymongo

   


   ## Crawling and analysing Bei-Shang-Guang-Shen rent data from Lianjia.

   This project Crawls Bei-Shang-Guang-Shen renting data from Lianjia, and analyses the distribution of the rent, and provides renting advices in those cities.
   The main files are listed below:
   - house_data_crawler.py：codes for crawling Bei-Shang-Guang-Shen rent data from Lianjia（with annotation, MongoDB needs to be installed.）
   - info.py：infos about renting type and districts of Bei-Shang-Guang-Shen，for house_data_crawler.py
   - 北上广深租房图鉴.ipynb: Jupyter notebook codes，analysing Bei-Shang-Guang-Shen renting data
   - data_sample.csv: 12000 renting data by random choices

   #### Python environment
   - Python3.7

   #### Packages need to be installed
   - requests
   - pyecharts
   - pandas
   - numpy
   - pymongo

## 实习僧网站数据挖掘、机器学习职位数据分析

This directory contains font_decode.py for crawling data from shixiseng.com, the data crawled from shixiseng.com(datamining.csv, machinelearning.csv, mlalgorithm.csv), and the codes for analysing the data(数据挖掘、机器学习算法实习生需求分析.ipynb).

- crawler: font_decode.py
- data: datamining.csv, machinelearning.csv, mlalgorithm.csv
- data analysis: 数据挖掘、机器学习算法实习生需求分析.ipynb

## 3.临床NLP——从病例记录预测患者是否再次入院

利用 BERT 模型解析电子病历

主要的文件：
- 临床NLP——从病例记录预测患者是否再次入院.ipynb: Jupyter notebook代码，对患者的电子病历进行数据清洗，通过对大量未标注的语料进行非监督的预训练，来学习其中的表达法。其次，使用少量标记的训练数据以监督方式微调（fine tuning）预训练模型以进行各种监督任务。
- sample.csv:训练集、验证集和测试集均含有三列，分别为TEXT（文本内容），ID（即HADM_ID），Label（0或1）。

#### 运行环境
- python 3.8


#### 需要安装的包
- pytorch
- pandas
- numpy
- sklearn
- matplotlib

#### 配置推理参数
- output_dir: 输出文件的目录
- task_name: 任务名称
- bert_model: 模型目录
- data_dir: 数据目录，默认文件名称为 sample.csv
- max_seq_length: 最大字符串序列长度
- eval_batch_size: 推理批的大小，越大占内存越大



## Clinical NLP -- Predicting whether or not a patient is readmitted from the case record

BERT model was used to analyze electronic medical records

#### Main documents:

- Clinical NLP -- predict whether patients will be re-admitted from the case records. Ipynb: Jupyter notebook code, data cleaning of patients' electronic medical records, and unsupervised pre-training of a large number of unlabeled corpus to learn the expression method. Second, fine tuning the pre-training model by using a small amount of marked training data was used to perform various supervision tasks.
- sample.csv: The training set, validation set and test set all contain three columns, namely TEXT (TEXT content), ID (i.e., HADM_ID) and Label (0 or 1).

#### python environment

- python 3.8


#### Packages need to be installed

- pytorch
- pandas
- numpy
- sklearn
- matplotlib

##### Configure reasoning parameters

- output_dir: The directory where the files are output
- Task_name: task name
- Bert_model: Model directory
- data_dir: Data directory. The default file name is called sample.csv
- MAX_seq_length: Maximum string sequence length
- eval_batch_size: Inferences about the size of a batch. The larger the batch size, the greater the memory footprint



## 4.共享单车数据集探索及可视化
分析摩拜单车订单的相关数据对骑行时长的影响；分析骑行时间（包括工作日/双休日、高峰时段/非高峰时段两个维度）、骑行位置、用户价值这些变量对骑行时长的影响。

#### 主要的文件
- Mobike_shanghai.ipynb：Jupyter notebook代码，对共享单车数据集可视化分析。

#### 数据集概要

- 原数据集来自Udacity提供的摩拜单车上海城区2016年8月随机抽样百万条用户使用数据，共有102361条订单记录，包含起点、目的地、租赁时间、还车时间、用户ID、车辆ID、交易编号和路线轨迹信息。
- 经过清洗整理和信息提取后，新数据集增加了22个新变量，主要用于分析的变量为：ttl_min（骑行时长(min)）、distance（骑行始末点的直线距离(km)）、daytype（工作日/双休日）、hourtype（高峰时段/非高峰时段）、ring_stage（内环内/中环内/外环内/外环外）、rate（高价值用户/中等价值用户/低价值用户）这六个变量。
- 新数据集在使用过程中亦去除了少量骑行速度、距离、时长的异常记录，最终的订单记录数量为102338条。



#### 运行环境

- python 3.8

#### 需要安装的包

- seaborn
- pandas
- numpy
- matplotlib



##  Exploration and visualization of shared bike data sets

Analyze the impact of mobike order data on cycling time; The influences of cycling time (including working days/weekends, peak hours/off-peak hours), cycling position and user value on cycling time were analyzed.

#### main file

- Mobike_shanghai. Ipynb: Jupyter code, visual analysis of shared bike data sets.

Summary of the data set

- The original data set is from the randomly sampled data of millions of users of Mobike in Shanghai urban area provided by Udacity in August 2016, with a total of 102,361 order records, including the starting point, destination, rental time, vehicle return time, user ID, vehicle ID, transaction number and route track information.
- after cleaning processing and information extraction, a new data set added 22 new variables, it is mainly used for the analysis of the variable is: ttl_min (riding time (min)), short (beginning and end of the ride of the straight line distance (km)), daytype (weekday/weekend), hourtype (peak/off-peak hours), ring_stage (within the inner ring/central inner/outer ring inner/outer ring), rate (high value users/medium/low value users value) the six variables.
- In the process of using the new data set, a few abnormal records of cycling speed, distance and length of time were also removed. The final order record number was 102338.

#### Python enviroment

- python 3.8

#### Packages need to be installed

- seaborn
- pandas
- numpy
- matplotlib


## 5.奥运会数据集可视化分析

受疫情影响，2020东京奥运会将延期至2021年举行。本次分析将会从各国累计奖牌数、各项运动产生金牌数、运动员层面主要国家表现等角度来呈现奥运会历史。

#### 主要文件
- athlete_events.csv：参赛运动员基本生物数据和奖牌结果。
- noc_regions.csv：国家奥委会3个字母的代码与对应国家信息。
- Olympic.ipynb:Jupyter notebook代码，对奥运会历史数据集分析及可视化

#### 运行环境
- python 3.8

#### 需要安装的包
- pyecharts
- pandas
- numpy



## Visual analysis of Olympic Data sets

Due to the epidemic, the 2020 Tokyo Olympic Games will be postponed to 2021. This analysis will present the History of the Olympic Games from the perspectives of the cumulative number of MEDALS won by each country, the number of gold MEDALS won by each sport, and the performance of major countries at the athlete level.

#### main file

- Athlete_events.CSV: basic biometric data and medal results of athletes participating in the games.
- Noc_region.CSV: The three-letter code of the National Olympic Committee and the information of the corresponding country.
- Olympic.ipynb:Jupyter code, analysis and visualization of Olympic history data sets

#### Python environment

- python 3.8

#### Packages need to be installed

- pyecharts
- pandas
- numpy


## 6.世界大学排名数据分析及可视化

选用的6月份刚刚公布的2021年度英国QS世界大学排名

主要文件：
- top_university.csv：QS对世界大学排名的指标进行评估
- QS_university.ipynb：Jupyter notebook代码，对世界大学排名一局的指标进行分析


#### 运行环境
- python3.8

##### 需要安装的包
- pyecharts
- pandas
- numpy



##  Data analysis and Visualization of world University rankings

Selected by the QS World University Rankings 2021, which was published in June

#### Main Documents:

- TOP_university.CSV: QS index for evaluating world University rankings
- QS_university. Ipynb: Jupyter code, to analyze the index of world University ranking


#### Python environment

- python3.8

##### Packages need to be installed

- pyecharts
- pandas
- numpy
