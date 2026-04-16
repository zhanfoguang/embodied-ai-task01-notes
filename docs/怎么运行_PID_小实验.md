# 怎么运行 PID 小实验

## 这个实验是什么

这个实验是一个最小版 PID 控制 demo，用来帮你理解：

> 控制不是一次性到达目标，而是不断比较“目标值”和“当前值”的误差，再一步步修正动作。

它不是接真实机器人，也不是运行 Windows 仿真器，而是用 Python 写了一个很小的“假系统”来模拟控制过程。

实验里设置了：

- 目标值：100
- 当前值：从 0 开始
- 控制器：根据误差不断给出控制量
- 结果：当前值会一步步接近 100，误差逐渐变小

## 它到底怎么模拟

这个 demo 分成两部分：

### 1. 控制器公式

PID 控制器根据误差计算控制量：

```text
误差 error = 目标值 target - 当前值 current
控制量 control = P 项 + I 项 + D 项
```

在代码里大概是：

```python
error = self.setpoint - measured
self.integral += error * self.dt
derivative = (error - self.prev_error) / self.dt
output = self.kp * error + self.ki * self.integral + self.kd * derivative
```

这里的 `kp`、`ki`、`kd` 就是 PID 的三个参数。

### 2. 一个简化的被控对象

真实机器人会有电机、摩擦、惯性、负载、地面、传感器误差等复杂因素。这个 demo 为了让零基础先看懂，就把被控对象简化成一句：

```python
current += control * 0.05
```

意思是：

> 控制器给出一个控制量，系统当前值就按这个控制量的一小部分往目标靠近。

所以它不是精确物理仿真，而是一个“公式级模拟”。它的目的不是还原真实机器人，而是让你直观看到：

- 目标值不变。
- 当前值逐步接近目标。
- 误差越来越小。
- 控制器每一步都根据反馈修正动作。

## 和 CartPole 的区别

`cartpole建模与控制.md` 里的 CartPole 一般会更接近物理建模。它模拟的是“小车上立一根杆”的系统，通常会有：

- 小车位置
- 小车速度
- 杆子角度
- 杆子角速度
- 重力、质量、杆长、推力等物理参数

CartPole 的模拟通常是：

```text
当前状态 + 控制动作 + 物理方程 -> 下一时刻状态
```

也就是说，它也是用 Python 算出来的，但它比这个 PID 小实验更接近真实动力学系统。

本文件里的 PID demo 是最低门槛版本：

```text
当前值 + PID 控制量 -> 下一步当前值
```

它适合用来理解“反馈控制”的直觉。

## 文件在哪里

实验代码：

```text
/Users/zfg/Desktop/workspace/具身智能/demos/task01_pid_demo.py
```

运行结果：

```text
/Users/zfg/Desktop/workspace/具身智能/outputs/task01_pid_demo_result.csv
```

## 怎么运行

### 方法一：在 VS Code 终端运行

1. 在 VS Code 左边打开 `具身智能` 文件夹。
2. 打开菜单：`终端` -> `新建终端`。
3. 确认终端路径在 `具身智能` 文件夹下。
4. 输入：

```bash
python3 demos/task01_pid_demo.py
```

5. 回车。

如果看到类似下面的输出，就说明跑通了：

```text
step=01 target=100.0 current=5.76 error=94.24 control=115.20
step=20 target=100.0 current=33.17 error=66.83 control=26.06
step=40 target=100.0 current=56.16 error=43.84 control=20.37
step=80 target=100.0 current=87.50 error=12.50 control=11.76
```

### 方法二：先切到文件夹再运行

如果终端不在 `具身智能` 文件夹，可以先输入：

```bash
cd /Users/zfg/Desktop/workspace/具身智能
```

再输入：

```bash
python3 demos/task01_pid_demo.py
```

## 怎么看结果

最重要看三列：

- `target`：目标值，这里一直是 100。
- `current`：当前值，从 0 开始逐渐变大。
- `error`：误差，等于目标值减当前值。

你会看到：

- 一开始离目标很远，所以误差很大。
- 控制器不断调整，当前值越来越接近目标。
- 到第 80 步时，当前值已经到 87.50，误差降到 12.50。

## 可以写进打卡的话

我跑了一个最小 PID 控制实验。实验目标值是 100，系统从 0 开始，在控制器不断修正下逐步接近目标。运行结果显示，误差从一开始的 94.24 逐步降到第 80 步的 12.50。这个实验让我理解到，控制系统的核心不是一次性完成动作，而是不断根据反馈修正误差。
