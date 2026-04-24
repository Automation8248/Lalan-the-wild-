import os
import random
import requests
import datetime
import re
import time

# ==========================================
# 1. UNIVERSAL TITLES (NO Hashtags/Stars)
# ==========================================
UNIVERSAL_TITLES = [
    "Majestic King of the Jungle", "Fierce Predators in Action", "Beautiful Wildlife Photography",
    "Elephants Roaming the Savanna", "A Glimpse into the Wild", "Nature and Its Fiercest Creations",
    "Wild Animals in Their Natural Habitat", "The Beauty of the Animal Kingdom", "Stunning Safari Sights",
    "Graceful Cheetah on the Run", "The Raw Power of Nature", "Incredible Wildlife Moments",
    "Lions Pride in the Wild", "Tigers Prowling the Forest", "Wild and Free", "Amazing Animal Portraits",
    "The Wonders of the Wilderness", "Captivating Wildlife Shots", "Survival in the Wild",
    "Magnificent Beasts of the Earth", "The Great Migration Up Close", "Wild Animals Striking a Pose",
    "Nature Photography at Its Best", "The Spirit of the Wild", "Fascinating Jungle Life",
    "Unleashing the Wild", "Wonders of the Animal World", "Raw and Untamed Beauty",
    "Grace and Power Combined", "Epic Wildlife Encounters", "Kings and Queens of the Wild",
    "A Journey Through the Jungle", "Discovering Wild Habitats", "The Art of Camouflage",
    "Majestic Creatures of the Earth", "Wild Instincts on Display", "Nature's Perfect Hunters",
    "Serenity in the Wilderness", "The Circle of Life", "Breathtaking Safari Adventures",
    "Untamed Nature at Its Finest", "Incredible Beasts in the Wild", "The Beauty of Predators",
    "Wilderness Exploration", "Spectacular Animal Kingdom", "The Heart of the Jungle",
    "A Look at the Wild Side", "Fierce and Beautiful", "Animals in Their Element",
    "Stunning Creatures of the Wild", "The Majesty of the Savannah", "Wilderness Unplugged",
    "Capturing the Untamed", "The Magic of Wildlife", "Roam Free", "Wildlife Wonders Revealed"
]

# ==========================================
# 2. UNIVERSAL CAPTIONS (NO Hashtags/Stars)
# ==========================================
UNIVERSAL_CAPTIONS = [
    "Witness the raw beauty of nature and its majestic creatures.",
    "A stunning glimpse into the animal kingdom.",
    "Wildlife photography at its absolute best.",
    "Nature never ceases to amaze with these incredible animals.",
    "The power and grace of wild animals are truly unmatched.",
    "Every creature plays a vital role in the wild ecosystem.",
    "Capturing the untamed spirit of the wilderness.",
    "An unforgettable moment from the heart of the jungle.",
    "The animal kingdom is full of fascinating surprises.",
    "Observing these magnificent beasts in their natural habitat.",
    "There is something deeply calming about watching wild animals.",
    "Nature is the greatest artist, and these animals are the masterpiece.",
    "A breathtaking view of survival and beauty in the wild.",
    "These majestic animals remind us of the power of the natural world.",
    "Exploring the untamed corners of the earth and its inhabitants.",
    "The wild is calling, and its beauty is absolutely captivating.",
    "Just a beautiful moment shared with the creatures of the wild.",
    "Fierce, free, and absolutely magnificent.",
    "The wonders of wildlife never fail to leave us speechless.",
    "A perfect capture of life in the untamed wilderness.",
    "Experiencing the sheer majesty of wild animals up close.",
    "This is what pure, unedited nature looks like.",
    "Every detail of this magnificent creature is absolutely perfect.",
    "The beauty of the wild is something that must be protected.",
    "A raw and authentic look at life in the animal kingdom.",
    "The wilderness holds some of the most breathtaking sights on earth.",
    "Grace, power, and instinct beautifully combined.",
    "A truly incredible wildlife encounter caught on camera.",
    "The fascinating behavior of wild animals in their natural element.",
    "Nature showcases its ultimate predators and gentle giants.",
    "There is endless beauty to be found in the untamed world.",
    "An incredible display of nature's finest creations.",
    "The serenity and danger of the wild perfectly balanced.",
    "A majestic creature owning its territory in the wild.",
    "This remarkable animal is a true testament to the wonders of nature."
]

# ==========================================
# 3. PLATFORM SPECIFIC SEO TAGS 
# ==========================================
def get_platform_tags():
    fb_tags = "#Wildlife #WildAnimals #NaturePhotography #AnimalKingdom #Safari #WildlifePlanet"
    ig_tags = "#WildlifeIG #NatureLovers #Wilderness #AnimalsOfInstagram #WildlifePerfection #JungleLife"
    yt_tags = "#WildlifeDocumentary #Animals #NatureShorts #WildLife #Jungle #AnimalShorts"
    return fb_tags, ig_tags, yt_tags

QUERIES = [
    "wild animals nature", "lion in wild savanna", "tiger hunting jungle", 
    "elephants migrating", "majestic wildlife photography", "cheetah running wild", 
    "leopard resting on tree", "wolf pack in snow", "rhino wild safari",
    "beautiful wild birds", "wildlife predator and prey"
]

import os
import random
import requests
import datetime
import re
import time

# ==========================================
# 1. UNIVERSAL TITLES (NO Hashtags/Stars)
# ==========================================
UNIVERSAL_TITLES = [
    "Majestic King of the Jungle", "Fierce Predators in Action", "Beautiful Wildlife Photography",
    "Elephants Roaming the Savanna", "A Glimpse into the Wild", "Nature and Its Fiercest Creations",
    "Wild Animals in Their Natural Habitat", "The Beauty of the Animal Kingdom", "Stunning Safari Sights",
    "Graceful Cheetah on the Run", "The Raw Power of Nature", "Incredible Wildlife Moments",
    "Lions Pride in the Wild", "Tigers Prowling the Forest", "Wild and Free", "Amazing Animal Portraits",
    "The Wonders of the Wilderness", "Captivating Wildlife Shots", "Survival in the Wild",
    "Magnificent Beasts of the Earth", "The Great Migration Up Close", "Wild Animals Striking a Pose",
    "Nature Photography at Its Best", "The Spirit of the Wild", "Fascinating Jungle Life",
    "Unleashing the Wild", "Wonders of the Animal World", "Raw and Untamed Beauty",
    "Grace and Power Combined", "Epic Wildlife Encounters", "Kings and Queens of the Wild",
    "A Journey Through the Jungle", "Discovering Wild Habitats", "The Art of Camouflage",
    "Majestic Creatures of the Earth", "Wild Instincts on Display", "Nature's Perfect Hunters",
    "Serenity in the Wilderness", "The Circle of Life", "Breathtaking Safari Adventures",
    "Untamed Nature at Its Finest", "Incredible Beasts in the Wild", "The Beauty of Predators",
    "Wilderness Exploration", "Spectacular Animal Kingdom", "The Heart of the Jungle",
    "A Look at the Wild Side", "Fierce and Beautiful", "Animals in Their Element",
    "Stunning Creatures of the Wild", "The Majesty of the Savannah", "Wilderness Unplugged",
    "Capturing the Untamed", "The Magic of Wildlife", "Roam Free", "Wildlife Wonders Revealed"
]

# ==========================================
# 2. UNIVERSAL CAPTIONS (NO Hashtags/Stars)
# ==========================================
UNIVERSAL_CAPTIONS = [
    "Witness the raw beauty of nature and its majestic creatures.",
    "A stunning glimpse into the animal kingdom.",
    "Wildlife photography at its absolute best.",
    "Nature never ceases to amaze with these incredible animals.",
    "The power and grace of wild animals are truly unmatched.",
    "Every creature plays a vital role in the wild ecosystem.",
    "Capturing the untamed spirit of the wilderness.",
    "An unforgettable moment from the heart of the jungle.",
    "The animal kingdom is full of fascinating surprises.",
    "Observing these magnificent beasts in their natural habitat.",
    "There is something deeply calming about watching wild animals.",
    "Nature is the greatest artist, and these animals are the masterpiece.",
    "A breathtaking view of survival and beauty in the wild.",
    "These majestic animals remind us of the power of the natural world.",
    "Exploring the untamed corners of the earth and its inhabitants.",
    "The wild is calling, and its beauty is absolutely captivating.",
    "Just a beautiful moment shared with the creatures of the wild.",
    "Fierce, free, and absolutely magnificent.",
    "The wonders of wildlife never fail to leave us speechless.",
    "A perfect capture of life in the untamed wilderness.",
    "Experiencing the sheer majesty of wild animals up close.",
    "This is what pure, unedited nature looks like.",
    "Every detail of this magnificent creature is absolutely perfect.",
    "The beauty of the wild is something that must be protected.",
    "A raw and authentic look at life in the animal kingdom.",
    "The wilderness holds some of the most breathtaking sights on earth.",
    "Grace, power, and instinct beautifully combined.",
    "A truly incredible wildlife encounter caught on camera.",
    "The fascinating behavior of wild animals in their natural element.",
    "Nature showcases its ultimate predators and gentle giants.",
    "There is endless beauty to be found in the untamed world.",
    "An incredible display of nature's finest creations.",
    "The serenity and danger of the wild perfectly balanced.",
    "A majestic creature owning its territory in the wild.",
    "This remarkable animal is a true testament to the wonders of nature."
]

# ==========================================
# 3. PLATFORM SPECIFIC SEO TAGS 
# ==========================================
def get_platform_tags():
    fb_tags = "#Wildlife #WildAnimals #NaturePhotography #AnimalKingdom #Safari #WildlifePlanet"
    ig_tags = "#WildlifeIG #NatureLovers #Wilderness #AnimalsOfInstagram #WildlifePerfection #JungleLife"
    yt_tags = "#WildlifeDocumentary #Animals #NatureShorts #WildLife #Jungle #AnimalShorts"
    return fb_tags, ig_tags, yt_tags

QUERIES = [
    "wild animals nature", "lion in wild savanna", "tiger hunting jungle", 
    "elephants migrating", "majestic wildlife photography", "cheetah running wild", 
    "leopard resting on tree", "wolf pack in snow", "rhino wild safari",
    "beautiful wild birds", "wildlife predator and prey"
]

HISTORY_FILE = "history.txt"

# ==========================================
# 4. HELPER FUNCTIONS
# ==========================================
def get_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return set(f.read().splitlines())
    return set()

def save_history(url):
    with open(HISTORY_FILE, "a") as f:
        f.write(url + "\n")

# ==========================================
# 5. MAIN AUTOMATION LOGIC (BING ONLY + DIRECT URL)
# ==========================================
def run_automation():
    history = get_history()
    base_query = random.choice(QUERIES)
    
    # Pick random Title and Caption
    selected_title = random.choice(UNIVERSAL_TITLES)
    selected_caption = random.choice(UNIVERSAL_CAPTIONS)
    fb_tags, ig_tags, yt_tags = get_platform_tags()
    
    search_query = f"{base_query} high resolution {random.randint(1, 1000)}"
    print(f"🚀 Searching Bing for: '{search_query}'")

    # Adding human-like behavior logic to avoid platform blocks
    human_delay = random.uniform(1.5, 4.0)
    print(f"⏳ Waiting {human_delay:.2f} seconds to simulate human behavior...")
    time.sleep(human_delay)

    # Custom Bing Image Search Logic with robust headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    search_url = f"https://www.bing.com/images/search?q={search_query}"
    
    try:
        response = requests.get(search_url, headers=headers)
        
        # Bing HTML se direct Image URL nikalna
        image_urls = re.findall(r'murl&quot;:&quot;(.*?)&quot;', response.text)
        if not image_urls:
            image_urls = re.findall(r'murl":"(.*?)"', response.text)
            
        if not image_urls:
            print("❌ No images found on Bing for this query.")
            return

        success = False
        
        # Loop chala kar pehli 'Fresh' image process karenge
        for img_url in image_urls:
            if img_url.startswith("http") and img_url not in history:
                print(f"✅ Found New Unique Bing Image URL: {img_url}")
                
                try:
                    # Telegram remove kar diya gaya hai, isliye local image download block bhi hata diya gaya hai taaki script fast chale.
                    
                    # --- CURRENT DATE, DAY, AND TIME LOGIC ---
                    now = datetime.datetime.now()
                    current_day = now.strftime("%A")            
                    current_date = now.strftime("%d-%B-%Y")     
                    current_time = now.strftime("%H:%M:%S")     

                    # --- SEND TO WEBHOOK (Full Data + URL!) ---
                    webhook_url = os.getenv("WEBHOOK_URL")
                    if webhook_url:
                        payload = {
                            "image_url": img_url,  
                            "title": selected_title,
                            "caption": selected_caption,
                            "facebook_tags": fb_tags,
                            "instagram_tags": ig_tags,
                            "youtube_tags": yt_tags,
                            "status": "Success_BING",
                            "run_day": current_day,
                            "run_date": current_date,
                            "run_time": current_time
                        }
                        requests.post(webhook_url, json=payload)
                        print("🔗 Sent full data + Bing Image URL to Webhook.")
                    else:
                        print("⚠️ WEBHOOK_URL environment variable is missing.")

                    # Save the URL to history so it never repeats
                    save_history(img_url)
                    
                    success = True
                    break # STRICTLY 1 Image process karega aur loop band kar dega
                    
                except Exception as e:
                    print(f"⚠️ Error with this specific image, trying next: {e}")
                    continue 

        if not success:
            print("❌ All scraped images were either already used or invalid.")
            
    except Exception as e:
        print(f"❌ Critical Error searching Bing: {e}")

if __name__ == "__main__":
    run_automation()
