#-*- coding:utf-8 -*-
#owner:houyizhong
import re

enter=input('>>>')

def pre_symbol_split(operation):
	loop_flag=True
	while loop_flag:
		if operation.find('/') != -1:
			division_cal=re.search('[0-9]+.[0-9]+/[0-9]+.[0-9]+',operation).group()
			num1=re.findall('([0-9]+.[0-9]+)/',operation)
			num2=re.findall('/([0-9]+.[0-9]+)',operation)
			print('division left:',num1)
			print('division right:',num2)
			num1=float(num1[0])
			num2=float(num2[0])
			division_result=num1/num2
			print('division result:',division_result)
			operation=operation.replace(division_cal,str(division_result))
			print('now operation is:',operation)
		elif operation.find('*') != -1:
			mutlip_cal=re.search('[0-9]+.[0-9]+\*[0-9]+.[0-9]+',operation).group()
			num1=re.findall('([0-9]+.[0-9]+)\*',operation)
			num2=re.findall('\*([0-9]+.[0-9]+)',operation)
			print('multiplication left:',num1)
			print('multiplication right:',num2)
			num1=float(num1[0])
			num2=float(num2[0])
			mutlip_result=num1*num2
			print('multiplication result:',mutlip_result)
			operation=operation.replace(mutlip_cal,str(mutlip_result))
			print('now operation is:',operation)
			print(type(operation))
		else:
			loop_flag=False
	return operation

def pri_symbol_cal(operation):
	loop_flag=True
	while loop_flag:
		new_operation=operation.strip('()')
		if len(re.split('[+-]',new_operation)) > 1 and re.split('[+-]',new_operation)[0]:
			pri_cal=re.search('[\+\-]?[0-9]+.[0-9]+[\+\-][0-9]+.[0-9]+',new_operation).group()
			num1=re.findall('([\+\-]?[0-9]+.[0-9]+)[\+\-]',pri_cal)
			num2=re.findall('[\+\-]?[0-9]+.[0-9]+([\+\-][0-9]+.[0-9]+)',pri_cal)
			num1=float(num1[0])
			num2=float(num2[0])
			pri_result=num1+num2
			operation=operation.replace(pri_cal,str(pri_reuslt))
			print('now operation is:',new_operation)
		else:
			loop_flag=False
	return operation

re_result=re.findall(r'\([^()]+\)',enter)
print('brackets inner:',re_result)
for i in re_result:
	'''
	print('i=',i)
	list=re.findall('[0-9]+',i)
	print(list)
	for n in list:
		searchnumber=re.search('[0-9]+',i).group()
		floatnumber=float(searchnumber)
		i=i.replace(searchnumber,str(floatnumber))
	print(i)
	'''
	pre_symbol_result=pre_symbol_split(i)
	pri_symbol_result=pri_symbol_cal(pre_symbol_result)
