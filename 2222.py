import os
import requests
import xlrd
import time

readbook = xlrd.open_workbook(r'D:\1111.xlsx')
sheet = readbook.sheet_by_index(0)
nrows = sheet.nrows
print (nrows)
num = 0
for i in range(nrows):
    # print(sheet.cell(0,0).value)
    externalid = sheet.cell(i,0).value#获取i行3列的表格值
    url = sheet.cell(i,1).value#获取i行4列的表格值
    # url="http://develop.kingchannels.cn:50053/files/upload/210/2107527420931db85fd20c6da6eecd9f-475898.jpg"
    new_url = url
    d='D:\\B\\'
    path=d+externalid+'.jpg'
    # print (path)
    # print (requests.get(new_url))

    try:
        if not os.path.exists(d):
            os.mkdir(d)
        if not os.path.exists(path):
            r=requests.get(new_url)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                num = num+1
                print("第%s张图片%s保存成功"%num%externalid)
                time.sleep(4)
                f.close()

        else:
            print("图片已存在")
    except:
        print("图片获取失败%s,'%s'"%(externalid,new_url))





# l = ['http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/250/25080aea662fec94d59108145123bdd7-38038.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/736/73628284f67b914ca3907464056d03e5-1120502.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/91a/91ad135e17dbe4d23ac98b288e7622d8-32006.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/337/3375d7e52dfa6463aeb25a36c2af532b-13291.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/9a5/9a51591af3827709c1893c466d38e66d-420948.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/83e/83e857fd55736905a5103543ce946fff-67899.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/2a7/2a79821ccae2dac48f45cf5c00c7f21d-39265.jpg'
# ,'http://124.207.5.140:8001http://api.aqr.keledge.cn/files/upload/813/81392c5ac354a1c53c77dde57c912aa9-217478.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/a21/a21e7495f7094f14dd05d1c0e43a243c-211787.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/ea5/ea5437eb608b1d999bf73ac739d5c108-171680.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/6c3/6c3b839baf332f26bd7a91756fa07d51-37535.jpg'
# ,'http://124.207.5.140:8001http://124.207.5.140:8001/files/upload/532/532bee4f4da28de540feae6b79c70582-43510.jpg'
# ,'http://124.207.5.140:8001http://api.aqr.keledge.cn/files/upload/71e/71ea5c5b4fe1be9fb5f6bf92dd1a0ecd-30640.jpg']


