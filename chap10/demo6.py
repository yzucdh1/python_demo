#教育机构 ：马士兵教育
#讲    师：杨淑娟
def fun(*args):  #函数定义时的 可变的位置参数
    print(args)
    #print(args[0])

fun(10)
fun(10,30)
fun(30,405,50)

def fun1(**args):
    print(args)

fun1(a=10)
fun1(a=20,b=30,c=40)

print('hello','world','java')

'''def fun2(*args,*a):   
    pass   
    以上代码，程序会报错，个数可变的位置参数，只能是1个 
    def fun2(**args,**args):
    pass
 以上代码，程序会报错，个数可变的关键字参数，只能是1个 
    '''
def fun2(*args1,**args2):
    pass

'''def fun3(**args1,*arg2):
    pass
    在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参之前
 '''


