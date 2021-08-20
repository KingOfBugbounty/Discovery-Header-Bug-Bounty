# Search Headers DoD Priv8
# @OFJAAAH & @wellpunk
# Script Server Banner

import requests
from colorama import Fore, Style
from threading import Thread
import argparse

# Parser
parser = argparse.ArgumentParser(description="Run to code = python3 searchHEADER.py FileToUrls ")
parser.add_argument(
    "-f", "--file", metavar="", help="define a file")
parser.add_argument(
    "-t", "--threads", metavar="", default="2", help="Define a number of threads [ Default 2 ]")
parser.add_argument(
    "-o", "--output", metavar="", default="result.txt", help="output in txt [ Default result.txt ]")
args = parser.parse_args()

def parser_file_urls(file):
    with open(file, 'r') as arquivo:
        dominios = arquivo.read().split('\n')[:-1]
        for dominio in dominios:
            all_urls.append(dominio)

def headersURL():
    while len(all_urls) != 0:
        url = all_urls[0]
        all_urls.remove(url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        try:
            r = requests.get(url, headers=headers)
            print(
                f"{Fore.RED}{r.headers['server'] if r.headers['server'] else 'none'}{Style.RESET_ALL}:{url}")
            string = f"{r.headers['server'] if r.headers['server'] else 'none'}:{url}"
            save_urls(string)
        except:
            pass


def save_urls(url):
    with open(f"{args.output}", "a") as file:
        file.write(url + "\n")


def all_threads(number_threads):
    controler = 0
    for thread in range(0 + int(number_threads)):
        Thread(target=headersURL).start()
        controler += 1


if __name__ == "__main__":
    all_urls = [] # Controler for threads
    file = args.file
    number_of_threads = args.threads
    try:
        parser_file_urls(file)
        all_threads(number_of_threads)

    except Exception as e:
        print(
            f"{Fore.RED}[!]{Style.RESET_ALL} Please pass a file with url's as argument")
        exit(-1)
