#coding=utf-8
fp = open('jlc.csv', 'r')
idx = 0
vehi_set = set()
for line in fp.readlines():
    if idx != 0:
        items = line.strip('\n').split(',')
        bid = items[1].strip('"')
        vehi_set.add(bid)
    idx += 1
fp.close()

fpy = open('wba.csv', 'r')
fp1 = open('1.csv', 'w')
fp2 = open('2.csv', 'w')

idx = 0
cnt1, cnt2 = {}, {}
cn = ['xiaoming', 'ofo', 'mb', 'hellobike', 'qibei', 'mt']
for c in cn:
    cnt1[c], cnt2[c] = 0, 0
for line in fpy.readlines():
    if idx == 0:
        pass
    else:
        items = line.strip('\n').split(',')
        bid = items[1].strip('"')
        cid = items[0].strip('"')
        if bid in vehi_set:
            cnt1[cid] += 1
            fp1.write(line)
        else:
            cnt2[cid] += 1
            fp2.write(line)
    idx += 1
fp1.close()
fp2.close()

for c in cn:
    print c, cnt1[c]
for c in cn:
    print c, cnt2[c]