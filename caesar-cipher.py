#By Trisna Nugraha - 20170801209

MAX=26
UPCHAR=[chr(i) for i in range(65,65+MAX)]
LOWCHAR=[chr(i) for i in range(97,97+MAX)]

#function untuk enkripsi teks
def getenchar(ch, key, enc):
    idx = (ord(ch) + key) if enc else (ord(ch) - key)
    idx = (idx-65 if ch.isupper() else idx-97) % MAX
    return UPCHAR[idx] if ch.isupper() else (LOWCHAR[idx] if ch.islower() else ch)

#function untuk dekripsi teks
def encdec(message, key, enc):
    result=[]
    for i in message:
        result.append(getenchar(i,key,enc))
    return ''.join(result)

#print menu
while True :
    print("\nProgram Enkripsi Dekripsi - Metode Caesar Cipher\n");
    print("1. Enkripsi");
    print("2. Dekripsi");
    print("3. Keluar");
    choice = int(input("\nMasukkan pilihan : "));
    if (choice==1):
        print('\nKetik pesan Anda disini\t\t: ', end='')
        teks=input(); key=0;
        while not (key > 0 and key < MAX):
            print('\nKetik Nilai Kunci [1-25]\t: ', end='')
            key=int(input())
        encMsg = encdec(teks, key, True)
        print('\nPesan yang dienkripsi\t\t: %s' % encMsg)
    elif choice == 2:
        print('\nKetik enkripsi pesan Anda disini\t: ', end='')
        teks=input(); key=0;
        while not (key > 0 and key < MAX):
            print('\nKetik Nilai Kunci [1-25]\t\t: ', end='')
            key=int(input())
            decMsg = encdec(encMsg, key, False)
            print('\nPesan yang didekripsi\t\t\t: %s' % decMsg)
    elif choice == 3:
        exit();
    else:
        print("Menu tidak tersedia..!!");
