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
    return render_template('fujian_map.html', myechart=tree.render_embed(), host=REMOTE_HOST,
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









if __name__ == "__main__":
    app.run()
