#教育机构 ：马士兵教育
#讲    师：杨淑娟
def get_count(s,ch):
    count=0
    for item in s:
        if ch.upper()==item or ch.lower()==item:
            count+=1
    return count

if __name__ == '__main__':
    s='hellopyhton,hellojava,hellogo'
    ch=input('请输入要统计的字符:')
    count=get_count(s,ch)
    print(f'{ch}在{s}中出现的次数为:{count}')