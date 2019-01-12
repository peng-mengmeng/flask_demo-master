# coding=utf8
"""
Migrate pyecharts and Flask with custom template functions.
"""
from __future__ import unicode_literals

import random
import datetime

from flask import Flask, render_template
from flask.templating import Environment

from pyecharts import HeatMap, Map
from pyecharts.engine import ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig


# # ----- Adapter ---------
# class FlaskEchartsEnvironment(Environment):
#     def __init__(self, *args, **kwargs):
#         super(FlaskEchartsEnvironment, self).__init__(*args, **kwargs)
#         self.pyecharts_config = PyEchartsConfig(jshost='/static/js')
#         self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)
#
#
# # ---User Code ----
#
# class MyFlask(Flask):
#     jinja_environment = FlaskEchartsEnvironment


app = Flask(__name__)

REMOTE_HOST = "https://pyecharts.github.io/assets/js"

@app.route("/")
def index():
    return render_template('index.html')

"""
@app.route("/heatmap/")
def heatmap():
    hm = create_heatmap()
    # return render_template('heatmap.html', hm=hm)
    return render_template('heatmap.html', myechart2=hm.render_embed(), host=REMOTE_HOST,
                           script_list=hm.get_js_dependencies(), )



def create_heatmap():
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)),
             random.randint(1000, 25000)] for i in
            range((end - begin).days + 1)]
    heatmap = HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=1100)
    heatmap.add("", data, is_calendar_heatmap=True,
                visual_text_color='#000', visual_range_text=['', ''],
                visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
                is_visualmap=True, calendar_date_range="2017",
                visual_orient="horizontal", visual_pos="center",
                visual_top="80%", is_piecewise=True)
    return heatmap


@app.route('/fujian/')
def fujian():
    value = [20, 190, 253, 77, 65]
    attr = ['武汉市', '咸宁市', '孝感市', '十堰市', '襄阳市']
    map = Map("福建地图示例", width='100%', height=600)
    map.add("", attr, value, maptype='湖北',is_visualmap=True,
            visual_text_color='#000')
    return render_template('fujian_map.html', myechart=map.render_embed(), host=REMOTE_HOST,
                           script_list=map.get_js_dependencies(), )
"""


from pyecharts import Tree
@app.route('/tree/')
def tree():
    data = [
        {
            "children": [
                {
                    "children": [],
                    "name": "海林"
                },
                {
                    "children": [],
                    "name": "道固"
                },
                {
                    "children": [],
                    "name": "我"
                }
            ],
            "name": "雄哥"
        }
    ]

    tree = Tree("雄哥的小弟阵容")
    tree.add("", data)
    # tree.render()
    return render_template('tree.html', tree=tree.render_embed(), host=REMOTE_HOST,
                           script_list=tree.get_js_dependencies(), )



from pyecharts import WordCloud
@app.route('/wordcloud/')
def wordcloud():
    name = [
        '余小雄', '雄哥组','小雄','昨天还没睡够啊','不是9点就回去','道固','讨论阵容、分路','海林:后羿','彭涛:悟空']
    value = [
        10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112]
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    # wordcloud.render()
    return render_template('wordcloud.html', myechart=wordcloud.render_embed(), host=REMOTE_HOST,
                           script_list=wordcloud.get_js_dependencies(), )


from pyecharts import Map
@app.route('/map/')
def xiong_map():
    value = [200, 190,]
    attr = ['汕头市', '汕尾市']
    map = Map("雄哥的势力范围", width=1200, height=600)
    map.add(
        "", attr, value, maptype="广东", is_visualmap=True, visual_text_color="#000",is_label_show=True
    )
    # map.render()
    return render_template('map.html', myechart=map.render_embed(), host=REMOTE_HOST,
                           script_list=map.get_js_dependencies(), )


from pyecharts import Bar3D
@app.route('/bar3d/')
def bar3d ():
    # bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
    x_axis = [
        "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
        "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
    ]
    y_axis = [
        "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
    ]
    data = [
        [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
        [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
        [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
        [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
        [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
        [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
        [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
        [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
        [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
        [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
        [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
        [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
        [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
        [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
        [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
        [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
        [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
        [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
        [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
        [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
        [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
        [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
        [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
        [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
        [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
        [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
        [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
        [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
    bar3d.add(
        "",
        x_axis,
        y_axis,
        [[d[1], d[0], d[2]] for d in data],
        is_visualmap=True,
        visual_range=[0, 20],
        visual_range_color=range_color,
        grid3d_width=200,
        grid3d_depth=80,
        is_grid3d_rotate=True,
    )
    # bar3d.render()
    return render_template('bar3d.html', bar3d=bar3d.render_embed(), host=REMOTE_HOST,
                           script_list=bar3d.get_js_dependencies(), )

from pyecharts import GeoLines, Style
@app.route('/geolines/')
def geolines():
    data_beijing = [
        ["北京", "上海"],
        ["北京", "广州"],
        ["北京", "南京"],
        ["北京", "重庆"],
        ["北京", "兰州"],
        ["北京", "杭州"]
    ]

    data_guangzhou = [
        ["广州", "上海", 10],
        ["广州", "北京", 20],
        ["广州", "南京", 30],
        ["广州", "重庆", 40],
        ["广州", "兰州", 50],
        ["广州", "杭州", 60],
    ]
    style = Style(
        title_top="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59"
    )

    style_geo = style.add(
        is_label_show=True,
        line_curve=0.2,
        line_opacity=0.6,
        legend_text_color="#eee",
        legend_pos="right",
        geo_effect_symbol="plane",
        geo_effect_symbolsize=15,
        label_color=['#a6c84c', '#ffa022', '#46bee9'],
        label_pos="right",
        label_formatter="{b}",
        label_text_color="#eee",
    )
    geolines = GeoLines("GeoLines", **style.init_style)
    geolines.add("从广州出发", data_guangzhou, **style_geo)
    geolines.add("从北京出发", data_beijing, **style_geo)
    # geolines.render()
    return render_template('geolines.html', geolines=geolines.render_embed(), host=REMOTE_HOST,
                           script_list=geolines.get_js_dependencies(), )



if __name__ == "__main__":
    app.run()
