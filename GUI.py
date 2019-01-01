import webbrowser
import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sys
import tkinter.messagebox
from tkinter import *


def imageView():
    clicked_items = List1.curselection()
    print(List1.get(clicked_items))
        
def mgnetBt():
    try:
        clicked_items = List1.curselection()
        clicked_items_num = clicked_items[0] + 1
       
        mglink = mglist[clicked_items_num]
        webbrowser.open("magnet:?xt=urn:btih:"+mglink)
    except:
        tkinter.messagebox.showinfo('안내','마그넷 주소가 존재하지 않거나 불러올 수 없습니다.')
        
def searchBt(self):
    List1.delete(0, 20)
    mtext = ment.get()
    search = urllib.parse.quote(mtext) #URL Encoding
    req = Request('https://torrentwal.net/bbs/s.php?k='+str(search)+'&q=', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage,"lxml")
    num = 0  #num 초기값
    for link1 in soup.find_all(name="td",attrs={"class":"subject"}):
        try:
            title = link1.select('a')[1] #a태그중 0다음인 1번째 데이터 가져오기
            num = num+1
            List1.insert(num, title.get_text().strip())
        except:
                pass
    global mglist
    mglist = [] * num #리스트 생성
    for link2 in soup.find_all(name="td",attrs={"class":"num"}):
        try:
            mgnet = link2.select('a')[0]['href'] #a 태그에서 href만 가져오기
        except:
            pass
                #print("href 없음")
        mgnet = mgnet.strip("javascript:Mag_dn('')") #문자열 자르기
        mglist.append(str(mgnet)) #리스트에 넣기
            
    #List1.insert(1,mtext)
mGui = Tk()
ment = StringVar()
mGui.geometry('750x450')
mGui.title("마그넷 검색기")

mlabel = Label(text='제작 : jinho021712@gmail.com').pack()
mlabel = Label(text='아래 검색창에 입력 후 엔터 → 선택 후 다운로드 버튼').pack()
mEntry = Entry(mGui, textvariable = ment, width = 92)
mEntry.bind("<Return>", searchBt)
mEntry.pack()

mbutton = Button(mGui, text = '다운로드', command = mgnetBt, width = 92).pack()
List1 = Listbox(mGui, width = 92)
#List1.bind("<Button-1>", imageView)
List1.pack()
mlabel = Label(text='Ver1.0').pack()
#mbutton = Button(mGui, text = '미리보기', command = imageView, width = 92).pack()
#canvas = Canvas(mGui, width = 750, height = 450,bg = "blue").pack()


mGui.mainloop()
