import os
import pathlib

from conf.setting import DIR_PATH
from logging_conf.logging_config import logs
import traceback
import openpyxl
from common.Webkey import Webkey

#读取excel文件，获取指定的sheet页
excel_PATH = pathlib.Path(__file__).parents[0].resolve() / 'demo.xlsx'
excel = openpyxl.load_workbook(str(excel_PATH))
# sheet = excel['Sheet1'] # 考虑到可能有多个sheet页的用例需要执行，所以需要获取所有sheet页
print(excel)

# --- 查看 Excel 内容的函数 ---
def read_and_print_excel(workbook):
    """
    读取并打印一个 openpyxl 工作簿对象的所有内容。
    """
    # 3. 获取工作表 (这里我们用表名来获取第一张表)
    sheet_name = workbook.sheetnames[0]
    sheet = workbook[sheet_name]
    print(f"--- 开始读取工作表: '{sheet.title}' ---")

    # 4. 遍历所有行并打印
    for row in sheet.iter_rows():
        # 提取当前行所有单元格的值
        row_values = [cell.value for cell in row]
        print(row_values)

    print(f"--- '{sheet.title}' 读取完毕 ---")

#参数解析方法
def arguments(data):
    temp_data = {}
    # 参数要解析，需要基于参数的分号分割数据，再基于等号进行key和value的值的准备，从而实现最终的字典格式
    if data:
        str_temp = data.split(';') #基于分号分割后生成list列表
        for temp in str_temp:
            t = temp.split('=',1) #基于等号再分割一次
            temp_data[t[0]] = t[1] # 以等号左边的字符串为key，等号右边的字符串为value，存储到字典中
    return temp_data

def excel_run():
    """
    从excel文件中读取测试用例，并执行这些用例。
    """
    excel_path = os.path.join(DIR_PATH, 'testcase', 'demo.xlsx')
    # 验证文件是否存在
    if not os.path.exists(excel_path):
        logs.error(f"Excel文件不存在: {excel_path}")
        print(f"错误: Excel文件不存在 - {excel_path}")
        return
    try:
        # 加载外部Excel文件
        logs.info(f"正在加载Excel文件: {excel_path}")
        excel = openpyxl.load_workbook(excel_path)
        for name in excel.sheetnames: #遍历所有sheet页
            sheet = excel[name]
            logs.info(f'当前sheet页名称为：{sheet.title}')
            for value in sheet.values:
                #读取测试用例的正文内容
                if type(value[0]) is int: #基于序号的数据类型来判断是否进入正文
                    logs.info(f"正在执行的操作为：{value[3]}<UNK>")
                # 参数的解析：将参数解析为字典格式。方便直接传入到函数之中。
                    test_data = arguments(value[2]) #获取每一行的操作参数
                    """
                     所有的操作分为如下不同类型：
                                1. 实例化driver对象
                                2. 基于driver对象进行的常规操作行为
                                3. 断言，因为需要对excel文件进行写入
                    """
                    if value[1] == 'open_browser':
                        driver = Webkey(**test_data)
                    elif 'assert' in value[1]: #所有需要断言的测试用例都要以assert开头
                        status = getattr(driver, value[1])(**test_data,expected =value[4])
                        #通过断言方法生成一个结果，基于结果来判断流程的结果是成功还是失败
                        if status:
                            sheet.cell(row=value[0] + 2, column=6).value = 'PASS'
                        else:
                            sheet.cell(row=value[0] + 2, column=6).value = 'FAIL'
                        excel.save(excel_PATH)
                    else:
                        getattr(driver, value[1])(**test_data)
    except:
        logs.error(traceback.format_exc())
    finally:
        excel.close()

