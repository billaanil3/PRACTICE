from datetime import datetime as dt

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

# def custom_strftime(format, t):
#     # return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))
#     return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

war_start = "2018-09-19"
# print dt.now()
t = dt.strptime(war_start, '%Y-%m-%d')
print type(t)
# print custom_strftime('{S} %B, %Y', t)

print (t.strftime('{S} %B,%Y'.replace('{S}', str(t.day) + suffix(t.day))))
