# archiv

日喀则电力公司文件归档小助手

## 主要功能

1. 自动添加档案章，档案号和序号
2. 自动添加卷内页码
3. 自动生成卷册封面，目录，备考表
4. 自动生成档案盒侧边贴条
5. 自动生成资料交接单

## 使用方法

1. 下载[archiv](https://github.com/rcqed/archiv/releases)（国内访问：[archiv](https://gitee.com/rcqed/archiv/releases)）

2. 将归档好的PDF文件放入``archiv``文件夹中，并按"档号__名字"的格式命名卷册名和文件名

```
目录结构如下：
├─archiv
   └─XXXXXX-XXXXXX-XX-XXXX-XXX__卷册名称1
   │   ├─XXXXXX-XXXXXX-XX-XXXX-XXX-XXX__文件名1.pdf
   │   ├─XXXXXX-XXXXXX-XX-XXXX-XXX-XXX__文件名2.pdf
   └─XXXXXX-XXXXXX-XX-XXXX-XXX__卷册名称2
       ├─XXXXXX-XXXXXX-XX-XXXX-XXX-XXX__文件名3.pdf
       ├─XXXXXX-XXXXXX-XX-XXXX-XXX-XXX__文件名4.pdf
```

3. ``双击运行.bat``即可
4. 输出文件在``output``目录下

## 感谢

Python库：openpyxl，PyPDF2--2.10.8，reportlab，pywin32，pyautogui

软件：[WinPython](http://winpython.github.io/)，[Excle精灵](https://lestore.lenovo.com/detail/L105090)，[Office Excle](https://www.microsoftstore.com.cn/software/office)

## 请作者喝奶茶

![support](./config/support.png)
