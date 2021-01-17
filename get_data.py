
def get_data(cur,query_string):
    cur.execute(query_string)
    fetched_data = cur.fetchall()
    print(fetched_data)


