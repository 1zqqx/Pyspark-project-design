# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: wordCloud.py
# @Time    : 2024/1/12 0012 11:48
# @Software: PyCharm
import pymysql
from pyecharts.charts import WordCloud
from pyecharts import options as opts


def _test():
    conn = pymysql.connect(
        host="192.168.231.140",
        port=3306,
        user="liuqiqi",
        password="liuqiqi",
        database="pysql",
        charset="utf8"
    )
    cursor = conn.cursor()
    sql = """
    select * from pysql.qd_yuepiao_cloud_part_list
    """
    cursor.execute(sql)
    dt_data = []
    for it in cursor.fetchall():
        dt_data.append((it[0], it[1]))
        pass
    print(dt_data)
    c = (
        WordCloud()
        .add(series_name="", data_pair=dt_data, word_size_range=[6, 66])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="最热二级分类展示", title_textstyle_opts=opts.TextStyleOpts(font_size=23)),
            tooltip_opts=opts.TooltipOpts(is_show=True)
        )
        .render("./templates/wordcloud_custom.html")
    )

    cursor.close()
    conn.close()
    pass


if __name__ == '__main__':
    _test()
