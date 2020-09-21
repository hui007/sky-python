import xlrd
import requests
from xlrd import xldate_as_tuple
import datetime

'''
xlrd中单元格的数据类型
数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换
成我们想要的数据类型
0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
'''


class ExcelData():
    # 初始化方法
    def __init__(self, data_path, sheetname):
        # 定义一个属性接收文件路径
        self.data_path = data_path
        # 定义一个属性接收工作表名称
        self.sheetname = sheetname
        # 使用xlrd模块打开excel表读取数据
        self.wb = xlrd.open_workbook(self.data_path)
        # 根据工作表的名称获取工作表中的内容（方式①）
        self.ws = self.wb.sheet_by_name(self.sheetname)
        # 根据工作表的索引获取工作表的内容（方式②）
        # self.ws = self.wb.sheet_by_name(0)
        # 获取第一行所有内容,如果括号中1就是第二行，这点跟列表索引类似
        self.keys = self.ws.row_values(0)
        # 获取工作表的有效行数
        self.rowNum = self.ws.nrows
        # 获取工作表的有效列数
        self.colNum = self.ws.ncols

    # 定义一个读取excel表的方法
    def read_excel(self):
        # 定义一个空列表
        datas = []
        for i in range(1, self.rowNum):
            # 定义一个空字典
            sheet_data = {}
            for j in range(self.colNum):
                # 获取单元格数据类型
                c_type = self.ws.cell(i, j).ctype
                # 获取单元格数据
                c_cell = self.ws.cell_value(i, j)
                if c_type == 2 and c_cell % 1 == 0:  # 如果是整形
                    c_cell = int(c_cell)
                elif c_type == 3:
                    # 转成datetime对象
                    date = datetime.datetime(*xldate_as_tuple(c_cell, 0))
                    c_cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif c_type == 4:
                    c_cell = True if c_cell == 1 else False
                sheet_data[self.keys[j]] = c_cell
                # 循环每一个有效的单元格，将字段与值对应存储到字典中
                # 字典的key就是excel表中每列第一行的字段
                # sheet_data[self.keys[j]] = self.ws.row_values(i)[j]
            # 再将字典追加到列表中
            datas.append(sheet_data)
        # 返回从excel中获取到的数据：以列表存字典的形式返回
        return datas

    # 发起http post请求
    def post_excel(self, url, headers, param):
        response = requests.post(url, data=param, headers=headers)
        # 响应状态码
        print(response.status_code)
        # 响应内容
        print(response.content.decode("utf-8"))
        # cookie
        print(response.cookies)
        # 响应头信息
        print(response.headers)

if __name__ == "__main__":
    data_path = "/Users/jianghui/Downloads/定义客户属性1234_v20200917.xls"
    sheetname = "SQL Results"
    get_data = ExcelData(data_path, sheetname)

    url="http://172.31.1.8:30101/api/merchant/v1/example"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    data = {
        "name": "aa",
        "age": 23
    }
    get_data.post_excel(url,headers=headers,param=data)
    if True:
        exit()

    datas = get_data.read_excel()
    # print(datas)
    for index, row in enumerate(datas):
        print("行号: ", index + 1, "。数据：", row)
        chn_codes=row["渠道编码"].rstrip(";").split(";") # 去掉垃圾数据：最后边的分号
        if len(chn_codes) == 1:
            # print(index, row)
            pass
        else:
            chn_names = row["渠道名称"].split(";")
            # print(index, row)
            # print(index, chn_codes, chn_names)
            for index_2, chn in enumerate(chn_codes):
                row["渠道编码"] = chn
                row["渠道名称"] = chn_names[index_2]
                print("主行号: ",index+1,"。拆分行：",index_2+1, row)
