# My_LeetCode : Pandas
This repo contains all Pandas solutions from LeetCode website in order to practice fundamental programming skills.

1. Creating a DataFrame:
   pd.DataFrame(student_data, columns=['student_id', 'age']): Creates a DataFrame named student_data with columns student_id and age. Ensure that student_data is a list of dictionaries or a NumPy array.

2. Getting DataFrame Shape:
   list(players.shape): Returns a list containing the number of rows and columns in the DataFrame named players.

3. Displaying DataFrame Head:
  employees.head(3): Displays the first 3 rows of the DataFrame named employees.

4. Filtering DataFrame:
  students[students['student_id']==101][['name','age']]: Filters the students DataFrame to only include rows where student_id is 101, then selects the name and age columns.

5. Adding a New Column:
   employees['bonus'] = employees['salary']*2: Creates a new column named bonus in the employees DataFrame, calculating each employee's bonus as twice their salary.

6. Removing Duplicate Rows:
   customers.drop_duplicates(subset=['email']): Removes duplicate rows in the customers DataFrame based on the email column.

7. Dropping Rows with Missing Values:
    students.dropna(subset=['name']): Drops rows from the students DataFrame where the name column contains missing values.

8. Updating Column Values:
    employees["salary"] = employees["salary"]  * 2: Multiplies the salary of each employee in the employees DataFrame by 2.

9. Renaming DataFrame Columns:
    students = students.rename(columns={"id":"student_id","first":"first_name",'last':"last_name","age":"age_in_years"}): Renames the columns in the students DataFrame to the specified names.

10. Converting Column Data Type:
    students["grade"] = students["grade"].astype(int): Converts the data type of the grade column in the students DataFrame to integer.

11. Filling Missing Values:
    products["quantity"] = products["quantity"].fillna(0): Fills missing values in the quantity column of the products DataFrame with 0.

12. Concatenating DataFrames:
    pd.concat([df1,df2]): Concatenates the DataFrames df1 and df2 vertically.

13. Pivoting DataFrame:
    weather.pivot(index='month',columns='city',values='temperature'): Pivots the weather DataFrame, using month as the index, city as the columns, and temperature as the values.

14. Melting DataFrame:
pd.melt(report, id_vars=['product'], var_name='quarter', value_name="sales"): Melts the report DataFrame, keeping product as the identifier, renaming the variable columns to quarter, and renaming the value columns to sales.

15. Sorting DataFrame:
animals.sort_values(by=['weight'],ascending=False): Sorts the animals DataFrame by the weight column in descending order.
