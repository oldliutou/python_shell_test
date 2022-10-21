#condind: utf-8
import xlsxwriter
workbook = xlsxwriter.Workbook('demo1.xlsx')#创建一个Excel
worksheet = workbook.add_worksheet()#创建一个工作表对象
worksheet.set_column('A:A',20)#设定第一列（A）宽度为20像素
bold = workbook.add_format({'bold':True})#定义一个加粗的格 式对象
worksheet.write('A1','Hello')#A1单元格写入'Hello'
worksheet.write('A2','Hello',bold)#A2单元格写入'World'并 引用加粗格式对象bold
worksheet.write('B2',u'中文测试',bold)#B2单元格写入中文并引 用加粗格式对象bold
worksheet.write(2,0,32)#用行列表示法写入数字'32'与'35.5'
worksheet.write(3,0,35.5)#行列表示法的单元格下标以0作为起始值，'3，0'等价于'A3'
worksheet.write(4,0,'=SUM(A3:A4)')#求A3：A4的和，并将结 果写入'4，0'，即'A5'
worksheet.insert_image('B5',r"C:\Users\sysadmin\Pictures\Camera Roll\2.jpg")#在B5单 元格插入图片

workbook.close()#关闭Excel文件

'''
    Workbook类定义：Workbook（filename[， options]），该类实现创建一个XlsxWriter的Workbook
对象。Workbook类代表整个电子表格文件，并且存 储在磁盘上。
    add_worksheet（[sheetname]）方法，作用是添加一个 新的工作表，参数sheetname（String类型）为可选的 工作表名称，默认为Sheet1。
    add_format（[properties]）方法，作用是在工作表中 创建一个新的格式对象来格式化单元格。参数 properties（dict类型）为指定一个格式属性的字典， 例如设置一个加粗的格式对象， workbook.add_format（{'bold'：True}）。通过Format methods（格式化方法）也可以实现格式的设置，等 价的设置加粗格式代码如下：bold = workbook.add_format（） bold.set_bold（）
    add_chart（options）方法，作用是在工作表中创建一 个图表对象，内部是通过insert_chart（）方法来实 现，参数options（dict类型）为图表指定一个字典属 性，例如设置一个线条类型的图表对象，代码为 chart=workbook.add_chart（{'type'：'line'}）。
    close（）方法，作用是关闭工作表文件，如 workbook.close（）。
    set_row（row，height，cell_format，options）方法， 作用是设置行单元格的属性。
    set_column（first_col，last_col，width，cell_format， options）方法，作用为设置一列或多列单元格属性。
    insert_image（row，col，image[，options]）方法， 作用是插入图片到指定单元格，支持PNG、JPEG、 BMP等图片格式.
    
'''

'''
    Worksheet类代表了一个Excel工作表，是XlsxWriter模 块操作Excel内容最核心的一个类，例如将数据写入 单元格或工作表格式布局等。Worksheet对象不能直
接实例化，取而代之的是通过Workbook对象调用 add_worksheet（）方法来创建。
    write（row，col，*args）方法，作用是写普通数据 到工作表的单元格，参数row为行坐标，col为列坐 标，坐标索引起始值为0；*args无名字参数为数据内 容，可以为数字、公式、字符串或格式对象.
    write_string（）写入字符串类型数据
    write_number（）写入数字类型数据
    write_blank（）写入空类型数据
    write_formula（）写入公式类型数据
    ·write_datetime（）写入日期类型数据
    write_boolean（）写入逻辑类型数据
    write_url（）写入超链接类型数据
    
'''

'''
    Chart类实现在XlsxWriter模块中图表组件的基类，支 持的图表类型包括面积、条形图、柱形图、折线图、 饼图、散点图、股票和雷达等，一个图表对象是通过 Workbook（工作簿）的add_chart方法创建，通过 {type，'图表类型'}字典参数指定图表的类型:chart = workbook.add_chart（{type， 'column'}）
    ·area：创建一个面积样式的图表； ·bar：创建一个条形样式的图表； ·column：创建一个柱形样式的图表； ·line：创建一个线条样式的图表； ·pie：创建一个饼图样式的图表； ·scatter：创建一个散点样式的图表； ·stock：创建一个股票样式的图表； ·radar：创建一个雷达样式的图表。
    再通过Worksheet（工作表）的insert_chart（）方法插入到指定位置，语句如下： worksheet.insert_chart（'A7'， chart） #在A7单元格插入图表
    
    
'''