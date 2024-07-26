import os
import re
import time
import base64
import random
import requests
import ctypes
import threading
import telebot
import cfscrape
from string import ascii_letters, digits
from urllib.parse import urlparse
from queue import Queue
from threading import Lock

class DungTuongTheLaHay:
	def __init__(self):
		self.base_url = 'https://zefoy.com/'
		self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "zefoy.com",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }
		self.session = cfscrape.create_scraper()
		self.captcha_1 = None
		self.captcha_ = {}
		self.service = 'Views'
		self.video_key = None
		self.services = {}
		self.services_ids = {}
		self.services_status = {}
		self.dem = 0
		self.total_views = 0
		self.url = 'None'
		self.text = 'VUHOANGPRO'
		self.iceArrow = "\033[1;36m~\033[1;37m[\033[1;36m❆\033[1;37m] \033[1;36m>\033[0;m "
		#linkvid = input(self.iceArrow + "Nhập Link Video: \033[1;36m")
		#self.url = linkvid

	def VuHoangTaDayPro(self):
		if os.path.exists('session'): self.session.cookies.set("PHPSESSID", open('session',encoding='utf-8').read(), domain='zefoy.com')
		request = self.session.get(self.base_url, headers=self.headers)
		if '>Just a moment...<' in request.text:
		    apikey = choice(['6462fad5778f01c3530c971a96f84ad685adfe95', '02ccae8a776e5b7880956a21a24891fb33502bb8', '630aab3e9036d1c1f9db358bef58897abf4186ca'])
		    params = {
                'url': self.base_url,
                'apikey': apikey,
            	'js_render': 'true',
            	'custom_headers': 'true',
            }
		    request = requests.get('https://api.zenrows.com/v1/', params=params, headers=self.headers)
		if 'Enter Video URL' in request.text: self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]; return True

		try:
			for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text): self.captcha_[x[0]] = x[1]

			self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
			captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
			request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
			open('z_captcha_icetool_vip_pro.png', 'wb').write(request.content)
			print("\033[1;36mĐang Xử Lý...", end="\r")
			return False
		except Exception as e:
			print(self.iceArrow + '\033[1;31mLỗi Khi Giải Captcha: ' + str(e))
			time.sleep(2)
			self.VuHoangTaDayPro()

	def TheySayGoSlow(self, new_session = False):
		if new_session: self.session = cfscrape.create_scraper(); os.remove('session'); time.sleep(2)
		if self.VuHoangTaDayPro(): print(self.iceArrow + '\033[1;32mGiải Captcha Success.\033[0;m'); return (True, 'The session already exists')
		captcha_solve = self.WeSayGoGo('z_captcha_icetool_vip_pro.png')[1]
		self.captcha_[self.captcha_1] = captcha_solve
		request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)

		if 'Enter Video URL' in request.text: 
			open('session','w',encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
			#print(self.iceArrow + '\033[1;32mGiải Captcha Success.\033[0;m')
			self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
			return (True,captcha_solve)
		else: return (False,captcha_solve)

	def WeSayGoGo(self, path_to_file = None, b64 = None, delete_tag = ['\n','\r']):
		if path_to_file: task = path_to_file
		else: open('temp.png','wb').write(base64.b64decode(b64)); task = 'temp.png'
		request = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(task,'rb')}).json()
		solved_text = request['ParsedResults'][0]['ParsedText']
		for x in delete_tag: solved_text = solved_text.replace(x,'')
		return (True, solved_text)

	def Rebooted(self):
		request = self.session.get(self.base_url, headers=self.headers).text
		for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request): self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
		for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request): self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
		for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request): self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False if 'disabled class' in x else True
		return (self.services, self.services_status)

	def get_table(self, i = 1):
	    print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
		# table = PrettyTable(field_names=["ID", "DỊCH VỤ", "Status"], title="Status Services", header_style="upper",border=True)
		# while True:
			# if len(self.Rebooted()[0])>1:break
			# else:print(self.iceArrow + '\033[1;31mKhông Thể Get Dịch Vụ...');self.TheySayGoSlow();time.sleep(2)
		# for service in self.services: table.add_row([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{Fore.GREEN if 'ago updated' in self.services[service] else Fore.RED}{self.services[service]}{Fore.RESET}"]); i+=1
		# table.title =  f"{Fore.YELLOW}Số Dịch Vụ Hoạt Động: {len([x for x in self.services_status if self.services_status[x]])}{Fore.RESET}"
		# print(table)

	def March_Of_The_Oni(self):
		if self.service is None: return (False, "You didn't choose the service")
		while True:
			if self.service not in self.services_ids: self.Rebooted(); time.sleep(1)
			#request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers = {"Origin": "https://zefoy.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","X-Requested-With": "XMLHttpRequest",}, data = {self.video_key: self.url})
			request = self.session.post(f'https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V', headers = {"Origin": "https://zefoy.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","X-Requested-With": "XMLHttpRequest",}, data = {self.video_key: self.url})
			try: self.video_info = base64.b64decode(requests.utils.unquote(request.text.encode()[::-1])).decode();
			except: time.sleep(3); continue
			if 'Session expired. Please re-login' in self.video_info: self.TheySayGoSlow(); return
			elif 'service is currently not working' in self.video_info: return (True, self.iceArrow + '\033[1;31mDịch Vụ Hiện Tại Không Hoạt Động, Hãy Thử Lại Sau.');
			elif """onsubmit="showHideElements""" in self.video_info:
				self.total_views = re.search(r'<i[^>]*></i>\s*([\d,]+)', self.video_info)
				self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
				return (True, request.text)
			elif 'Checking Timer...' in self.video_info:
				try: 
					t = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
					vudz = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
				except: 
					return (False,)
				time.sleep(vudz)
					
				continue
			elif 'Too many requests. Please slow' in self.video_info: time.sleep(3)
			else: print(self.video_info)

	def Crystalized(self):
		if self.March_Of_The_Oni()[0] is False: return False
		self.token = "".join(random.choices(ascii_letters+digits, k=16))
		#request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers = {"Origin": "https://zefoy.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","X-Requested-With": "XMLHttpRequest",}, data = {self.video_info[0]: self.video_info[1]})
		request = self.session.post(f'https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V', headers = {"Origin": "https://zefoy.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","X-Requested-With": "XMLHttpRequest",}, data = {self.video_info[0]: self.video_info[1]})
		try: res = base64.b64decode(requests.utils.unquote(request.text.encode()[::-1])).decode();
		except: time.sleep(3); return ""
		if 'Session expired. Please re-login' in res: self.TheySayGoSlow(); return ""
		elif 'Too many requests. Please slow' in res: time.sleep(3)
		elif 'service is currently not working' in res: return (self.iceArrow + '\033[1;31mDịch Vụ Hiện Tại Không Hoạt Đông, Hãy Thử Lại Sau.')
		elif 'Checking Timer...' in res and not 'Successfully 1000 views sent.' in res:
		    try: 
		        vudz = int(re.findall(r'ltm=(\d*);', res)[0])
		        time.sleep(vudz)
		    except: return False
		else: print(res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])
		    # self.dem += 1
		    # #match = re.search(r'<i[^>]*></i>\s*([\d,]+)', self.total_views)
		    # views = self.total_views.group(1)
		    # print(IceVip(self.dem) + time.strftime('%H:%M') + " \033[1;36m->\033[0;m VIEW \033[1;36m->\033[0;m " + str(maskX(self.video_info[1])) + " \033[1;36m->\033[0;m " + views + " \033[1;36m->\033[0;m +1.0K")

	def Spinjitzu(self):
		request = self.session.get(f'https://tiktok.livecounts.io/video/stats/{urlparse(self.url).path.rpartition("/")[2]}',headers={'authority':'tiktok.livecounts.io','origin':'https://livecounts.io','user-agent':self.headers['user-agent']}).json()
		if 'viewCount' in request: return request
		else: return {'viewCount':0, 'likeCount':0,'commentCount':0,'shareCount':0}

	def Day_of_the_Departed(self, url_ = None, set_url=True):
		if url_ is None: url_ = self.url
		if url_[-1] == '/': url_=url_[:-1]
		url = urlparse(url_).path.rpartition('/')[2]
		if url.isdigit(): self.url = url_; return url_
		request = requests.get(f'https://api.tokcount.com/?type=videoID&username=https://vm.tiktok.com/{url}',headers={'origin': 'https://tokcount.com','authority': 'api.tokcount.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
		if request.text == '': print(self.iceArrow + '\033[1;31mLink Video Không Hợp Lệ!'); return False
		else: json_=request.json()
		if 'author' not in json_: print(self.iceArrow + '\033[1;31mLink Video Không Hợp Lệ!'); return False
		if set_url: self.url = f'https://www.tiktok.com/@{json_["author"]}/video/{json_["id"]}';#print(f'Formated video url --> {self.url}')
		return request.text

	def Hands_of_Time(self):
		
		while True:
			try: 
				last_url = self.url
				if last_url != self.url: self.Day_of_the_Departed()
			except Exception as e: print(e)
			time.sleep(4)
	def Ninjago(self):
		while True:
			try:
				ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
				video_info = self.Spinjitzu()
			except: pass
			time.sleep(5)

               
API_TOKEN = '7297514837:AAFNydW28Ano-cw4v7Y0b5OA-7JilZVxpZA'
bot = telebot.TeleBot(API_TOKEN)

# Sử dụng Queue để quản lý hàng đợi và Lock để đảm bảo truy cập an toàn
buff_queue = Queue()
lock = Lock()

# Lưu thời gian hoàn thành của người dùng
user_last_run = {}

# Thời gian chờ 20 phút (1200 giây)
COOLDOWN_PERIOD = 20 * 60

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Chào mừng bạn! Sử dụng lệnh /buffview <link> <target> để bắt đầu.")

@bot.message_handler(commands=['buffview'])
def handle_buffview(message):
    user_id = message.from_user.id

    # Kiểm tra nếu người dùng đang trong thời gian chờ
    if user_id in user_last_run and time.time() - user_last_run[user_id] < COOLDOWN_PERIOD:
        remaining_time = COOLDOWN_PERIOD - (time.time() - user_last_run[user_id])
        minutes, seconds = divmod(remaining_time, 60)
        bot.reply_to(message, f"Bạn cần chờ thêm {int(minutes)} phút {int(seconds)} giây nữa trước khi sử dụng lại.")
        return

    try:
        _, link, target = message.text.split()
        target = int(target)
    except ValueError:
        bot.reply_to(message, "Vui lòng cung cấp đúng định dạng: /buffview <link> <target>")
        return

    # Đưa người dùng vào hàng đợi
    buff_queue.put((user_id, link, target))
    queue_position = buff_queue.qsize()  # Lấy số lượng phần tử trong hàng đợi
    bot.reply_to(message, f"Đã thêm vào hàng chờ. Số hàng đợi của bạn: {queue_position}. Vui lòng chờ...")

    # Thực hiện xử lý hàng đợi
    process_queue()

def process_queue():
    lock.acquire()
    try:
        if not buff_queue.empty():
            user_id, link, target = buff_queue.get()
            bot.send_message(user_id, f"Đang thực hiện {target} lần với link: {link}")
            buffview(user_id, link, target)
    finally:
        lock.release()

def buffview(user_id, link, target):
    # Đây là nơi bạn sẽ triển khai logic để thực hiện hành động buffview
    # Ví dụ: gửi thông báo cho người dùng mỗi lần thực hiện
    VuHoangPro = DungTuongTheLaHay()
    VuHoangPro.url = link
    threading.Thread(target=VuHoangPro.Hands_of_Time).start()
    threading.Thread(target=VuHoangPro.Ninjago).start()
    # time.sleep(5)
    VuHoangPro.TheySayGoSlow()
    VuHoangPro.get_table()
    for i in range(target):
        bot.send_message(user_id, f"Thực hiện lần thứ {i + 1} cho link: {link}")
        VuHoangPro.Crystalized()
    bot.send_message(user_id, "Đã hoàn thành.")
    
    # Cập nhật thời gian hoàn thành cuối cùng của người dùng
    user_last_run[user_id] = time.time()

bot.polling()
                
