import os
import shutil

# 定义目标文件路径
source_file = r"D:\LearnDeepLearning\yolov5-mask-42-master\yolov5-mask-42-master\BasketballVideo\stand\692.txt"

# 定义目标文件夹路径
destination_folder = r'D:\LearnDeepLearning\yolov5-mask-42-master\yolov5-mask-42-master\BasketballVideo\stand\labels\copies'

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 复制文件
for i in range(692,973):
    destination_file = os.path.join(destination_folder, f"{i}.txt")
    shutil.copy(source_file, destination_file)
