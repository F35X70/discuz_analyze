# -*- coding: utf-8 -*-
import readfile_discuz
import jieba
if __name__ == '__main__':
	feedback_name = "discuz.txt"
	file_content = readfile_discuz.ReadContent(feedback_name)
	feedback_comment_stat = {}
	feedback_comment_stat_detail = {}
	
	for i in file_content:
		#discuz_stat
		if i[1] != "":
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

	#output
	feedback_comment_stat_sort =  sorted(feedback_comment_stat.iteritems(), key=lambda d:d[1], reverse = True)
	for i in feedback_comment_stat_sort:
		if i[1] >= 1:
			with file("discuz_stat.txt","a") as feedback_stat:
				write_string = i[0]+","+str(i[1])+":"+"\n"
				for x in feedback_comment_stat_detail[i[0]]:
					write_string = write_string + str(x) + ","
				feedback_stat.write(write_string+"\n"+"\n")
	