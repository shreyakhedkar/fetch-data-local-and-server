from get_data import get_data
from connect import connect
import sys
import json

db_cred = sys.argv[1]
cur = connect(db_cred)
print(cur, "printing cur")
def execute_query(cur):
    with open('queryList.json') as query_file:
            data = json.load(query_file)
            for value in data.values():
                data = get_data(cur, value)
                print(data)
        
execute_query(cur)
cur.close()