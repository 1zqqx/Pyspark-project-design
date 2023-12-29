# 
# @author x_DARK_
# @description scatter_style
# @date 2023/12/28 0028 15:28
# 


from pyecharts.charts import Scatter
from pyecharts import options as opts


def main():
    scatter_style = Scatter()
    scatter_style.set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-Style"))

    x_data = [0, 1, 2, 3, 4, 5]
    y_data = [9, 8, 7, 6, 5]
    scatter_style.add_xaxis(x_data)
    scatter_style.add_yaxis("Series 1", y_data)

    scatter_style.render("scatter_style.html")
    scatter_style.render_notebook()
    pass


if __name__ == '__main__':
    main()
