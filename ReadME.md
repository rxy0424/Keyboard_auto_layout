# 键盘自动布局程序使用说明
## 用途
根据键盘配列自动在PCB中摆放轴的位置，当前是最原始能用的版本，只适用于KiCAD且限制较多，目前只在Linux环境下进行过测试。
## 依赖
- Python2
- demjson
- PyUserInput

## 声明
本程序现在模拟键盘按键完成，运行过程中基本不可停止。请严格按本说明使用，且在使用前保存并关闭所有无关程序和文档，以免造成损失。本程序开源免费，作者对由程序造成的任何可能损失不负任何责任。另，程序不能判断当前激活窗口，所以请避免程序运行过程中有其他窗口弹出改变当前窗口的激活状态。

## 使用限制
1. 保证switch元件的命名按行连续。如第一行为S2,S3,S4，第二行为S5,S6等等
2. 保证pcb中switch是在top层中(Board Side为Front)

## 使用流程
1. 将Pcbnew的工作单位切换为mils
2. 使用set the origin point for the grid 工具将grid的原点设置在想要第一个switch所在的位置
3. 随便选中一个switch，按ctrl+m弹出Move Item窗口，将Move Relative To选项选中为Grid origin，单击OK关闭对话框
4. 打开auto-layout4Kicad.py文件，将switch_begin修改为switch命名的前缀，如s；将switch_begin修改为第一个switch前缀后的编号的数字如2；使用你自己的layout数据替换rawData变量三个单引号中间的内容；三个变量修改完之后保存。
5. 打开命令行，保证使用alt+tab可以在命令行和Pcbnew间切换，即在命令行中按一次alt+tab切换到Pcbnew中，重复一次可直接回到命令行中。运行`python auto_layout4Kicad.py`　
6. 耐心等待将switch将自动移动正确位置。
7. **程序运行期间请不要对电脑进行任何操作**