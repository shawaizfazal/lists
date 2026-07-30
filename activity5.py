student_data={
    "id1":{"name":"sara","class":"v","subjects":"maths ,science english and gp"},
    "id2":{"name":"ali","class":"v","subjects":"maths ,science english and gp"},
    "id3":{"name":"essa","class":"v","subjects":"maths ,science english and gp"},
    "id4":{"name":"hussain","class":"v","subjects":"maths ,science english and gp"},
}
result={}
seen_keys=[]
for student_id,details in  student_data.items():
     unique_key=(details['name'],details["class"],
details["subjects"])
if unique_key not in seen_keys:
 seen_keys.append(unique_key)
result[student_id]=details
for k,v in result.items():
 print(k,":",v)


    
    
