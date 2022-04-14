#教育机构 ：马士兵教育
#讲    师：杨淑娟
dict_ticket={'G1569':['北京南-天津南','18:05','18:39','00:34'],
             'G1567':['北京南-天津南','18:15','18:49','00:34'],
             'G8917':['北京南-天津西','18:20','19:19','00:59'],
             'G203 ':['北京南-天津南','18:35','19:09','00:34']}
print('车次\t\t出发站-到达站\t\t出发时间\t\t\t到达时间\t\t\t历时时长')
for item in dict_ticket:
    print(item,end='  ')
    for i in dict_ticket[item]:
        print(i,end='\t\t\t')
    print() # 换行
#输入要购买的车次
while True:
    train_no = input('请输入要购买的车次:')
    if dict_ticket.get(train_no) is None:
        print('对不起，车次不存在，请重新输入！')
        continue
    else:
        break
persons = input('请输入乘车人，如果是多人请使用逗号分隔')
s = f'您已购买了{train_no}次列车  '
s_info = dict_ticket[train_no]  # 获取车次详细信息
s += s_info[0] + '  ' + s_info[1] + '开  '
print(f'{s}请{persons}尽快取走纸制车票。【铁路客服】')
