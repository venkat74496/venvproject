#st=y.execute("create table student (first_name text, last_name text, dob text, gender text, email text, phonenumber int, parents_name text, phonenumber_parents int, address_line1 text, address_line2 text, landmark text,pincode int, tenth_school_name text, tenth_mark int, stream text, twelth_school_name text, twelth_mark int)")
import sqlite3 as s
y=s.connect("student.db")
def storedata(x):
	#st=y.execute("insert into student (first_name, last_name, dob, gender, email, phonenumber, parents_name, phonenumber_parents, address_line1, address_line2, landmark, pincode, tenth_school_name, tenth_mark, stream, twelth_school_name, twelth_mark) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(x["firstName"], x["lastName"], x["birthdayDate"], x["inlineRadioOptions"], x["email"], x["phoneNumber"], x["parents_name"], x["phoneNumber_p"], x["Address1"], x["Address2"], x["Landmark"], x["Pincode"], x["ten_school_name"], x["ten_mark"], x["stream"], x["twel_school_name"], x["twel_mark"]))
	print(x)