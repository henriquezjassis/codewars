def to_camel_case(text):
	text = text.replace('_','-')
	textList = text.split("-")
	result = ""
	for index,word in enumerate(textList):
		if(index != 0):
			result += word.title()
		else:
			result += word

	return result



print(to_camel_case("the_stealth_warrior"))