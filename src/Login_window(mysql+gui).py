from tkinter import *
from tkinter import ttk
from datetime import *
import pymysql
import pyautogui as pg
import random

tk = Tk()
tk.geometry("600x800")
tk.title("Login")

mySiteImg = PhotoImage(file="src\\mySite.png")
imgLb = Label(image=mySiteImg)

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="c0ding_gw4n9",
    db="login_users",
    charset="utf8",
)
cur = conn.cursor()

cur.execute("SELECT id, password, phone FROM users;")
id2pw = cur.fetchall()

id2pwDict = dict()
id2phone = dict()
tries = dict()

for rows in id2pw:
    id2pwDict[rows[0]] = rows[1]
    id2phone[rows[0]] = rows[2]
    tries[rows[0]] = 0

currentUserInfo = []
limitedList = []

ifHome = 0
suCheck = 0
phoneCheck = 0
newOtp = "1000000"


def hideWidgets():
    idEntry.place_forget()
    pwEntry.place_forget()
    nameEn.place_forget()
    maleBt.place_forget()
    femaleBt.place_forget()
    yearEn.place_forget()
    monthBox.place_forget()
    dateBox.place_forget()
    phoneNum.place_forget()
    otpNum.place_forget()
    otpBt.place_forget()
    otpConf.place_forget()
    imgLb.place_forget()

    lb1.place_forget()
    lb2.place_forget()
    lb3.place_forget()
    lb4.place_forget()
    lb5.place_forget()
    lb6.place_forget()
    lb7.place_forget()
    lb8.place_forget()
    lb9.place_forget()
    lb10.place_forget()

    warn1.place_forget()
    warn2.place_forget()
    warn3.place_forget()
    warn4.place_forget()
    warn5.place_forget()
    warn6.place_forget()
    warn7.place_forget()


def showWidgets():
    stateLb.place_forget()
    pwEntry.place(x=200, y=210)
    nameEn.place(x=200, y=270)
    maleBt.place(x=200, y=328)
    femaleBt.place(x=300, y=328)
    yearEn.place(x=200, y=390)
    monthBox.place(x=295, y=390)
    dateBox.place(x=365, y=390)
    phoneNum.place(x=200, y=450)
    otpBt.place(x=380, y=440)
    otpNum.place(x=200, y=510)
    otpConf.place(x=336, y=500)
    otpConf.config(text="인증확인", bg="light gray")

    lb1.place(x=140, y=150)
    lb2.place(x=100, y=210)
    lb3.place(x=142, y=270)
    lb4.place(x=142, y=330)
    lb5.place(x=100, y=390)
    lb6.place(x=100, y=450)
    lb7.place(x=260, y=390)
    lb8.place(x=340, y=390)
    lb9.place(x=410, y=390)
    lb10.place_forget()

    warn1.place(x=200, y=182)
    warn2.place(x=200, y=242)
    warn3.place(x=200, y=302)
    warn4.place(x=200, y=362)
    warn5.place(x=200, y=422)
    warn6.place(x=200, y=482)
    warn7.place(x=200, y=542)

    warn1["fg"] = "black"
    warn2["fg"] = "black"
    warn3["fg"] = "black"
    warn4["text"] = ""
    warn5["text"] = ""
    warn6["text"] = ""
    warn7["text"] = ""

    idEntry.delete(0, END)
    pwEntry.delete(0, END)
    genValue.set(0)
    nameEn.delete(0, END)
    yearEn.delete(0, END)
    monValue.set("")
    dateValue.set("")
    phoneNum.delete(0, END)
    otpNum.delete(0, END)


def beforeSet():
    global currentUserInfo, ifHome, suCheck, phoneCheck

    ifHome = 0
    suCheck = 0
    phoneCheck = 0

    loginBt.place(x=400, y=145)
    signupBt.place(x=360, y=400)

    viewBt.place_forget()
    logoutBt.place_forget()
    withdrawBt.place_forget()
    backBt.place_forget()
    backBt2.place_forget()
    wdConfirmBt.place_forget()
    modifyBt.place_forget()
    idLabel.place_forget()

    hideWidgets()

    idEntry.place(x=150, y=150)
    idEntry.delete(0, END)
    pwEntry.place(x=150, y=200)
    pwEntry.delete(0, END)

    lb1.place(x=90, y=150)
    lb2.place(x=50, y=200)
    lb10.place(x=120, y=410)

    stateLb.config(
        height=2, width=55, anchor="center", text="", font=("맑은 고딕", 12), fg="red"
    )
    stateLb.place(x=0, y=250)

    titleLb.config(width=8, anchor="center", text="로그인")
    titleLb.place(x=245, y=40)

    currentUserInfo = []

    return


def afterSet(thisId):
    global currentUserInfo, ifHome, suCheck, phoneCheck

    ifHome = 1
    suCheck = 0
    phoneCheck = 0

    loginBt.place_forget()
    signupBt.place_forget()
    withdrawBt.place_forget()
    backBt.place_forget()
    backBt2.place_forget()
    wdConfirmBt.place_forget()
    modifyBt.place_forget()
    idLabel.place_forget()
    stateLb.place_forget()

    hideWidgets()

    viewBt.place(x=350, y=30)
    logoutBt.place(x=450, y=30)
    viewBt.config(bg="light gray", text="내정보")

    imgLb.place(x=0, y=100)

    if currentUserInfo == []:
        cur.execute(f"SELECT * FROM users WHERE id = '{thisId}';")
        fetch = cur.fetchall()
        for i in fetch[0]:
            currentUserInfo.append(i)

    titleLb.config(width=22, anchor="w", text=f"{currentUserInfo[2]} 님, 환영합니다!")
    titleLb.place(x=30, y=40)

    return


def viewOrHome():
    global currentUserInfo, ifHome

    if ifHome == 1:
        ifHome == 0
        viewBt.config(bg="light blue", text="Home")
        viewInfo()
    elif ifHome == 0:
        ifHome == 1
        afterSet(currentUserInfo[0])


def viewInfo():
    global currentUserInfo, ifHome, suCheck, phoneCheck

    ifHome = 0
    suCheck = 0
    phoneCheck = 0

    withdrawBt.place(x=320, y=550)
    modifyBt.place(x=180, y=550)
    backBt.place_forget()
    wdConfirmBt.place_forget()
    idLabel.place_forget()

    hideWidgets()

    titleLb.config(width=8, text="내정보")
    titleLb.place(x=30, y=40)

    stateLb.config(
        height=13,
        width=55,
        fg="black",
        font=("맑은 고딕", 12),
        anchor="w",
        justify="left",
    )
    stateLb["text"] = (
        "        ID:  "
        + currentUserInfo[0]
        + "\n\n비밀번호:  "
        + ("●" * 10)
        + "\n\n     이름:  "
        + currentUserInfo[2]
        + "\n\n     성별:  "
        + ("남" if currentUserInfo[3] == "M" else "여")
        + "\n\n생년월일:  "
        + str(currentUserInfo[4])
        + "\n\n전화번호:  "
        + currentUserInfo[5]
    )
    stateLb.place(x=140, y=120)


def login():
    global id2pwDict, tries, limitedList

    thisId = (idEntry.get()).strip()
    thisPw = (pwEntry.get()).strip()
    idEntry.delete(0, END)
    pwEntry.delete(0, END)

    if len(thisId) == 0 or len(thisPw) == 0:
        stateLb["text"] = "ID와 비밀번호를 올바르게 입력해 주세요."
        return

    if thisId in id2pwDict.keys():
        if thisId in limitedList:
            res = pg.confirm("로그인 제한된 계정입니다.", buttons=["확인"])
            if res is not None:
                pass
            return

        if thisPw == id2pwDict[thisId]:
            tries[thisId] = 0
            afterSet(thisId)
            return
        else:
            tries[thisId] += 1

        if tries[thisId] == 5:
            stateLb["text"] = "5회 이상 비밀번호를 잘못 입력하여 접속이 제한됩니다."
            limitedList.append(thisId)
            ban = LoginBan(thisId)
            ban.timeCount()
            del ban
            # 5회이상 막힐 시 로그인제한 30초, 이후 시도횟수 초기화
        else:
            stateLb["text"] = (
                f"잘못된 비밀번호입니다. 남은 시도 횟수: {5 - tries[thisId]}/5"
            )
    else:
        stateLb["text"] = "해당 ID의 계정이 존재하지 않습니다."


class LoginBan:
    def __init__(self, thisId):
        self.id = thisId
        self.sec = 0

    def timeCount(self):
        global limitedList, tries

        if self.sec >= 30:
            limitedList.remove(self.id)
            tries[self.id] = 0
            stateLb["text"] = ""
            return
        else:
            self.sec += 1
            tk.after(1000, self.timeCount)


def infoCheck():
    global phoneCheck

    problems = 0

    thisId = (idEntry.get()).strip()
    thisPw = (pwEntry.get()).strip()
    thisName = (nameEn.get()).strip()
    thisGen = genValue.get()
    thisY = (yearEn.get()).strip()
    thisM = monValue.get()
    thisDate = dateValue.get()
    thisPhone = (phoneNum.get()).strip()

    warn1.config(text="ID는 4~20자로 영문 또는 숫자만 입력할 수 있습니다.", fg="black")
    warn2["fg"] = "black"
    warn3["fg"] = "black"
    warn4["text"] = ""
    warn5["text"] = ""
    warn6["text"] = ""
    warn7["text"] = ""

    for i in thisId:
        if not (
            (i >= "A" and i <= "Z")
            or (i >= "a" and i <= "z")
            or (i >= "0" and i <= "9")
        ):
            warn1["fg"] = "red"
            problems += 1
            break

    if len(thisId) < 4 or len(thisId) > 20:
        warn1["fg"] = "red"
        problems += 1

    for i in thisPw:
        if not (
            (i >= "A" and i <= "Z")
            or (i >= "a" and i <= "z")
            or (i >= "0" and i <= "9")
            or i in ["!", "_", "&", ".", "?", ";"]
        ):
            warn2["fg"] = "red"
            problems += 1
            break
    if (
        thisPw.isalpha()
        or thisPw.isnumeric()
        or all(thisPw) in ["!", "_", "&", ".", "?", ";"]
        or len(thisPw) < 8
        or len(thisPw) > 20
    ):
        warn2["fg"] = "red"
        problems += 1

    if not thisName.isalpha() or len(thisName) < 2 or len(thisName) > 10:
        warn3["fg"] = "red"
        problems += 1
    if thisGen not in [1, 2]:
        warn4["text"] = "성별을 선택해 주세요."
        problems += 1

    try:
        userDateInput = date(year=int(thisY), month=int(thisM), day=int(thisDate))
        if int(thisY) < 1900 or userDateInput > date.today():
            warn5["text"] = "올바른 날짜를 입력해 주세요."
            problems += 1
    except ValueError:
        warn5["text"] = "올바른 날짜를 입력해 주세요."
        problems += 1

    if len(thisPhone) != 11 or thisPhone[:3] != "010":
        warn6["text"] = "올바른 전화번호를 입력해 주세요."
        otpNum.delete(0, END)
        problems += 1

    return [
        thisId,
        thisPw,
        thisName,
        thisGen,
        thisY,
        thisM,
        thisDate,
        thisPhone,
        problems,
    ]


def signup():
    global id2pwDict, id2phone, suCheck, phoneCheck, tries, newOtp

    loginBt.place_forget()
    signupBt.place(x=250, y=620)
    backBt2.place(x=30, y=30)

    if suCheck == 1:
        newInfo = infoCheck()

        if newInfo[0] in id2pwDict.keys():
            warn1.config(fg="red", text="이미 사용 중인 ID입니다.")
            newInfo[8] += 1

        if newInfo[7] in id2phone.values():
            warn6["text"] = "이미 사용 중인 전화번호입니다."
            newInfo[8] += 1
        if phoneCheck == 0:
            warn7["text"] = "전화번호 인증 미완료"
            newOtp = "1000000"
            otpNum.delete(0, END)
            newInfo[8] += 1

        if newInfo[8] > 0:
            return

        cur.execute(
            f"INSERT INTO users VALUES('{newInfo[0]}','{newInfo[1]}','{newInfo[2]}','{"M" if newInfo[3]==1 else "F"}','{newInfo[4]}-{int(newInfo[5]):02d}-{int(newInfo[6]):02d}','{newInfo[7]}');"
        )
        res = pg.confirm("회원가입이 완료되었습니다.", buttons=["확인"])
        if res == "확인":
            id2pwDict[newInfo[0]] = newInfo[1]
            id2phone[newInfo[0]] = newInfo[7]
            tries[newInfo[0]] = 0
            conn.commit()
            beforeSet()
    else:
        suCheck = 1
        idEntry.place(x=200, y=150)
        warn1["text"] = "ID는 4~20자의 영문 또는 숫자를 입력해 주세요."
        titleLb["text"] = "회원가입"
        showWidgets()


def modify():
    global currentUserInfo, id2pwDict, id2phone, suCheck, phoneCheck, newOtp

    modifyBt.place(x=250, y=620)
    backBt.place(x=30, y=30)
    withdrawBt.place_forget()

    titleLb["text"] = "정보수정"
    titleLb.place(x=150, y=40)

    if suCheck == 1:
        modInfo = infoCheck()

        warn1["text"] = "※ ID는 변경이 불가능합니다."

        if modInfo[7] != currentUserInfo[5]:
            if modInfo[7] in id2phone.values():
                warn6["text"] = "이미 사용 중인 전화번호입니다."
                modInfo[8] += 1
            if phoneCheck == 0:
                warn7["text"] = "전화번호 인증 미완료"
                newOtp = "1000000"
                otpNum.delete(0, END)
                modInfo[8] += 1

        if modInfo[8] > 0:
            return

        cur.execute(
            f"UPDATE users\nSET password = '{modInfo[1]}', \nname='{modInfo[2]}', \ngender='{"M" if modInfo[3]==1 else "F"}', \nbirth='{modInfo[4]}-{int(modInfo[5]):02d}-{int(modInfo[6]):02d}', \nphone='{modInfo[7]}'\nWHERE id='{currentUserInfo[0]}';"
        )
        res = pg.confirm("회원정보가 수정되었습니다.", buttons=["확인"])
        if res == "확인":
            id2pwDict[currentUserInfo[0]] = modInfo[1]
            id2phone[currentUserInfo[0]] = modInfo[7]

            currentUserInfo = []
            cur.execute(f"SELECT * FROM users WHERE id = '{modInfo[0]}';")
            fetch = cur.fetchall()
            for i in fetch[0]:
                currentUserInfo.append(i)

            conn.commit()
            viewInfo()
    else:
        suCheck = 1

        idLabel["text"] = currentUserInfo[0]
        idLabel.place(x=200, y=150)
        warn1["text"] = "※ ID는 변경이 불가능합니다."
        showWidgets()

        idEntry.insert(0, currentUserInfo[0])
        pwEntry.insert(0, currentUserInfo[1])
        nameEn.insert(0, currentUserInfo[2])
        genValue.set(1 if currentUserInfo[3] == "M" else 2)
        yearEn.insert(0, currentUserInfo[4].year)
        monValue.set(currentUserInfo[4].month)
        dateValue.set(currentUserInfo[4].day)
        phoneNum.insert(0, currentUserInfo[5])
        otpNum.delete(0, END)


def otpMake():
    global phoneCheck, newOtp, id2phone, currentUserInfo

    if phoneCheck == 1:
        warn6["text"] = ""
        return

    phone1 = (phoneNum.get()).strip()

    if len(phone1) != 11 or phone1[:3] != "010":
        warn6["text"] = "올바른 전화번호를 입력해 주세요."
        newOtp = "1000000"
        return

    if phone1 in id2phone.values():
        if currentUserInfo == [] or phone1 != currentUserInfo[5]:
            warn6["text"] = "이미 사용 중인 전화번호입니다."
            newOtp = "1000000"
        else:
            warn6["text"] = ""
        return

    otp1 = random.randrange(0, 1000000)
    newOtp = str("%06d" % otp1)

    print(
        "\n===========================\n인증번호는 ["
        + newOtp
        + "] 입니다.\n===========================\n"
    )
    warn6["text"] = ""
    return


def otpCheck():
    global phoneCheck, newOtp, currentUserInfo

    if phoneCheck == 1:
        return
    else:
        if currentUserInfo != [] and (phoneNum.get()).strip() == currentUserInfo[5]:
            warn7["text"] = ""
            otpNum.delete(0, END)
            return

        otp2 = (otpNum.get()).strip()
        if otp2 == newOtp:
            phoneCheck = 1
            otpConf.config(bg="light blue", text="인증완료")
            warn7["text"] = ""
        else:
            warn7["text"] = "인증 실패"
            otpNum.delete(0, END)
            newOtp = "1000000"
        return


def withdraw():
    pwEntry.place(x=140, y=350)
    pwEntry.delete(0, END)

    wdConfirmBt.place(x=390, y=340)
    backBt.place(x=30, y=30)
    withdrawBt.place_forget()
    modifyBt.place_forget()

    titleLb["text"] = "회원탈퇴"
    titleLb.place(x=150, y=40)

    stateLb.config(
        height=2, width=55, anchor="center", fg="black", font=("맑은 고딕", 12)
    )
    stateLb["text"] = "회원 탈퇴를 위해 비밀번호를 입력해 주세요."
    stateLb.place(x=0, y=250)


def wdCheck():
    global id2pwDict, id2phone, currentUserInfo, tries

    checkPw = (pwEntry.get()).strip()

    if len(checkPw) > 0:
        if checkPw == currentUserInfo[1]:
            stateLb.config(
                fg="black", text="회원 탈퇴를 위해 비밀번호를 입력해 주세요."
            )

            res = pg.confirm(
                "정말 탈퇴하시겠습니까?\n탈퇴한 계정은 복구할 수 없습니다.",
                buttons=["예", "아니요"],
            )
            if res is not None and res == "예":
                cur.execute(f"DELETE FROM users WHERE id = '{currentUserInfo[0]}';")
                conn.commit()

                del id2pwDict[currentUserInfo[0]]
                del id2phone[currentUserInfo[0]]
                del tries[currentUserInfo[0]]
                beforeSet()
            else:
                pwEntry.delete(0, END)
        else:
            pwEntry.delete(0, END)
            stateLb.config(fg="red", text="잘못된 비밀번호입니다.")


def onClosing():
    res = pg.confirm(
        "정말 종료하시겠습니까?", buttons=["예", "아니요"]
    )  # 와 이거 개신박해 더 공부해야겟다
    if res == "예":
        conn.commit()
        conn.close()
        exit(0)
    else:
        pass


tk.protocol("WM_DELETE_WINDOW", onClosing)  # 닫을때 쓰는 함수

idEntry = Entry(font=("맑은 고딕", 12), width=20)
pwEntry = Entry(font=("맑은 고딕", 12), width=20, show="●")
nameEn = Entry(font=("맑은 고딕", 12), width=20)

genValue = IntVar()
maleBt = Radiobutton(text="남", font=("맑은 고딕", 12), value=1, variable=genValue)
femaleBt = Radiobutton(text="여", font=("맑은 고딕", 12), value=2, variable=genValue)

monList = []
dateList = []
for i in range(1, 13):
    monList.append(str(i))
for i in range(1, 32):
    dateList.append(str(i))
monValue = StringVar()
dateValue = StringVar()

yearEn = Entry(font=("맑은 고딕", 12), width=5)
monthBox = ttk.Combobox(
    font=("맑은 고딕", 12), width=2, textvariable=monValue, values=monList
)
dateBox = ttk.Combobox(
    font=("맑은 고딕", 12), width=2, textvariable=dateValue, values=dateList
)


phoneNum = Entry(font=("맑은 고딕", 12), width=15)
otpNum = Entry(font=("맑은 고딕", 12), width=10)

otpBt = Button(
    text="인증",
    font=("맑은 고딕", 12),
    bg="light gray",
    width=4,
    height=1,
    command=otpMake,
)
otpConf = Button(
    font=("맑은 고딕", 12),
    width=8,
    height=1,
    command=otpCheck,
)

loginBt = Button(
    text="로그인",
    height=2,
    font=("맑은 고딕", 15),
    fg="white",
    bg="blue",
    command=login,
)
signupBt = Button(
    text="회원가입",
    font=("맑은 고딕", 15),
    command=signup,
    bg="light green",
)
viewBt = Button(
    font=("맑은 고딕", 15),
    width=6,
    command=viewOrHome,
)  # 내정보
modifyBt = Button(
    text="정보수정",
    font=("맑은 고딕", 15),
    bg="orange",
    command=modify,
)  # 정보수정
withdrawBt = Button(
    text="회원탈퇴",
    font=("맑은 고딕", 15),
    bg="red",
    fg="white",
    command=withdraw,
)  # 회원탈퇴 버튼
wdConfirmBt = Button(
    text="확인",
    font=("맑은 고딕", 12),
    width=8,
    bg="light gray",
    command=wdCheck,
)  # 회원탈퇴시 비밀번호 확인
backBt = Button(
    text=" <- ",
    font=("맑은 고딕", 15),
    width=6,
    bg="light gray",
    command=viewInfo,
)  # 정보수정/회원탈퇴시 뒤로가기
backBt2 = Button(
    text=" <- ",
    font=("맑은 고딕", 15),
    width=6,
    bg="light gray",
    command=beforeSet,
)  # 회원가입시 뒤로가기
logoutBt = Button(
    text="로그아웃",
    font=("맑은 고딕", 15),
    width=8,
    bg="pink",
    command=beforeSet,
)

lb1 = Label(text="ID ", font=("맑은 고딕", 12), width=4, anchor="e")
lb2 = Label(text="비밀번호 ", font=("맑은 고딕", 12), width=8, anchor="e")
lb3 = Label(text="성명 ", font=("맑은 고딕", 12), width=4, anchor="e")
lb4 = Label(text="성별 ", font=("맑은 고딕", 12), width=4, anchor="e")
lb5 = Label(text="생년월일 ", font=("맑은 고딕", 12), width=8, anchor="e")
lb6 = Label(text="전화번호 ", font=("맑은 고딕", 12), width=8, anchor="e")
lb7 = Label(text="년", font=("맑은 고딕", 12), width=2)
lb8 = Label(text="월", font=("맑은 고딕", 12), width=2)
lb9 = Label(text="일", font=("맑은 고딕", 12), width=2)
lb10 = Label(text="아직 계정이 없으신가요?", font=("맑은 고딕", 12))

warn1 = Label(
    font=("맑은 고딕", 8), text="ID는 4~20자의 영문 또는 숫자를 입력해 주세요."
)
warn2 = Label(
    font=("맑은 고딕", 8),
    text="비밀번호는 8~20자로 영문, 숫자, 특수문자를 조합해야 합니다.",
)
warn3 = Label(font=("맑은 고딕", 8), text="이름은 2~10자의 한글/영문을 입력해 주세요.")
warn4 = Label(font=("맑은 고딕", 8), fg="red")
warn5 = Label(font=("맑은 고딕", 8), fg="red")
warn6 = Label(font=("맑은 고딕", 8), fg="red")
warn7 = Label(font=("맑은 고딕", 8), fg="red")

stateLb = Label(text="", font=("맑은 고딕", 12))
idLabel = Label(font=("맑은 고딕", 12), anchor="w")
titleLb = Label(font=("맑은 고딕", 15))

beforeSet()

tk.mainloop()
