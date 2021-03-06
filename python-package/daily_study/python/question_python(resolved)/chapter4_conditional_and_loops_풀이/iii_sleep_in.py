# -*- coding: utf-8 -*-


def sleep_in(weekday, vacation):
    """ weekday에는 일을 해야 한다(자면 안된다), 
        weekday가 아니면(주말이란 거니까) 자도 된다
        그런데 weekday이더라도 vacation이면 자도 된다

        True/False 값을 가질 수 있는 weekday와 vacation를 전달받아서 
        자도 되는지/아닌지를 bool(True 또는 False를 갖는 자료형) 값으로 반환하는 함수를 작성하자

        sample in/out:
            sleep_in(False, False) -> True
            sleep_in(True, False) -> False
            sleep_in(False, True) -> True
    """
##    if vacation or not weekday:
##        return True
##    else:
##        return False

    return True if (vacation or not weekday) else False


if __name__ == "__main__":
    print sleep_in(False, False)# -> True
    print sleep_in(True, False)# -> False
    print sleep_in(False, True)# -> True

