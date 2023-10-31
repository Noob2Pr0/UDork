import os
import sys
from bs4 import BeautifulSoup
import urllib.parse
import requests
from requests.exceptions import ConnectionError
import re
import warnings
import time

warnings.filterwarnings('ignore')

def update():
    version = '1.0'
    server='https://omidnasiripouya.ir/MyTools/UDork/version.txt'
    update_request=requests
    orginal = update_request.get(server)
    answer = BeautifulSoup(orginal.content, 'html.parser')
    orginal_answer = answer.find_all('version')
    result = re.search('>(.*)<', str(orginal_answer))
    latest_version = str(result.group(1))
    if str(version) == latest_version:
        print ('\u001b[32mYour are using a Latest of version '+latest_version+'. thank you\u001b[37m')
        time.sleep(5)
    else:
        print('\u001b[31mYou are Using a out of date version of UDork tool.\u001b[37m')
        print('Your Current Version '+version+' and latest version '+str(result))
        print('You can download new version of UDork with this links')
        print('\u001b[36mhttps://github.com/Noob2Pr0/UDork \u001b[37m')
        print('\u001b[36mhttps://omidnasiripouya.ir/MyTools/UDork/ \u001b[37m')
        time.sleep(5)
    

def clsdis():
    os.system("cls")

def rules():
    print('''\u001b[31m
Any illegal use of this tool is your responsibility.
\u001b[33m
-------------------------------------------------
The results of this tool are influenced by Google captcha.
Before working with the tool, solve the Google captcha several times
and then run the software.
You can also try it manually to be more sure of the results.
-------------------------------------------------\u001b[36m
If captcha is not involved in the scanning process
this tool is able to extract up to 10 Google pages
equivalent to 100 links at most. This restriction
is also due to the prevention of expensive abuse
-------------------------------------------------\u001b[37m
    ''')
    qu = input('Have you read the rules and do you agree with them? (y=yes): \u001b[37m')
    if 'y' in qu:
        banner()
    else:
        sys.exit()

def banner():
    os.system("cls")
    print(u"""\u001b[36m
         ___           _    
 /\ /\  /   \___  _ __| | __
/ / \ \/ /\ / _ \| '__| |/ /
\ \_/ / /_// (_) | |  |   < 
 \___/___,' \___/|_|  |_|\_\\\u001b[34m v1.0 \u001b[37m
 Author: Omid Nasiri Pouya
""")



def menu():
    global subm1,subm2
    print('''
    1. Simple Dorks
    2. Advanced Dors
    ''')
    subm1= input('\u001b[36mEnter Menu Number: \u001b[37m')
    print('''
    1. Automatic Search
    2. Manualy Search
    ''')
    subm2= input('\u001b[36mEnter Menu Number: \u001b[37m')

def OSINT():
    global default_intext,default_inurl,default_cached,default_intitle,date
    default_intext= '*'
    default_inurl='*'
    default_cached='cached='+url
    default_intitle='*'
    date='*'
    
def s_end():
    print('''This tool doesn't need your email but it needs your support.\nIf you don't want to support us, leave the field empty \n----------------------------------------------------''')
    email=input('\u001b[32mEnter Your Email: \u001b[37m')
    try:
        data2 = {"email": email}
        response2 = requests.post(Eurl, data=data2)
    except ConnectionError:
        print ('\u001b[31mConnection to the server fail.\u001b[37m')
        print('Please check you internet connection')
        sys.exit(141)
    if email==None:
        pass
    else:
        print('Creating Profile for You Please Wait a Sec')
        if response2.status_code==200:
            print ('\u001b[32mConnection to the server successfuly.\u001b[37m')
            profile = open( 'UDProfile.ini', 'w' )
            profile.write(str(email)+'\n')
            profile.close()
            print ("""I created a profile for your email address\nso that you don't see this message again\nthe next time you open the software it won't bother you anymore.""")
            print("Thank you for supporing us \u001b[31m♥\u001b[37m")
        else:
            print ('\u001b[31mConnection to the server fail.\u001b[37m')
            print('Please check you internet connection')


def collect():
    global Eurl
    Eurl = 'https://omidnasiripouya.ir/MyTools/Log/Email.php'
    if os.path.exists("UDProfile.ini"):
        UR = open("UDProfile.ini", "r")
        URContent = UR.read()
        if '@' in str(URContent):
            cuser = os.getlogin()
            print('Welcome ',cuser)
            time.sleep(1)
            try:
                data = {"email": URContent}
                response = requests.post(Eurl, data=data)
            except ConnectionError:
                print ('\u001b[31mConnection to the server fail.\u001b[37m')
                print('Please check you internet connection')
                sys.exit(141)
        else:
            s_end()
    else:
        s_end()

def getdorkinfo():
    print('If you want to get better results, use your local language other than English')
    global filetype,intext,inurl,intitle
    print('Examples: xlsx xlsx db doc accdb docx zip rar 7z')
    filetype = input('\u001b[36mEnter the file extension: ')
    print('-------------------------------------------')
    print('Examples: @gmail.com @yahoo.com +1 +98 0912 password username email')
    intext = input('\u001b[36mEnter the desired text: ')
    print('-------------------------------------------')
    print('Examples: * .php .asp logs images books cv')
    inurl = input('\u001b[36mEnter the desired path: ')
    print('-------------------------------------------')
    print('Examples: cpanel panel login user welcome')
    intitle = input('\u001b[36mEnter the desired title: ')


def RunScan():
    clsdis()
    banner()
    ScanFile = UserInputScan
    global smartagent
    smartagent='python/3.7'
    filetypelist = ['xls','xlsx','doc','docx','log','conf','bak','rar','zip','7z','tar.gz','paa','mdb','accdb','txt','dbs','xml','tmp','git']
    default_filetype= 'filetype:xls | filetype:xlsx | filetype:doc | filetype:docx | filetype:log | filetype:bak | filetype:conf | filetype:rar | filetype:zip | filetype:pass | filetype:mdb | filetype:accdb | filetype:sql | filetype:txt | filetype:dbs | filetype:xml'
    if '1' in subm1:
        if '2' in subm2:
            print('You have selected SIMPLE dork with manual scan.')
            print('You can open the following links in your browser with the control key + left click\u001b[37m')
            print('\u001b[32m----------[File Type All in One Dork]----------\u001b[37m')
            print('https://www.google.com/search?q=site:'+url+'%20filetype:'+urllib.parse.quote(default_filetype))
            print('\u001b[32m..........[File Type Small Dork].........\u001b[37m')
            for x in range(len(filetypelist)):
                print('https://www.google.com/search?q=site:'+url+'%20filetype:'+urllib.parse.quote(filetypelist[x]))
            print('\u001b[32m----------[Cached Page Dork]----------\u001b[37m')
            print('https://www.google.com/search?q=cached:'+url)
        if '1' in subm2:
            if os.path.exists(ScanFile):
                os.remove(ScanFile)
            else:
                pass
            
            GOPage = 0
            while GOPage <= 100:
                headers = {
                'User-Agent': str(smartagent)
                }
                response = requests.get("https://www.google.com/search?q=site:"+url+" filetype:"+default_filetype+"&start="+str(GOPage), headers=headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                if 'Your client does not have permission' in str(soup):
                    print('''\u001b[31mGoogle has completely blocked the request
                    and it is not possible to continue scanning automatically.\u001b[37m''')
                    sys.exit()
                if 'Our systems have detected unusual traffic from your computer' in str(soup):
                    print('\u001b[31mGoogle detected the tool, this has an effect on the answers\u001b[37m')
                    googlecaptcha = input('Do you want to continue? (y=Yes/n=No): ')
                    if 'n' in googlecaptcha:
                        sys.exit()
                    else:
                        #one day found a way to bypass google captcha
                        pass
                if 'did not match any documents.' in str(soup):
                    print('\u001b[32mScan Complete\u001b[37m')
                    sys.exit()
                links = soup.find_all("a")
                for link in links:
                    if link.string == None:
                        if '://' in str(link.get("href")):
                            answer=(link.get("href"))
                            result = re.search('q=(.*)&sa=', answer)
                            if result == None:
                                print('I did not find any links')
                            else:
                                urldecode = urllib.parse.unquote(result.group(1))
                                print('\nLink: '+str(urldecode))
                                f = open(ScanFile, 'a' )
                                f.write('\nLink: '+str(urldecode))
                                f.close()    
                GOPage += 10
                print('\u001b[32m-----------[Google Page '+str(GOPage/10),' END]----------\u001b[37m')
    if '2' in subm1:
        if '2' in subm2:
            getdorkinfo()
            print('You have selected Advance dork with manual scan.')
            print('You can open the following links in your browser with the control key + left click\u001b[37m')
            print('\u001b[32m----------[File Type All in One Dork]----------\u001b[37m')
            print('https://www.google.com/search?q=site:'+url+'%20filetype:'+filetype+'%20intext:'+intext+'%20inurl:'+inurl+'%20intitle:'+intitle)
            print('\u001b[32m..........[File Type Small Dork].........\u001b[37m')
            print('https://www.google.com/search?q=site:'+url+'%20filetype:'+filetype+'%20intext:'+intext)
            print('https://www.google.com/search?q=site:'+url+'%20filetype:'+filetype+'%20intext:password | intext:username | intext:email | intext:phone')
            print('https://www.google.com/search?q=site:'+url+'%20inurl:'+inurl)
            print('https://www.google.com/search?q=site:'+url+'%20inurl:'+inurl+'%20intext:'+intext)
            print('https://www.google.com/search?q=site:'+url+'%20inurl:'+inurl+'%20intitle:'+intitle)
            print('https://www.google.com/search?q=site:'+url+'%20inurl:'+filetype+'%20intext:'+intext)
            print('\u001b[32m----------[Cached Page Dork]----------\u001b[37m')
            print('https://www.google.com/search?q=cached:'+url)
        if '1' in subm2:
            getdorkinfo()
            Advance_loop = [url+' filetype:'+filetype,
            url+' filetype:'+filetype+' intext:'+intext,
            url+' filetype:'+filetype+' intitle:'+intitle,
            url+' filetype:'+filetype+' intext:'+intext+' intitle:'+intitle,
            url+' inurl:'+inurl,
            url+' inurl:'+inurl+' intext:'+intext,
            url+' inurl:'+inurl+' intext:'+intext+' intitle:'+intitle,]
            GOPage = 0
            while GOPage <= 100:
                headers = {
                'User-Agent': str(smartagent)
                }
                for advloop in range(len(Advance_loop)):
                    response = requests.get("https://www.google.com/search?q=site:"+str(Advance_loop[advloop])+"&start="+str(GOPage), headers=headers)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    if 'Your client does not have permission' in str(soup):
                        print('''\u001b[31mGoogle has completely blocked the request
                        and it is not possible to continue scanning automatically.\u001b[37m''')
                        sys.exit()
                    if 'Our systems have detected unusual traffic from your computer' in str(soup):
                        print('\u001b[31mGoogle detected the tool, this has an effect on the answers\u001b[37m')
                        googlecaptcha = input('Do you want to continue? (y=Yes/n=No): ')
                        if 'n' in googlecaptcha:
                            sys.exit()
                        else:
                            #one day found a way to bypass google captcha
                            pass
                    if 'did not match any documents.' in str(soup):
                        print('\u001b[32mNo link found with this dork: '+str(Advance_loop[advloop])+'\u001b[37m')
                        pass
                    links = soup.find_all("a")
                    for link in links:
                        if link.string == None:
                            if '://' in str(link.get("href")):
                                answer=(link.get("href"))
                                result = re.search('q=(.*)&sa=', answer)
                                if result == None:
                                    print('I did not find any links')
                                else:
                                    urldecode = urllib.parse.unquote(result.group(1))
                                    print('\n\u001b[36mLink: '+str(urldecode))
                                    f = open(UserInputScan, 'a' )
                                    f.write('\nLink: '+str(urldecode))
                                    f.close()    
                    GOPage += 10
                    print('\u001b[32m-----------[Google Page '+str(GOPage/10),' END]----------\u001b[37m')
            print('\u001b[32mScan Complete\u001b[37m')
    else:
        print('Wrong Number')
        sys.exit()


clsdis()
rules()
collect()
update()
clsdis()
banner()
global url,UserInputScan
print('Example: site.com mysite.com ac.ir edu.com')
url = input('\u001b[36mEnter the site address: \u001b[37m')
print('\nWARNING: If the name you entered already exists, the file will be overwritten.')
print('Example: site.txt mysite.txt')
UserInputScan = input('\u001b[36mEnter a name for Scan file: \u001b[37m')
menu()
RunScan()


