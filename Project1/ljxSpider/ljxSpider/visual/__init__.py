# 
# @author x_DARK_
# @description __init__.py
# @date 2023/12/29 0029 14:56
#
import collections
import json

import pyecharts.options as opts
from pyecharts.charts import WordCloud


def main():
    # 打开json文件
    with open("../spiders/a.json", "r", encoding="UTF-8") as f:
        # 解析数据
        data = json.load(f)
    # print(data)
    wd = []
    for i in data:
        wd += i['moviesSector']
    # print(wd)
    dt = collections.Counter(wd).most_common()
    # print(dt)
    (
        WordCloud()
        .add("dt", data_pair=dt, word_size_range=[20, 100])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=23)),
            tooltip_opts=opts.TooltipOpts(is_show=True))
        .render("../static/wordcloud.html")
    )
    pass


if __name__ == '__main__':
    main()
