from flask import Flask
import pandas as pd
import requests
import wget
import os
import subprocess 
from selenium import webdriver
app = Flask(__name__)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(threadName)s] %(message)s",
)
WEBHOOK_URL = "https://cloud.activepieces.com/api/v1/webhooks/h40XOlvtPd8efwh4fKpzw/"

# Example HTML input
worker_code = """
<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body>
    <h1>Hello World</h1>
    <p>This is a simple HTML test.</p>
</body>
</html>
"""

def extract_h1_and_body(html):
    soup = BeautifulSoup(html, "html.parser")

    # Extract H1
    h1_tag = soup.find("h1")
    h1_text = h1_tag.get_text(strip=True) if h1_tag else None

    # Extract body HTML
    body_tag = soup.find("body")
    body_html = body_tag.decode_contents() if body_tag else ""

    return h1_text, body_html

# Extract data

import zipfile
import os
print(os.getcwd(),os.listdir())
url = "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip"
zip_path = "chromedriver.zip"
extract_dir = "chromedriver"

# Download using wget library
print("⬇️ Downloading...")
wget.download(url, zip_path)

# Extract zip
print("\n📦 Extracting...")
os.makedirs(extract_dir, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Give execution permission (Linux/Mac)
driver_path = os.path.join(extract_dir, "chromedriver")
if os.path.exists(driver_path):
    os.chmod(driver_path, 0o755)
print(os.getcwd(),os.listdir())
print("✅ Done! ChromeDriver ready.")
import traceback

def hello_world():
      

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1280,2000")
        driver1 = webdriver.Chrome(service=Service(), options=chrome_options)
        driver1.get("https://www.python.org")
        h1_text, body_html = extract_h1_and_body(worker_code)

# Send to webhook
        data = {
    "text1": "test",
    "text2": driver1.page_source   # <-- real HTML here
         }

        response = requests.post(WEBHOOK_URL, json=data)

        print("Status:", response.status_code)
        print("Response:", response.text)
   
    except :
        print(traceback.print_exc())



    

@app.route('/task/<string:name>')
def task(name):
 return subprocess.getoutput(name)
@app.route('/start')
def taskgetready():
 wget.download("https://testi123.pythonanywhere.com/static/9854758/key")   
 wget.download("https://testi123.pythonanywhere.com/static/9854758/key.pub") 
 text=""   
 text=text+"<br>"+subprocess.getoutput("chmod 600 key")
 text=text+"<br>"+subprocess.getoutput("chmod 600 key.pub")
 text=text+"<br>"+subprocess.getoutput("ssh-agent ssh-add key")
 text=text+"<br>"+subprocess.getoutput("git clone https://github.com/misterbahaehmimdi/flask-hello-world")   

 text=text+"<br>"+subprocess.getoutput("git config --global user.signingkey key.pub")

 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git remote add bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git remote set-url bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")


 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git config --global user.email 'bahae-123@hotmail.com'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git config --global user.name 'misterbahaehmimdi'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git add .")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git status")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git commit -m 'bahae'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git push origin master")
 return text 
@app.route('/sync')
def sync():
 text=""
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git remote add bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git remote set-url bahaeelhmimdi git@github.com:misterbahaehmimdi/flask-hello-world.git")
    
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git config --global user.email 'bahae-123@hotmail.com'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git config --global user.name 'bahaeelhmimdi'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git add .")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git status")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git commit -m 'bahae'")
 text=text+"<br>"+subprocess.getoutput("cd flask-hello-world;git push bahaeelhmimdi master")
 return text 

erros=[]
@app.route('/clone/')
def clone():
    subprocess.getoutput("git clone https://github.com/misterbahaehmimdi/flask-hello-world")
    return "done"
@app.route('/eros/')
def err():
    return str(erros)
@app.route('/check/check')
def check():
    lis=[]
    wget.download("https://testi123.pythonanywhere.com/static/datacheck.xlsx")
    data = pd.read_excel("datacheck.xlsx")
    al=list(data.iterrows())
    lal=len(al)
    for index2,d1 in al[:int(lal/4)]:
     try:
      nm=d1['name']
      print("-+-+-+",nm,"-+-+-+-+",d1['name']) 

      if not type(nm)==type(""):
         nm=str(nm)
      wget.download("https://testi123.pythonanywhere.com/static/data"+nm+".xlsx")       
      data2 = pd.read_excel("data"+nm+".xlsx")
      
       
      rr=requests.get(d1['url']).text
     
      for index2,d2 in data2.iterrows():
       try: 
        if not type(d2['text'])==type(""):
            continue
        if d2['text'].replace("\n","#012") in rr.replace("\\n","#012").replace("\#012","#012"):
        # d2['statut']=1
         data2.loc[index2, 'statut'] =1
        else:
         data2.loc[index2, 'statut'] =0
  
        # d2['statut']=0
        
       except Exception as eror:
        lis.append({"name":nm,"url":d1['url'],"text":d2['text'],"error":str(eror)})
        print("----",lis)
      data2.to_excel("data"+nm+".xlsx",index=False) 
      if True:   
       
       url = 'https://testi123.pythonanywhere.com/remplacer_xlsx/'+nm
       files = {'file': open('data'+nm+'.xlsx', 'rb')}

       r = requests.post(url, files=files)
       del data2 
     except Exception as first:
                lis.append({"url":d1['url'],"name":d1['name']   })
                print("++++",lis)
     erros.append(lis)
    return "done"
from flask import request, jsonify, send_from_directory
import cv2
import time

VIDEO_FOLDER = "videos"
FRAME_FOLDER = "frames"

os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(FRAME_FOLDER, exist_ok=True)

import traceback

from flask import request, jsonify, send_from_directory
from playwright.sync_api import sync_playwright
import cv2
import os

VIDEO_FOLDER = "videos"
FRAME_FOLDER = "frames"

os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(FRAME_FOLDER, exist_ok=True)

import traceback
@app.route('/create-video', methods=['POST'])
def create_video():
  os.makedirs(VIDEO_FOLDER, exist_ok=True)
  os.makedirs(FRAME_FOLDER, exist_ok=True)  
  try:    
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL required"}), 400

    # Clean frames
    for f in os.listdir(FRAME_FOLDER):
        os.remove(os.path.join(FRAME_FOLDER, f))

    frames = []

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 2000})

        page.goto(url, timeout=60000)
        page.wait_for_timeout(3000)

        total_height = page.evaluate("document.body.scrollHeight")

        step = 300
        frame_id = 0

        for y in range(0, total_height, step):
            page.evaluate(f"window.scrollTo(0, {y})")
            page.wait_for_timeout(200)

            path = os.path.join(FRAME_FOLDER, f"frame_{frame_id}.png")
            page.screenshot(path=path)
            frames.append(path)

            frame_id += 1

        browser.close()

    # Create video
    video_path = os.path.join(VIDEO_FOLDER, "output.mp4")

    first = cv2.imread(frames[0])
    height, width, _ = first.shape

    out = cv2.VideoWriter(
        video_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        10,
        (width, height)
    )

    for f in frames:
        img = cv2.imread(f)
        out.write(img)

    out.release()
    return jsonify({
        "video_url": "/video/output.mp4"
    })
  except Exception as error:  
   return jsonify({
        "error": str(traceback.format_exc())
    })

@app.route('/video/<filename>')
def serve_video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)
 

def create_video1():
    import traceback
    import time
    import uuid

    task_id = str(uuid.uuid4())[:8]  # short ID for tracking logs
    logging.info(f"[{task_id}] Request received")

    os.makedirs(VIDEO_FOLDER, exist_ok=True)
    os.makedirs(FRAME_FOLDER, exist_ok=True)

    try:
    

        url = "https://hubspot.bahaedev.com/blog/lart_de_la_conversion_avec_bahaedev"

        if not url:
            logging.warning(f"[{task_id}] Missing URL")
            return jsonify({"error": "URL is required"}), 400

        logging.info(f"[{task_id}] Processing URL: {url}")

        # Clean folders
        logging.info(f"[{task_id}] Cleaning frame folder")
        for f in os.listdir(FRAME_FOLDER):
            os.remove(os.path.join(FRAME_FOLDER, f))

        # Setup browser
        logging.info(f"[{task_id}] Starting Chrome")

        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1024, 600")

        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        driver.set_window_size(1024, 600)

        logging.info(f"[{task_id}] Opening page")
        driver.get(url)

        time.sleep(3)

        total_height = driver.execute_script("return document.body.scrollHeight")
        logging.info(f"[{task_id}] Page height: {total_height}")

        scroll_step = 300
        frames = []

        current = 0
        frame_count = 0

        logging.info(f"[{task_id}] Starting scrolling & screenshots")

        while current < total_height:
            driver.execute_script(f"window.scrollTo(0, {current});")
            time.sleep(0.2)

            path = os.path.join(FRAME_FOLDER, f"frame_{frame_count}.png")
            driver.save_screenshot(path)
            frames.append(path)

            if frame_count % 10 == 0:
                logging.info(f"[{task_id}] Captured frame {frame_count}")

            current += scroll_step
            frame_count += 1

        logging.info(f"[{task_id}] Total frames: {len(frames)}")

        # Create video
        video_path = os.path.join(VIDEO_FOLDER, "output.mp4")
        logging.info(f"[{task_id}] Creating video: {video_path}")

        first_frame = cv2.imread(frames[0])
        height, width, _ = first_frame.shape

        out = cv2.VideoWriter(
            video_path,
            cv2.VideoWriter_fourcc(*'mp4v'),
            10,
            (width, height)
        )

        for i, frame in enumerate(frames):
            img = cv2.imread(frame)
            out.write(img)

            if i % 10 == 0:
                logging.info(f"[{task_id}] Writing frame {i}")

        out.release()
        logging.info(f"[{task_id}] Video created successfully")

        # Send webhook
        logging.info(f"[{task_id}] Sending webhook")

        data = {
            "text1": "https://bahaedev.onrender.com/video/output.mp4",
            "text2": driver.page_source
        }

        response = requests.post(WEBHOOK_URL, json=data)
        logging.info(f"[{task_id}] Webhook status: {response.status_code}")

        driver.quit()
        logging.info(f"[{task_id}] Browser closed get your file from https://bahaedev.onrender.com/video/output.mp4")

  

    except Exception:
        error = traceback.format_exc()
        logging.error(f"[{task_id}] ERROR:\n{error}")

   

from threading import Thread



@app.route("/starting")
def starting():
    Thread(target=create_video1).start()
    return "Started"

