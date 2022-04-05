import xlwings as xw

class SetExcel:
    def set_excel(self):
        data = ['50%,30%,45%,80%,90%']
        e.open('Track.xlsx')

app =xw.App(visible=True,add_book=False)
wb = app.books.add()
wb.sheets[0].name = '课时报'
wb.sheets.add('日报')
wb.sheets.add('周报')

data = [{"姓名":"杨栋","低头":"50%","举手":"30%","互动":"45%","关注":"80%","书写":"90%"},
        {"姓名":"杨敏","低头":"70%","举手":"40%","互动":"25%","关注":"10%","书写":"5%"},
        {"姓名":"武壮","低头":"70%","举手":"40%","互动":"25%","关注":"10%","书写":"5%"},
        ]

data1 =[]
data2=[]
lesson_report = wb.sheets['课时报']
for k in data[0]:
    data1.append(k)
lesson_report.range('A1').value = data1
for i in range(0,len(data)):
    a= data[i]
    for k,v in a.items():
        data2.append(v)
    num =i+2
    lesson_report.range('A%s'%num).value = data2
    data2.clear()


data_report = wb.sheets['日报']
week_report = wb.sheets['周报']


wb.save('./Track.xlsx')
wb.close()
app.quit()