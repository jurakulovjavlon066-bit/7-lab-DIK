# Elektron murojaatlar tizimi - Prototip V3.0

murojaatlar = []

def murojaat_yuborish():
    print("\n--- Yangi murojaat yuborish ---")
    ism = input("Ismingizni kiriting: ").strip()
    matn = input("Murojaat matnini kiriting: ").strip()
    
    # V3.0: Validatsiya (bo'sh qoldirmaslikni tekshirish)
    if not ism or not matn:
        print("Xatolik: Barcha maydonlarni to'ldirishi shart!")
        return
    
    murojaat_id = len(murojaatlar) + 1
    yangi_murojaat = {
        "id": murojaat_id,
        "ism": ism,
        "matn": matn,
        "holati": "Yuborildi",
        "javob": "Hozircha javob berilmagan"
    }
    murojaatlar.append(yangi_murojaat)
    print(f"Muvaffaqiyatli yuborildi! Sizning murojaat raqamingiz (ID): {murojaat_id}")

def murojaatni_tekshirish():
    print("\n--- Murojaat holatini tekshirish ---")
    try:
        m_id = int(input("Murojaat ID raqamini kiriting: "))
    except ValueError:
        print("Xatolik: Faqat raqam kiriting!")
        return
    
    topildi = False
    for m in murojaatlar:
        if m["id"] == m_id:
            print(f"\nID: {m['id']}")
            print(f"Foydalanuvchi: {m['ism']}")
            print(f"Murojaat: {m['matn']}")
            print(f"Holati: {m['holati']}")
            print(f"Admin javobi: {m['javob']}")
            topildi = True
            break
    if not topildi:
        print("Bunday ID raqamdagi murojaat topilmadi.")

def admin_javob_berish():
    print("\n--- Administrator paneli ---")
    try:
        m_id = int(input("Javob beriladigan murojaat ID raqamini kiriting: "))
    except ValueError:
        print("Xatolik: Faqat raqam kiriting!")
        return
    
    for m in murojaatlar:
        if m["id"] == m_id:
            print(f"Hozirgi murojaat: {m['matn']}")
            javob_matni = input("Admin javobini kiriting: ").strip()
            if not javob_matni:
                print("Xatolik: Javob bo'sh bo'lishi mumkin emas!")
                return
            m["javob"] = javob_matni
            m["holati"] = "Javob berildi"
            print("Javob muvaffaqiyatli saqlandi!")
            return
    print("Murojaat topilmadi.")

# Asosiy menyu loopi
while True:
    print("\n=== ELEKTRON MUROJAATLAR TIZIMI ===")
    print("1. Murojaat yuborish")
    print("2. Murojaat holatini tekshirish (Qidiruv)")
    print("3. Admin: Javob berish")
    print("4. Chiqish")
    
    tanlov = input("Tanlovingizni kiriting (1-4): ")
    
    if tanlov == "1":
        murojaat_yuborish()
    elif tanlov == "2":
        murojaatni_tekshirish()
    elif tanlov == "3":
        admin_javob_berish()
    elif tanlov == "4":
        print("Dastur tugatildi.")
        break
    else:
        print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")
