# -*- coding: utf-8 -*-
import readfile_discuz
import jieba
if __name__ == '__main__':

	feedback_name = "discuz.txt"
	file_content = readfile_discuz.ReadContent(feedback_name)
	feedback_tag_stat = {}
	feedback_tag_stat_detail = {}
	feedback_id = []
	feedback_list = []

	#delete id
	with file("del.txt","r") as del_read:
		del_read_content = del_read.read()
		del_read_content = del_read_content.strip("\n")
		delete_id = del_read_content.split(";")

	for i in file_content:
		
		#feedback_id
		feedback_id.append(i[0])
		
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

	for i in feedback_id:
		feedback_item = {"id":0,"fid":0,"typeid":0}
		feedback_item["id"] = i
		if i in feedback_tag_stat_detail["火狐阅读"] or i in delete_id:
			pass
		elif i in feedback_tag_stat_detail["壁纸"]:
			feedback_item["fid"] = 54
		elif i in feedback_tag_stat_detail["火狐壁纸"]:
			feedback_item["fid"] = 54
		elif i in feedback_tag_stat_detail["校园活动"]:
			feedback_item["fid"] = 51
		elif i in feedback_tag_stat_detail["活动"]:
			feedback_item["fid"] = 50
		elif i in feedback_tag_stat_detail["核心用户组"]:
			feedback_item["fid"] = 52
		elif i in feedback_tag_stat_detail["火狐水区"]:
			feedback_item["fid"] = 53
		elif i in feedback_tag_stat_detail["火狐商店"]:
			feedback_item["fid"] = 53
		elif i in feedback_tag_stat_detail["社区帮助"]:
			feedback_item["fid"] = 55
			feedback_item["typeid"] = 6
		elif i in feedback_tag_stat_detail["火狐社区帮助"]:
			feedback_item["fid"] = 55
			feedback_item["typeid"] = 6
		elif i in feedback_tag_stat_detail["Thunderbird"]:
			feedback_item["fid"] = 43
		elif i in feedback_tag_stat_detail["雷鸟"]:
			feedback_item["fid"] = 43
		elif i in feedback_tag_stat_detail["官方博客"]:
			feedback_item["fid"] = 2
		elif i in feedback_tag_stat_detail["火狐快讯"]:
			feedback_item["fid"] = 37
		elif i in feedback_tag_stat_detail["火狐移动版"]:
			feedback_item["fid"] = 42
		elif i in feedback_tag_stat_detail["javascript"]:
			feedback_item["fid"] = 47
		elif i in feedback_tag_stat_detail["JS"]:
			feedback_item["fid"] = 47
		elif i in feedback_tag_stat_detail["css"]:
			feedback_item["fid"] = 47
		elif i in feedback_tag_stat_detail["html5"]:
			feedback_item["fid"] = 47
		elif i in feedback_tag_stat_detail["Firefox OS"] and i in feedback_tag_stat_detail["web app"]:
			feedback_item["fid"] = 46
		elif i in feedback_tag_stat_detail["Firefox OS"] and i in feedback_tag_stat_detail["开发者学堂"]:
			feedback_item["fid"] = 46
		elif i in feedback_tag_stat_detail["Firefox OS"] and i in feedback_tag_stat_detail["开发者问答"]:
			feedback_item["fid"] = 46
		elif i in feedback_tag_stat_detail["Firefox OS"]:
			feedback_item["fid"] = 41
		elif i in feedback_tag_stat_detail["开发者问答"]:
			feedback_item["fid"] = 45
		elif i in feedback_tag_stat_detail["兼容性"]:
			feedback_item["fid"] = 40
			feedback_item["typeid"] = 4
		elif i in feedback_tag_stat_detail["插件"]:
			feedback_item["fid"] = 40
			feedback_item["typeid"] = 3
		elif i in feedback_tag_stat_detail["第三方插件"]:
			feedback_item["fid"] = 40
			feedback_item["typeid"] = 3
		elif i in feedback_tag_stat_detail["扩展"]:
			feedback_item["fid"] = 40
			feedback_item["typeid"] = 2
		else:
			feedback_item["fid"] = 40
			feedback_item["typeid"] = 1
		feedback_list.append(str(feedback_item["id"])+","+str(feedback_item["fid"])+","+str(feedback_item["typeid"]))
		
	with file("discuz_import.txt","a") as discuz_import:
		write_cache = ""
		for i in feedback_list:
			write_cache = write_cache + i +"\n"
		discuz_import.write(write_cache)