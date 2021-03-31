# coding:utf-8

# f = open("email.txt")
# str = f.read();
# str1 = "<597234159@qq.com>"
# count = 0;
# temp = []
# len = len(str)
# while count < len:
#     if str[count] == '<':
#         count+=1
#         start = count
#         while str[count] != '>':
#             count+=1
#         end = count
#         temp.append(str[start:end])
#     count+=1
# print(temp)
# f.close()

def readIntro(filePath):
    f = open(filePath, encoding='utf-8')
    temp = ""
    for line in f:
        temp += line
    print(temp)
    temp.replace("\n", "%0A")
    return temp
# emailList = getEmailAd("email.txt")
intro = readIntro("introduce.txt")