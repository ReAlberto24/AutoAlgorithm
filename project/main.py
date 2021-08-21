import os, screeninfo, pyautogui, pytesseract, re, time, mouse, threading, keyboard, traceback
from playsound import playsound

def checkIfProcessRunning(processName):
    import psutil
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if os.path.exists('C:\\Program Files\\Tesseract-OCR') == True:
    pass
else:
    os.system('download/tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe')

    while True:
        if checkIfProcessRunning('tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe') == True:
            pass
        else:
            break

if os.path.exists('C:\\Program Files\\Tesseract-OCR') == True:
    pass
else:
    input('Bisogna installare tesseract!')
    exit()

if screeninfo.get_monitors()[0].width == 1920 and screeninfo.get_monitors()[0].height == 1080:
    pass
else:
    input('Risoluzione non valida (Richiesta = 1920x1080)')
    exit()

every = float(input('Ogni quanto cerco il migliore? (esempio 1.0) (consigliato 5.0) '))
print('Iniziando in 3 secondi')
time.sleep(3)
print('Iniziato')

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

try: os.mkdir('algDir')
except: pass

runAFK = False

def algC():
    
    global runAFK
    runAFK = False
    bestAlg = ''

    while True:
        try:
            # SHA-512
            SHA512 = pyautogui.screenshot(region=(1400, 655, 300, 35))

            # Dagger
            Dagger = pyautogui.screenshot(region=(1400, 705, 300, 36))

            # Scrypt
            Scrypt = pyautogui.screenshot(region=(1400, 758, 300, 36))

            # Bloxchain
            Bloxchain = pyautogui.screenshot(region=(1400, 813, 300, 36))
            
            SHA512.save(f'algDir\\SHA512.png')
            Dagger.save(f'algDir\\Dagger.png')
            Scrypt.save(f'algDir\\Scrypt.png')
            Bloxchain.save(f'algDir\\Bloxchain.png')

            algList = []

            # SHA-512
            SHA512V = pytesseract.image_to_string(f'algDir\\SHA512.png')
            SHA512VL = re.findall(r'\d+', SHA512V)
            SHA512VS = SHA512VL[1]+SHA512VL[2]
            SHA512VS2 = SHA512VL[1]+'.'+SHA512VL[2]+'x'
            algList.append(SHA512VS)

            # Dagger
            DaggerV = pytesseract.image_to_string(f'algDir\\Dagger.png')
            DaggerVL = re.findall(r'\d+', DaggerV)
            DaggerVS = DaggerVL[0]+DaggerVL[1]
            DaggerVS2 = DaggerVL[0]+'.'+DaggerVL[1]+'x'
            algList.append(DaggerVS)

            # Scrypt
            ScryptV = pytesseract.image_to_string(f'algDir\\Scrypt.png')
            ScryptVL = re.findall(r'\d+', ScryptV)
            ScryptVS = ScryptVL[0]+ScryptVL[1]
            ScryptVS2 = ScryptVL[0]+'.'+ScryptVL[1]+'x'
            algList.append(ScryptVS)

            # Bloxchain
            BloxchainV = pytesseract.image_to_string(f'algDir\\Bloxchain.png')
            BloxchainVL = re.findall(r'\d+', BloxchainV)
            BloxchainVS = BloxchainVL[0]+BloxchainVL[1]
            BloxchainVS2 = BloxchainVL[0]+'.'+BloxchainVL[1]+'x'
            algList.append(BloxchainVS)
            
            #print(SHA512VS, DaggerVS, ScryptVS, BloxchainVS)

            if SHA512VS == max(algList):
                if bestAlg != 'SHA-512':
                    print('\n')
                    print('Il miglior algoritmo è SHA-512 con {}'.format(SHA512VS2))
                    bestAlg = 'SHA-512'
                    if every > 2.0:
                        mouse.move(1323, 1060, True, 0)
                        mouse.click('left')
                        time.sleep(0.1)
                        mouse.move(1365, 670, True, 1)
                        mouse.click('left')
                        mouse.click('left')
                    else:
                        mouse.move(1323, 1060, True, 0)
                        mouse.click('left')
                        time.sleep(0.1)
                        mouse.move(1365, 670, True, 0)
                        mouse.click('left')
                        mouse.click('left')

            elif DaggerVS == max(algList):
                if bestAlg != 'Dagger':
                    print('\n')
                    print('Il miglior algoritmo è Dagger con {}'.format(DaggerVS2))
                    bestAlg = 'Dagger'
                    if every > 2.0:
                        mouse.move(1323, 1060, True, 0)
                        mouse.click('left')
                        time.sleep(0.1)
                        mouse.move(1365, 725, True, 1)
                        mouse.click('left')
                        mouse.click('left')
                    else:
                        mouse.move(1323, 1060, True, 0)
                        mouse.click('left')
                        time.sleep(0.1)
                        mouse.move(1365, 725, True, 0)
                        mouse.click('left')
                        mouse.click('left')

            elif ScryptVS == max(algList):
                if bestAlg != 'Scrypt':
                    print('\n')
                    print('Il miglior algoritmo è Scrypt con {}'.format(ScryptVS2))
                    bestAlg = 'Scrypt'
                    if every > 2.0:
                        mouse.move(1323, 1060, True, 0)
                        mouse.click('left')
                        time.sleep(0.1)
                        mouse.move(1365, 775, True, 1)
                        mouse.click('left')
                        mouse.click('left')
                    else:
                        mouse.move(1323, 1060, True, 0)
                        mouse.click('left')
                        time.sleep(0.1)
                        mouse.move(1365, 775, True, 0)
                        mouse.click('left')
                        mouse.click('left')

            elif BloxchainVS == max(algList):
                if bestAlg != 'Bloxchain':
                    print('\n')
                    print('Il miglior algoritmo è Bloxchain con {}'.format(BloxchainVS2))
                    bestAlg = 'Bloxchain'
                    if every > 2.0:
                        mouse.move(1323, 1060, True, 0)
                        mouse.click('left')
                        time.sleep(0.1)
                        mouse.move(1365, 830, True, 1)
                        mouse.click('left')
                        mouse.click('left')
                    else:
                        mouse.move(1323, 1060, True, 0)
                        mouse.click('left')
                        time.sleep(0.1)
                        mouse.move(1365, 830, True, 0)
                        mouse.click('left')
                        mouse.click('left')

            else:
                pass
        except: traceback.print_exc()
            

        runAFK = True

        time.sleep(every)

algCT = threading.Thread(target=algC)
algCT.daemon = True
algCT.start()

while True:
    if runAFK == True:
        keyboard.press("w")
        time.sleep(0.08)
        keyboard.release("w")
        time.sleep(0.2)
        keyboard.press("s")
        time.sleep(0.08)
        keyboard.release("s")
        time.sleep(0.2)
    else:
        keyboard.release("w")
        keyboard.release("s")