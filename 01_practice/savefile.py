def main():
    f= open("log_text_file_test.txt","w+")
    #f=open("log_text_file_test.txt","a+")
    for i in range(10):
         f.write("작성중 %d\r\n" % (i+1))
    f.close()
 
    #파일을 다시 열고 내용을 읽으십시오
    #f=open("Entity01.txt", "r")
    #if f.mode == 'r':
        #contents =f.read()
        #print (contents)
    #또는 readlines는 개별 행을 목록으로 읽습니다.
    #fl =f.readlines()
    #for x in fl:
        #print(x)
 
if __name__== "__main__":
  main()
