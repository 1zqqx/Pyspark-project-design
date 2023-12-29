# 
# @author x_DARK_
# @description map
# @date 2023/12/28 0028 15:20
# 


from pyecharts import options as opts
from pyecharts.charts import Map


def main():
    # 定义地图数据
    map_data = {
        "北京": 50,
        "上海": 60,
        "广州": 40,
        "深圳": 30,
        "杭州": 20,
        "苏州": 10,
    }

    # 创建地图对象
    map_style = Map()

    # 添加地图数据
    map_style.add("城市", [list(z) for z in map_data.items()], "china")

    # 设置地图属性
    map_style.set_global_opts(
        title_opts=opts.TitleOpts(title="城市GDP排名"),
        visualmap_opts=opts.VisualMapOpts(min_=0, max_=100,
                                          range_color=["#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#ffffbf",
                                                       "#fee090", "#fdae61", "#f46d43", "#d73027", "#a50026"]),
    )

    # 渲染地图
    map_style.render("city_map.html")
    pass


if __name__ == '__main__':
    main()
