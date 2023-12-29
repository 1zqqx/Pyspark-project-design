# 
# @author x_DARK_
# @description columnar
# @date 2023/12/28 0028 15:02
# 

from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot

from snapshot_selenium import snapshot


# ERROR

def main():
    # 创建柱状图对象
    bar_charts = Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))

    bar_charts.set_global_opts(
        title_opts=opts.TitleOpts(title="柱状图示例"),
        xaxis_opts=opts.AxisOpts(name="X轴"),
        yaxis_opts=opts.AxisOpts(name="Y轴"))

    bar_charts.add_xaxis(["A", "B", "C", "D", "E"])
    bar_charts.add_yaxis("系列1", [10, 20, 30, 40, 50])

    # bar_charts.render("bar_chart.html")
    make_snapshot(snapshot, bar_charts.render(), "bar_chart.png")
    pass


if __name__ == '__main__':
    main()
