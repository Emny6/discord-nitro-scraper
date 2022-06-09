import discum
import time 
import colorama
import os
from sty import fg

reset = colorama.Fore.RESET

os.system("cls")

text1 = f'''

          $$\      $$\  $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ 
          $$$\    $$$ |$$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ \____$$  |
          $$$$\  $$$$ |$$ /  $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|    $$  / 
          $$\$$\$$ $$ |$$ |  $$ |$$ |  $$ |$$ $$\$$ |\$$$$$$\     $$  /  
          $$ \$$$  $$ |$$ |  $$ |$$ |  $$ |$$ \$$$$ | \____$$\   $$  /   
          $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$\   $$ | $$  /    
          $$ | \_/ $$ | $$$$$$  | $$$$$$  |$$ | \$$ |\$$$$$$  |$$$$$$$$\ 
          \__|     \__| \______/  \______/ \__|  \__| \______/ \________|
                                                                 
                                                                 
                                                                 
                                                                 
                            [+] DISCORD NITRO SCRAPPER [+]
'''

text = text1.replace('$', f'{fg(240, 179, 255)}$').replace('\\', reset+'\\').replace('|', reset+'|').replace('/', reset+'/').replace('>', reset+'>')+reset

print(text)

token = str(input(f"{fg(255,0,0)}   [!] Token >> {reset}"))
guild_id = str(input(f"{fg(255,0,0)}   [!] Guild Id >> {reset}"))
channel_id = str(input(f"{fg(255,0,0)}   [!] Channel Id >> {reset}"))
print('\n\n')
bot = discum.Client(token= token, log=True)

bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since'],startIndex=0, method='overlap')
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' members fetched')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()


with open('ids.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            if "000" in disc or "0030" in disc or "0040" in disc or "1234" in disc or "0001" in disc or "0002" in disc or "0003" in disc or "0010" in disc or "0020" in disc or "0004" in disc or "0005" in disc or "0006" in disc or "0007" in disc or "0008" in disc or "0009" in disc or "1000" in disc or "2000" in disc or "3000" in disc or "4000" in disc or "5000" in disc or "6000" in disc or "7000" in disc or "8000" in disc or "9000" in disc or "1234" in disc or "4321" in disc or "0101" in disc or "1337" in disc or "1111" in disc or "2222" in disc or "3333" in disc or "4444" in disc or "5555" in disc or "6666" in disc or "7777" in disc or "8888" in disc or "9999" in disc or "2020" in disc or "2021" in disc or "2022" in disc or "1010" in disc or "2020" in disc or "3030" in disc or "4040" in disc or "5050" in disc or "6060" in disc or "7070" in disc or "8080" in disc or "9090" in disc or "0171" in disc or "1710" in disc or "0900" in disc:
                print(f'{fg(255,0,0)}{user}{fg(0,255,0)}#{reset}{disc}')
                file.write(f'{id}\n')