"""
Click Bot for "The Perfect Tower"
Link: https://www.fs-studios.com/games/perfecttower/

Need program to upgrade offensive, defensive, and utility abilities of the tower constantly on a loop.
Upgrade the basic options in each category before the other ones.
Open the laboratory tab to research every 2 minutes. (Make sure it doesn't click already researching buttons as it will reset the timer)
Loop code and game should play itself.
"""
import pyautogui as p
import time as t


# p.mouseInfo()
run = True

# time when code begins
time1 = t.time()

# loops forever
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

    # time when it reaches this part of the code
    time2 = t.time()

    # if 2 minutes have passed since the start run the loop
    if time2 >= time1 + 120:
        # laboratory tab, research upgrades
        p.click(x=1023, y=636)

        t.sleep(0.5)
        # clicks button to upgrade if color matches because if it doesn't match it means it's unavailable/already upgrading 
        # pressing it when it's already upgrading will cause the timer to reset
        if p.pixelMatchesColor(480, 296, (163, 200, 154)):
            p.click(x=487, y=293)
        if p.pixelMatchesColor(494, 333, (164, 201, 155)):
            p.click(x=472, y=332)
        # sets a new time1 so the next time it clicks the research tab it will be 2 minutes after the last
        time1 = t.time()
    else:
        pass

    t.sleep(1)
