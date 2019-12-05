#file.py
f = open(r'words.txt')
list1 = (f.read()).split()

list2= list(set(list1))
list2.sort(key = list1.index)


for i in range(len(list2)):
  print(list2[i],list2.index(list2[i]),list1.count(list2[i]))

f = open('Q1.txt','w')
for i in range(len(list2)):
  print(list2[i],list2.index(list2[i]),list1.count(list2[i]),file=open('Q1.txt','a'))
f.close()


"""
參考
1.https://repl.it/@aggiec/Du-Qu-Dang-An-Zi-Liao(檔案讀取)
2.https://www.cnblogs.com/nzyjlr/p/4174145.html(剃除重複項)
3.https://ithelp.ithome.com.tw/articles/10201641(for迴圈)
4.https://footmark.info/programming-language/python/python-base/(檔案輸出)
"""

