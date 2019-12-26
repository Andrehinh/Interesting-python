import pandas as pd
from pyecharts import HeatMap
from pyecharts import Timeline
dataset = pd.read_csv('clear_train.csv')
data1 = dataset[dataset.year == 2011]
data2 = dataset[dataset.year == 2012]
data1 = data1[['hour', 'weekday', 'count']]
data2 = data2[['hour', 'weekday', 'count']]
data1 = data1.values.tolist()  # 转化为数组形式
data2 = data2.values.tolist()  # 转化为数组形式
x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_axis = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

heatmap = HeatMap()
heatmap1 = heatmap.add("热力图直角坐标系", x_axis, y_axis, data1,
                       is_visualmap=True,
                       visual_range=[2, 420],
                       visual_orient="horizontal",  # 设置组件条横竖，默认竖
                       visual_pos="center",
                       calendar_cell_size=["auto", 30],  # 单元格大小
                       visual_text_color="#000"
                       )
heatmap2 = heatmap.add("热力图直角坐标系", x_axis, y_axis, data1,
                       is_visualmap=True,
                       visual_range=[2, 420],
                       visual_orient="horizontal",  # 设置组件条横竖，默认竖
                       visual_pos="center",
                       calendar_cell_size=["auto", 30],  # 单元格大小
                       visual_text_color="#000"
                       )
chart = Timeline(timeline_bottom=0)
chart.add(heatmap1, '2011')
chart.add(heatmap2, '2012')

chart.render('result/Heatap.html')


