import pygal

# 模块已经改了，是我没配置好吗，智能提示好垃圾啊
wm = pygal.maps.world.World()
wm.title = 'North, Center and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv']) 
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('chapter16/americas.svg')