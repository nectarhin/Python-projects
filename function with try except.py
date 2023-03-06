def spam ():
    try:
        var = int (input('enter value:)'))
        if var >=5:
            print('Good')
        elif var < 0:
            print('???')
        else:
            print('Low')
    except ValueError:
        print('Maybe enter a value?:)')
spam()
