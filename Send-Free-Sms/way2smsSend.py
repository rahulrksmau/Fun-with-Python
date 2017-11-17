import urllib
import urllib2
import cookielib
import sys
from getpass import getpass

def cook(cj):
    j = str(cj)
    t2= j.find(' for ')
    t1= int(j.find('~'))+1
    tokken= str(j[t1:t2])
    return tokken

def main():
    number = int(raw_input('Username or mobile number '))
    password=int(getpass('Please enter password'))
    if len(str(number))== 10:
        pass
    else:
        print "Invalid username"
        sys.exit(0)
    url = 'http://site24.way2sms.com/Login.action'
    data= { 'username':str(number),'password':str(password) }
    data= urllib.urlencode(data)
    cj = cookielib.CookieJar()
    #header={'User-Agent':'Rahul Kumar rkvns15@gmail.com'}
    header = {'User-Agent':'Mozilla/5.0 (X11; LINUX x86_64; rv:31.0 Gecko/20100101 Firefox/31.8.0'}
    req = urllib2.Request(url, data, header=header)
    opennr = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),
                          urllib2.HTTPRedirectHandler())
    print "[+] Please Wait Trying To Login "
    req = opennr.open(req)
    sucess=str(req.info())
    sucess=sucess.find('Set-Cookies')
    if (sucess== -1):
        print '\n Login Successful '
        pass
    else:
        print '\n Login Fails '
        raw_input(' ')
        sys.exit(0)
    tokken=cook(cj)
    print 'Token Received :' ,tokken
    url = 'http://site24.way2sms.com/smstoss.action'
    head = {'User-Agent':'Mozilla/5.0 (X11; LINUX x86_64; rv:31.0 Gecko/20100101 Firefox/31.8.0','Refere':str('http://site24.way2sms.com/sendSMS?Token='+tokken)}
    mobiles= raw_input('Mobile numbers to sending : ').split(',')
    print ' total mobile number added : ', len(mobiles)
    while True:
        message_raw = str(raw_input('Enter messages less then 140 :'))
        message = message_raw.replace(' ', '+')
        msglen = 140-len(message)
        if len(message) > 140:
            break
        else:
            pass
    failed_number = []
    for mobile in mobiles:
        if len(mobile)==10:
            data = 'ssaction=ss&Token='+tokken+'&mobile='+str(mobile)+'&message='+str(message)+'&msgLen='+str(msglen)
            req  = urllib2.Request(url, data=data, header=head)
            print 'Sending SMS to {0}.....'.format(mobile)
        req  = opennr.open(req)
        print 'Done! Sms sent to ... {0}'.format(mobile)
    else:
        failed_number.append(mobile)
        for i in failed_number:
            print 'Wrong Number...{0}'.format(mobile)

if __name__ == '__main__':
    main()

