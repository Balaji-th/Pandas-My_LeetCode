pd.DataFrame(student_data, columns = ['student_id','age'])
list(players.shape)
employees.head(3)
students[students['student_id']==101][['name','age']]
employees['bonus'] = employees['salary']*2
customers.drop_duplicates(subset=['email'])
students.dropna(subset=['name'])
employees["salary"] = employees["salary"]  * 2
students = students.rename(columns={"id":"student_id","first":"first_name",'last':"last_name","age":"age_in_years"})
students["grade"] = students["grade"].astype(int)
products["quantity"] = products["quantity"].fillna(0)
pd.concat([df1,df2])
weather.pivot(index='month',columns='city',values='temperature')
pd.melt(report, id_vars=['product'], var_name='quarter', value_name="sales")
animals.sort_values(by=['weight'],ascending=False)