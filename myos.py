import os

# 指定文件夹路径
folder_path = r'D:\LearnDeepLearning\yolov5-mask-42-master\BasketballData\orginalimage\5'

# 获取文件夹中的文件列表，并按文件名排序
files = sorted(os.listdir(folder_path), key=lambda x: int(''.join(filter(str.isdigit, x))))

# 遍历文件列表，逐个重命名
for i, file_name in enumerate(files, start=13243):
    # 构建新文件名
    new_file_name = os.path.join(folder_path, f'{i}.png')
    # 构建旧文件名
    old_file_name = os.path.join(folder_path, file_name)
    # 重命名文件
    os.rename(old_file_name, new_file_name)

print("文件重命名完成")
