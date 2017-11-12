#!/usr/bin/python
#-*-coding:utf-8-*-
# 自定义工具集
import os
import re
import ConfigParser

CWD=os.path.abspath(os.path.dirname(__file__))

def getImgs(suffixs=['jpg']):
	'获取指定后缀到图片文件名'
	#构造匹配表达式
	img_pattern='$|.*\.'.join(suffixs)
	if  img_pattern!="":
		img_pattern+='$'
		img_pattern='.*\.'+img_pattern
		#print img_pattern;exit()
	dirs=os.listdir('.')
	imgs=[]
	for img in dirs:
		if re.match(img_pattern,img,re.I):
			imgs.append(img)
	return imgs

def getSuffixs():
	'获取默认到文件后缀'
	config=ConfigParser.ConfigParser()
	config.read(CWD+'/config.ini')
	return config.get('default','suffixs').split(',')

def getFormat():
	'获取默认到命名格式'
	config=ConfigParser.ConfigParser()
	config.read(CWD+'/config.ini')
	return config.get('default','format')

def getFileSuffix(filename=''):
	'获取文件后缀'
	if filename!='':
		tmp=filename.split('.')
		if tmp.count>0:
			return tmp.pop()

if __name__ == '__main__':
	'模块测试'
	print getFileSuffix('fsdfsd')
	#print getImgs()
