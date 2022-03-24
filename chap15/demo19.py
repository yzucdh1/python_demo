#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  os
path=os.getcwd()
lst_files=os.walk(path) #返回生成器类型
for dirpath,dirnames,filenames in lst_files:
    print(dirpath)
    print(dirnames)
    print(filenames)
    print('-------------------------------------')
    for dir in dirnames:
        print(os.path.join(dirpath,dir))

    for file in filenames:
        print(os.path.join(dirpath,file))
    print('----------------------------------')