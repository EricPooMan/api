import time
import random
#123=stone,45=gold,67=diamond,8=ruby
gamemode=True
#PICKAXES
pickaxebuy=[{'Stone Pickaxe':'Rare','HV':5,'Cost':150,'Unit':'Coins'},{'Golden Pickaxe':'Rare','HV':5,'Cost':10,'Unit':'Gems'},
{'Ice Pickaxe':'Epic','HV':20,'Cost':600,'Unit':'Coins'},{'Diamond Pickaxe':'Epic','HV':50,'Cost':1500,'Unit':'Coins'},
{'Legend Pickaxe':'Legendary','HV':100,'Cost':1000,'Unit':'Gems'}]            
starterpickaxe={'Starter Pickaxe':'Common','HV':2}
pickaxes=[starterpickaxe]
pickaxesname=['starter pickaxe']
usingpickaxe={'Starter Pickaxe':'Common','HV':2}
stonepickaxe={'Stone Pickaxe':'Rare','HV':5,'Cost':150,'Unit':'Coins'}
goldpickaxe={'Golden Pickaxe':'Rare','HV':5,'Cost':10,'Unit':'Gems'}
icepickaxe={'Ice Pickaxe':'Epic','HV':20,'Cost':600,'Unit':'Coins'}
diamondpickaxe={'Diamond Pickaxe':'Epic','HV':50,'Cost':1500,'Unit':'Coins'}
legendpickaxe={'Legend Pickaxe':'Legendary','HV':500,'Cost':1000,'Unit':'Gems'}

#evolves
common=400
rare=800
epic=100
legendary=500
#Ores
diamond=0
ruby=0
stone=1
gold=0
coins=0
gems=0
diamondset={'HV':20}
rubyset={'HV':50}
stoneset={'HV':2}
goldset={'HV':5}
possibleOres=[1,2,3,4,5,6,7,8]
#setting
print("----------Miner Legend V 2.1----------")
time.sleep(0.5)
username=input("Please enter your username:")
print("\nHello,"+username+'!'+"I am your guider,Sam!")
time.sleep(2)
print("""\nThis is the basic rule in Miner Legend:
1.The system will ask you where do you want to go,you just answer.Type 'quit' to end the game.
2.Each pickaxe has different HV. HV is a unit in Miner Legend.
Different ores need different HV to mine.
3.In shop,you need coins or gems to but pickaxe.
LAST.Enjoy this game!""")
time.sleep(1)
print("""\n\n----------Latest Update----------
-The gold become priceless
-Diamonds can exchange more gems
-BUG fixed
""")
time.sleep(5)
print("\n\nLOADING......")
time.sleep(1.5)
print("\nHello,"+username+'!'+"I am your helper,Judy!")
#Helper set
while gamemode:
    
    time.sleep(1.5)
    ask=input("\nWhere do you want to go?(Type 'help' to see where you can go to, 'quit' to end the game)")
    #Help
    if ask=='help':
        print("""These are the places you can go to:
-inventory
-shop
-mining field
-money exchange
-pickaxe improve station""")
        time.sleep(3)
        print("You can type the  first letter of each word,\nExample:mining field into 'MF'")
        print()
        time.sleep(0.8)
        print("If you like to just type the name, you can.")
        time.sleep(0.5)
        continue
    #Inventory
    if ask=='inventory'or ask=='I':
        print("This is your inventory:")
        time.sleep(2)
        print()
        print("All pickaxes:")
        for i in pickaxes:
            print(i)
            print()
            time.sleep(0.5)
        time.sleep(1)
        print("Now using:")
        print()
        print(usingpickaxe)
        time.sleep(1)
        time.sleep(1)
        print("\nOre:"+str(stone)+' Stone,'+str(gold)+' Gold,'+str(diamond)+' Diamond,'+str(ruby)+' Ruby.')
        time.sleep(1)
        print("\nCoins:"+str(coins))
        time.sleep(1)
        print("\nGems:"+str(gems))
        time.sleep(3)
        ask=input("\n Do you want to switch a pickaxe?")
        if ask=='yes' or ask == 'Yes':
            ask=input("Which pickaxe do you want to switch to?(pickaxe name, no capitalize)")
            if ask in pickaxesname:
                if ask=='starter pickaxe':
                    usingpickaxe=starterpickaxe

                if ask=='stone pickaxe':
                    usingpickaxe=stonepickaxe

                if ask=='golden pickaxe':
                    usingpickaxe=goldpickaxe
                    
                if ask=='diamond pickaxe':
                    usingpickaxe=diamondpickaxe

                if ask=='legend pickaxe':
                    usingpickaxe=legendpickaxe
                print("\nYou have succesfully switched pickaxe!")
            else:
                print("Looks like you do not have that pickaxe...")
                time.sleep(1)
        ask=input("\nDo you want to go back?(Yes)")
        if ask=='yes'or ask=='Yes':
            continue
    #Quit system
    elif ask=='quit':
        ask=input("Are you sure you want to leave the game?(You will lost all your progress)")
        if ask=='Yes'or ask=='yes':
            gamemode=False
            quit()
        else:
            continue
    #Shop
    elif ask=='shop'or ask=='S':
        print("Hello bro!I am the shop keeper Grim!")
        time.sleep(1)
        print("Here's my pickaxes:")
        time.sleep(0.5)
        print()
        for i in pickaxebuy:
            if i not in pickaxes:
                print(i)
                print()
                time.sleep(0.5)
        ask=input("\nWhich pickaxe do you want to buy?")
        if ask=='stone pickaxe'or ask=='Stone Pickaxe':
            print("You have "+str(coins)+" coin(s).")
            time.sleep(0.5)
            print("The pickaxe cost:"+str(stonepickaxe['Cost'])+"Coins.")
            if coins>=int(stonepickaxe['Cost']):
                print("Deal!")
                pickaxesname.append('stone pickaxe')
                pickaxes.append(stonepickaxe)
                usingpickaxe=stonepickaxe
                coins-=int(stonepickaxe['Cost'])

            elif coins<int(stonepickaxe['Cost']):
                print("Oops,sorry that you did not have that much money...")
                ask=input("Do you want to go back?")
                if ask=='yes'or ask=='Yes':
                    continue
        elif ask=='golden pickaxe'or ask=='golden Pickaxe':
            print("You have "+str(gems)+" gem(s).")
            time.sleep(0.5)
            print("The pickaxe cost:"+str(goldpickaxe['Cost'])+" Gems.")
            if gems>=int(goldpickaxe['Cost']):
                print("Deal!")
                pickaxesname.append('golden pickaxe')
                pickaxes.append(goldpickaxe)
                usingpickaxe=goldpickaxe
                gems-=int(goldpickaxe['Cost'])

            elif coins<int(goldpickaxe['Cost']):
                print("Oops,sorry that you did not have that much money...")
                ask=input("Do you want to go back?")
                if ask=='yes'or ask=='Yes':
                    continue
        elif ask=='ice pickaxe'or ask=='Ice Pickaxe':
            print("You have "+str(coins)+" coin(s).")
            time.sleep(0.5)
            print("The pickaxe cost:"+str(icepickaxe['Cost'])+"Coins.")
            if coins>=int(icepickaxe['Cost']):
                print("Deal!")
                pickaxesname.append('ice pickaxe')
                pickaxes.append(icepickaxe)
                usingpickaxe=icepickaxe
                coins-=int(icepickaxe['Cost'])

            elif coins<int(icepickaxe['Cost']):
                print("Oops,sorry that you did not have that much money...")
                ask=input("Do you want to go back?")
                if ask=='yes'or ask=='Yes':
                    continue
        elif ask=='diamond pickaxe'or ask=='Diamond Pickaxe':
            print("You have "+str(coins)+" coin(s).")
            time.sleep(0.5)
            print("The pickaxe cost:"+str(diamondpickaxe['Cost'])+"Coins.")
            if coins>=int(diamondpickaxe['Cost']):
                print("Deal!")
                pickaxesname.append('diamond pickaxe')
                pickaxes.append(diamondpickaxe)
                usingpickaxe=diamondpickaxe
                coins-=int(diamondpickaxe['Cost'])

            elif coins<int(diamondpickaxe['Cost']):
                print("Oops,sorry that you did not have that much money...")
                ask=input("Do you want to go back?")
                if ask=='yes'or ask=='Yes':
                    continue
        elif ask=='legend pickaxe'or ask=='Legend Pickaxe':
            print("You have "+str(gems)+" gem(s).")
            time.sleep(0.5)
            print("The pickaxe cost:"+str(legendpickaxe['Cost'])+"Gems.")
            if gems>=int(legendpickaxe['Cost']):
                print("Deal!")
                pickaxesname.append('legend pickaxe')
                pickaxes.append(legendpickaxe)
                usingpickaxe=legendpickaxe
                gems-=int(legendpickaxe['Cost'])

            elif coins<int(legendpickaxe['Cost']):
                print("Oops,sorry that you did not have that much money...")
                ask=input("Do you want to go back?")
                if ask=='yes'or ask=='Yes':
                    continue
    #Money Exchange
    elif ask=='money exchange'or ask=='Money Exchange'or ask=='ME':
        print("\nYo!Who's there?I am the money exchanger Flash!")
        time.sleep(2)
        print("""\nLook at this:
1 stone = 20 coins
1 gold = 80 coins
1 diamond = 25 gems
1 ruby = 200 coins and 50 gems""")
        time.sleep(1)
        print("\nAnd you have "+str(stone)+' stone, '+str(gold)+' gold, '+str(diamond)+' diamond, '+str(ruby)+' ruby.')
        ask=input("Which type of ores you want to exchange?")
        if ask=='stone'or ask=='Stone':
              time.sleep(0.5)
              ask=input("\nHow much do you want to pay?")
              if int(stone)-int(ask)<0:
                  print("\nI am sorry that you don't have that much ores.")
                  time.sleep(0.5)
                  print("Go to mine some ores and come back.See you!")
                  continue
              coins+=int(ask)*20
              stone-=int(ask)
              time.sleep(0.4)              
              print("\nThanks a lot!See you next time!You have exchanged coins.")
              continue
        elif ask=='gold'or ask=='Gold':
              time.sleep(0.5)
              ask=input("\nHow much do you want to pay?")
              if int(gold)-int(ask)<0:
                  print("\nI am sorry that you don't have that much ores.")
                  time.sleep(0.5)
                  print("Go to mine some ores and come back.See you!")
                  continue
              coins+=int(ask)*80
              gold-=int(ask)
              time.sleep(0.4)              
              print("\nThanks a lot!See you next time!You have exchanged coins.")
              continue
        elif ask=='diamond'or ask=='Diamond':
              time.sleep(0.5)
              ask=input("\nHow much do you want to pay?")
              if int(diamond)-int(ask)<0:
                  print("\nI am sorry that you don't have that much ores.")
                  time.sleep(0.5)
                  print("Go to mine some ores and come back.See you!")
                  continue
              gems+=int(ask)*50
              diamond-=int(ask)
              time.sleep(0.4)
              print("\nThanks a lot!See you next time!You have exchanged gems.")
              continue
        elif ask=='ruby'or ask=='Ruby':
              time.sleep(0.5)
              ask=input("\nHow much do you want to pay?")
              if int(ruby)-int(ask)<0:
                  print("\nI am sorry that you don't have that much ores.")
                  time.sleep(0.5)
                  print("Go to mine some ores and come back.See you!")
                  continue
              gems+=int(ask)*25
              coins+=int(ask)*200
              ruby-=int(ask)
              time.sleep(0.4)
              print("\nThanks a lot!See you next time!You have exchanged coins and gems.")
              continue
    #Mining field
    elif ask=='mining field'or ask=='Mining Field'or ask=='MF':
        time.sleep(0.5)
        print('Hello there!Welcome to our mining field.My name is Finch.')
        time.sleep(1)
        ask=int(input("How many times do you want to mine?"))
        time.sleep(0.8)
        print("Ok,Let's start mining now!")
        time.sleep(1)
        for i in range(ask):
            split=random.randint(1,len(possibleOres))
            blizzard=random.randint(1,8)
            if split==1 or split==2 or split==3:
                print("\nYou have found "+str(blizzard)+" stone!This requires a 2HV pickaxe.")
                time.sleep(2.5)
                print("Let's mine it!")
                time.sleep(1.5)
                if usingpickaxe['HV']>=stoneset['HV']:
                    print("You have successfully mined!")
                    stone+=blizzard
                else:
                    print("Oof,this is too hard to mine!")
            elif split==4 or split==5:
                print("\nYou have found "+str(blizzard)+" gold!This requires a 5HV pickaxe.")
                time.sleep(2.5)
                print("Let's mine it!")
                time.sleep(1.5)
                if usingpickaxe['HV']>=goldset['HV']:
                    print("\nYou have successfully mined!")
                    gold+=blizzard
                else:
                    print("\nOof,this is too hard to mine!")
            elif split==6 or split==7:
                print("\nYou have found "+str(blizzard)+" diamond!This requires a 20HV pickaxe.")
                time.sleep(2.5)
                print("Let's mine it!")
                time.sleep(1.5)
                if usingpickaxe['HV']>=diamondset['HV']:
                    print("\nYou have successfully mined!")
                    diamond+=blizzard
                else:
                        print("\nOof,this is too hard to mine!")
            elif split==8:
                print("\nYou have found "+str(blizzard)+" ruby!This requires a 50HV pickaxe.")
                time.sleep(2.5)
                print("Let's mine it!")
                time.sleep(1.5)
                if usingpickaxe['HV']>=rubyset['HV']:
                    print("\nYou have successfully mined!")
                    ruby+=blizzard
                else:
                    print("\nOof,this is too hard to mine!")
        time.sleep(1)
        print("Great job!You have finish mining!")
        time.sleep(0.2)
        continue
    #pickaxe evolver
    elif ask=='pickaxe improve station'or ask=='Pickaxe Improve Station'or ask=='PIS':
        time.sleep(0.2)
        print("\nWell hello to you!")
        time.sleep(0.5)
        print("I am the pickaxe improver Bible!I can evolve your pickaxe!")
        time.sleep(1)
        ask=input("Which pickaxe do you want to evolve?(pickaxe name, no capitalize)")
        if ask in pickaxesname:
            if ask=='starter pickaxe'or ask=='Starter Pickaxe':
                print("This will cost "+str(common)+" .")
                if coins>=int(common):
                    print("\nI see that you have enough money,good!")
                    time.sleep(1)
                    print("EVOLVING...")
                    coins-=common
                    starterpickaxe['HV']*=5
                    print("See you next time!")
                    continue
                else:
                    print("Wow,you came with a pickaxe but not enough money,lol.")
                    continue
            if ask=='stone pickaxe'or ask=='Stone Pickaxe'or ask=='golden pickaxe'or ask=='Golden Pickaxe':
                print("This will cost "+str(rare)+" coins.")
                if coins>=int(rare):
                    print("\nI see that you have enough money,good!")
                    time.sleep(1)
                    print("EVOLVING...")
                    if ask=='golden pickaxe'or ask=='Golden Pickaxe':
                        goldpickaxe['HV']*=2
                        coins-=rare
                    if ask=='stone pickaxe'or ask=='Stone Pickaxe':
                        stonepickaxe['HV']*=2
                        coins-=rare
                    time.sleep(2)
                    print("\nSee you next time!")
                    continue
                else:
                    print("Wow,you came with a pickaxe but not enough money,lol.")
                    continue
            if ask=='ice pickaxe'or ask=='Ice Pickaxe'or ask=='diamond pickaxe'or ask=="Diamond Pickaxe":
                print("This will cost "+str(epic)+" gems.")
                if gems>=int(epic):
                    print("\nI see that you have enough money,good!")
                    time.sleep(1)
                    print("EVOLVING...")
                    if ask=='diamond pickaxe'or ask=='Diamond Pickaxe':
                        diamondpickaxe['HV']*=2
                        gems-=epic
                    if ask=='ice pickaxe'or ask=='Ice Pickaxe':
                        icepickaxe['HV']*=2
                        gems-=epic
                    time.sleep(2)
                    print("\nSee you next time!")
                    continue
                else:
                    print("Wow,you came with a pickaxe but not enough money,lol.")
                    continue
            if ask=='legend pickaxe'or ask=='Legend Pickaxe':
                print("This will cost "+str(legendary)+" gems.")
                if gems>=int(legendary):
                    print("\nI see that you have enough money,good!")
                    time.sleep(1)
                    print("EVOLVING...")
                    gems-=legendary
                    legendpickaxe['HV']*=2
                    print("See you next time!")
                    continue
                else:
                    print("Wow,you came with a pickaxe but not enough money,lol.")
                    continue
        else:
            print("Do not lie infront of me, you do not have that pickaxe! Or you just spell wrong lol.")
            continue
        
                
    
                    
            
    
        


                    
                
            
            
                
    

