# 🏀 智慧篮球：基于 AI 的实时动作识别系统 (Smart Basketball Action Recognition)

> **BIYOO-CHATPPT TEAM** | 22级软件工程1班队
> *致力于通过物联网与人工智能技术，为篮球爱好者提供个性化的训练反馈与技能提升方案。*

---

## 📖 项目简介 (Introduction)

本项目名为 **“智慧篮球动作识别” (Smart Basketball Action Recognition)**，旨在解决传统篮球训练中聘请专业摄影师和剪辑师费用高昂的问题 。通过在篮球场馆部署智能摄像头并结合物联网技术，系统能够自动捕捉运动员的动作细节，利用 AI 算法进行动作识别与分析，最终通过手机 App 或公众号向用户展示可视化数据与优质视频。

核心价值：
* **低成本普及**：费用包含在场馆使用费中，大众可接受 。
* **AI 赋能**：自动识别动作事件，支持 2D 关键点提取与 3D 重建 。
* **数据可视化**：提供精准的运动效果分析与反馈 。

---

## 🛠️ 技术栈 (Tech Stack)

本项目基于深度学习目标检测框架开发，主要包含以下组件：

* **核心算法**: YOLOv5 (You Only Look Once)
* **基础模型**: 选用 `YOLOv5x6` 或 `best.pt` 进行微调
* **GUI 框架**: Python Qt (`PyQt` / `PySide`) 
* **硬件环境**: NVIDIA GeForce RTX 4090 (推荐) 
* **数据标注**: LabelImg 

---

## 📂 数据集准备 (Dataset Preparation)

我们需要创建一个自定义数据集来识别特定的篮球动作。

### 1. 动作类别 (Classes)
根据 `BasketballActionRecognition_data.yaml` 配置文件，我们将动作定义为以下 5 类:
* `dribble` (运球)
* `shoot` (投篮)
* `run` (跑动)
* `stand` (站立)
* `defence` (防守)

### 2. 目录结构 (Directory Structure)
请按照以下结构组织您的数据:

```text
BasketballVideo/
├── images/
│   ├── train/    # 训练集图片
│   ├── val/      # 验证集图片
│   └── test/     # 测试集图片
├── labels/
│   ├── train/    # 对应训练集的 txt 标签
│   ├── val/      # 对应验证集的 txt 标签
│   └── test/     # 对应测试集的 txt 标签

└── BasketballActionRecognition_data.yaml  # 数据集配置文件
```

### 3.配置文件（Config）

BasketballActionRecognition_data.yaml内容示例：


```yaml
train: BasketballVideo/images/train
val: BasketballVideo/images/val
nc: 5
names: 
['dribble', 'shoot', 'run', 'stand', 'defence']
```
### 4.实际演示效果
<img width="626" height="691" alt="屏幕截图 2026-01-14 155741" src="https://github.com/user-attachments/assets/89ab2781-1640-4c69-8c1c-de37c1ecce67" />







