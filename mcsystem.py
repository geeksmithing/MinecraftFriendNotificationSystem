import pandas as pd
import time
import requests
import board
import neopixel
# since "mcstatus v9.0.2" you must use JaverServer or BedrockServer not MinecraftServer!
from mcstatus import MinecraftServer


# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
# since "mcstatus v9.0.2" you must use JaverServer or BedrockServer not MinecraftServer!
server = MinecraftServer.lookup("minecraft.geeksmithing.com")

# this enables a test mode to light up all letters at once when unit is powered on.  This was helpful when building the unit
# Set this variable to 0 to disable test mode
# Set this variable to 3 to enable test mode.
# Set this variable to 4 to enable nether test mode
testing = 0


# Nether Mode is a special lighting mode (celebrating the new Nether Update)  when no tracked players are online... when this is set to 0, all letters are set to off instead
nether_mode= 1

# tracking variable for special guest state ** Do not change ***
special_flag = 0

# this number is how often the RPi will ping the Minecraft server to see who is playing. Currently, it is set to every 10 seconds.  Setting this to check too often could result in server lag.
serverQueryInterval=10

# Setup the NeoPixels
pixel_pin = board.D18

# Define the number of pixels in your strip that you are using
num_pixels =49
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=.75, auto_write=False, pixel_order=ORDER)

# Clear LED Strip before continuing and illuminate all letters GREEN to confirm system is up and running
for i in range(num_pixels):
    pixels[i]=(0,255,0)
pixels.show()
time.sleep(5)

# Define all of the colors for the letters here in RGB format
M_color=(100,180,15)
I_color=(255,69,0)
N_color=(255,0,0)
E_color=(0,0,255)
C_color=(45,0,128)
R_color=(1,255,163)
A_color=(0,255,0)
F_color=(255,230,0)
T_color=(255,0,255)

# When no players listed below are detected, it will illuminate all letters with the following... (0,0,0) is not illuminated at all, i.e. OFF ;)
OFF_color=(0,0,0)

# Enter YOUR username here...This causes all offline letters to illuminate bright white when you join the server.  Otherwise, leave it blank like this:  U =[""]
U =["Geeksmithing"]

# Enter one very special guest username here to trigger a special colorful animation to play if they are in the server.  Their presence overrides all other user color status'
SPECIAL  =["Dinnerbone"]

# Define player usernames and their assigned letters in the word MINECRAFT
M =["PickSwitch"]
I =["Geeksmithing"]
N =["NicoleLucente"]
E =["EyesEpicBlue"]
C =["WannabeMaker"]
R =["brokenantler"]
A =["josh_BreaksStuff"]
F =["Wilkebeast"]
T =["lttrotter"]

# Define what individual pixels on the strip define each Letter in MINECRAFT
def M_colorize():
    pixels[0] =M_color
    pixels[1] =M_color
    pixels[30]=M_color
    pixels[31]=M_color
    pixels[32]=M_color
    pixels[33]=M_color
    pixels[34]=M_color
    pixels[35]=M_color
    pixels.show()

def M_colorize_nether():
    pixels[0] =(255,42,0)
    pixels[1] =(255,42,0)
    pixels[30]=(255,162,0)
    pixels[31]=(255,162,0)
    pixels[32]=(255,162,0)
    pixels[33]=(255,220,22)
    pixels[34]=(255,220,22)
    pixels[35]=(255,220,22)
    pixels.show()

def M_off():
    pixels[0] =OFF_color
    pixels[1] =OFF_color
    pixels[30]=OFF_color
    pixels[31]=OFF_color
    pixels[32]=OFF_color
    pixels[33]=OFF_color
    pixels[34]=OFF_color
    pixels[35]=OFF_color
    pixels.show()


def I_colorize():
    pixels[2] =I_color
    pixels[29]=I_color
    pixels[36]=I_color
    pixels.show()

def I_colorize_nether():
    pixels[2] =(255,42,0)
    pixels[29]=(255,162,0)
    pixels[36]=(255,220,22)
    pixels.show()


def I_off():
    pixels[2] =OFF_color
    pixels[29]=OFF_color
    pixels[36]=OFF_color
    pixels.show()

def N_colorize():
    pixels[3] =N_color
    pixels[4] =N_color
    pixels[28]=N_color
    pixels[27]=N_color
    pixels[37]=N_color
    pixels[38]=N_color
    pixels.show()

def N_colorize_nether():
    pixels[3] =(255,42,0)
    pixels[4] =(255,42,0)
    pixels[28]=(255,162,0)
    pixels[27]=(255,162,0)
    pixels[37]=(255,220,22)
    pixels[38]=(255,220,22)
    pixels.show()

def N_off():
    pixels[3] =OFF_color
    pixels[4] =OFF_color
    pixels[28]=OFF_color
    pixels[27]=OFF_color
    pixels[37]=OFF_color
    pixels[38]=OFF_color
    pixels.show()

def E_colorize():
    pixels[5]= E_color
    pixels[6]= E_color
    pixels[25]=E_color
    pixels[26]=E_color
    pixels[39]=E_color
    pixels[40]=E_color

def E_colorize_nether():
    pixels[5] =(255,42,0)
    pixels[6] =(255,42,0)
    pixels[26]=(255,162,0)
    pixels[25]=(255,162,0)
    pixels[39]=(255,220,22)
    pixels[40]=(255,220,22)
    pixels.show()


def E_off():
    pixels[5]= OFF_color
    pixels[6]= OFF_color
    pixels[25]=OFF_color
    pixels[26]=OFF_color
    pixels[39]=OFF_color
    pixels[40]=OFF_color
    pixels.show()

def C_colorize():
    pixels[7] =C_color
    pixels[8] =C_color
    pixels[24]=C_color
    pixels[41]=C_color
    pixels[42]=C_color
    pixels.show()

def C_colorize_nether():
    pixels[7] =(26,130,139)
    pixels[8] =(26,130,139)
    pixels[24]=(69,134,140)
    pixels[41]=(207,218,218)
    pixels[42]=(207,218,218)
    pixels.show()


def C_off():
    pixels[7] =OFF_color
    pixels[8] =OFF_color
    pixels[24]=OFF_color
    pixels[41]=OFF_color
    pixels[42]=OFF_color
    pixels.show()

def R_colorize():
    pixels[9] =R_color
    pixels[10]=R_color
    pixels[22]=R_color
    pixels[23]=R_color
    pixels[43]=R_color
    pixels[44]=R_color

def R_colorize_nether():
    pixels[9] =(26,130,139)
    pixels[10] =(26,130,139)
    pixels[23]=(69,134,140)
    pixels[22]=(69,134,140)
    pixels[43]=(207,218,218)
    pixels[44]=(207,218,218)
    pixels.show()


def R_off():
    pixels[9]= OFF_color
    pixels[10]=OFF_color
    pixels[22]=OFF_color
    pixels[23]=OFF_color
    pixels[43]=OFF_color
    pixels[44]=OFF_color
    pixels.show()

def A_colorize():
    pixels[11]=A_color
    pixels[12]=A_color
    pixels[20]=A_color
    pixels[21]=A_color
    pixels[45]=A_color
    pixels[46]=A_color
    pixels.show()

def A_colorize_nether():
    pixels[11]=(26,130,139)
    pixels[12]=(26,130,139)
    pixels[20]=(69,134,140)
    pixels[21]=(69,134,140)
    pixels[45]=(207,218,218)
    pixels[46]=(207,218,218)
    pixels.show()


def A_off():
    pixels[11]=OFF_color
    pixels[12]=OFF_color
    pixels[20]=OFF_color
    pixels[21]=OFF_color
    pixels[45]=OFF_color
    pixels[46]=OFF_color
    pixels.show()

def F_colorize():
    pixels[13]=F_color
    pixels[14]=F_color
    pixels[18]=F_color
    pixels[19]=F_color
    pixels[47]=F_color
    pixels.show()

def F_colorize_nether():
    pixels[13]=(26,130,139)
    pixels[14]=(26,130,139)
    pixels[18]=(69,134,140)
    pixels[19]=(69,134,140)
    pixels[47]=(207,218,218)
    pixels.show()


def F_off():
    pixels[13]=OFF_color
    pixels[14]=OFF_color
    pixels[18]=OFF_color
    pixels[19]=OFF_color
    pixels[47]=OFF_color
    pixels.show()

def T_colorize():

    pixels[15]=T_color
    pixels[16]=T_color
    pixels[17]=T_color
    pixels[48]=T_color
    pixels.show()

def T_colorize_nether():

    pixels[15]=(26,130,139)
    pixels[16]=(26,130,139)
    pixels[17]=(69,134,140)
    pixels[48]=(207,218,218)
    pixels.show()


def T_off():

    pixels[15]=OFF_color
    pixels[16]=OFF_color
    pixels[17]=OFF_color
    pixels[48]=OFF_color
    pixels.show()

# This bit of code is for the cycling rainbow effect when a special player joins ######
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

# THIS IS THE START OF THE LOOP#####################################
def executeSomething():

# Check to make sure the server is online, if not, flash RED
    counter = 0
    global OFF_color
    global special_flag

    while counter < 3:
        try:
            status = server.status()

            counter = 3
            print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
        except:
            print("encountered error")
            print (counter)
            counter += 1
            if counter >= 3:
                for i in range(num_pixels):
                   pixels[i]=(255,0,0)
                pixels.show()
                print ("error?")
                time.sleep(10)
                for i in range(num_pixels):
                    pixels[i]=OFF_color
                pixels.show()
                time.sleep(5)
                counter = 0
# This is part of the test mode script
    if testing == 0:

        playerList =[]

# Check Number of Players who are on the server and display the names of online players in the console
# If there are no players detected, turn all colors OFF or to Nether colors in case of Nether mode being activated
        if status.players.online < 1:
            if nether_mode ==0:
                print ("No one is playing right now")
                OFF_color =(0,0,0)
                special_flag = 0
                for i in range(num_pixels):
                    pixels[i]=OFF_color
                pixels.show()

            if nether_mode ==1:
                M_colorize_nether()
                I_colorize_nether()
                N_colorize_nether()
                E_colorize_nether()
                C_colorize_nether()
                R_colorize_nether()
                A_colorize_nether()
                F_colorize_nether()
                T_colorize_nether()
                special_flag = 0
                pixels.show()

# this is the bit of the code where it checks to see if the player names in the list of current players matches the entered usernames above
# if it matches, illuminate the letter with the above color definition
# if not, turn off all pixels associated with that letter (if nether mode is not enabled)
# the "print ("X is online")" or offline bit was just for debug/testing purposes. It only prints that to the RPI console


        else:
            print (f"List of players")


            for player in status.players.sample:
                playerList.append(player.name)

            print (playerList)

#  If the special player listed above is detected online, display a fun rainbow fanfare
            if SPECIAL[0] in playerList:
                print ("Special Guest is online!")
                special_flag = 1
                rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
                rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
                rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
                rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
                rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
            else:
                print ("Special Guest is Offline!!")
                special_flag = 0

# begin colorizing of letters based on online status
            if special_flag == 0:
                if U[0] in playerList:
                    print (U[0]," is online")
                    OFF_color =(255,255,255)
                    print ("Current OFF Color is: ", OFF_color)
                else:
                    print (U[0]," is Offline")
                    print("what is happening")
                    OFF_color =(0,0,0)
                    pixels.show()


                if M[0] in playerList:
                    print (M[0]," is online")
                    M_colorize()
                else:
                    M_off()
                    print (M[0]," is Offline")

                if I[0] in playerList:
                    print(I[0]," is online")
                    I_colorize()
                else:
                    I_off()
                    print(I[0]," is Offline")

                if N[0] in playerList:
                    print(N[0]," is online")
                    N_colorize()
                else:
                    N_off()
                    print(N[0]," is Offline")

                if E[0] in playerList:
                    print(E[0]," is online")
                    E_colorize()
                else:
                    E_off()
                    print(E[0]," is Offline")

                if C[0] in playerList:
                    print(C[0]," is online")
                    C_colorize()
                else:
                    C_off()
                    print(C[0]," is Offline")

                if R[0] in playerList:
                    print(R[0]," is online")
                    R_colorize()
                else:
                    R_off()
                    print(R[0]," is Offline")

                if A[0] in playerList:
                    print(A[0]," is online")
                    A_colorize()
                else:
                    A_off()
                    print(A[0]," is Offline")

                if F[0] in playerList:
                    print(F[0]," is online")
                    F_colorize()
                else:
                    F_off()
                    print(F[0]," is Offline")

                if T[0] in playerList:
                    print(T[0]," is online")
                    T_colorize()
                else:
                    T_off()
                    print(T[0]," is Offline")

# this is used to help test nether stuffs

    if testing == 4:

        M_colorize_nether()
        I_colorize_nether()
        N_colorize_nether()
        E_colorize_nether()
        C_colorize_nether()
        R_colorize_nether()
        A_colorize_nether()
        F_colorize_nether()
        T_colorize_nether()

        pixels.show()


    if testing == 3:

# This is a test of all letters and colors at once for diagnostic purposes

        M_colorize()
        I_colorize()
        N_colorize()
        E_colorize()
        C_colorize()
        R_colorize()
        A_colorize()
        F_colorize()
        T_colorize()

# If the special player fanfare goes off, it takes about 10 seconds to complete, so this changes the timing dealing with how often to attempt to re-ping the server
    if special_flag == 1:
        time.sleep(0)
    else:
        time.sleep(serverQueryInterval)
while True:
    executeSomething()
