ó
ô¯²^c           @   s¶   d  d l  Z  d  d l Z d  d l Z d Z d Z d Z d Z d Z d Z d Z	 d	 Z
 d
   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z e d k r² e   n  d S(   iÿÿÿÿNs   [90;1ms   [91;1ms   [92;1ms   [93;1ms   [94;1ms   [95;1ms   [96;1ms   [97;1mc         C   s   i d d 6d d 6d d 6d d 6d	 d
 6d d 6d d 6d d 6} x, | D]$ } |  j  d | d | |  }  qE W|  d 7}  |  j  d d  }  |  GHd  S(   NiZ   t   wi   t   mi    t   hi!   t   ki"   t   bi#   t   pi`   t   aia   t   ss   %ss   [%s;1ms   [0ms   0(   t   replace(   t   xR    t   i(    (    s   /sdcard/termux.pyt   zidan   s    >"
c         C   sC   x< |  D]4 } t  j j |  t  j j   t j d d  q Wd  S(   NiP   id   (   t   syst   stdoutt   writet   flusht   timet   sleep(   t   lolzt   noobs(    (    s   /sdcard/termux.pyt   runntxt   s    c           C   s   t  j d  t  j d  t d  t d GHt d  t d  t d  t d GHt d	  t d
  t d  t d  t d GHd  S(   Nt   clears   figlet THEMEs#   b          TOOLS EDIT TERMUX KERENs/   +---------------------------------------------+s   s|  Author  :h King Mr_Z17s   s|  YouTube :m Mr_Z17s1   s|  github  :a https://www.github.com/KingMrZ17s/   |   +-----------------------------------------+s;   s|   | m[s1m]k  Ubah termux kamu sekarang..       s |s;   s|   | m[s2m]k  Cara Mengedit.....                s |s;   s|   | m[s3m]h  Install Bahan bahannya bosq.....  s |s;   s|   | m[s0m]m  Keluar                            s |s/   +---+-----------------------------------------+(   t   ost   systemR   R   (    (    (    s   /sdcard/termux.pyt   banner#   s    
	


	



c          C   sB  t    t d Gt d Gt d Gt d GHt d  }  |  d k r¢ t   t t d  d GHt j	 d	  t t d
  d GHt t
 d  d GHd GHt j	 d  n |  d k rÎ t d GHt j	 d  t   np |  d k rþ t j	 d  t   t j	 d  n@ |  d k r7t j	 d  t d GHt j	 d  t   n t   d  S(   Ns   ,~~~~~t   [s   Pilih Opsinyat   ]s   [95m'#~~>   i   s	   .........t    i   s            S u c c s e s s ...s     s"    Silahkan buka jendela termux barui   s   sedang proses.......i   i   i    s,   Jangan Lupa Subscribe Channel YouTube Mr_Z17(   R   R   R   R   t   inputt   pertamaR   R    R   R   R   R   t   installt   keluart   main(   t   zidan_noobs(    (    s   /sdcard/termux.pyR    2   s8    !	
	
c           C   s4   t  j d  t  j d  t  j d  t d GHd  S(   Ns   rm $HOME/../usr/etc/bash.bashrcs"   cp -f bash.bashrc $HOME/../usr/etcR   s   sedang proses.......(   R   R   R    (    (    (    s   /sdcard/termux.pyR   P   s    c           C   s%   t  j d  t  j d  t   d  S(   Ns%   pkg install ruby cowsay toilet figlets   gem install lolcat(   R   R   R    (    (    (    s   /sdcard/termux.pyR   U   s    c           C   s   t  j   d  S(   N(   R   t   exit(    (    (    s   /sdcard/termux.pyR   Y   s    c          C   s\   t  d GHt d  }  |  d k s- |  d k rQ t j d  t j d  t   n t   d  S(   Nsr  
  CARA EDIT SCRIPT BASH.BASHRC
[97m

   Ganti Kalimat yg bertuliskan  
"[91mKing Mr_Z17[97m" dengan nama kamu.
Jangan ubah kalimat selain yg bertuliskan "[91mKing Mr_Z17[97m",
dikhawatirkan program menjadi error...
jika sudah di edit, tinggal save dengan cara tekan 
tombol [95mCTRL + X + Y + ENTER                
[90m
                 Powered by: King Mr_Z17 
s5   [92;1m  E D I T  S E K A R A N G ?[91m  [ Y / N ]: t   yt   Ys   pkg install nanos   nano bash.bashrc(   R   t	   raw_inputR   R   R    (   t   lol(    (    s   /sdcard/termux.pyR   \   s    
t   __main__(   R   R   R   R    R   R   R   R   R   R   R   R   R   R   R    R   R   R   R   t   __name__(    (    (    s   /sdcard/termux.pyt   <module>   s(   								