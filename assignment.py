import pyautogui as p
import time as t

# p.mouseInfo()
run = True

time1 = t.time()

while run == True:

    # offense tab, upgrade atk dmg and atk spd
    p.click(x=413, y=635)
    p.click(x=627, y=193)
    p.click(x=618, y=234)

    t.sleep(1)

    # defensive tab, upgrade hp and hp regen
    p.click(x=493, y=632)
    p.click(x=627, y=193)
    p.click(x=618, y=234)

    t.sleep(1)

    # utility tab, upgrade resource % bonus and resource per wave
    p.click(x=574, y=637)
    p.click(x=627, y=193)
    p.click(x=618, y=234)

    t.sleep(1)

    # offense tab, upgrade crit chance, crit dmg, and atk range
    p.click(x=413, y=635)
    p.click(x=622, y=282)
    p.click(x=633, y=328)
    p.click(x=620, y=368)

    t.sleep(1)

    # defensive tab, upgrade absolute def and relative defense
    p.click(x=493, y=632)
    #p.click(x=622, y=282)
    p.click(x=633, y=328)

    t.sleep(1)

    # utility tab, upgrade special resource income and bonus special resource %
    p.click(x=574, y=637)
    p.click(x=622, y=282)
    #p.click(x=633, y=328)

    t.sleep(1)

    time2 = t.time()
    if time2 >= time1 + 10:
        # laboratory tab, research upgrades
        p.click(x=1023, y=636)
        t.sleep(0.5)
        if p.pixelMatchesColor(480, 296, (163, 200, 154)):
            p.click(x=487, y=293)
        if p.pixelMatchesColor(494, 333, (164, 201, 155)):
            p.click(x=472, y=332)

        time1 = t.time()
    else:
        pass

    t.sleep(1)
