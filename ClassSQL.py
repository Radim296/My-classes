import sqlite3 as sq

class database:

    tables = []

    def __init__(self, name):
        conn = sq.connect((name + ".db"))
        cursor = conn.cursor()
        self.db = cursor
    
    def createTable(self, tableName, columns):

        self.tables.append(tableName)
        columns_ = ""

        for i in columns:
            if len(columns) - 1 == columns.index(i):
                columns_ += i
                continue
            columns_ += (i+",")
        
        param = "CREATE TABLE {}({})".format(tableName, columns_)

        try:
            self.db.execute(param)
        except:
            param.format(tableName, columns)
            self.db.execute(param)    

    def addColumn(self, tableName, column):
        param = "ALTER TABLE {} ADD COLUMN {}".format(tableName, column)
        self.db.execute(param)

    def addInfo(self, tableName, info):
        param = "INSERT INTO {} VALUES ({})".format(tableName, info)
        print(param)
        self.db.execute(param)



a = database("mydatabase")



a.addInfo("tableb", 17)

a.db.execute("SELECT * FROM tableb")
