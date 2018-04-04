# -*- coding: utf-8 -*-
# Thanks to Ghost Team & One Piece Team
# Fix and remake by Alevan
#Jangan hapus ini, hargai creator

from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

#buat login via qr, yg lainnya buat sendiri
#ale = LINE()
#ale.log("Auth Token : " + str(ale.authToken))
#ale.log("Timeline Token : " + str(ale.tl.channelAccessToken))

ale = LINE("ErrMqVsRNiedypad4lnc.wAsBzKxje3PMXUvNCCeata.UXQRz4DmuOex3Wgv7/I/z76aQbvdN/4RbUxISojaNI8=")
ale.log("Auth Token : " + str(ale.authToken))
ale.log("Timeline Token : " + str(ale.tl.channelAccessToken) + "\n")

ale1 = LINE("ErrMqVsRNiedypad4lnc.wAsBzKxje3PMXUvNCCeata.UXQRz4DmuOex3Wgv7/I/z76aQbvdN/4RbUxISojaNI8=")
ale1.log("Auth Token : " + str(ale1.authToken))
ale1.log("Timeline Token : " + str(ale1.tl.channelAccessToken) + "\n")

ale2 = LINE("ErrMqVsRNiedypad4lnc.wAsBzKxje3PMXUvNCCeata.UXQRz4DmuOex3Wgv7/I/z76aQbvdN/4RbUxISojaNI8=")
ale2.log("Auth Token : " + str(ale2.authToken))
ale2.log("Timeline Token : " + str(ale2.tl.channelAccessToken) + "\n")

ale3 = LINE("ErrMqVsRNiedypad4lnc.wAsBzKxje3PMXUvNCCeata.UXQRz4DmuOex3Wgv7/I/z76aQbvdN/4RbUxISojaNI8=")
ale3.log("Auth Token : " + str(ale3.authToken))
ale3.log("Timeline Token : " + str(ale3.tl.channelAccessToken) + "\n")

ale4 = LINE("ErrMqVsRNiedypad4lnc.wAsBzKxje3PMXUvNCCeata.UXQRz4DmuOex3Wgv7/I/z76aQbvdN/4RbUxISojaNI8=")
ale4.log("Auth Token : " + str(ale4.authToken))
ale4.log("Timeline Token : " + str(ale4.tl.channelAccessToken))

# Helo hanya beberapa ditulis, belom ditulis semua
#edit sendiri yak:'v
helpMessage ="""╔═══════════════╗
║          ALEVAN           ║
╚═══════════════╝
╔═══════════════╗
║   Menu For Public    ║
╠═══════════════╝
╠ Adminlist
╠ Ownerlist
╠ Info Group
╠ Welcome
╠ Creator
╠ Bot
╠══════════════╗
║  Menu For Admin  ║
╠══════════════╝
╠ Cancel
╠ 「Buka/Tutup」qr
╠ Mid Bot
╠ Speed/Sp
╠ 「Cctv/Ciduk」
╠ Status/Set
╠ Gurl
╠ Jam「On/Off」
╠ Tag all/Tagall
╠ Absen/Respon
╠ Banlist
╚════════════════
╔═══════════════╗
║      P R O T E C T      ║
╚═══════════════╝"""

oepoll = OEPoll(ale)
KAC=[ale,ale1,ale2,ale3,ale4]
mid = ale.getProfile().mid
Amid = ale1.getProfile().mid
Bmid = ale2.getProfile().mid
Cmid = ale3.getProfile().mid
Dmid = ale4.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid]
admin=["u136360f65010efb7f8dcad362cb2c3cc",""] 
owner=["u136360f65010efb7f8dcad362cb2c3cc",""]
whitelist=[""]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""╔═══════════════╗
║          ALEVAN           ║
╚═══════════════╝
 ◄    Open Sewa
╔═══════════════╗
╠ VPS.                          ║
╠ SelfBot.                     ║
╠ Bot Protect               ║
╚═══════════════╝
Minat?
http://line.me/ti/p/~shandiap""",
    "lang":"JP",
    "comment":"Lb ke #punyaalevan",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cName2":"",
    "cName3":"",
    "cName4":"",
    "cName5":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "autoLeave":True,
    "Protectjoin":False,
    "Protectgr":True,
    "Protectcancl":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    years, month = divmod(month,12)
    return '\n╠▶ %02d Years \n╠▶ %02d Month\n╠▶ %02d Days\n╠▶ %02d нσυяѕ\n╠▶ %02d мιиυтє\n╠▶ %02d ѕє¢σи∂」' %(years, month, days ,hours, mins,secs)
    
def logError(text):
    ale.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@alevan "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
        ale.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                ale.findAndAddContactsByMid(op.param1)
                sendMention(op.param1, "Halo @! , \nTerimakasih telah menambahkan saya sebagai teman :3")
                ale.sendText(op.param1,str(wait["message"]))

#======================================================================================================#

        if op.type == 11:
          if wait["Protectgr"] == True:
            if ale.getGroup(op.param1).preventedJoinByTicket == False:
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                try:
                  ale.sendText(op.param1,ale.getContact(op.param2).displayName + " Jangan Buka Kode QR Njiiir")
                  ale.kickoutFromGroup(op.param1,[op.param2])
                  X = ale.getGroup(op.param1)
                  X.preventedJoinByTicket = True
                  ale.updateGroup(X)
                except:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Jangan Buka Kode QR Njiiir")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  Z = random.choice(KAC).getGroup(op.param1)
                  Z.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(Z)

#======================================================================================================#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = ale.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
              random.choice(KAC).sendText(op.param1, random.choice(KAC).getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner😛")

#======================================================================================================#

#========================================================================================================#
        if op.type == 32:
          if wait["Protectcancel"] == True:
            if op.param2 not in admin:
              if op.param2 in Bots or admin:
                pass
              else:
                random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Canceled Invitation")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                time.sleep(0.00001)
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True


#==================================================================#
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or admin:
                  ale.acceptGroupInvitation(op.param1)
                  ale.sendMention(op.param1, "Halo @!, Terimakasih Udah Invite Ale")
                else:
                  ale.rejectGroupInvitation(op.param1)
                  ale.sendMention(op.param1, "Halo @!, Terimakasih Udah Invite Ale")


            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ale1.acceptGroupInvitation(op.param1)
                else:
                  ale1.rejectGroupInvitation(op.param1)
                
            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ale2.acceptGroupInvitation(op.param1)
                else:
                  ale2.rejectGroupInvitation(op.param1)
                
            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ale3.acceptGroupInvitation(op.param1)
                else:
                  ale3.rejectGroupInvitation(op.param1)
                
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ale4.acceptGroupInvitation(op.param1)
                else:
                  ale4.rejectGroupInvitation(op.param1)
                    

#======================================================================================================#
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if mid in op.param3:
                if settings["autoJoin"] == True:
                    ale.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "Halo @! , \nTerimakasih Udah Invite Ale")

        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                sendMention(op.param1, "Oi @! , \nUdah ijin blom kalo mo invite??")
                ale.leaveRoom(op.param1)
#======================================================================================================#
        if op.type == 17: #Protect Join
          if wait["Protectjoin"] == True:
            if wait["blacklist"][op.param2] == True:
              ale.sendText(op.param1,ale.getContact(op.param2).displayName + " On Blacklist Boss\nWe Will Kick")
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              time.sleep(0.00001)
            else:
              pass
#======================================================================================================#

        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            try:
              ale.kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
              ale.inviteIntoGroup(op.param1,[op.param3])
            except:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19: #bot Ke Kick
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or admin:
                try:
                  G = ale1.getGroup(op.param1)
                  ale2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ale2.updateGroup(G)
                  Ticket = ale2.reissueGroupTicket(op.param1)
                  ale1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ale2.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ale1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Bmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ale3.getGroup(op.param1)
                  ale3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ale3.updateGroup(G)
                  Ticket = ale3.reissueGroupTicket(op.param1)
                  ale2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ale3.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ale2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Cmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ale4.getGroup(op.param1)
                  ale4.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ale4.updateGroup(G)
                  Ticket = ale4.reissueGroupTicket(op.param1)
                  ale3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ale4.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ale3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Dmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ale.getGroup(op.param1)
                  ale.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ale.updateGroup(G)
                  Ticket = ale.reissueGroupTicket(op.param1)
                  ale4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ale.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ale4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in admin:
              if op.param2 not in Bots:
                try:
                  ale.kickoutFromGroup(op.param1,[op.param2])
                  ale.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  try:
                    ale.kickoutFromGroup(op.param1,[op.param2])
                    ale.inviteIntoGroup(op.param1,[admin])
                    wait["blacklist"][op.param2] = True
                  except:
                    try:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                      wait["blacklist"][op.param2] = True
#=======================================================================
        if op.type == 19: #admin dan staff
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
            try:
              if op.param3 in admin:
                if op.param2 not in Bots or owner:
                  if op.param2 in Bots:
                    pass
                  elif op.param2 in owner:
                    pass
                  else:
                    try:
                      ale.kickoutFromGroup(op.param1,[op.param2])
                      time.sleep(0.00001)
                      ale1.kickoutFromGroup(op.param1,[op.param2])
                      time.sleep(0.00001)
                      ale2.kickoutFromGroup(op.param1,[op.param2])
                      time.sleep(0.00001)
                      ale3.kickoutFromGroup(op.param1,[op.param2])
                      time.sleep(0.00001)
                      ale4.kickoutFromGroup(op.param1,[op.param2])
                      time.sleep(0.00001)
                      ale.inviteIntoGroup(op.param1,[op.param3])
                      time.sleep(0.00001)
                      ale1.inviteIntoGroup(op.param1,[op.param3])
                      time.sleep(0.00001)
                      ale2.inviteIntoGroup(op.param1,[op.param3])
                      time.sleep(0.00001)
                      ale3.inviteIntoGroup(op.param1,[op.param3])
                      time.sleep(0.00001)
                      ale4.inviteIntoGroup(op.param1,[op.param3])
                      time.sleep(0.00001)
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).getGroup(op.param1)
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      time.sleep(0.00001)
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    
              elif op.param3 in staff:
                if op.param2 not in Bots or admin:
                  try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    time.sleep(0.00001)
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).getGroup(op.param1)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    time.sleep(0.00001)
                    wait["blacklist"][op.param2] = True
            except:
              try:
                ale.kickoutFromGroup(op.param1,[op.param2])
                time.sleep(0.00001)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                time.sleep(0.00001)
                wait["blacklist"][op.param2] = True
#=============================================================

        if op.type == 22:
            if wait["leaveRoom"] == True:
                ale.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ale.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ale.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ale.like(url[25:58], url[66:], likeType=1001)
                ale1.like(url[25:58], url[66:], likeType=1001)
                ale2.like(url[25:58], url[66:], likeType=1001)
                ale3.like(url[25:58], url[66:], likeType=1001)
                ale4.like(url[25:58], url[66:], likeType=1001)
                ale.comment(url[25:58], url[66:], wait["comment"])
                
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ale.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ale.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ale.sendText(msg.to,"Deleted")
                        wait["dblack"] = False
                   else:
                        wait["dblack"] = False
                        ale.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ale.sendText(msg.to,"Already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ale.sendText(msg.to,"Aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ale.sendText(msg.to,"Deleted")
                        wait["dblacklist"] = False
                   else:
                        wait["dblacklist"] = False
                        ale.sendText(msg.to,"It is not in the black list")

               elif wait["contact"] == True:
                    msg.contentType = 0
                    ale.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ale.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ale.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ale.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = ale.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ale.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ale.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                        ale.sendText(msg.to,msg.text)

            elif msg.text is None:
                return

            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    ale.sendText(msg.to,helpMessage)
                else:
                    ale.sendText(msg.to,helpt)

            elif ("Gn " in msg.text):
              if msg._from in admin:
                if msg.toType == 2:
                    X = ale.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    ale.updateGroup(X)
                else:
                    ale.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick " in msg.text:
              if msg._from in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])

            elif "Invite " in msg.text:
              if msg._from in admin:
                midd = msg.text.replace("Invite ","")
                ale.findAndAddContactsByMid(midd)
                ale.inviteIntoGroup(msg.to,[midd])

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Admin add @" in msg.text:
              if msg._from in owner:
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = ale.getGroup(msg.to)
                gs = ale1.getGroup(msg.to)
                gs = ale2.getGroup(msg.to)
                gs = ale3.getGroup(msg.to)
                gs = ale4.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            ale.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
              else:
                ale.sendText(msg.to,"Perintah Ditolak.")
                ale.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif "Admin remove @" in msg.text:
              if msg._from in owner:
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ale.getGroup(msg.to)
                gs = ale1.getGroup(msg.to)
                gs = ale2.getGroup(msg.to)
                gs = ale3.getGroup(msg.to)
                gs = ale4.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ale.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
              else:
                ale.sendText(msg.to,"Perintah Ditolak.")
                ale.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  ale.sendText(msg.to,"The stafflist is empty")
              else:
                  ale.sendText(msg.to,"Tunggu...")
                  mc = "||Admin Ghost Team||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +ale.getContact(mi_d).displayName + "\n"
                  ale.sendText(msg.to,mc)

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg._from in owner:
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = ale.getGroup(msg.to)
                  gs = ale1.getGroup(msg.to)
                  gs = ale2.getGroup(msg.to)
                  gs = ale3.getGroup(msg.to)
                  gs = ale4.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        ale.findAndAddContactsByMid(target)
                        ale1.findAndAddContactsByMid(target)
                        ale2.findAndAddContactsByMid(target)
                        ale3.findAndAddContactsByMid(target)
                        ale4.findAndAddContactsByMid(target)
                      except:
                        ale.sendText(msg.to,"Error")
              else:
                ale.sendText(msg.to,"Perintah Ditolak.")                
                ale.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Allbio:" in msg.text:
              if msg._from in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ale.getProfile()
                    profile.statusMessage = string
                    ale.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ale1.getProfile()
                    profile.statusMessage = string
                    ale1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ale2.getProfile()
                    profile.statusMessage = string
                    ale2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ale3.getProfile()
                    profile.statusMessage = string
                    ale3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ale4.getProfile()
                    profile.statusMessage = string
                    ale4.updateProfile(profile)
                    ale.sendText(msg.to,"Bio berubah menjadi " + string + "")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Spam: " in msg.text:
              if msg._from in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           ale.sendText(msg.to, teks)
                    else:
                       ale.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        ale.sendText(msg.to, tulisan)
                    else:
                        ale.sendText(msg.to, "Kelebihan batas :v")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg._from}
                random.choice(KAC).sendMessage(msg)

            elif msg.text in ["Cancel","cancel"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ale.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ale.sendText(msg.to,"No one is inviting")
                        else:
                            ale.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ale.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Cancel all","Bot cancel"]:
              if msg._from in admin:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Buka qr","Open qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
              else:
                ale.sendText(msg.to,"Perintah Ditolak.")
                ale.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")

            elif msg.text in ["Tutup qr","Close qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventedJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
              else:
                ale.sendText(msg.to,"Perintah Ditolak.")
                ale.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")

            elif "Info group" == msg.text:
              if msg.toType == 2:
                if msg._from in admin:
                  ginfo = ale.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventedJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    ale.sendText(msg.to,"Can not be used outside the group")
                  else:
                    ale.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
              if msg._from in admin:
                random.choice(KAC).sendText(msg.to, msg._from)

            elif msg.text in ["Cancel on","cancel on"]:
              if msg._from in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        ale.sendText(msg.to,"done")

            elif msg.text in ["Cancel off","cancel off"]:
              if msg._from in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        ale.sendText(msg.to,"done")

            elif msg.text in ["Qr on","qr on"]:
              if msg._from in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Protect QR On")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Protect QR On")
                    else:
                        ale.sendText(msg.to,"done")

            elif msg.text in ["Qr off","qr off"]:
              if msg._from in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Protect QR Off")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Protect QR Off")
                    else:
                        ale.sendText(msg.to,"done")

            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg._from in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        ale.sendText(msg.to,"done")

            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg._from in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        ale.sendText(msg.to,"done")

            elif msg.text in ["Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg._from in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already on")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already on")
                    else:
                        ale.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg._from in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already off")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already off")
                    else:
                        ale.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            ale.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            ale.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            ale.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            ale.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Value is wrong")
                    else:
                        ale.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg._from in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already on")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg._from in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already off")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg._from in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already on")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg._from in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already off")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","Set"]:
              if msg._from in admin:
                md = "⭐Status Proteksi⭐\n*============*\n"
                if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
                if wait["contact"] == True: md+="[•]Contact [On]\n"
                else: md+="[•]Contact [Off]\n"
                if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[•]Auto Leave [On]\n"
                else: md+=" Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="[•]Share [On]\n"
                else:md+="[•]Share [Off]\n"
                if wait["autoAdd"] == True: md+="[•]Auto Add [On]\n"
                else:md+="[•]Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="[•]Comment [On]\n"
                else:md+="[•]Comment [Off]\n*============*\n✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰⭐\n*============*"
                ale.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = ale.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"There is no album")
                    else:
                        ale.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    ale.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = ale.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"There is no album")
                    else:
                        ale.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = ale.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        ale.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    ale.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    ale.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = ale.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (ale.getGroup(i).name,i)
                ale.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg._from in admin:
                gid = ale.getGroupIdsInvited()
                for i in gid:
                    ale.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ale.sendText(msg.to,"All invitations have been refused")
                else:
                    ale.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = ale.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        ale.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    ale.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    ale.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg._from in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already on")
                    else:
                        ale.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Done")
                    else:
                        ale.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg._from in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"already off")
                    else:
                        ale.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                ale.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    ale.sendText(msg.to,"message changed")
                else:
                    ale.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    ale.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    ale.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    ale.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    ale.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    ale.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    ale.sendText(msg.to,"changed\n\n" + c)

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "/invitemeto: " in msg.text:
              if msg._from in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  ale.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ale.findAndAddContactsByMid(msg._from)
                    ale.inviteIntoGroup(gid,[msg._from])
                  except:
                    ale.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg._from in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
              if msg._from in admin:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"done")
                    else:
                        ale.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                ale.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg._from in admin:
                if msg.toType == 2:
                    x = ale.getGroup(msg.to)
                    if x.preventedJoinByTicket == True:
                        x.preventedJoinByTicket = False
                        ale.updateGroup(x)
                    gurl = ale.reissueGroupTicket(msg.to)
                    ale.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Can't be used outside the group")
                    else:
                        ale.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                ale.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                ale.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    ale.sendText(msg.to,"confirmed")
                else:
                    ale.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +ale.getContact(mi_d).displayName + "\n"
                    ale.sendText(msg.to,mc)

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Jam on"]:
              if msg._from in admin:
                if wait["clock"] == True:
                    ale3.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = ale3.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    ale3.updateProfile(profile)
                    ale3.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg._from in admin:
                if wait["clock"] == False:
                    ale3.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    ale3.sendText(msg.to,"Jam Sedang Off")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    ale.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    ale.sendText(msg.to,"changed to\n\n" + n)

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = ale3.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    ale3.updateProfile(profile)
                    ale3.sendText(msg.to,"Sukses update")
                else:
                    ale3.sendText(msg.to,"Aktifkan jam terlebih dulu")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text == "Cctv":
              if msg._from in admin:
                ale.sendText(msg.to, "Cek CCTV")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
              
            elif msg.text == "Ciduk":
                 if msg._from in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        ale.sendText(msg.to, "╔═════════════\n║👀Seen By👀%s\n╠═════[Result]═════\n║👀The Siders👀\n%s║Pray For Sider Sick Strooke\n║[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        ale.sendText(msg.to, "Ketik Cctv dulu\nBaru Ketik Ciduk\nDASAR PIKUN ♪")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Kuy"]: #Panggil Semua Bot
              if msg._from in owner:
                G = ale.getGroup(msg.to)
                ginfo = ale.getGroup(msg.to)
                G.preventedJoinByTicket = False
                ale.updateGroup(G)
                invsend = 0
                Ticket = ale.reissueGroupTicket(msg.to)
                ale1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ale2.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ale3.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ale4.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = ale.getGroup(msg.to)
                ginfo = ale.getGroup(msg.to)
                G.preventedJoinByTicket = True
                ale.updateGroup(G)

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Kabur all","Kaboor all"]: #Bot Ninggalin Group termasuk Bot Induk
              if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ale.getGroup(msg.to)
                    try:
                        ale1.leaveGroup(msg.to)
                        ale2.leaveGroup(msg.to)
                        ale3.leaveGroup(msg.to)
                        ale4.leaveGroup(msg.to)
                        ale.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["Kaboor"]: #Semua Bot Ninggalin Group Kecuali Bot Induk
              if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ale.getGroup(msg.to)
                    try:
                        ale1.leaveGroup(msg.to)
                        ale2.leaveGroup(msg.to)
                        ale3.leaveGroup(msg.to)
                        ale4.leaveGroup(msg.to)
                    except:
                        pass

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#
            elif msg.text in ['mention']:
                group = client.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                k = len(nama)//100
                for a in range(k+1):
                    txt = u''
                    s=0
                    b=[]
                    for i in group.members[a*100 : (a+1)*100]:
                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                        s += 7
                        txt += u'@alevan \n'
                    ale.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    ale4.sendMessage(to, "Total {} Mention".format(str(len(nama))))  
#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Bot Like", "Bot like"]:
              if msg._from in owner:
                ale.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like temen", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg._from in owner:
                ale.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                ale.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  autolike()
                except:
                  pass

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Kill "]:
              if msg._from in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                        except:
                            pass

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Ready op" in msg.text:
              if msg._from in owner:
                if msg.toType == 2:
                    _name = msg.text.replace("Ready op","")
                    gs = ale.getGroup(msg.to)
                    gs = ale1.getGroup(msg.to)
                    gs = ale2.getGroup(msg.to)
                    gs = ale3.getGroup(msg.to)
                    gs = ale4.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"Eh Kontol Ini Room apaan?")
                    random.choice(KAC).sendText(msg.to,"Ratain aja lah\nRoom Ga Berguna..")
                    random.choice(KAC).sendText(msg.to,"Jangan Baper yah Tollll;")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target in Bots:
                            pass
                          elif target in admin:
                            pass
                          else:
                            try:
                              klist=[cl,ki,kk,kc,ks]
                              kicker=random.choice(klist)
                              kicker.kickoutFromGroup(msg.to,[target])
                            except:
                              random.choice(KAC).kickoutFromGroup(msg.to,[target])
                              random.choice(KAC).sendText(msg.to,"Koq Ga Ditangkis Njiiing?\nLemah Banget Nih Room")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Nk " in msg.text:
              if msg._from in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                targets = []
                for s in gs.members:
                  if _name in s.displayName:
                    targets.append(s.mid)
                if targets == []:
                  sendMessage(msg.to,"user does not exist")
                  pass
                else:
                  for target in targets:
                    try:
                      ale.kickoutFromGroup(msg.to,[target])
                    except:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Blacklist @ " in msg.text:
              if msg._from in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Banned @" in msg.text:
              if msg._from in admin:
                if msg.toType == 2:
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ale.getGroup(msg.to)
                    gs = ale1.getGroup(msg.to)
                    gs = ale2.getGroup(msg.to)
                    gs = ale3.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ale.sendText(msg.to,"Dilarang Banned Bot")
                        ale1.sendText(msg.to,"Dilarang Banned Bot")
                        ale2.sendText(msg.to,"Dilarang Banned Bot")
                        ale3.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Mid @" in msg.text:
              if msg._from in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = ale.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Unban @" in msg.text:
              if msg._from in admin:
                if msg.toType == 2:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ale.getGroup(msg.to)
                    gs = ale1.getGroup(msg.to)
                    gs = ale2.getGroup(msg.to)
                    gs = ale3.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ale.sendText(msg.to,"Tidak Ditemukan.....")
                        ale1.sendText(msg.to,"Tidak Ditemukan.....")
                        ale2.sendText(msg.to,"Tidak Ditemukan.....")
                        ale3.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ale.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ale1.sendText(msg.to,"Error")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg._from in admin:
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ale1.sendText(msg.to,"P 􀔃􀆶squared up!����")
                ale2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif "Bc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg._from in owner:
                bctxt = msg.text.replace("Bc ","")
                a = ale.getGroupIdsJoined()
                a = ale1.getGroupIdsJoined()
                a = ale2.getGroupIdsJoined()
                a = ale3.getGroupIdsJoined()
                a = ale4.getGroupIdsJoined()
                for taf in a:
                  ale.sendText(taf, (bctxt))
                  ale1.sendText(taf, (bctxt))
                  ale2.sendText(taf, (bctxt))
                  ale3.sendText(taf, (bctxt))
                  ale4.sendText(taf, (bctxt))

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["LG"]: #Melihat List Group
              if msg._from in admin:
                gids = ale.getGroupIdsJoined()
                h = ""
                for i in gids:
                  h += "[•]%s Member\n" % (ale.getGroup(i).name   +"👉"+str(len(ale.getGroup(i).members)))
                  ale.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Bot out","Op bye"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg._from in owner:
                gid = ale.getGroupIdsJoined()
                gid = ale1.getGroupIdsJoined()
                gid = ale2.getGroupIdsJoined()
                gid = ale3.getGroupIdsJoined()
                gid = ale4.getGroupIdsJoined()
                for i in gid:
                  ale4.leaveGroup(i)
                  ale3.leaveGroup(i)
                  ale1.leaveGroup(i)
                  ale2.leaveGroup(i)
                  ale.leaveGroup(i)
                if wait["lang"] == "JP":
                  ale.sendText(msg.to,"Sayonara")
                else:
                  ale.sendText(msg.to,"He declined all invitations")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Op katakan hi"]:
                ale1.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ale2.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ale3.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say hinata pekok"]:
                ale1.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ale2.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ale3.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                ale1.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                ale2.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                ale3.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ale1.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                ale2.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                ale3.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ale1.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                ale2.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                ale3.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ale1.sendText(msg.to,"Selamat datang di Group Kami")
                ale2.sendText(msg.to,"Jangan nakal ok!")
            elif msg.text in ["PING","Ping","ping"]:
                ale1.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ale2.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ale3.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Absen","Absen bot","Absen dulu","Respon"]:
              if msg._from in admin:
                ale.sendText(msg.to,"Tukang Sayur On")
                ale1.sendText(msg.to,"Tukang Colli On")
                ale2.sendText(msg.to,"Tukang Boker On")
                ale3.sendText(msg.to,"Tukang Becak On")
                ale4.sendText(msg.to,"Tukang Boong")
                ale.sendText(msg.to,"Semua Udah Hadir Boss\nSiap Protect Group\nAman Gak Aman Yang Penting Anu")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ale1.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Speed","Sp"]:
#              if msg._from in admin:
                start = time.time()
                ale.sendText(msg.to, "Menghitung...")
                elapsed_time = time.time() - start
                ale.sendText(msg.to, "%s Detik" % (elapsed_time))

#======================================================================================================#
            elif msg.text in ["Restart"]:
              if msg._from in admin:
                ale.sendMessage(to, "Berhasil merestart Bot")
                restartBot()
#======================================================================================================#
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "║「вσт яυииιиg "+waktu(eltime)
                ale.sendText(msg.to,"╔═════════════════\n║ ☆☞ UNITY RUNTIME ☆\n╠════════════════\n" + van + "\n╚════════════════")
#======================================================================================================#

            elif msg.text in ["Ban"]:
              if msg._from in owner:
                wait["wblacklist"] = True
                ale.sendText(msg.to,"Kirim contact")

            elif msg.text in ["Unban"]:
              if msg._from in owner:
                wait["dblacklist"] = True
                ale.sendText(msg.to,"Kirim contact")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'ued156c86ffa56024c0acba16f7889e6d'}
              ale.sendText(msg.to,"======================")
              ale.sendMessage(msg)
              ale.sendText(msg.to,"======================")
              ale.sendText(msg.to,"Itu Creator Kami Yang Pea 😜")

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 ale.sendText(msg.to,psn)

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Banlist"]:
              if msg._from in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ale.getContact(mi_d).displayName + "\n"
                    ale.sendText(msg.to,mc)

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

            elif msg.text in ["Cek ban"]:
              if msg._from in admin:
                if msg.toType == 2:
                    group = ale.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg._from in admin:
                if msg.toType == 2:
                    group = ale.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg._from in admin:
                if msg.toType == 2:
                    group = ale.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ale.cancelGroupInvitation(msg.to,[_mid])
                    ale.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg._from in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = ale.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            ale.updateGroup(group)
                    except:
                        ale.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    ale.createAlbum(gid,name)
                    ale.sendText(msg.to,name + "created an album")
                except:
                    ale.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    ale.sendText(msg.to,str(ale.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        ale.sendText(msg.to,str(e))
                    except:
                        pass

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = ale.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              ale.sendText
          except:
             pass

#======================================================================================================#
#======================================================================================================#
#======================================================================================================#

        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = ale.getGroup(op.param1)
          random.choice(KAC).sendText(op.param1, "Selamat Datang")
        if op.type == 15:
          if op.param2 in Bots:
             return
          random.choice(KAC).sendText(op.param1, "Selamat Jalan")
#------------------------
        if op.type == 59:
            print ("op")


    except Exception as error:
        print ("error")


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,500):
      hasil = ale.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          ale.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ale.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"╔════════════╗\n     ✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰\n╚════════════╝\n══════════════\n ◄]·♦·Open Sewa·♦·[►\n╔═════════════\n╠ VPS\n╠ SelfBot\n╠ Bot Protect\n╚═════════════\nMinat?\nhttp://line.me/ti/p/~iiipuuul")
          ale1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ale1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"╔════════════╗\n     ✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰\n╚════════════╝\n══════════════\n ◄]·♦·Open Sewa·♦·[►\n╔═════════════\n╠ VPS\n╠ SelfBot\n╠ Bot Protect\n╚═════════════\nMinat?\nhttp://line.me/ti/p/~iiipuuul")
          ale2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ale2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"╔════════════╗\n     ✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰\n╚════════════╝\n══════════════\n ◄]·♦·Open Sewa·♦·[►\n╔═════════════\n╠ VPS\n╠ SelfBot\n╠ Bot Protect\n╚═════════════\nMinat?\nhttp://line.me/ti/p/~iiipuuul")
          ale3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ale3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"╔════════════╗\n     ✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰\n╚════════════╝\n══════════════\n ◄]·♦·Open Sewa·♦·[►\n╔═════════════\n╠ VPS\n╠ SelfBot\n╠ Bot Protect\n╚═════════════\nMinat?\nhttp://line.me/ti/p/~iiipuuul")
          ale4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ale4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"╔════════════╗\n     ✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰\n╚════════════╝\n══════════════\n ◄]·♦·Open Sewa·♦·[►\n╔═════════════\n╠ VPS\n╠ SelfBot\n╠ Bot Protect\n╚═════════════\nMinat?\nhttp://line.me/ti/p/~iiipuuul")
          ale.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"╔════════════╗\n     ✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰\n╚════════════╝\n══════════════\n ◄]·♦·Open Sewa·♦·[►\n╔═════════════\n╠ VPS\n╠ SelfBot\n╠ Bot Protect\n╚═════════════\nMinat?\nhttp://line.me/ti/p/~iiipuuul")
          print ("Like")
        except:
          pass
      else:
          print ("Already Liked")
time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,500):
        hasil = ale.activity(limit=500)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    ale.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ale1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ale2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ale3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ale4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ale.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like")
                    ale.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like")
                    print ("Like")
                except:
                    pass
            else:
                print ("Status Sudah di Like")
                
def nameUpdate():
    while True:
        try:
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = ale.getProfile()
                profile.displayName = wait["cName"]
                ale.updateProfile(profile)

                profile2 = ale1.getProfile()
                profile2.displayName = wait["cName2"]
                ale1.updateProfile(profile2)

                profile3 = ale2.getProfile()
                profile3.displayName = wait["cName3"]
                ale2.updateProfile(profile3)

                profile4 = ale3.getProfile()
                profile4.displayName = wait["cName4"]
                ale3.updateProfile(profile4)

                profile5 = ale4.getProfile()
                profile5.displayName = wait["cName5"]
                ale4.updateProfile(profile5a)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
