import json
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

from countries import get_country_code

# 将数据加载到一个列表
filename = 'chapter16/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数据的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop 

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Populations in 2010, by Country'
wm.add('0-10m', cc_pops_1) 
wm.add('10m-1bn', cc_pops_2) 
wm.add('>1bn', cc_pops_3)

wm.render_to_file('chapter16/world_population.svg')
        
    