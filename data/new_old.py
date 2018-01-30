import MySQLdb
from DBUtils.PooledDB import PooledDB

fp1 = open('ofo.csv', 'r')
# fp2 = open('2.csv', 'r')

old_no = []
no_set = set()
for line in fp1.readlines():
    bid = str(line.strip('\n'))
    tup = ('ofo', bid, '1', '1')
    no_set.add(bid)
    old_no.append(tup)

print len(no_set)

sql_settings = {'mysql': {'host': 'localhost', 'port': 3306, 'user': 'root',
                                  'passwd': 'tw85450077', 'db': 'ptdata'}}
pool = PooledDB(creator=MySQLdb,
                mincached=1, maxcached=20,
                use_unicode=True, charset='utf8',
                **sql_settings['mysql'])
dbConn = pool.connection()
cursor = dbConn.cursor()

update_sql = "insert ignore into tb_bike_status_realtime (CompanyId, BicycleNo, IsOut" \
             ", Batch) values(%s,%s,%s,%s) " \
             "on duplicate key update IsOut = values(IsOut), Batch = values(Batch)"

cursor.executemany(update_sql, old_no)
dbConn.commit()
dbConn.close()
