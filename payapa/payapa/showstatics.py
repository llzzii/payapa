import numpy as np
import matplotlib.pyplot as plt
from juejinDao import JuejinDao
from collections import Counter
import jieba
from wordcloud import WordCloud, STOPWORDS

jjDao = JuejinDao()
# print(jjDao.findTags())
# print(jjDao.findUsers())

# 两行代码支持显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 分块代码：
fig = plt.figure()
subplot = fig.add_subplot(2, 1, 1)

# 数据处理
result_users = np.array(jjDao.findUsers()).reshape(-1)
countDict = Counter(result_users)
xArr = []
yArr = []
index = 0
for inx, item in sorted(countDict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
    index += 1
    if(index < 11):
        xArr.append(item)
        yArr.append(inx)
    else:
        break
bar_width = 0.35  # 定义一个数字代表每个独立柱的宽度

rects1 = plt.bar(yArr, xArr, width=bar_width, alpha=0.4,
                 color='b', label='legend1')  # 参数：左偏移、高度、柱宽、透明度、颜色、图例
# 关于左偏移，不用关心每根柱的中心不中心，因为只要把刻度线设置在柱的中间就可以了
# plt.xlabel('作者', fontsize=12, loc="right", labelpad=1)
plt.ylabel('文章', fontsize=12)
plt.xticks(rotation=270, fontsize=12)
plt.legend()  # 显示图例
plt.tight_layout()  # 自动控制图像外部边缘，此方法不能够很好的控制图像间的间隔

subplot2 = fig.add_subplot(2, 1, 2)

userText = ",".join(result_users)
wc = WordCloud(background_color='white',
               max_font_size=220, random_state=50, font_path='STXINGKA.TTF')
wc.generate(text=userText)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
