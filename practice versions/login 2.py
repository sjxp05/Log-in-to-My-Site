userList = {
    "sjxp05": "123asdfghjkl",
    "byulha": "qwerty1234",
    "wkdixir": "xh156qef",
    "jibebonejwo": "rtus3sss",
    "san_ho": "6u76r353",
}


def idCheck():
    print()
    while True:
        userId = input("아이디: ")

        if userId in userList.keys():
            return userId

        else:
            print("\n존재하지 않는 아이디입니다.\n")
            continue


def pwCheck(name):
    pwTry = 0
    while True:
        userPw = input("비밀번호: ")

        if userPw == userList[name]:
            return pwTry

        else:
            pwTry += 1

            if pwTry < 3:
                print(f"\n잘못된 비밀번호입니다. (3회 시도 중 {pwTry}회 남음)\n")
                print("아이디: %s" % (name))
                continue

            elif pwTry == 3:
                print(
                    "\n잘못된 비밀번호입니다.\n3회 이상 비밀번호를 틀려 접속이 제한됩니다.\n"
                )
                return pwTry


def new_idCheck():
    print()
    while True:
        newId = input("새로운 아이디: ")

        if newId in userList.keys():
            print("\n이미 존재하는 아이디입니다.\n")
            continue

        else:
            return newId


def new_pwCheck():
    while True:
        newPw = input("비밀번호(8 ~ 16자의 영어 대소문자 및 숫자): ")
        if len(newPw) >= 8 and len(newPw) <= 16:
            if newPw.isalnum() and not (newPw.isalpha() or newPw.isdecimal()):
                break
            else:
                print("\n영문과 숫자로 이루어진 비밀번호를 입력해 주세요.\n")
                continue

        else:
            print("\n8 ~ 16자의 비밀번호를 입력해 주세요.\n")
            continue

    while True:
        check = input("비밀번호 확인: ")

        if newPw == check:
            return newPw
        else:
            print("\n비밀번호가 다릅니다. 다시 입력해 주세요.\n")
            continue


while True:
    sel = input(
        "메뉴를 선택해 주세요\n(1: 로그인 2: 회원가입 3: 회원탈퇴 x:종료)\n --> "
    )

    if sel == "1":
        if pwCheck(idCheck()) < 3:
            print("\n로그인 성공\n")

        continue

    elif sel == "2":
        newKey = new_idCheck()
        newValue = new_pwCheck()

        userList[newKey] = newValue
        print("\n회원가입이 정상적으로 완료되었습니다.\n")
        continue

    elif sel == "3":
        print("\n회원탈퇴를 위해 개인정보 확인을 진행합니다.")
        outId = idCheck()

        if pwCheck(outId) < 3:
            userList.pop(outId)
            print("\n회원탈퇴가 정상적으로 완료되었습니다.\n")

        continue

    elif sel.lower() == "x":
        print("\n종료되었습니다.\n")
        break

    else:
        print("\n잘못된 입력입니다!\n")
        continue
