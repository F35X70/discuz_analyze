# -*- coding: utf-8 -*-
import readfile_discuz
import jieba
if __name__ == '__main__':
	print "step1"
	feedback_name = "discuz.txt"
	file_content = readfile_discuz.ReadContent(feedback_name)
	feedback_comment_stat = {}
	feedback_comment_stat_detail = {}
	feedback_tag_stat = {}
	feedback_tag_stat_detail = {}
	feedback_id = []
	feedback_list = []

	#delete id
	with file("del.txt","r") as del_read:
		del_read_content = del_read.read()
		del_read_content = del_read_content.strip("\n")
		delete_id = del_read_content.split(";")
	print "step2"
	for i in file_content:
		
		#feedback_id
		feedback_id.append(i[0])
		
		#discuz_stat
		seg_list = jieba.cut_for_search(i[1])
		for x in seg_list:
			x = x.encode("utf-8")
			if  len(x) != 1 and len(x) != 3 :
				try:
					feedback_comment_stat[x] = feedback_comment_stat[x] + 1
				except KeyError:
					feedback_comment_stat[x] = 1
				try:
					feedback_comment_stat_detail[x].append(i[0])
				except KeyError:
					feedback_comment_stat_detail[x] = []
					feedback_comment_stat_detail[x].append(i[0])
		
		#tag_stat
		for feedback_tag in i[-1]:
			try:
				feedback_tag_stat[feedback_tag] = feedback_tag_stat[feedback_tag] + 1
			except KeyError:
				feedback_tag_stat[feedback_tag] = 1
			try:
				feedback_tag_stat_detail[feedback_tag].append(i[0])
			except KeyError:
				feedback_tag_stat_detail[feedback_tag] = []
				feedback_tag_stat_detail[feedback_tag].append(i[0])

	for i in feedback_comment_stat_detail:
		feedback_comment_stat_detail[i] = list(set(feedback_comment_stat_detail[i]))
	"""
	#output
	feedback_comment_stat_sort =  sorted(feedback_comment_stat.iteritems(), key=lambda d:d[1], reverse = True)
	feedback_tag_stat_sort =  sorted(feedback_tag_stat.iteritems(), key=lambda d:d[1], reverse = True)
	
	with file("discuz_comment_stat.txt","a") as feedback_stat:
		write_string = ""
		for i in feedback_comment_stat_sort:
				write_string = write_string + i[0]+";"+str(i[1])+";"+"\n"
				#for x in feedback_comment_stat_detail[i[0]]:
				#	write_string = write_string + str(x) + ","
		feedback_stat.write(write_string)
	
	with file("discuz_tag_stat.txt","a") as tag_stat:
		write_string = ""
		for i in feedback_tag_stat_sort:
			write_string = write_string + i[0]+";"+str(i[1])+";"+"\n"
			#for x in feedback_tag_stat_detail[i[0]]:
			#	write_string = write_string + str(x) + ","
		tag_stat.write(write_string)
	"""
	print "step3"
	for i in feedback_id:
		feedback_item = {"id":0,"fid":0,"typeid":0}
		feedback_item["id"] = i
		if i in delete_id or i in feedback_tag_stat_detail["火狐阅读"]:
			feedback_item["fid"] = 0
			feedback_item["typeid"] = 0
		elif i in feedback_tag_stat_detail["NULLX"]:
			pass
		elif i in feedback_tag_stat_detail["校园活动"]:
			feedback_item["fid"] = 51
			feedback_item["typeid"] = 0
		elif i in feedback_tag_stat_detail["活动"]:
			feedback_item["fid"] = 50
			feedback_item["typeid"] = 0
		elif i in feedback_tag_stat_detail["核心用户组"]:
			feedback_item["fid"] = 52
			feedback_item["typeid"] = 0
		elif i in feedback_tag_stat_detail["火狐水区"] or i in feedback_tag_stat_detail["火狐商店"]:
			feedback_item["fid"] = 53
			feedback_item["typeid"] = 0
		elif i in feedback_tag_stat_detail["社区帮助"] or i in feedback_tag_stat_detail["火狐社区帮助"]:
			feedback_item["fid"] = 55
			if i in ["30435","30432","30434","30421"]:
				feedback_item["typeid"] = 35
			else:
				feedback_item["typeid"] = 32
		elif i in feedback_tag_stat_detail["壁纸"] or i in feedback_tag_stat_detail["火狐壁纸"]:
			feedback_item["fid"] = 54
			feedback_item["typeid"] = 0
		elif i in feedback_tag_stat_detail["Thunderbird"] or i in feedback_tag_stat_detail["雷鸟"]:
			feedback_item["fid"] = 43
			feedback_item["typeid"] = 20
		elif i in feedback_tag_stat_detail["Thunderbird"] or i in feedback_tag_stat_detail["雷鸟"]:
			feedback_item["fid"] = 43
			feedback_item["typeid"] = 20
		
		
		
		else: 
			feedback_item["fid"] = 40
			feedback_item["typeid"] = 6

		feedback_list.append(feedback_item.values())
		
	print "step4"

	with file("discuz_output.txt","a") as feedback_output:
		write_string = ""
		for i in feedback_list:
			write_string = write_string + str(i[1]) +","+str(i[2])+","+str(i[0])+"\n"
		feedback_output.write(write_string)
		