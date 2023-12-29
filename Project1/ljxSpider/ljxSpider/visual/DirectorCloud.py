# 
# @author x_DARK_
# @description DirectorCloud
# @date 2023/12/29 0029 15:21
#
import collections
import json
import re

from pyecharts.charts import WordCloud
import pyecharts.options as opts


def main():
    # 打开json文件
    with open("../spiders/a.json", "r", encoding="UTF-8") as f:
        # 解析数据
        data = json.load(f)
    # print(data)
    wd = []
    for i in data:
        temp = re.findall(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', i['moviesDirector'])
        wd += temp
    # print(wd)
    dt = collections.Counter(wd).most_common()
    # print(dt)
    (
        WordCloud()
        .add("Director", data_pair=dt, word_size_range=[20, 100])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=23)),
            tooltip_opts=opts.TooltipOpts(is_show=True))
        .render("../static/director_word_cloud.html")
    )
    pass


if __name__ == '__main__':
    main()
