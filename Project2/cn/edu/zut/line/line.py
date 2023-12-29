# 
# @author x_DARK_
# @description line.py
# @date 2023/12/28 0028 14:44
#

import pyecharts
from pyecharts import charts


def main():
    # 初始化折线对象
    line_charts = charts.Line()
    # 设置图像标题
    line_charts.set_global_opts(title_opts=pyecharts.options.TitleOpts(title="折线图示例"))
    # 添加横轴数据
    line_charts.add_xaxis(["周一", "周二", "周三", "周四", "周五", "周六", "周日"])
    line_charts.add_yaxis("Factor1", [-10, 32, 43, -2, 19, 33, 83], is_smooth=True)
    line_charts.add_yaxis("Factor2", [1, 2, 3, 4, 5, 6, 7])
    # 生成视图html
    line_charts.render("line_chart.html")
    pass


if __name__ == '__main__':
    main()
