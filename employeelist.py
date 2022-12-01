employee={"name":"John","age":29,"salary":25000,"company":"google"}
print("printing employee data....")
print(employee)
print("deleting some of the employee data")
del employee["name"]
del employee["company"]
print("printing the modified information")
print(employee)
