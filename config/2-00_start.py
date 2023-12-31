import os
import subprocess

# 运行每个 .py 文件的列表
script_files = [
    "2-01_creatinf.py",
    "2-02_changesheet1.py",
    "2-03_changesheet2.py",
    "2-04_changelittle.py",
    "2-05_mergerxls1.py",
    "2-06_mergerxls2.py",
    "2-07_copydel.py",
    "3-00_deldocx.py",
    "3-01_generatedoc1.py",
    "3-02_generatedoc2.py",
    "3-03_generatedoc3.py",
    "3-04_generatedoc4.py",
    "3-05_generatedocx_list.py",
    "3-06_generatedocx_catalog1.py",
    "3-06_generatedocx_catalog2.py",
    "3-06_generatedocx_catalog3.py",
    "3-06_generatedocx_catalog4.py",
    "3-06_generatedocx_catalog5.py",
    "3-06_generatedocx_catalog6.py",
    "3-06_generatedocx_catalog7.py",
    "3-06_generatedocx_catalog8.py",
    "3-06_generatedocx_catalog9.py",
    "3-06_generatedocx_catalog10.py",
    "3-06_generatedocx_catalog11.py",
    "3-06_generatedocx_catalog12.py",
    "3-06_generatedocx_catalog13.py",
    "3-06_generatedocx_catalog14.py",
    "3-06_generatedocx_catalog15.py",
    "3-07_moverm.py"
]

# 创建窗口
print("===================================")
print("程序开始运行")
print("===================================")

error_occurred = False

# 依次运行每个 .py 文件
for script in script_files:
    # 显示正在运行的文件名
    print(f"\n{script} 正在运行")

    # 运行 .py 文件
    try:
        subprocess.check_call(["python", script])
        print(f"{script} 运行完成")
    except subprocess.CalledProcessError:
        print("出错了，请检查PDF源文件")
        error_occurred = True
        break  # 出错则停止继续运行其他文件

# 完成（仅当没有出错时才打印）
if not error_occurred:
    print("\n===================================")
    print("运行完成，请核对生成的文件")
    print("===================================")