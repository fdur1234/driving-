#行車年齡的程式（課程例子）
country = input('請問你是哪一國人？')
age = input('請輪入年齡：')
age = int(age)
if country == '香港':
	if age >= 18:
		print('你可以考車牌')
	else:
		print('你還不可以揸車')
elif country == '美國':
	if age >= 16:
		print('你可以考車牌')
	else:
		print('你還不可以揸車')