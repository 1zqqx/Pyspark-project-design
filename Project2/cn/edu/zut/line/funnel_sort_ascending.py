# 
# @author x_DARK_
# @description funnel_sort_ascending
# @date 2023/12/28 0028 16:51
#
import random

# 漏斗图

from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker

key = ["草莓", "芒果", "葡萄", "雪梨", "西瓜", "柠檬", "车厘子"]
value = [random.randint(1000, 100000) for i in key]


def main():
    (
        Funnel(init_opts=opts.InitOpts())
        .add(
            "商品",
            [list(z) for z in zip(key, value)],
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="F"))
        .render("funnel_sort_ascending.html")
    )

    pass


if __name__ == '__main__':
    main()
