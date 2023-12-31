# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: app.py
# @Time    : 2023/12/31 0031 14:10
# @Software: PyCharm

import pyecharts
from flask import Flask, render_template
from pyecharts.charts import Line, Gauge
from pyecharts import options as opts
from pyecharts.globals import ThemeType

app = Flask(__name__, static_folder="./templates")


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
    pass


@app.route('/line', methods=['GET', 'POST'])
def get_line_chart():
    c = (
        Line()
        .set_global_opts(title_opts=pyecharts.options.TitleOpts(title="折线图示例"))
        .add_xaxis(["周一", "周二", "周三", "周四", "周五", "周六", "周日"])
        .add_yaxis("Factor1", [-10, 32, 43, -2, 19, 33, 83], is_smooth=True)
        .add_yaxis("Factor2", [12, 2, 6, 4, 9, 6, 19])
    )
    return c.dump_options_with_quotes()
    pass


@app.route('/gauge', methods=['GET', 'POST'])
def get_gauge_chart():
    c = (
        Gauge(init_opts=opts.InitOpts(width="300px", height="200px", theme=ThemeType.ESSOS))
        .add(
            "业务指标",
            [("完成率", 55.5)],
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Gauge-不同颜色"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c.dump_options_with_quotes()
    pass


if __name__ == '__main__':
    app.run()
    pass
