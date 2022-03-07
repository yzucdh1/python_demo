#教育机构 ：马士兵教育
#讲    师：杨淑娟

'''
MyContentMgr实现了特殊方法__enter__(),__exit__()称为该类对象遵守了上下文管理器协议
该类对象的实例对象，称为上下文管理器

MyContentMgr()

'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了',1/0)

with  MyContentMgr() as file:    #相当于file=MyContentMgr()
    file.show()