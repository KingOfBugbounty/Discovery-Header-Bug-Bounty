# Search Headers DoD Priv8
# @OFJAAAH & @wellpunk
 

import requests
from colorama import Fore, Style
import sys
import argparse

#Parser
parser = argparse.ArgumentParser()
parser.add_argument("help", help="Run to code = python3 searchHEADER.py FileToUrls ")
args = parser.parse_args()

def headersURL():

    with open(file, 'r') as arquivo:
        dominios = arquivo.read().split('\n')[:-1]
    with open('results.txt', 'w') as fp:
       
        for url in dominios:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
            try:
                r = requests.get(url, headers=headers)
                print(f"{Fore.RED}{r.headers['server'] if r.headers['server'] else 'none'}{Style.RESET_ALL}:{url}")
                fp.write(f"{r.headers['server'] if r.headers['server'] else 'none'}:{url}\n")
            except:
                pass

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        headersURL()

    except Exception as e:
        print(f"{Fore.RED}[!]{Style.RESET_ALL} Please pass a file with url's as argument")
        exit(-1)