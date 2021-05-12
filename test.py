
import jieba    //jieba分词工具包
import wordcloud    //词云包
import os     //获取路径
import imageio    //图片操作
import matplotlib.pyplot as plt     //绘图

d = os.path.dirname(__file__)     //获取当前路径

isCN = 1      //中文分词
background_image = "2.png"    
font_path1 = "STXINGKA.TTF"     //路径名
image1 = "wordcloudimage1.png"    
image2 = "wordclooudimage2.png"
back_coloring = imageio.imread(background_image)    //读取背景图片，设定词云样式
wca = wordcloud.WordCloud(font_path=font_path1,
                          background_color="white",
                          max_words=200,
                          mask=back_coloring,
                          max_font_size=300,
                          random_state=42,
                          width=1000, height=860, margin=2)       //创建词云对象，
file = open("175315.txt",'rb').read()     //读取要分析的文本文件
seg_list = jieba.cut(file, cut_all=False)     //
seg_list = " ".join(seg_list)
wca.generate(seg_list)
image_colors = wordcloud.ImageColorGenerator(back_coloring)
plt.figure()
plt.imshow(wca)
plt.axis("off")
plt.show()
wca.to_file(os.path.join(d, image1))
plt.imshow(wca.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.imshow(back_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
wca.to_file(os.path.join(d, image2))
