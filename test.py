
import jieba
import wordcloud
import os
import imageio
import matplotlib.pyplot as plt

d = os.path.dirname(__file__)

isCN = 1
background_image = "2.png"
font_path1 = "STXINGKA.TTF"
image1 = "wordcloudimage1.png"
image2 = "wordclooudimage2.png"
back_coloring = imageio.imread(background_image)
wca = wordcloud.WordCloud(font_path=font_path1,
                          background_color="white",
                          max_words=200,
                          mask=back_coloring,
                          max_font_size=300,
                          random_state=42,
                          width=1000, height=860, margin=2)
file = open("175315.txt",'rb').read()
seg_list = jieba.cut(file, cut_all=False)
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
