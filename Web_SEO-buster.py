import os
import sys
import time
import random
import subprocess
import urllib.parse
from datetime import datetime

# ==========================================
# AUTO-INSTALLER
# ==========================================
def install_requirements():
    required_libs = ["requests", "beautifulsoup4", "colorama"]
    for lib in required_libs:
        try:
            __import__(lib if lib != "beautifulsoup4" else "bs4")
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

install_requirements()

try:
    import requests
    from bs4 import BeautifulSoup
    from colorama import init, Fore, Style
    init(autoreset=True)
except Exception:
    pass

# ==========================================
# SEO CONFIGURATION (Yahan Setup Karein)
# ==========================================
MY_WEBSITE = "example.com"  # <--- Yahan apni website ka naam likhein (bina https ke)
FILE_NAME = "keywords.txt"   # Keywords ki file

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Version/16.5 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) Chrome/112.0.0.0 Mobile Safari/537.36"
]

class SEOBot:
    def log(self, msg, status="INFO"):
        t = datetime.now().strftime("%H:%M:%S")
        if status == "FOUND":
            print(Fore.GREEN + Style.BRIGHT + f"[{t}] {msg}")
        elif status == "ERROR":
            print(Fore.RED + f"[{t}] {msg}")
        else:
            print(Fore.CYAN + f"[{t}] {msg}")

    def google_search(self, keyword):
        """Sirf Search karega aur aapki site dhundega"""
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }
        
        # Google Search URL
        query = urllib.parse.quote(keyword)
        url = f"https://www.google.com/search?q={query}&num=20" # Top 20 results layega
        
        self.log(f"🔍 Searching Keyword: '{keyword}'", "INFO")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # Check agar hamari website result mein hai
                if MY_WEBSITE in response.text:
                    self.log(f"  ✅ SUCCESS! '{MY_WEBSITE}' search results mein mil gayi!", "FOUND")
                else:
                    self.log(f"  ❌ Not Found: '{MY_WEBSITE}' top 20 mein nahi hai.", "ERROR")
                
                # Human Waiting Time
                wait = random.uniform(5, 10)
                time.sleep(wait)
            else:
                self.log(f"  ⚠️ Google blocked request (Status: {response.status_code})", "ERROR")
                
        except Exception as e:
            self.log(f"  ⚠️ Error: {e}", "ERROR")

def run_seo_bot():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + "=== SEO SEARCH VOLUME BOOSTER ===")
    print(Fore.YELLOW + f"Target Site: {MY_WEBSITE}\n")

    # File Check
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            f.write("python tutorial\nbest coding tips\nlearn seo")
        print(f"File created: {FILE_NAME}. Please add keywords inside it.")
        return

    # Loop
    while True:
        with open(FILE_NAME, "r") as f:
            keywords = [k.strip() for k in f.readlines() if k.strip()]
        
        random.shuffle(keywords)
        
        for keyword in keywords:
            bot = SEOBot()
            bot.google_search(keyword)
        
        print(Fore.MAGENTA + "\nAll keywords done. Resting for 2 mins...\n")
        time.sleep(120) 

if __name__ == "__main__":
    run_seo_bot()

