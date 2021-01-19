# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    for num in user_input_number:
        if num<str(0) or num>str(9):
            return False
    return True


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    result=0
    digit=len(user_input_number)-1
    for num in user_input_number:
        result+=((int)(num))*(10**digit)
        digit-=1 
    if result>=100 and result<1000:
        return True
    return False


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    for num in three_digit:
        count = three_digit.count(num)
        if count!=1:
            return True
    return False


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    result = True if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number) else False
    # ==================================
    return result


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # get_random_number() 함수를 사용하여 random number 생성
    result = 0
    while True: 
        temp = get_random_number()
        temp_str = str(int(temp / 100))
        temp %= 100
        temp_str += str(int(temp / 10))
        temp %= 10
        temp_str +=str(temp)
        if is_duplicated_number(temp_str)==True:
            continue
        else:
            result=temp_str
            break
    # ==================================
    return result


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    result = [0, 0]
    for num1 in user_input_number:
        for num2 in random_number:
            if num1==num2:
                if user_input_number.index(num1)==random_number.index(num2):
                    result[0]+=1
                else:
                    result[1]+=1
    # ==================================
    return result


def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if len(one_more_input)==1:
        if one_more_input[0]=='y' or one_more_input[0]=='Y':
            return True
        else:
            return False
    elif len(one_more_input)==3:
        if (one_more_input[0]=='y' or one_more_input[0]=='Y') and (one_more_input[1]=='e' or one_more_input[1]=='E') and (one_more_input[2]=='s' or one_more_input[2]=='S'):
            return True
        else:
            return False
    else:
        return False


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if len(one_more_input)==1:
        if one_more_input[0]=='n' or one_more_input[0]=='N':
            return True
        else:
            return False
    elif len(one_more_input)==2:
        if (one_more_input[0]=='n' or one_more_input[0]=='N') and (one_more_input[1]=='o' or one_more_input[1]=='O'):
            return True
        else:
            return False
    else:
        return False


def main():
    while True:
        print("Play Baseball")
        user_input=""
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        EOG=False
        while True:
            while True:
                user_input=input("Input guess number : ")
                flag=is_validated_number(user_input)
                if flag:
                    break
                else:
                    if user_input=='0':
                        EOG=True
                        break
                    print("WRONG INPUT , Input again")
                    continue
            if EOG==True:
                break
            temp_result=get_strikes_or_ball(user_input, random_number)
            print(f"Strikes : {temp_result[0]} , Balls : {temp_result[1]}")
            if temp_result[0]==3:
                break
        if EOG==True:
            break
        while True:
            one_more=input("You win, one more(Y/N) ?")
            if is_yes(one_more) or is_no(one_more):
                if is_yes(one_more):
                    break
                else:
                    EOG=True
                    break
            else:
                print("WRONG INPUT , Input again")
                continue
        if EOG==True:
            break
    print("Thank you for using this program")
    print("End of the Game")
    

if __name__ == "__main__":
    main()
