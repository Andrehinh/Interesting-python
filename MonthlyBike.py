import pandas as pd
from pyecharts import Bar, Line
from pyecharts import Overlap, Timeline,Page
page = Page()

dataset = pd.read_csv('clear_train.csv')
Month_tendency_2011 = dataset[dataset.year == 2011].groupby('month')[['casual', 'registered', 'count']].sum()
Month_tendency_2012 = dataset[dataset.year == 2012].groupby('month')[['casual', 'registered', 'count']].sum()
data=dataset[dataset.year == 2011]
Month_tendency_2011['rate'] = Month_tendency_2011['registered'] / Month_tendency_2011['count']
Month_tendency_2012['rate'] = Month_tendency_2012['registered'] / Month_tendency_2012['count']


attr = Month_tendency_2011.index.tolist()
bar_1 = Bar("柱状图数据堆叠示例", title_pos='center', title_top='18', width=800, height=400)
bar_1.add("registered", attr, Month_tendency_2011['registered'], is_stack=True, label_color=['#426ab3', '#f47920'])
bar_1.add("casual", attr, Month_tendency_2011['casual'], is_stack=True)
line_1 = Line()
line_1.add("", attr, Month_tendency_2011['rate'], label_color=['#f47920'])
overlap_0 = Overlap()
overlap_0.add(bar_1)
overlap_0.add(line_1, is_add_yaxis=True, yaxis_index=1)

bar_2 = Bar("柱状图数据堆叠示例", title_pos='center', title_top='18', width=800, height=400)
bar_2.add("registered", attr, Month_tendency_2012['registered'], is_stack=True, label_color=['#426ab3', '#f47920'])
bar_2.add("casual", attr, Month_tendency_2012['casual'], is_stack=True)
line_2 = Line()
line_2.add("", attr, Month_tendency_2012['rate'], label_color=['#f47920'])
overlap_1 = Overlap()
overlap_1.add(bar_2)
overlap_1.add(line_2, is_add_yaxis=True, yaxis_index=1)

chart = Timeline(timeline_bottom=0)
chart.add(overlap_0, '2011')
chart.add(overlap_1, '2012')

chart.render('w.html')
