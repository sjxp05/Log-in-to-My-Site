userList = {
    "sjxp05": "1234",
    "byolha": "5678",
    "wkdixir": "1562",
    "jibebonejwo": "0147",
    "san_ho": "5396",
}

while True:
    sel = input("메뉴를 선택하세요.\n(1: 로그인 2: 회원가입 3:회원탈퇴 x:종료)\n --> ")

    if sel == "1":
        print()
        while True:
            userIndex = -1
            loginId = input("아이디: ")

            for i in userList.keys():
                if loginId == i:
                    userIndex = i
                    break

            if userIndex != -1:
                break
            else:
                print("\n존재하지 않는 아이디입니다.\n")
                continue

        pwTry = 0
        while True:
            loginPw = input("비밀번호: ")

            if loginPw == userList[loginId]:
                print("\n로그인 성공\n")
                break

            else:
                pwTry += 1

                if pwTry < 3:
                    print(
                        "\n잘못된 비밀번호입니다. (3회 중 %d회 실패)\n\n아이디: %s"
                        % (pwTry, loginId)
                    )
                elif pwTry == 3:
                    print(
                        "\n잘못된 비밀번호입니다.\n비밀번호를 3회 이상 잘못 입력하여 로그인이 제한됩니다.\n"
                    )
                    break

                continue

    elif sel == "2":
        print()
        while True:
            newId = input("새로운 아이디: ")
            flag = 0

            for i in userList.keys():
                if newId == i:
                    flag = 1
                    break

            if flag == 1:
                print("\n이미 존재하는 아이디입니다.\n")
                continue

            else:
                break

        newPw = input("비밀번호: ")

        while True:
            pwCheck = input("비밀번호 확인: ")

            if newPw == pwCheck:
                userList[newId] = newPw
                print("\n회원가입이 정상적으로 완료되었습니다.\n")
                break

            else:
                print("잘못된 비밀번호입니다. 다시 입력해 주세요.\n\n")
                continue

    elif sel == "3":
        print()
        print("본인확인을 위해 개인정보를 입력해 주세요.")

        while True:
            extId = input("아이디: ")
            ex_userIndex = -1

            for i in userList.keys():
                if extId == i:
                    ex_userIndex = i
                    break

            if ex_userIndex != -1:
                break
            else:
                print("\n존재하지 않는 아이디입니다.\n")
                continue

        ex_pwTry = 0
        while True:
            extPw = input("비밀번호: ")

            if extPw == userList[extId]:
                tal = input("\n정말 탈퇴하시겠습니까? (y/n)\n --> ")

                if tal == "y":
                    userList.pop(extId)
                    print("\n회원탈퇴가 정상적으로 완료되었습니다.\n")
                elif tal == "n":
                    print(
                        "\n회원탈퇴가 완료되지 않았습니다. 처음 화면으로 돌아갑니다.\n"
                    )
                break

            else:
                ex_pwTry += 1

                if ex_pwTry < 3:
                    print(
                        "\n잘못된 비밀번호입니다. (3회 중 %d회 실패)\n\n아이디: %s"
                        % (ex_pwTry, extId)
                    )
                elif ex_pwTry == 3:
                    print(
                        "\n잘못된 비밀번호입니다.\n비밀번호를 3회 이상 잘못 입력하여 로그인이 제한됩니다.\n"
                    )
                    break

                continue

    elif sel == "x":
        print("\n종료되었습니다.\n")
        break

    else:
        print("\n잘못된 입력입니다.\n")
        continue
