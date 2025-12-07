"""
Copyright (c) 2025 obitouka
See the file 'LICENSE' for copying permission
"""

from core.accountDataFetcher import fetch_data 
from core.mediaDownloader import download_media
from lib.banner import printBanner
from utils.parser import getArguments

args = getArguments()

if args.name:https://www.instagram.com/_gizoosss?igsh=MTI5Z2tudDNveTdybQ==
    printBanner()
    fetch_data(args.name)
elif args.dload:
    printBanner()
    download_media(args.dload)
