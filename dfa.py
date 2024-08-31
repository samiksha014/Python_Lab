
#function which checks whether the string is accepted or not
def dfa_ends_with_a(text):

#inner function two check whether both states are getting the given condition true
	def q0(text):
		if not text:
			return "rejected"
		if text[0] == "a":
			return q1(text[1:])
		elif text[0] == "b":
			return q0(text[1:])
		else:
			return "rejected"
	
	def q1(text):
		if not text:
			return "accepted"
		if text[0] == "a":
			return q1(text[1:])
		elif text[0] == 'b':
			return q0(text[1:])
		else:
			return "rejected"
			
	return q0(text)

#implementation of the both the conditions accepted and rejected
print(dfa_ends_with_a("abbaa"))
print(dfa_ends_with_a("b"))

			
