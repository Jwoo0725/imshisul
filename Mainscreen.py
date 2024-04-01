import GwamokCaller
import time
#def(nugu, id):

#id = '학생'
#print("성공적으로 로그인되었습니다, 잠시만 기다려주세요.")
#time.sleep(1)
#print ("\n" * 20)
print(" ======================= 아주대학교 수강신청 =======================\n")
print("수강과목 : \n")
print(GwamokCaller.gwamok,'\n')
print('당신의 신분은',id,'입니다.')
print('원하는 작업을 선택해주세요 :\n')

if id =='학생' :
    Haksang(nugu)
    
elif id == '관리자' :
    Gwanli(nugu)

else :
    print('잘못된 접근 발생! 프로그램을 강제 종료합니다...')
    
