import os
import banner
import sys
import smtplib
import time
import uso
os.system("clear")
#Comienza el bucle
while True:
     banner.banner()# Banner Principal-----------------
     opcion = input('\u001b[31;1m'+'opcion'+'\u001b[37;1m'+" > ")
     if opcion == "1":
             os.system("clear")
             banner.pishing_banner()# Banner Phishing-------------
             opcion = input('\u001b[35;1m'+"opcion"+'\u001b[33;1m'+" > "+'\u001b[37;1m')
             if opcion == "1":
                     os.system("clear")
                     banner.pishing_FotoSploit()# Banner Fotosploit-------------
                     opcion = input('\u001b[33;1m'+"opcion"+'\u001b[35;1m'+" > "+'\u001b[37;1m')
                     if opcion == "1":
                        os.system("clear")
                        uso.uso_Fotosploit() # GUIA FotoSploit -------------------
                        print('\u001b[35;1m'+"> "+'\u001b[33;1m'+"["+'\u001b[337;1m'+'x'+'\u001b[33;1m'+']'+'\u001b[37;1m'+'para salir')
                        opcion = input('\u001b[33;1m'+"opcion"+'\u001b[35;1m'+" > "+'\u001b[37;1m')
                        if opcion == "x":
                                os.system("clear")
                                continue
                        else:
                            print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'ERROR')
                            print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'Elija una opcion vailda')
                            time.sleep(2)
                            os.system("clear")
                     elif opcion == "x":
                           os.system("clear")
                           continue
                     elif opcion == "2":
                           print('\u001b[35;1m'+"> "+'\u001b[37;1m'+'Esto puede demorar')
                           time.sleep(2)
                           os.system("clear")
                           os.system("pkg install php")
                           os.system("pkg install git")
                           os.system("pkg install bash")
                           os.system("git clone https://github.com/Cesar-Hack-Gray/FotoSploit")
                           os.system('mv FotoSploit /data/data/com.termux/files/home')
                           os.system("clear")
                           print('\u001b[35;1m'+'> '+'\u001b[37;1m'+"Instalacion Completa\n"+'\u001b[35;1m'+'> '+'\u001b[37;1m'+"Ahora solo as los pasos del #2")
                           print('\u001b[35;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[35;1m'+"]"+'\u001b[37;1m'+"Continuar")
                           continuar = input('\u001b[35;1m'+"opcion"+'\u001b[37;1m'+'\u001b[37;1m'+" > ")
                           if continuar == "c":
                                      os.system("clear")
                                      continue
                           else:
                              print('\u001b[35;1m'+'> '+'\u001b[37;1m'+"ERROR")
                              print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                              time.sleep(2)
                              os.system("clear")
                     else:
                        print('\u001b[33;1m'+'> '+'\u001b[37;1m'+"ERROR")
                        print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                        time.sleep(2)
                        os.system("clear")
             elif opcion == "x":
                       os.system("clear")
                       continue
             elif opcion == "2":
                      os.system("clear")
                      banner.pishing_scam()# Banner phising Scam----------------------
                      opcion = input('\u001b[37;1m'+"opcion"+'\u001b[36;1m'+" > "+'\u001b[37;1m')
                      if opcion == "x":
                            os.system("clear")
                            continue
                      elif opcion == "1":
                            print('\u001b[36;1m'+'> '+'\u001b[37;1m'+"Esto puede demorar")
                            time.sleep(2)
                            os.system("pkg install git")
                            os.system("pkg install bash")
                            os.system("git clone https://github.com/Cesar-Hack-Gray/scam.git")
                            os.system("mv scam /data/data/com.termux/files/home")
                            os.system("clear")
                            print('\u001b[36;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[36;1m'+"> "+'\u001b[37;1m'+"ahora solo as los pasos del #2")
                            print('\u001b[36;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[36;1m'+"]"+'\u001b[37;1m'+"Continuar")
                            continuar = input('\u001b[37;1m'+"opcion"+'\u001b[36;1m'+" > ")
                            if continuar == "c":
                                    os.system("clear")
                                    continue
                            else:
                               print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'ERROR')
                               print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                      else:
                         print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'ERROR')
                         print('\u001b[36;1m'+'> '+'\u001b[37;1m'+"Elija una opcion valida")
                         time.sleep(2)
                         os.system("clear")
                         continue
             elif opcion == "3":
                      os.system("clear")
                      banner.pishing_adv()# Banner phising adv ----------------------
                      opcion = input('\u001b[37;1m'+"opcion"+'\u001b[30;1m'+" > "+'\u001b[37;1m')
                      if opcion == "1":
                             print('\u001b[30;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar ")
                             time.sleep(2)
                             os.system("pkg install git")
                             os.system("git clone https://github.com/Ignitetch/AdvPhishing.git")
                             os.system("mv AdvPhishing /data/data/com.termux/files/home")
                             os.system("clear")
                             print('\u001b[30;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[30;1m'+'> '+'\u001b[37;1m'+"ahora solo as los pasos del #2")
                             print('\u001b[30;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[30;1m'+"]"+'\u001b[37;1m'+"Continuar")
                             continuar = input('\u001b[37;1m'+"opcion"+'\u001b[30;1m'+' > '+'\u001b[37;1m')
                             if continuar == "c":
                                   os.system("clear")
                                   continue
                             else:
                               print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'ERROR')
                               print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                               time.sleep(2)
                               os.system("clear")
                      elif opcion == "x":
                               os.system("clear")
                               continue
                      else:
                         print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'ERROR')
                         print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                         time.sleep(2)
                         os.system("clear")
             elif opcion == "4":
                        os.system("clear")
                        banner.pishing_social()#Banner Phising Social------------------
                        opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
                        if opcion == "1":
                               print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar ")
                               time.sleep(2)
                               os.system("pkg install curl")
                               os.system("pkg install ssh")
                               os.system("pkg install python2")
                               os.system("pkg install wget")
                               os.system("pkg install git")
                               os.system("git clone https://github.com/Cesar-Hack-Gray/SocialSploit.git ")
                               os.system("mv SocialSploit /data/data/com.termux/files/home")
                               os.system("clear")
                               print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[31;1m'+'> '+'\u001b[37;1m'+"ahora solo as los pasos del numero #2 ")
                               print('\u001b[31;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[31;1m'+"]"+'\u001b[37;1m'+"Continuar")
                               continuar = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+" > "+'\u001b[37;1m')
                               if continuar  == "c":
                                        os.system("clear")
                                        continue
                               else:  
                                  print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                  print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                                  time.sleep(2)
                                  os.system("clear")
                        elif opcion == "x":
                                  os.system("clear")
                                  continue
                        else:
                          print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"ERROR")
                          print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Elija una opcion valida")
                          time.sleep(2)
                          os.system("clear")
                          continue
             elif opcion == '5':
                       os.system("clear")
                       banner.wishfish()
                       opcion = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+' > '+'\u001b[37;1m')
                       if opcion == '1':
                               print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar ")
                               os.system('pkg install git')
                               os.system('pkg install php')
                               os.systen('pkg install openssh')
                               os.system('pkg install wget')
                               os.system('git clone https://github.com/kinghacker0/WishFish.git')
                               os.system("mv WishFish /data/data/com.termux/files/home")
                               os.system("clear")
                               print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[32;1m'+'> '+'\u001b[37;1m'+"ahora solo as los pasos del numero #2 ")
                               print('\u001b[32;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[32;1m'+"]"+'\u001b[37;1m'+"Continuar")
                               continuar = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+" > "+'\u001b[37;1m')
                               if continuar == "c": 
                                         os.system("clear")
                                         continue
                               else:
                                  print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                  print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                                  time.sleep(2)
                                  os.system("clear")
                                  continue
                       elif opcion == "2":
                               print("Falta")
                       elif opcion == "x": 
                                 os.system("clear")
                                 continue
                       else: 
                          print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"ERROR")
                          print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"Elija una opcion valida")
                          time.sleep(2)
                          os.system("clear")
                          continue
             elif opcion == '6':
                       os.system("clear")
                       banner.koroni()
                       opcion = input('\u001b[37;1m'+"opcion"+'\u001b[33;1m'+' > '+'\u001b[37;1m')
                       if opcion == '1':
                              print('\u001b[33;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar ")
                              os.system("pkg install git")
                              os.system("pkg install php")
                              os.system("git clone https://github.com/DeepSociety/koroni.git")
                              os.system("mv koroni /data/data/com.termux/files/home")
                              os.system("clear")
                              print('\u001b[33;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[33;1m'+'> '+'\u001b[37;1m'+"ahora solo as los pasos del numero #2")
                              print('\u001b[33;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[33;1m'+"]"+'\u001b[37;1m'+"Continuar")
                              continuar = input('\u001b[37;1m'+"opcion"+'\u001b[33;1m'+" > "+'\u001b[37;1m')
                              if continuar == 'c':
                                         os.system("clear")
                                         continue
                              else:
                                 print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                 print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                                 time.sleep(2)
                                 os.system("clear")
                                 continue
                       elif opcion == '2':
                                   os.system("clear")
                                   uso.uso_koroni()
                                   print('\u001b[33;1m'+"> "+'\u001b[37;1m'+"["+'\u001b[33;1m'+'x'+'\u001b[37;1m'+']'+'\u001b[37;1m'+'para salir')
                                   opcion = input('\u001b[37;1m'+"opcion"+'\u001b[33;1m'+" > "+'\u001b[37;1m')
                                   if opcion == 'x':
                                            os.system("clear")
                                            continue
                                   else:
                                      print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                      print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                                      time.sleep(2)
                                      os.system("clear")
                                      continue
                       elif opcion == "x":
                                 os.system("clear")
                                 continue
                       else:
                            print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'ERROR')
                            print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                            time.sleep(2)
                            os.system("clear")
                            continue
             else:
               print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'ERROR')
               print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
               time.sleep(2)
               os.system("clear")
               continue
     elif opcion == "2":
            os.system("clear")
            banner.banner_Fuerza()#Banner Principal Fuerza Bruta---------------
            opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+" > "+'\u001b[37;1m')
            if opcion == "1":
                   os.system("clear")
                   banner.fuerza_Facebook_brute()# Banner Facebook_brute-------------------
                   opcion =input('\u001b[37;1m'+"opcion"+'\u001b[34;1m'+" > "+'\u001b[37;1m')
                   if opcion == "1":
                             print('\u001b[34;1m'+'> '+'\u001b[37;1m'"Esto Puede demorar")
                             time.sleep(2)
                             os.system("pkg install python2")
                             os.system("pkg install python2-dev")
                             os.system("pkg install pip2")
                             os.system("pkg install mechanize")
                             os.system("pkg install git")
                             os.system("git clone https://github.com/perjayro/Facebook_brute.git ")
                             os.system("mv Facebook_brute /data/data/com.termux/files/home")
                             os.system("clear")
                             print('\u001b[34;1m'+"> "+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[34;1m'+"> "+'\u001b[37;1m'+"ahora solo tienes que aser el #2")
                             print('\u001b[34;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[34;1m'+"]"+'\u001b[37;1m'+"Continuar")
                             continuar = input('\u001b[37;1m'+"opcion"+'\u001b[34;1m'+" > "+'\u001b[37;1m')
                             if continuar == "c":
                                      os.system("clear")
                                      continue
                             else:
                               print('\u001b[34;1m'+'> '+'\u001b[37;1m'+'ERROR')
                               print('\u001b[34;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                               time.sleep(2)
                               os.system("clear")
                   elif opcion == "x":
                             os.system("clear")
                             continue
                   elif opcion == "2":
                             os.system("clear")
                             uso.uso_Facebook_brute()#Guia de Facebook_brute----------------
                             print('\u001b[33;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[33;1m'+"]"+'\u001b[37;1m'+"Continuar")
                             opcion = input('\u001b[37;1m'+"opcion"+'\u001b[35;1m'+" > "+'\u001b[37;1m')
                             if opcion == "c":
                                      os.system("clear")
                                      continue
                             else:
                                 print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                 print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                                 time.sleep(2)
                                 os.system("clear")
                   else: 
                      print('\u001b[34;1m'+'> '+'\u001b[37;1m'+'ERROR')
                      print('\u001b[34;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                      time.sleep(2)
                      os.system("clear")
            elif opcion == "2":
                   os.system("clear")
                   banner.Diccionario()#Banner Principal de Diccionarii
                   opcion =input('\u001b[37;1m'+"opcion"+'\u001b[33;1m'+" > "+'\u001b[37;1m')
                   if opcion == "1":
                            os.system("clear")
                            banner.Diccionario_cupp()#Banner de cupp--------------------
                            opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+" > "+'\u001b[37;1m')
                            if opcion == "1":
                                      print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Esto puede demorar")
                                      time.sleep(2)
                                      os.system("pkg install python")
                                      os.system("pkg install git")
                                      os.system("git clone https://github.com/Mebus/cupp.git")
                                      os.system("mv cupp /data/data/com.termux/files/home")
                                      os.system("clear")
                                      print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[31;1m'+'> '+'\u001b[37;1m'+"ahora solo as los pasos del #2")
                                      print('\u001b[31;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[31;1m'+"]"+'\u001b[37;1m'+"Continuar")
                                      opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
                                      if opcion == "c":
                                               os.system("clear")
                                               continue
                                      else: 
                                         print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                         print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                                         time.sleep(2)
                                         os.system("clear")
                            elif opcion == "2":
                                   os.system("clear")
                                   uso.uso_cupp()#GUIA de cupp-----------------------------
                                   print('\u001b[33;1m'+"["+'\u001b[37;1m'+'c'+'\u001b[33;1m'+"]"+'\u001b[37;1m'+"Continuar")
                                   opcion = input('\u001b[37;1m'+"opcion"+'\u001b[35;1m'+" > "+'\u001b[37;1m')
                                   if opcion == "c":
                                          os.system("clear")
                                          continue
                                   else:
                                       print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                       print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                                       time.sleep(2)
                                       os.system("clear")
                            elif opcion == "x":
                                  os.system("clear")
                                  continue
                            else:
                               print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                               print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                               time.sleep(2)
                               os.system("clear")
                   elif opcion == "x":
                            os.system("clear")
                            continue
                   else:
                       print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'ERROR')
                       print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                       time.sleep(2)
                       os.system("clear")
            elif opcion == "x":
                   os.system("clear")
                   continue
            elif opcion == "3":
                    os.system("clear")
                    banner.Fuerza_Gemail()#Banner Gemail-------------------------
                    opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
                    if opcion == "1":
                          print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Esto puede demorar")
                          time.sleep(2)
                          os.system("apt install vim")
                          os.system("pkg install git")
                          os.system("apt install cat")
                          os.system("pkg install python2")
                          os.system("git clone https://github.com/Ha3MrX/Gemail-Hack.git")
                          os.system("mv Gemail-Hack /data/data/com.termux/files/home")
                          os.system("clear")
                          print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[31;1m'+'> '+'\u001b[37;1m'+"Ahora solo as los pasos del #2")
                          print('\u001b[31;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[31;1m'+"]"+'\u001b[37;1m'+"continuar")
                          opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
                          if opcion == "c":
                                 os.system("clear")
                                 continue
                          else:
                            print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'ERROR')
                            print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                            time.sleep(2)
                            os.system("clear")
                    elif opcion == "2":
                        os.system("clear")
                        uso.uso_gemail()#GUIA de gemail--------------------------
                        print('\u001b[33;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[33;1m'+']'+'\u001b[37;1m'+"Continuar")
                        opcion = input('\u001b[37;1m'+"opcion"+'\u001b[35;1m'+' > '+'\u001b[37;1m')
                        if opcion == "c":
                               os.system("clear")
                               continue
                        else:
                           print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'ERROR')
                           print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                           time.sleep(2)
                           os.system("clear")
                    elif opcion == "x":
                            os.system("clear")
                            continue
                    else:
                        print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                        print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                        time.sleep(2)
                        os.system("clear")
            else: 
                print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                time.sleep(2)
                os.system("clear")
     elif opcion =="3":
              os.system("clear")
              banner.banner_spam()#Banner principal de spam------------------
              opcion = input('\u001b[37;1m'+"opcion"+'\u001b[36;1m'+' > '+'\u001b[37;1m')
              if opcion == "1":
                    os.system("clear")
                    banner.banner_setsms()#banner de setsms---------------------
                    opcion = input('\u001b[37;1m'+"opcion"+'\u001b[36;1m'+' > '+'\u001b[37;1m')
                    if opcion == "1":
                            print('\u001b[36;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar")
                            time.sleep(2)
                            os.system("apt install git")
                            os.system("git clone https://github.com/TermuxHacking000/SETSMS")
                            os.system('mv SETSMS /data/data/com.termux/files/home')
                            os.system("clear")
                            print('\u001b[36;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[36;1m'+'> '+'\u001b[37;1m'+"ahora solo as los pasos del #2")
                            print('\u001b[36;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[36;1m'+"]"+'\u001b[37;1m'+"Continuar")
                            opcion = input('\u001b[37;1m'+"opcion"+'\u001b[36;1m'+' > '+'\u001b[37;1m')
                            if opcion == "c":
                                   os.system("clear")
                                   continue
                            else:
                              print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'ERROR')
                              print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                              time.sleep(2)
                              os.system("clear")
                    elif opcion == "x": 
                            os.system("clear")
                            continue
                    else: 
                       print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'ERROR')
                       print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                       time.sleep(2)
                       os.system("clear")
              elif opcion == '2':
                        os.system("clear")
                        banner.tbomb()
                        opcion = input('\u001b[37;1m'+"opcion"+'\u001b[37;1m'+' > '+'\u001b[37;1m')
                        if opcion == "1":
                                 print('\u001b[37;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar")
                                 time.sleep(2)
                                 os.system("pkg install python")
                                 os.system("pkg install python2")
                                 os.system('pkg install git')
                                 os.system("git clone https://github.com/TheSpeedX/TBomb.git")
                                 os.system('mv TBomb /data/data/com.termux/files/home')
                                 os.system("clear")
                                 print('\u001b[37;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[37;1m'+'> '+'\u001b[37;1m'+"ahora solo as los pasos del #2")
                                 print('\u001b[37;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[37;1m'+"]"+'\u001b[37;1m'+"Continuar")
                                 opcion = input('\u001b[37;1m'+"opcion"+'\u001b[37;1m'+' > '+'\u001b[37;1m')
                                 if opcion == 'c':
                                          os.system("clear")
                                          continue
                                 else:
                                      print('\u001b[37;1m'+'> '+'\u001b[37;1m'+'ERROR')      
                                      print('\u001b[37;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                                      time.sleep(2)
                                      os.system("clear")
                                      continue
        
                        elif opcion == '2':
                                   os.system("clear")
                                   uso.uso_tbomb()
                                   print('\u001b[32;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[32;1m'+']'+'\u001b[37;1m'+"Continuar")
                                   opcion = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+' > '+'\u001b[37;1m')
                                   if opcion == "c":
                                           os.system("clear")
                                           continue
                                   else:
                                       print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                       print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                                       time.sleep(2)
                                       os.system("clear")
                                       continue
                        elif opcion == 'x':
                                      os.system("clear")
                                      continue
                        else:
                             print('\u001b[37;1m'+'> '+'\u001b[37;1m'+'ERROR')
                             print('\u001b[37;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                             time.sleep(2)
                             os.system("clear")
                             continue
                              
              elif opcion == "x":
                      os.system("clear")
                      continue
              else:
                 print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'ERROR')
                 print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                 time.sleep(2)
                 os.system("clear")
                 continue
     elif opcion == "4":
             os.system("clear")
             banner.banner_DDOS()#Banner DDos ---------------------------
             opcion = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+' > '+'\u001b[37;1m')
             if opcion == "1":
                    os.system("clear")
                    banner.banner_hammer()#Banner Hammer----------------------
                    opcion = input('\u001b[37;1m'+"opcion"+'\u001b[35;1m'+' > '+'\u001b[37;1m')
                    if opcion == "1":
                           print('\u001b[35;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar")
                           time.sleep(2)
                           os.system("pkg install python")
                           os.system("pkg install git")
                           os.system("git clone https://github.com/rk1342k/Hammer.git")
                           os.system("mv hammer /data/data/com.termux/files/home")
                           os.system("clear")
                           print('\u001b[35;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[35;1m'+'> '+'\u001b[37;1m'+"Ahora solo as los pasos del #2")
                           print('\u001b[35;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[35;1m'+"]"+'\u001b[37;1m'+"Continuar")
                           opcion = input('\u001b[37;1m'+"opcion"+'\u001b[35;1m'+' > '+'\u001b[37;1m')
                           if opcion == "c":
                                    os.system("clear")
                                    continue
                           else:
                              print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'ERROR')
                              print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                              time.sleep(2)
                              os.system("clear")
                    elif opcion == "2":
                             os.system("clear")
                             uso.uso_hammer()#GUIA de hammer---------------------
                             print('\u001b[35;1m'+"["+'\u001b[37;1m'+'c'+'\u001b[35;1m'+"]"+'\u001b[37;1m'+"Continuar")
                             opcion = input('\u001b[37;1m'+"opcion"+'\u001b[33;1m'+" > "+'\u001b[37;1m')
                             if opcion == "c":
                                      os.system("clear")
                                      continue
                             else: 
                                 print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                 print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                                 time.sleep(2)
                                 os.system("clear")
                    elif opcion == "x":
                          os.system("clear")
                          continue
                    else:
                       print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'ERROR')
                       print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                       time.sleep(2)
                       os.system("clear")
             elif opcion == "x":
                      os.system("clear")
                      continue
             elif opcion == "2":
                     os.system("clear")
                     banner.banner_hulk()#Banner hulk--------------------------
                     opcion = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+" > "+'\u001b[37;1m')
                     if opcion == "1":
                           print('\u001b[32;1m'+"> "+'\u001b[37;1m'+"Esto Pude Demorar")
                           time.sleep(2)
                           os.system("pkg install git")
                           os.system("pkg install python2")
                           os.system("git clone https://github.com/grafov/hulk.git")
                           os.system("mv hulk /data/data/com.termux/files/home")
                           os.system("clear")
                           print('\u001b[32;1m'+"> "+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[32;1m'+'> '+'\u001b[37;1m'+"Ahora solo as los pasos del #2")
                           print('\u001b[32;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[32;1m'+"]"+'\u001b[37;1m'+"Continuar")
                           opcion = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+' > '+'\u001b[37;1m')
                           if opcion == "c":
                                   os.system("clear")
                                   continue
                           else:
                              print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'ERROR')
                              print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                              time.sleep(2)
                              os.system("clear")
                     elif opcion == "x":
                             os.system("clear")
                             continue
                     else:
                        print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'ERROR')
                        print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                        time.sleep(2)
                        os.system("clear")
             else: 
                 print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'ERROR')
                 print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                 time.sleep(2)
                 os.system("clear")
     elif opcion == "5":
             os.system("clear")
             banner.banner_datos()#BANNER Principal de datos--------------------
             opcion = input('\u001b[37;1m'+"opcion"+'\u001b[33;1m'+' > '+'\u001b[37;1m')
             if opcion == "1":
                     os.system("clear")
                     banner.Banner_Phone()#Banner de phoneinfoga-----------------------
                     opcion = input('\u001b[37;1m'+"opcion"+'\u001b[34;1m'+' > '+'\u001b[37;1m')
                     if opcion == "1":
                            print('\u001b[34;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar")
                            time.sleep(2)
                            os.system("pkg install python")
                            os.system("pkg install python2")
                            os.system("pkg install git ")
                            os.system("git clone https://github.com/Wes974/PhoneInfoga.git")
                            os.system("mv PhoneInfoga /data/data/com.termux/files/home")
                            os.system("clear")
                            print('\u001b[34;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[34;1m'+'> '+'\u001b[37;1m'+"Ahora solo sigue los pasos del #2")
                            print('\u001b[34;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[34;1m'+"]"+'\u001b[37;1m'+"Continuar")
                            opcion = input('\u001b[37;1m'+"opcion"+'\u001b[34;1m'+' > '+'\u001b[37;1m')
                            if opcion == "c":
                                   os.system("clear")
                                   continue
                            else: 
                               print('\u001b[34;1m'+'> '+'\u001b[37;1m'+'ERROR')
                               print('\u001b[34;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                               time.sleep(2)
                               os.system("clear")
                     elif opcion == "x":
                            os.system("clear")
                            continue
                     else:
                          print('\u001b[34;1m'+'> '+'\u001b[37;1m'+'ERROR')
                          print('\u001b[34;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                          time.sleep(2)
                          os.system("clear")
             elif  opcion == "2":
                    os.system("clear")
                    banner.banner_sherlock()#Banner de sherlock------------------
                    opcion = input('\u001b[37;1m'+"opcion"+'\u001b[30;1m'+' > '+'\u001b[37;1m')
                    if opcion == "1":
                            print("Esto Puede Demorar")
                            os.system("pkg install bash")
                            os.system("pkg install python")
                            os.system("git clone https://github.com/sherlock-project/sherlock.git")
                            os.system("mv sherlock /data/data/com.termux/files/home")
                            os.system("clear")
                            print('\u001b[30;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[30;1m'+'> '+'\u001b[37;1m'+"ahora solo as los pasos del #2")
                            print('\u001b[30;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[30;1m'+"]"+'\u001b[37;1m'+"Continuar")
                            opcion = input('\u001b[37;1m'+"opcion"+'\u001b[30;1m'+' > '+'\u001b[37;1m')
                            if opcion == "c":
                                  os.system("clear")
                                  continue
                            else: 
                               print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'ERROR')
                               print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                               time.sleep(2)
                               os.system("clear")
                    elif opcion == "x":
                             os.system("clear")
                             continue
                    else:
                       print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'ERROR')
                       print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                       time.sleep(2)
                       os.system("clear")
             elif opcion == "3":
                     os.system("clear")
                     banner.banner_FBI()
                     opcion = input('\u001b[37;1m'+"opcion"+'\u001b[36;1m'+' > '+'\u001b[37;1m')
                     if opcion == "1":
                              print('\u001b[36;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar")
                              time.sleep(2)
                              os.system("pkg install python2")
                              os.system("pkg install git")
                              os.system("git clone https://github.com/xHak9x/fbi.git")
                              os.system("mv fbi /data/data/com.termux/files/home")
                              os.system("clear")
                              print('\u001b[36;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[36;1m'+'> '+'\u001b[37;1m'+"Ahora solo as los pasos del #2")
                              print('\u001b[36;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[36;1m'+"]"+'\u001b[37;1m'+"Continuar")
                              opcion = input('\u001b[37;1m'+"opcion"+'\u001b[36;1m'+' > '+'\u001b[37;1m')
                              if opcion == "c":
                                    os.system("clear")
                                    continue
                              else:
                                 print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                 print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                                 time.sleep(2)
                                 os.system("clear")
                     if opcion == "2":
                              os.system("clear")
                              uso.uso_fbi()
                              print('\u001b[33;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[33;1m'+"]"+'\u001b[37;1m'+"Continuar")
                              opcion = input('\u001b[37;1m'+"opcion"+'\u001b[35;1m'+" > "+'\u001b[37;1m')
                              if opcion == "c":
                                      os.system("clear")
                                      continue          
                              else: 
                                 print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'ERROR')        
                                 print('\u001b[35;1m'+'> '+'\u001b[37;1m'+'Elije una opcion vailda')     
                                 time.sleep(2)
                                 os.system("clear")
                     if opcion == "x":
                              os.system("clear")
                              continue
                     else:  
                          print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'ERROR')
                          print('\u001b[36;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                          time.sleep(2)
                          os.system("clear")
             elif opcion == "x":
                    os.system("clear")
                    continue
             elif opcion == '4':
                     os.system("clear")
                     banner.cam_hacker()
                     opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
                     if opcion == "1":
                         print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar")
                         time.sleep(2)
                         os.system("pkg install git")
                         os.system("pkg install python2")
                         os.system("pkg install python")
                         os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers.git")
                         os.system("mv Cam-Hackers /data/data/com.termux/files/home")
                         os.system("clear")
                         print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[31;1m'+'> '+'\u001b[37;1m'+"Ahora solo as los pasos del #2")
                         print('\u001b[31;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[31;1m'+"]"+'\u001b[37;1m'+"Continuar")
                         opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
                         if opcion == 'c':
                                os.system("clear")
                                continue
                         else:
                            print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                            print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'Elije una opcion valida')
                            time.sleep(2)
                            os.system("clear")
                     elif opcion == 'x':
                              os.system("clear")
                              continue
                     else:
                          print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                          print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                          time.sleep(2)
                          os.system("clear")
                          continue
             else:
                print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'ERROR')
                print('\u001b[33;1m'+'> '+'\u001b[37;1m'+'Elija una opcion valida')
                time.sleep(2)
                os.system("clear")
                continue
     #elif
     elif opcion == "6":
               os.system("clear")
               banner.viruz()
               opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
               if opcion == '1':
                         os.system("clear")
                         banner.papaviruz()
                         opcion = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+' > '+'\u001b[37;1m')
                         if opcion == '1':                  
                                print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar") 
                                os.system("pkg install bash")             
                                os.system("apt install pv")           
                                os.system("pkg install git")
                                os.system("git clone https://github.com/Hacking-pch/papaviruz.git")
                                os.system("mv papaviruz /data/data/com.termux/files/home")
                                os.system("clear")
                                print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[32;1m'+'> '+'\u001b[37;1m'+"Ahora solo as los pasos del #2")
                                print('\u001b[32;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[32;1m'+"]"+'\u001b[37;1m'+"Continuar")
                                opcion = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+' > '+'\u001b[37;1m')
                                if opcion == 'c':
                                         os.system("clear")
                                         continue
                                else:
                                      print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                      print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"Debes Elegir una opcion valida")
                                      time.sleep(2)
                                      os.system("clear")
                                      continue
                         elif opcion == '2':
                                  os.system("clear")
                                  uso.uso_papaviruz()
                                  print('\u001b[32;1m'+"["+'\u001b[37;1m'+'c'+'\u001b[32;1m'+"]"+'\u001b[37;1m'+"Continuar")
                                  opcion = input('\u001b[37;1m'+"opcion"+'\u001b[32;1m'+" > "+'\u001b[37;1m')
                                  if opcion == "c":
                                         os.system("clear")
                                         continue
                                  else:
                                     print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                     print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"Debes Elegir una opcion valida")
                                     time.sleep(2)
                                     os.system("clear")
                                     continue
                         else:
                            print('\u001b[32;1m'+'> '+'\u001b[37;1m'+'ERROR')
                            print('\u001b[32;1m'+'> '+'\u001b[37;1m'+"Debes Elegir una opcion valida")
                            time.sleep(2)
                            os.system("clear")
                            continue
               elif opcion == '2':
                          os.system("clear")
                          banner.binarios()
                          opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
                          if opcion == '1':
                                  print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar")
                                  os.system("clear")
                                  os.system("pkg install git")
                                  os.system("git clone https://github.com/Cesar-Hacker/binarios.git")
                                  os.system("mv binarios /data/data/com.termux/files/home")
                                  os.system("clear")
                                  print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Instalado Correctamente\n"+'\u001b[31;1m'+'> '+'\u001b[37;1m'+"Ahora solo as los pasos del #2")
                                  print('\u001b[31;1m'+"["+'\u001b[37;1m'+"c"+'\u001b[31;1m'+"]"+'\u001b[37;1m'+"Continuar")
                                  opcion = input('\u001b[37;1m'+"opcion"+'\u001b[31;1m'+' > '+'\u001b[37;1m')
                                  if opcion == 'c':
                                           os.system("clear")
                                           continue
                                  else:
                                     print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                                     print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Debes Elegir una opcion valida")
                                     time.sleep(2)
                                     os.system("clear")
                                     continue
                          elif opcion == 'x':
                                       os.system("clear")
                                       continue
                          else:
                               print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                               print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Debes Elegir una opcion valida")
                               time.sleep(2)
                               os.system("clear")
                               continue
                            
               elif opcion == "x":
                        os.system("clear")
                        continue
               else:
                    print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
                    print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Debes Elegir una opcion valida")
                    time.sleep(2)
                    os.system("clear")
                    continue
     elif opcion == "7":
                   os.system("clear")
                   banner.proot()
                   opcion = input('\u001b[37;1m'+"opcion"+'\u001b[30;1m'+' > '+'\u001b[37;1m')
                   if opcion == "1":
                            print('\u001b[30;1m'+'> '+'\u001b[37;1m'+"Esto Puede Demorar")
                            os.system("clear")
                            os.system("pkg install proot")
                            os.system("clear")
                            print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'Proot instalado correctamente')
                            time.sleep(2)
                            os.system("clear")
                            continue
                   elif opcion == 'x':
                           os.system("clear")
                           continue
                   else:
                        print('\u001b[30;1m'+'> '+'\u001b[37;1m'+'ERROR')
                        print('\u001b[30;1m'+'> '+'\u001b[37;1m'+"Debes Elegir una opcion valida")
                        time.sleep(2)
                        os.system("clear")
                        continue
     elif opcion == "x":
             os.system("clear")
             sys.exit()
     else: 
        print('\u001b[31;1m'+'> '+'\u001b[37;1m'+'ERROR')
        print('\u001b[31;1m'+'> '+'\u001b[37;1m'+"Debes Elegir una opcion valida")
        time.sleep(2)
        os.system("clear")
        continue
