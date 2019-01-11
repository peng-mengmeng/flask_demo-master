from pyecharts import Map
#https://blog.csdn.net/d345389812/article/details/81750426
# #地图
# value = [20, 190, 253, 77, 65]
# attr = ['武汉市', '咸宁市', '孝感市', '十堰市', '襄阳市']
# map = Map("湖北地图示例", width=1200, height=600)
# map.add(
#     "", attr, value, maptype="湖北", is_visualmap=True,visual_range=[0,1000], visual_text_color="#000" ,is_label_show=True
# )
# map.render()

# #饼图
# from pyecharts import Pie
# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 10, 10]
# pie = Pie("饼图示例")
# pie.add("", attr, v1, is_label_show=True)
# pie.render()



# from pyecharts import Tree
#
# data = [
#     {
#         "children": [
#             {
#                 "children": [],
#                 "name": "海林"
#             },
#             {
#                 "children": [],
#                 "name": "道固"
#             },
#             {
#                 "children": [],
#                 "name": "我"
#             }
#         ],
#         "name": "雄哥"
#     }
# ]
#
# tree = Tree("雄哥的小弟阵容")
# tree.add("", data)
# tree.render()



# from pyecharts import WordCloud
#
# name = [
#     '余小雄', '雄哥组','小雄','昨天还没睡够啊','不是9点就回去','道固','讨论阵容、分路','海林:后羿','彭涛:悟空']
# value = [
#     10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112]
# wordcloud = WordCloud(width=1300, height=620)
# wordcloud.add("", name, value, word_size_range=[20, 100])
# wordcloud.render()



# from pyecharts import Map
#
# value = [200, 190,]
# attr = ['汕头市', '汕尾市']
# map = Map("雄哥的势力范围", width=1200, height=600)
# map.add(
#     "", attr, value, maptype="广东", is_visualmap=True, visual_text_color="#000"
# )
# map.render()

