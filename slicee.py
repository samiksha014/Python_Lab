

def slice_fun(string , sliced_parameter):
	
	sliced_string = ""
	
	# for [:end]/[start:end]/[start:] representation when list has two parameters
	if len(sliced_parameter) == 2:
	
		for i in range(len(sliced_parameter)-1):
		
		#here it returns empty string when the start > end
		    if sliced_parameter[i] >sliced_parameter[i+1]:
			    return ""
		    for j in range(sliced_parameter[i],sliced_parameter[i+1]):
			    sliced_string += string[j]
			
	#for [start:end:step]/[::step]/[start::step] representation when list has three parameters
	elif len(sliced_parameter) == 3:
	
		for i in range(len(sliced_parameter)-1):
			step = sliced_parameter[2]
			for j in range(sliced_parameter[i],sliced_parameter[i+1],step):
				sliced_string += string[j]
				
	return sliced_string
	
# all possibilities of the sliced operator when used

print("all possibilities of the sliced operation on a given string")
print("string :- ",slice_fun("rainbow",[0,2]))  #for[:2]
print("string :- ",slice_fun("rainbow",[2,7]))  #for[2:] and [2::]
print("string :- ",slice_fun("rainbow",[2,4]))  #for[2:4]
print("string :- ",slice_fun("rainbow",[2,7,2]))  #for[2::2]
print("string :- ",slice_fun("rainbow",[0,7,2]))  #for[::2]
print("string :- ",slice_fun("rainbow",[-7,-3]))  #for[:-3]
print("string :- ",slice_fun("rainbow",[-3,0]))  #for[-3:] and [-3::]
print("string :- ",slice_fun("rainbow",[0,6,-2]))  #for[::-2]
print("string :- ",slice_fun("rainbow",[-4,-1]))  #for[-4:-1]
print("string :- ",slice_fun("rainbow",[-4,-7,-2]))  #for[-4::-2]
print("string :- ",slice_fun("rainbow",[-4,0,2]))  #for[-4::2]

