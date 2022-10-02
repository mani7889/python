sh=input('enter hours')
sr=input('enter rate')
fh=float(sh)
fr=float(sr)
if fh>40:
    reg=fr*fh
    otp=(fh-40)*(fr*0.5)
    xp=reg+otp
else:
    xp=fh*fr
print('pay:',xp)
