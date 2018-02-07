import pymysql

pymysql.install_as_MySQLdb()  # 替换MySQLdb类库，Django启动时需导入MySQLdb包

# # 创建数据库连接
# db = pymysql.connect('localhost', 'django', 'zx123456', 'django')
#
# # 使用cursor()方法创建操作游标，sql语句由操作游标执行
# cursor = db.cursor()
#
# # 使用cursor的execute方法执行SQL语句
# cursor.execute('SELECT VERSION()')
#
# # 使用fetchone()获取数据
# data = cursor.fetchone()
#
# print('Database version is %s' %data)
#
# # 关闭数据库
# db.close()
