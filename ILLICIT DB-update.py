# UPDATE

query = "UPDATE trial_illicit SET Ten = 'stollen2' WHERE ROW_NO = 1"
query_str = str(query)
mycursor.execute(query_str)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")