# 
# @author x_DARK_
# @description Calendar_heatmap
# @date 2023/12/28 0028 16:34
# 

# 日历热力图

import random
import datetime

import pyecharts.options as opts
from pyecharts.charts import Calendar


def main():
    begin = datetime.date(2023, 1, 1)
    end = datetime.date(2023, 12, 31)
    data = [[str((begin + datetime.timedelta(days=i))),random.randint(0, 10)]
            for i in range((end - begin).days + 1)]

    (
        Calendar()
        .add("日历热力图",
             yaxis_data=data,
             calendar_opts=opts.CalendarOpts(
                 pos_top="120",
                 pos_left="30",
                 pos_right="30",
                 range_="2023",
                 yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
             ))
        .set_global_opts(
            title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2023日历热力图"),
            visualmap_opts=opts.VisualMapOpts(min_=0, max_=10, orient="horizontal", pos_bottom="60", pos_left="center"),
        )
        .render("calendar_heatmap.html")
    )
    pass


if __name__ == '__main__':
    main()
