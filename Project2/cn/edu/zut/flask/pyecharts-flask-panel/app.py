# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: app.py
# @Time    : 2023/12/31 0031 14:10
# @Software: PyCharm
from time import sleep

import pyecharts
import pymysql
from flask import Flask, render_template
from pyecharts.charts import Line, Pie, Bar, WordCloud
from pyecharts import options as opts

app = Flask(__name__, static_folder="./templates")


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
    pass


# 0.25  词云图
@app.route("/cloud", methods=['GET', 'POST'])
def get_cloud_chart():
    sql = """
    select * from pysql.qd_yuepiao_cloud_part_list
    """
    cursor = conn.cursor()
    sleep(0.25)
    cursor.execute(sql)
    dt_data = []
    for item in cursor.fetchall():
        dt_data.append((item[0], str(item[1])))
        pass
    print(dt_data)
    c = (
        WordCloud()
        .add(series_name="热门二级分类", data_pair=dt_data, word_size_range=[6, 66])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="热门二级分类", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c.dump_options_with_quotes()
    pass


# 0.4
@app.route("/bar_down", methods=['GET', 'POST'])
def get_bar_datazoom_chart():
    sql = """
    select * from pysql.qd_yuepiao_date_top_count
    """
    cursor = conn.cursor()
    sleep(0.4)
    cursor.execute(sql)
    result = cursor.fetchall()
    x_data_time = []
    y_1 = []
    y_2 = []
    y_3 = []
    y_4 = []
    y_5 = []
    for i in range(0, len(result), 5):
        x_data_time.append(result[i][0])
        y_1.append(result[i + 0][2])
        y_2.append(result[i + 1][2])
        y_3.append(result[i + 2][2])
        y_4.append(result[i + 3][2])
        y_5.append(result[i + 4][2])
        pass
    c = (
        # 实在不想写了 瞎J8写的
        Bar()
        .add_xaxis(x_data_time)
        .add_yaxis("都市", y_1, stack="stack1")
        .add_yaxis("玄幻", y_2, stack="stack1")
        .add_yaxis("仙侠", y_3, stack="stack1")
        .add_yaxis("轻小说", y_4, stack="stack1")
        .add_yaxis("历史", y_5, stack="stack1")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="近四年每月Top5类型书籍数目"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
        )
    )
    return c.dump_options_with_quotes()


# sleep(0.3)
@app.route("/bar", methods=['GET', 'POST'])
def get_funnel_chart():
    sql = """
    select * from pysql.qd_yuepiao_author_count order by count desc limit 15
    """
    cursor = conn.cursor()
    sleep(0.3)
    cursor.execute(sql)
    x_data = []
    y_data = []
    for item in cursor.fetchall():
        x_data.append(item[0])
        y_data.append(item[1])
    x_data.reverse()
    y_data.reverse()
    c = (
        Bar()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            "作品数量",
            y_data,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(color='#91CC75')
        )
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="卷王作者排行(Top15作品数量)"))
    )
    return c.dump_options_with_quotes()
    pass


# sleep(0.2)
@app.route('/line', methods=['GET', 'POST'])
def get_line_chart():
    sql = """
    select * from pysql.all_creation_dfsql
    """
    cursor = conn.cursor()
    sleep(0.2)
    cursor.execute(sql)

    x_data = []
    y_data_1 = []
    y_data_2 = []
    for item in cursor.fetchall():
        if item[0] not in set(x_data):
            x_data.append(item[0])
        if item[1] == "完结":
            y_data_1.append(item[2])
        else:
            y_data_2.append(item[2])
        pass
    cursor.close()
    c = (
        Line()
        .set_global_opts(title_opts=pyecharts.options.TitleOpts(title="最新人气榜书籍类型状态"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="完结",
            y_axis=y_data_1,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="连载",
            y_axis=y_data_2,
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    return c.dump_options_with_quotes()
    pass


# sleep(0.1)
# @app.route('/tab', methods=['GET', 'POST'])
# def get_gauge_chart():
#     def get_first_page():
#         c = (
#             Bar()
#             .add_xaxis(Faker.days_attrs)
#             .add_yaxis("商家A", Faker.days_values)
#             .set_global_opts(
#                 title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
#                 datazoom_opts=[opts.DataZoomOpts()],
#             )
#         )
#         return c
#
#     def get_second_page():
#         c = (
#             Line()
#             .add_xaxis(Faker.choose())
#             .add_yaxis(
#                 "商家A",
#                 Faker.values(),
#                 markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
#             )
#             .add_yaxis(
#                 "商家B",
#                 Faker.values(),
#                 markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
#             )
#             .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
#         )
#         return c
#         pass
#
#     tab = Tab()
#     tab.add(get_first_page(), "Bar")
#     tab.add(get_second_page(), "Line")
#     return render_template("tab.html", chart=tab.render_embed())
#     pass


# 多个函数同时请求数据库有时候服务器错误 暂时sleep一下
# sleep(0)

@app.route('/pie', methods=['GET', 'POST'])
def get_pie_chart():
    sql = """
    select * from pysql.qd_yuepiao_cloud_f_part_list
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    label = []
    data = []
    for item in cursor.fetchall():
        label.append(item[0])
        data.append(item[1])
    cursor.close()
    c = (
        Pie()
        .add("这是啥", [list(z) for z in zip(label, data)])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="近四年上榜不同类书籍数量"), legend_opts=opts.LegendOpts(is_show=False))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c.dump_options_with_quotes()
    pass


def __init():
    global conn
    conn = pymysql.connect(
        host="192.168.231.140",
        port=3306,
        user="liuqiqi",
        password="liuqiqi",
        database="pysql",
        charset="utf8"
    )
    pass


if __name__ == '__main__':
    __init()
    app.run()
    pass
