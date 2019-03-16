list=[1]
for i in range (10):
    print(list)
    appender = []
    appender.append(list[0])
    for i in range (len(list)-1):
        appender.append(list[i]+list[i+1])
    appender.append(list[-1])
    list=appender