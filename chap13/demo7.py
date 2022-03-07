#教育机构 ：马士兵教育
#讲    师：杨淑娟
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')


class Person:
    def eat(self):
        print('人吃五谷杂粮')


#定义一个函数
def fun(obj):
    obj.eat()

#开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('----------------------')
fun(Person())