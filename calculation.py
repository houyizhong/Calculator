#-*- coding:utf-8 -*-
#owner:houyizhong
import re

print('输入数字必须保留小数点一位\n例子：1.0-2.0*((60.0-30.0+(-40.0/5.0)*(9.0-2.0*5.0/3.0+7.0/3.0*99.0/4.0*2998.0+10.0*568.0/14.0))+(65.0+77.0)+6.0)')
enter=input('>>>')

def pre_symbol_cal(operation):
	loop_flag=True
	while loop_flag:
		if operation.find('/') != -1:
			division_cal=re.search('[0-9]+.[0-9]+/[\+\-]?[0-9]+.[0-9]+',operation).group()
			num1=re.findall('([0-9]+.[0-9]+)/',operation)
			num2=re.findall('/([\+\-]?[0-9]+.[0-9]+)',operation)
			print('division left:',num1)
			print('division right:',num2)
			num1=float(num1[0])
			num2=float(num2[0])
			division_result=num1/num2
			print('division result:',division_result)
			operation=operation.replace(division_cal,str(division_result))
			print('now operation is:',operation)
		elif operation.find('*') != -1:
			mutlip_cal=re.search('[0-9]+.[0-9]+\*[\+\-]?[0-9]+.[0-9]+',operation).group()
			num1=re.findall('([0-9]+.[0-9]+)\*',operation)
			num2=re.findall('\*([\+\-]?[0-9]+.[0-9]+)',operation)
			print('multiplication left:',num1)
			print('multiplication right:',num2)
			num1=float(num1[0])
			num2=float(num2[0])
			mutlip_result=num1*num2
			print('multiplication result:',mutlip_result)
			operation=operation.replace(mutlip_cal,str(mutlip_result))
			print('now operation is:',operation)
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
			operation=operation.replace(pri_cal,str(pri_result))
			print('now operation is:',operation)
		else:
			loop_flag=False
	return operation

def symbol_judge(enter):
	if '+-' in enter:
		enter=enter.replace('+-','-')
	elif '-+' in enter:
		enter=enter.replace('-+','-')
	elif '--' in enter:
		enter=enter.replace('--','+')
	return enter

def process(enter,re_result):
	for i in re_result:
		pre_symbol_result=pre_symbol_cal(i)
		pri_symbol_result=pri_symbol_cal(pre_symbol_result)
		pri_symbol_result=pri_symbol_result.strip('()')
		enter=enter.replace(i,pri_symbol_result)
	return enter

def three_level_brackets_func(enter):
	re_result=re.findall(r'\([^()]+\)',enter)
	print('brackets inner:',re_result)
	enter=process(enter,re_result)
	enter=symbol_judge(enter)
	print(enter)
	return enter
	
def no_brackets_func(enter):
	print('HIT no_brackets')
	if enter[0] == '-':
		enter='0'+enter
	raw_enter=pre_symbol_cal(enter)
	raw_enter=symbol_judge(raw_enter)
	enter=pri_symbol_cal(raw_enter)
	print(enter)
	return enter


loop_flag2=True
while loop_flag2:
	if re.findall('\([^()]+\)',enter):
		enter=three_level_brackets_func(enter)
	else:
		loop_flag2=False
else:
	finnal_result=no_brackets_func(enter)
	print(finnal_result)
