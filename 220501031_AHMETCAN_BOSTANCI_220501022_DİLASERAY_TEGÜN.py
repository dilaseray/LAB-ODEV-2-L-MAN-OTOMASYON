
import time
import ast
from termcolor import *

dosyaolustur=open("gemidurumu.txt","w",encoding="utf-8")
dosyaolustur.close()

def belirlisatırokuyucu(file,satır):
    dosya=open(file,"r",encoding="utf-8")

    for i in range(satır-1):
        dosya.readline()
    
    satırverisi=dosya.readline().strip("\n")
    satırverisi=ast.literal_eval(satırverisi)
    dosya.close()
    return satırverisi


def belirlisatıryazıcı(dosya_adı, satır, veri):
    
    with open(dosya_adı, 'r', encoding='utf-8') as dosya:
        satirlar = dosya.readlines()

    
    if len(satirlar) >= satır:
        del satirlar[satır - 1]

   
    satirlar.insert(satır - 1, str(veri) + '\n')

    
    with open(dosya_adı, 'w', encoding='utf-8') as dosya:
        dosya.writelines(satirlar)


class istif:
    def __init__(self,ulke):
        
        self.ulke=ulke
        self.istif1=0
        self.istif2=0
        
    def bos_mu(self):
        return self.istif1==0 and self.istif2==0

    def yuk_ekle(self, eklencek_yuk):
        yukkontrol=self.istif1+self.istif2
        if yukkontrol+eklencek_yuk<=1500:

            for i in range(int(eklencek_yuk)):
                if self.istif1<750:
                    self.istif1+=1
                elif self.istif2<750:
                    self.istif2+=1
                if self.istif1==750:
                    print(colored("1.ci istif alanı doldu yükler 2.ci istif alanına yönlendiriliyor.","red"))

        else:
            print("istif alanları kapasite yetersiz")
                

    def yuk_cikar(self,cıkanyuk):
        cıkacakyuk=cıkanyuk
        if not self.bos_mu():
            
            for i in range(int(cıkanyuk)):
                if self.istif2!=0:
                    self.istif2-=1
                else:
                    if self.istif1!=0:
                        self.istif1-=1
                    else:
                        print("çıkacak bu kadar yük yok")

        else:
            print("istif alanı boş.")
    def toplam_yuk(self):
        return self.istif1+self.istif2
    def yeteri_yuk_varmı(self,cekilecekyuk):
        return cekilecekyuk<=self.istif1+self.istif2

class TIR():
    def __init__(self,zaman,plaka):
        
        self.veri=tırdict[(zaman,plaka)]
        self.zaman=zaman
        self.plaka=plaka
        self.ulke=self.veri[0]
        self.yuk_kapasite=self.veri[1]
        self.yuk_miktarı=self.veri[2]
        self.maliyet=self.veri[3]
  
    def yukbosmu(self):
        if self.yuk_miktarı==0:
            return True
        else:
            return False

class GEMİ():
    
    def __init__(self,numara,ilkcalıstırma):
        # time.sleep(0.05)
        self.veri=gemidict[numara]
        self.kapasite=self.veri[1]
        if ilkcalıstırma:

            self.numara=numara
            self.zaman=self.veri[0]
            
            self.ulke=self.veri[2]

            self.yük=0
            self.min=self.kapasite*(95/100)
            veri=[numara,self.zaman,self.yük,self.min,self.ulke]
            belirlisatıryazıcı("gemidurumu.txt",int(numara),veri)
        else:
            veri=belirlisatırokuyucu("gemidurumu.txt",int(numara))
            
            self.numara=veri[0]
            self.zaman=veri[1]
            self.yük=veri[2]
            self.min=veri[3]
            self.ulke=veri[4]

    
    def gitmeyehazırmı(self):
        return self.yük>self.min
    def yük_ekle(self,yuk):
        self.yük+=yuk
        veri=[self.numara,self.zaman,self.yük,self.min,self.ulke]
        belirlisatıryazıcı("gemidurumu.txt",int(self.numara),veri)


def plakasıralama(a):
    return int(a[1][9:])


tırsorgudict=dict()

olaylarverisi=[]
olaylar=open("olaylar.csv","r",encoding="ISO-8859-9")
tırdict={}
for satır in olaylar:
    satırverisi=[]
    anlıkveri=satır.split(",")
    olaylarverisi.append([i.strip("\n") for i in anlıkveri])
olaylar.close()
olaylarverisi.pop(0) # başlıkların silinmesi
for sorgutır in olaylarverisi:
    tırsorgudict[(str(sorgutır[0]),str(sorgutır[1]))]=sorgutır[2:]


for index in olaylarverisi:
    if index[3]=="1":
        tırdict[(int(index[0]),index[1])]=[index[2],20000,int(index[5]),index[6]]
    else:
        tırdict[(int(index[0]),index[1])]=[index[2],30000,int(index[5]),index[6]]  # zaman ve plakaya karşılık : ülke ,yük kapasite,üzerindeki,maliyet



gemilerverisi=[]
gemisorgudict=dict()
gemiler=open("gemiler.csv","r",encoding="ISO-8859-9")
for satır in gemiler:
    satırverisi=[]
    anlıkveri=satır.split(",")
    gemilerverisi.append([i.strip("\n") for i in anlıkveri])
gemiler.close()
gemilerverisi.pop(0) # başlıkların silinmesi 

for gemisorgu in gemilerverisi:
    gemisorgudict[gemisorgu[1]]=[gemisorgu[0],gemisorgu[2],gemisorgu[3]]
gemidict=dict()
for index in gemilerverisi:
    gemidict[index[1]]=[int(index[0]),int(index[2]),index[3]]   # gemi numarasına karşılık : zaman  kapasite ülke


tır_dict_keys=tırdict.keys()
gemi_dict_keys=gemidict.keys()
zaman_listesi=[]
for zaman in tır_dict_keys:
    if  not (int(zaman[0]) in zaman_listesi):
        zaman_listesi.append(int(zaman[0]))

geminumara_iter=iter(gemidict.keys())


neverland_istifalanı=istif("Neverland")
mordor_istifalanı=istif("Mordor")
lilli_istifalanı=istif("Lilliputa")
ocean_istifalanı=istif("Oceania")
anlık_gemi=GEMİ(next(geminumara_iter),True)
bekleyengemiler=[]
yukindirentırlar=[]

for eszaman in zaman_listesi:
    
    eszamanlıtırlist=[]
    for eszamanlr_tir in tır_dict_keys: # aynı zamanları bir döngüye atmak için
        eszamantır=TIR(eszamanlr_tir[0],eszamanlr_tir[1])
        if eszaman==eszamantır.zaman:
            eszamanlıtırlist.append(eszamanlr_tir)
            
        
    
    eszamanlıtırlist.sort(key=plakasıralama)
    for tırlar in eszamanlıtırlist:
        aynızamanlıtır=TIR(tırlar[0],tırlar[1])
        if ocean_istifalanı.toplam_yuk()+lilli_istifalanı.toplam_yuk()+mordor_istifalanı.toplam_yuk()+neverland_istifalanı.toplam_yuk()<=1500:
            if not (tırlar[0],tırlar[1]) in yukindirentırlar:
                print(colored("{} zamanında {} plakalı tır {} ülkesine gitmek üzere {} ton yük indirdi maliyet:{} ".format(aynızamanlıtır.zaman,aynızamanlıtır.plaka,aynızamanlıtır.ulke,aynızamanlıtır.yuk_miktarı,aynızamanlıtır.maliyet),"green"))
                yukindirentırlar.append((tırlar[0],tırlar[1]))

            if anlık_gemi.gitmeyehazırmı():
                print(colored(" {} gemisi limandan ayrıldı. {}'e gidiyor".format(anlık_gemi.numara,anlık_gemi.ulke),"red"))
                anlık_gemi=GEMİ(next(geminumara_iter),True)

            if aynızamanlıtır.zaman>=anlık_gemi.zaman and aynızamanlıtır.ulke==anlık_gemi.ulke:
                print(colored("{} zamanında {} numaralı gemiye {}ton  yük yüklendi. gemi {} gitmek üzere bekliyor anlık yük: {}  harekete geçeceği yük:{}".format(aynızamanlıtır.zaman,anlık_gemi.numara,aynızamanlıtır.yuk_miktarı,anlık_gemi.ulke,anlık_gemi.yük+aynızamanlıtır.yuk_miktarı,anlık_gemi.min),"yellow"))
                anlık_gemi.yük_ekle(aynızamanlıtır.yuk_miktarı)
            else:
                print(colored(" {} yükü {} gemisi gelene kadar istif alanında bekletiliyor".format(aynızamanlıtır.plaka,aynızamanlıtır.ulke),"yellow"))
                if aynızamanlıtır.ulke=="Oceania":
                    ocean_istifalanı.yuk_ekle(aynızamanlıtır.yuk_miktarı)
                elif aynızamanlıtır.ulke=="Lilliputa":
                    lilli_istifalanı.yuk_ekle(aynızamanlıtır.yuk_miktarı)
                    
                elif aynızamanlıtır.ulke=="Mordor":
                    mordor_istifalanı.yuk_ekle(aynızamanlıtır.yuk_miktarı)
                elif aynızamanlıtır.ulke=="Neverland":
                   neverland_istifalanı.yuk_ekle(aynızamanlıtır.yuk_miktarı)
            
        else:

            if ocean_istifalanı.toplam_yuk()+lilli_istifalanı.toplam_yuk()+mordor_istifalanı.toplam_yuk()+neverland_istifalanı.toplam_yuk()<=1500:

                print(colored("istif alanı kapasitesi doldu"),"red")
            
            bekleyengemiler.append(anlık_gemi.numara)
            anlık_gemi=GEMİ(next(geminumara_iter),True)

            bekleyengemilerfor=bekleyengemiler
            for bekleyengemi in bekleyengemilerfor:
                anlık_gemi1=GEMİ(bekleyengemi,False)
                if anlık_gemi1.gitmeyehazırmı():
                    print(colored("{} gemisi {} gitmek üzere limandan ayrıldı.".format(anlık_gemi1.numara,anlık_gemi1.ulke),"magenta"))
                    bekleyengemiler.remove(bekleyengemi)
                if anlık_gemi1.ulke=="Oceania":
                    if ocean_istifalanı.yeteri_yuk_varmı(anlık_gemi1.min-anlık_gemi1.yük):
                        print(colored("{} gemisine istif alanından {} ton yük yüklendi ve {}e gitmek üzere limandan ayrıldı. ".format(anlık_gemi1.numara,anlık_gemi1.min-anlık_gemi1.yük,anlık_gemi1.ulke),"magenta"))
                        ocean_istifalanı.yuk_cikar(anlık_gemi1.min-anlık_gemi1.yük)
                        anlık_gemi1.yük_ekle(anlık_gemi1.min-anlık_gemi1.yük)
                        
                        bekleyengemiler.remove(bekleyengemi)
                    
                  
                elif anlık_gemi1.ulke=="Lilliputa":
                    if lilli_istifalanı.yeteri_yuk_varmı(anlık_gemi1.min-anlık_gemi1.yük):
                        print(colored("{} gemisine istif alanından {} ton yük yüklendi ve {}e gitmek üzere limandan ayrıldı. ".format(anlık_gemi1.numara,anlık_gemi1.min-anlık_gemi1.yük,anlık_gemi1.ulke),"magenta"))
                        lilli_istifalanı.yuk_cikar(anlık_gemi1.min-anlık_gemi1.yük)
                        anlık_gemi1.yük_ekle(anlık_gemi1.min-anlık_gemi1.yük)
                        
                        bekleyengemiler.remove(bekleyengemi)
                    


                elif anlık_gemi1.ulke=="Mordor":
                    if mordor_istifalanı.yeteri_yuk_varmı(anlık_gemi1.min-anlık_gemi1.yük):
                        print(colored("{} gemisine istif alanından {} ton yük yüklendi ve {}e gitmek üzere limandan ayrıldı.  ".format(anlık_gemi1.numara,anlık_gemi1.min-anlık_gemi1.yük,anlık_gemi1.ulke),"magenta"))
                        mordor_istifalanı.yuk_cikar(anlık_gemi1.min-anlık_gemi1.yük)
                        anlık_gemi1.yük_ekle(anlık_gemi1.min-anlık_gemi1.yük)
                        
                        bekleyengemiler.remove(bekleyengemi)
                    

                elif anlık_gemi1.ulke=="Neverland":
                    if neverland_istifalanı.yeteri_yuk_varmı(anlık_gemi1.min-anlık_gemi1.yük):
                        print(colored("{} gemisine istif alanından {} ton yük yüklendi ve {}e gitmek üzere limandan ayrıldı.  ".format(anlık_gemi1.numara,anlık_gemi1.min-anlık_gemi1.yük,anlık_gemi1.ulke),"magenta"))
                        neverland_istifalanı.yuk_cikar(anlık_gemi1.min-anlık_gemi1.yük)
                        anlık_gemi1.yük_ekle(anlık_gemi1.min-anlık_gemi1.yük)
                        
                        bekleyengemiler.remove(bekleyengemi)


while True:
    print(colored(''' 
    ===============================
    GEMİ SORGULAMAK İÇİN 1 BASINIZ

    TIR SORGULAMAK İÇİN 2 BASINIZ

    ÇIKMAK İÇİN Q BASINIZ
    ================================             
''',"magenta"))    
    secim = input("Sorgu numarasını giriniz : ")

    if secim=="1":
        gemino=input("GEMİ NUMARASINI GİRİNİZ")
        sorgu=gemisorgudict[gemino]
        print(colored(''' 
    ---------------------------------
    *    GEMİ NUMARASI : {}         *
    *                               *
    *    GELİŞ ZAMANI : {}          *
    *                               *  
    *    GEMİ KAPASİTESİ : {}       *
    *                               * 
    *    GİDECEĞİ ÜLKE : {}         *
    ---------------------------------

            '''.format(gemino,sorgu[0],sorgu[1],sorgu[2]),"red"))
    time.sleep(3)

    if secim=="2":
        tırzamanveplaka=input("Tır zaman ve plakasını , ayırarak giriniz.").split(",")
        sorgu=tırsorgudict[(tırzamanveplaka[0],"41_kostu_"+tırzamanveplaka[1])]
        print(colored(''' 
    -------------------------------
    *    GELİŞ ZAMANI : {}        *
    *    TIR PLAKASI : {}         *
    *    ÜLKE : {}                *
    *    20 TON ADET : {}         *
    *    30 TON ADET : {}         *
    *    YÜK MİKTARI : {}         *
    *    MALİYET : {}             *
    -------------------------------                 
'''.format(tırzamanveplaka[0],tırzamanveplaka[1],sorgu[0],sorgu[1],sorgu[2],sorgu[3],sorgu[4]),"light_red"))
    time.sleep(3)
    
    
    if secim.upper()=="Q":
        print(colored("PROGRAM SONA ERDİ","red"))
        break