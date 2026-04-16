# Task01 打卡草稿

## easy 模式：50 字心得

这次 Task01 我先理解了具身智能的基本框架。它不是单纯会对话的 AI，而是拥有身体，能在环境中感知、决策、控制并接收反馈的智能系统。结合之前在广交会智能制造展看到的大量传感器、去佛山嘉腾参观 AGV 的经历，以及扫地机器人路径选择的例子，我更能理解具身智能落地不是只有“大脑”，还需要传感器、本体、控制和场景配合。我也跑了一个最小 PID 控制实验，并跟着小红书教学视频在 gpufree.cn 云环境中跑通了 Habitat 导航 demo，看到 RGB、深度和地图轨迹输出，对控制闭环和仿真环境有了更直观的理解。

## normal 模式：公开笔记结构

标题建议：

《Task01：从传感器、AGV 和扫地机器人理解具身智能》

文章结构：

1. 我一开始的理解和疑问。
2. 什么是具身智能。
3. 感知、决策、控制、本体之间的关系。
4. 从广交会智能制造展理解传感器的重要性。
5. 从佛山嘉腾 AGV 参观看具身智能落地。
6. 从扫地机器人路径选择理解工程取舍。
7. 坐标变换解决什么问题。
8. PID 控制的直觉理解。
9. 我跑通的最小 PID demo。
10. 跟着小红书教学视频跑 Habitat 云端导航 demo。
11. 强化学习奖励机制会不会让机器人“开心”。
12. 本次学习遇到的问题和后续计划。

## 资料来源标注

发布公开笔记时，记得在文末标注：

- Datawhale Every-Embodied 开源教程：https://github.com/datawhalechina/every-embodied
- Task01 课程资料：
  - 具身智能概述：https://github.com/datawhalechina/every-embodied/blob/main/01-具身智能概述/01具身智能概述.md
  - 机器人空间描述与坐标变换：https://github.com/datawhalechina/every-embodied/blob/main/02-机器人基础和控制、手眼协调/01机器人空间描述与坐标变换.md
  - PID 控制基础：https://github.com/datawhalechina/every-embodied/blob/main/02-机器人基础和控制、手眼协调/补充02PID_Control.md
  - 综合实战与仿真：https://github.com/datawhalechina/every-embodied/blob/main/02-机器人基础和控制、手眼协调/05综合实战与仿真.md
