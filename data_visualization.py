import pandas as pd
from pyecharts import Line, Scatter, Boxplot, Bar3D, Bar
from pyecharts import Timeline, Overlap, Page

from pyecharts import configure  # 更换主题

configure(global_theme='dark')


dataset = pd.read_csv('clear_train.csv')

page = Page()
# 统计一周每日不同时段骑行需求的均值
Weekday_Demand = dataset.groupby(['weekday', 'hour'])[['count']].mean()
Weekday_Demand['count'] = Weekday_Demand['count'].astype('int')  # 取整
Weekday_Demand.reset_index(inplace=True)
# 准备数据 设置坐标属性
Weekday_Demand.sort_values(['weekday', 'hour'], ascending=True, inplace=True)  # 需要先排序
Data = Weekday_Demand.values.tolist()  # 转化为数组形式
# print(Data)
x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
]
y_axis = [
    "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']

bar3d = Bar3D('一周不同时间段的骑行需求', 'X轴为时间，Y轴为一周周期，Z轴为需求数', width=1200, height=600, background_color='white')  # 创建figure对象
bar3d.add('', x_axis, y_axis,
          [[d[1], d[0], d[2]] for d in Data],
          grid3d_width=200,
          grid3d_depth=80,
          visual_range=[0, 400],
          visual_range_color=range_color,  # 色谱范围设定 与is_visualmap搭配使用
          is_visualmap=True,
          is_grid3d_rotate=True,
          grid3d_shading="",
          grid3d_rotate_speed=10
          )
page.add(bar3d)

Month_tendency_2011 = dataset[dataset.year == 2011].groupby('month')[['casual', 'registered', 'count']].sum()
print(Month_tendency_2011)
Month_tendency_2012 = dataset[dataset.year == 2012].groupby('month')[['casual', 'registered', 'count']].sum()
print(Month_tendency_2011)
# 将每一列转换为列表
attr = Month_tendency_2011.index.tolist()

line_1 = Line(title='Demand Distribution')
line_1.add("casual", attr, Month_tendency_2011['casual'].tolist(), mark_point=["average"],
           is_xaxis_boundarygap=False,
           yaxis_min=0, yaxis_max=140000)
line_1.add("registered", attr, Month_tendency_2011['registered'].tolist(),
           mark_line=["average"], mark_point=["average", "min", "max"],
           is_xaxis_boundarygap=False,
           yaxis_min=0, yaxis_max=140000
           )
line_1.add("count", attr, Month_tendency_2011['count'].tolist(), mark_point=["average"],
           is_xaxis_boundarygap=False,
           yaxis_min=0, yaxis_max=140000
           )
line_2 = Line(title='Demand Distribution')
line_2.add("casual", attr, Month_tendency_2012['casual'].tolist(), mark_point=["average"],
           is_xaxis_boundarygap=False,
           yaxis_min=0, yaxis_max=140000)
line_2.add("registered", attr, Month_tendency_2012['registered'].tolist(),
           mark_line=["average"], mark_point=["average", "min", "max"],
           is_xaxis_boundarygap=False,
           yaxis_min=0, yaxis_max=140000
           )
line_2.add("count", attr, Month_tendency_2012['count'].tolist(), mark_point=["average"],
           is_xaxis_boundarygap=False,
           yaxis_min=0, yaxis_max=140000
           )
getLine = Timeline(timeline_bottom=0)
getLine.add(line_1, '2011')
getLine.add(line_2, '2012')

# chart.render('result/line.html')
page.add(getLine)

data = dataset[['temp', 'windspeed', 'count']]

data = data.values.tolist()

x_lst = [v[0] for v in data]
y_lst = [v[1] for v in data]
extra_data = [v[2] for v in data]
# print(extra_data)
sc = Scatter()
sc.add(
    "",
    x_lst,
    y_lst,
    extra_data=extra_data,
    is_visualmap=True,
    visual_dimension=2,
    visual_orient="horizontal",
    visual_type="color",
    visual_range_size=[5, 15],
    symbol_size=10,
    visual_range=[0, 700],
    visual_text_color="#000",
    label_color=['#A6FFA6'],
)
page.add(sc)

Month_tendency_2011 = dataset[dataset.year == 2011].groupby('month')[['casual', 'registered', 'count']].sum()
Month_tendency_2012 = dataset[dataset.year == 2012].groupby('month')[['casual', 'registered', 'count']].sum()
Month_tendency_2011['rate'] = Month_tendency_2011['registered'] / Month_tendency_2011['count']
Month_tendency_2012['rate'] = Month_tendency_2012['registered'] / Month_tendency_2012['count']
attr = Month_tendency_2011.index.tolist()
print(attr)
print(Month_tendency_2011['rate'])
bar_1 = Bar("柱状图数据堆叠示例", title_pos='center', title_top='18', width=800, height=400)
bar_1.add("registered", attr, Month_tendency_2011['registered'], is_stack=True, is_random=True)
bar_1.add("casual", attr, Month_tendency_2011['casual'], is_stack=True)
line_1 = Line()
line_1.add("", attr, Month_tendency_2011['rate'].tolist())
overlap_0 = Overlap()
overlap_0.add(bar_1)
overlap_0.add(line_1, is_add_yaxis=True, yaxis_index=1)

bar_2 = Bar("柱状图数据堆叠示例", title_pos='center', title_top='18', width=800, height=400)
bar_2.add("registered", attr, Month_tendency_2012['registered'], is_stack=True)
bar_2.add("casual", attr, Month_tendency_2012['casual'], is_stack=True, )
line_2 = Line()
line_2.add("", attr, Month_tendency_2012['rate'].tolist())
overlap_1 = Overlap()
overlap_1.add(bar_2)
overlap_1.add(line_2, is_add_yaxis=True, yaxis_index=1)

getBar = Timeline(timeline_bottom=0)
getBar.add(overlap_0, '2011')
getBar.add(overlap_1, '2012')

page.add(getBar)

df = dataset.groupby(['weekday', 'day'])[['count']].sum()
df.reset_index(inplace=True)
# Data = Weather_Demand.values.tolist()
df1 = df.loc[df['weekday'] == 'Mon']
df2 = df.loc[df['weekday'] == 'Tue']
df3 = df.loc[df['weekday'] == 'Wed']
df4 = df.loc[df['weekday'] == 'Thu']
df5 = df.loc[df['weekday'] == 'Fri']
df6 = df.loc[df['weekday'] == 'Sat']

getBoxplot = Boxplot("Daily Bike Rental by Weekday", title_pos='center', title_top='18', width=800, height=400)
x_axis = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
y_axis = [df1['count'], df2['count'], df3['count'], df4['count'], df5['count'], df6['count']]
# print(x_axis)
# print(y_axis)
_yaxis = getBoxplot.prepare_data(y_axis)
getBoxplot.add("boxplot", x_axis, _yaxis)
# chart.render('result/Boxplot.html')
page.add(getBoxplot)

# if __name__ == '__main__':
#     # getBar3D()
#     # getLine()
#     # getScatter()
#     # getBoxplot()
#     # getBar()
page.render()
