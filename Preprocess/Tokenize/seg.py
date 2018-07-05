#coding=utf-8
import json
import jieba
import os

jieba.analyse.set_stop_words(file_name)

def is_chinese(uchar):
	if uchar == u'\uff01' or uchar == u'\u3002' or \
	 uchar == u'\uff1f' or uchar == u'\uff0c':
		return True;
	if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
		return True;
	else:
		return False;

def get_seg(input_str):
	new_str = "";
	str_len = len(input_str);
	for i in range(0, str_len):
		if (is_chinese(input_str[i])):
			new_str += input_str[i];

	punctuation = u'\u0020-\u007f\u2000-\u206f\u3000-\u303f\uff00-\uffef';
	no_punc_str = re.sub(re.compile("[{}]+".format(punctuation)) ,"", new_str);
	word_list = jieba.cut(no_punc_str);
	final_str = " ".join(word_list);
	return final_str;
