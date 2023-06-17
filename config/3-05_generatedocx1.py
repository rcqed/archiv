import subprocess
import time
import pyautogui
import os
import win32com.client as win32

# Excel 文件路径
excel_file = r".\template\main\export.xlsx"

# 使用 subprocess 执行命令打开 Excel 文件
subprocess.call(["start", "excel", excel_file], shell=True)

# 延时等待 Excel 打开
time.sleep(9)

# 模拟按键输入
pyautogui.press('f10')  # 模拟按下 F10 键
pyautogui.typewrite('Y1')  # 输入 Y1
pyautogui.typewrite('YJ')  # 输入 YJ
pyautogui.press(['up'] * 3)  # 按下 4 次上箭头键
pyautogui.press('enter')  # 模拟按下回车键

# 获取当前脚本的绝对路径
script_path = os.path.dirname(os.path.abspath(__file__))
docx_file = os.path.join(script_path, 'template', 'main', 'list15', 'temp.docx')

# 模拟按键输入
pyautogui.press(['tab'])
pyautogui.press('enter')  # 模拟按下回车键
pyautogui.typewrite(docx_file)  # 输入 Word 文档路径
pyautogui.press('enter')  # 模拟按下回车键

# 输入文件地址
pyautogui.press(['tab']*2)
pyautogui.press('enter')  # 模拟按下回车键

# 输入单元格
pyautogui.typewrite('$A$1:$H$16')  # 输入字符串
pyautogui.press('enter')  # 模拟按下回车键

# 输入名称
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('tab')
pyautogui.press(['down']*12)
pyautogui.press(['tab']*2)
pyautogui.press('enter')  # 模拟按下回车键
pyautogui.press('enter')  # 模拟按下回车键

# 延时等待 Excel 导出
time.sleep(120)

# 关闭 Excel 应用程序
excel_app = win32.Dispatch("Excel.Application")
excel_app.DisplayAlerts = False  # 关闭警告弹窗
excel_app.Quit()

# 延时等待 Excel 关闭
time.sleep(6)