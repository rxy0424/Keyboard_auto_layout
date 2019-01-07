# 键盘自动布局程序使用说明
## 用途
根据键盘配列自动在PCB中摆放轴的位置，当前为测试版本，只适用于KiCAD且限制较多，目前只在Linux环境下进行过测试。
## 声明
请严格按本说明使用，且在使用前保存并关闭所有无关程序和文档并进行必要备份，以免造成损失。本程序开源免费，作者对由程序造成的任何可能损失不负任何责任。

## 依赖
- Python2
- demjson

## 安装
将keyboard_auto_layout.py复制到文件到"[KiCad安装目录]\share\kicad\scripting\plugins" 路径下（Linux下为/usr/share/kicad/scripting/plugings）


## 使用限制
1. 保证switch元件的命名按行连续。如第一行为S2,S3,S4，第二行为S5,S6等等
2. 保证pcb中switch是在top层中(Board Side为Front)

## 使用流程
1. 打开auto-layout4file.py文件
		(1) 将switch_begin修改为switch命名的前缀，如s
		(2) 将switch_begin修改为第一个switch前缀后的编号的数字如2
		(3) 使用你自己的layout数据替换rawData变量三个单引号中间的内容
        三个变量修改完之后保存。
2. 运行python auto_layout4file.py 生成pos.txt
3. 在Pcbnew中打开要布局的PCB文件，使用set the origin point for the grid 工具将grid的原点设置在想要第一个switch所在的位置
4. 运行[工具]->[外部工具]下执行Keyboard auto layout命令。
5. 在弹出的对话框中选择上面生成的pos.txt，完成布局