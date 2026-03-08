#!/usr/bin/env python3
# ==============================================
#  STOLICE ŚWIATA - QUIZ GEOGRAFICZNY
#  Zgadnij kraj po stolicy!
# ==============================================

import random
import time
import os
import sys


# ── Kolory ANSI ──────────────────────────────────────────
class Kolor:
    RESET    = "\033[0m"
    BOLD     = "\033[1m"
    DIM      = "\033[2m"
    BLINK    = "\033[5m"

    CZERWONY = "\033[91m"
    ZIELONY  = "\033[92m"
    ZOLTY    = "\033[93m"
    NIEBIESKI= "\033[94m"
    FIOLET   = "\033[95m"
    CYAN     = "\033[96m"
    BIALY    = "\033[97m"

    BG_CZERWONY = "\033[41m"
    BG_ZIELONY  = "\033[42m"
    BG_ZOLTY    = "\033[43m"
    BG_NIEBIESKI= "\033[44m"
    BG_FIOLET   = "\033[45m"


# ── ASCII Art ──────────────────────────────────────────

LOGO = r"""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ███████╗████████╗ ██████╗ ██╗     ██╗ ██████╗███████╗          ║
║   ██╔════╝╚══██╔══╝██╔═══██╗██║     ██║██╔════╝██╔════╝          ║
║   ███████╗   ██║   ██║   ██║██║     ██║██║     █████╗            ║
║   ╚════██║   ██║   ██║   ██║██║     ██║██║     ██╔══╝            ║
║   ███████║   ██║   ╚██████╔╝███████╗██║╚██████╗███████╗          ║
║   ╚══════╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝ ╚═════╝╚══════╝          ║
║                                                                   ║
║        ███████╗██╗    ██╗██╗ █████╗ ████████╗ █████╗              ║
║        ██╔════╝██║    ██║██║██╔══██╗╚══██╔══╝██╔══██╗             ║
║        ███████╗██║ █╗ ██║██║███████║   ██║   ███████║             ║
║        ╚════██║██║███╗██║██║██╔══██║   ██║   ██╔══██║             ║
║        ███████║╚███╔███╔╝██║██║  ██║   ██║   ██║  ██║             ║
║        ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝             ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""

GLOBUS_ART = r"""
                         .-''''-.
                        /        \
                       |  O    O  |
                        \  .__.  /
                    ____/ '    ' \____
                 .-'    \\      //    '-.
                /  .--.  \\    //  .--.  \
               |  /    \  \\  //  /    \  |
               | |      |  |  | |      | |
               |  \    /  //  \\  \    /  |
                \  '--'  //    \\  '--'  /
                 '-.__.-'        '-.__.-'
                        |  QUIZ  |
                        |  GEO   |
                         \_______/
                          |     |
                         /       \
                        /         \
                       /_____*_____\
"""

MAPA_ART = r"""
     ╔══════════════════════════════════════════════════════╗
     ║                   🌍 MAPA ŚWIATA 🌏                 ║
     ╠══════════════════════════════════════════════════════╣
     ║                                                      ║
     ║     _____         ___                                ║
     ║    /     \    ___/   \___         ____               ║
     ║   | EUROPA\__/ AZJA      \__    / JAPN\             ║
     ║   |       /  \            / \  |      |             ║
     ║    \_____/ AFR \__    ___/   \_/      |             ║
     ║          | YKA    \  /                /              ║
     ║    ___   |         \/  INDIE    _____/               ║
     ║   / AM \ |          \     ____/                      ║
     ║  | ERY  \|___        \   /                           ║
     ║  | KA   /    \   AUST\ /                             ║
     ║   \    / PŁD  \  RALI/                               ║
     ║    \__/ AMERYK \____/                                ║
     ║        \_______/            🧭                       ║
     ║                                                      ║
     ╚══════════════════════════════════════════════════════╝
"""

TROFEUM_ART = r"""
           ___________
          '._==_==_=_.'
          .-\:      /-.
         | (|:.     |) |
          '-|:.     |-'
            \::.    /
             '::. .'
               ) (
             _.' '._
            '-------'
         MISTRZ GEOGRAFII!
"""

SAMOLOT_ART = r"""
                  __|__
         ------@-/  |  \-@------
                 \__|__/
                   | |
                  /   \\
                 /     \\
"""

POPRAWNA_ART = r"""
     ╔════════════════════════╗
     ║   ✅ POPRAWNIE!  ✅   ║
     ║                        ║
     ║      ██╗  ██╗██╗       ║
     ║      ╚██╗██╔╝██║       ║
     ║       ╚███╔╝ ██║       ║
     ║       ██╔██╗ ╚═╝       ║
     ║      ██╔╝ ██╗██╗       ║
     ║      ╚═╝  ╚═╝╚═╝       ║
     ╚════════════════════════╝
"""

BLEDNA_ART = r"""
     ╔════════════════════════╗
     ║   ❌ NIESTETY...  ❌   ║
     ║                        ║
     ║      ██╗  ██╗          ║
     ║      ╚██╗██╔╝          ║
     ║       ╚███╔╝           ║
     ║       ██╔██╗           ║
     ║      ██╔╝ ██╗          ║
     ║      ╚═╝  ╚═╝          ║
     ╚════════════════════════╝
"""

PYTANIE_RAMKA = """
{kolor}╔══════════════════════════════════════════════╗
║  🏛️  STOLICA:                                ║
║                                              ║
║     {stolica:<38s} ║
║                                              ║
║  ❓ Jaki to kraj?                            ║
╚══════════════════════════════════════════════╝{reset}
"""


# ── Baza stolic ──────────────────────────────────────────

STOLICE = {
    # Europa
    "Warszawa": "Polska",
    "Berlin": "Niemcy",
    "Paryż": "Francja",
    "Londyn": "Wielka Brytania",
    "Madryt": "Hiszpania",
    "Rzym": "Włochy",
    "Lizbona": "Portugalia",
    "Wiedeń": "Austria",
    "Praga": "Czechy",
    "Bratysława": "Słowacja",
    "Budapeszt": "Węgry",
    "Bukareszt": "Rumunia",
    "Sofia": "Bułgaria",
    "Zagrzeb": "Chorwacja",
    "Belgrad": "Serbia",
    "Ateny": "Grecja",
    "Amsterdam": "Holandia",
    "Bruksela": "Belgia",
    "Berno": "Szwajcaria",
    "Sztokholm": "Szwecja",
    "Oslo": "Norwegia",
    "Helsinki": "Finlandia",
    "Kopenhaga": "Dania",
    "Dublin": "Irlandia",
    "Rejkjawik": "Islandia",
    "Tallinn": "Estonia",
    "Ryga": "Łotwa",
    "Wilno": "Litwa",
    "Kijów": "Ukraina",
    "Mińsk": "Białoruś",
    "Moskwa": "Rosja",
    "Ankara": "Turcja",
    "Lublana": "Słowenia",
    "Tirana": "Albania",
    "Podgorica": "Czarnogóra",
    "Skopje": "Macedonia Północna",

    # Azja
    "Tokio": "Japonia",
    "Pekin": "Chiny",
    "Seul": "Korea Południowa",
    "Nowe Delhi": "Indie",
    "Bangkok": "Tajlandia",
    "Hanoi": "Wietnam",
    "Dżakarta": "Indonezja",
    "Manila": "Filipiny",
    "Kuala Lumpur": "Malezja",
    "Singapur": "Singapur",
    "Teheran": "Iran",
    "Bagdad": "Irak",
    "Rijad": "Arabia Saudyjska",
    "Kabul": "Afganistan",
    "Islamabad": "Pakistan",
    "Dhaka": "Bangladesz",
    "Katmandu": "Nepal",

    # Ameryka Północna i Środkowa
    "Waszyngton": "Stany Zjednoczone",
    "Ottawa": "Kanada",
    "Meksyk": "Meksyk",
    "Hawana": "Kuba",
    "Gwatemala": "Gwatemala",
    "Panama": "Panama",

    # Ameryka Południowa
    "Brasília": "Brazylia",
    "Buenos Aires": "Argentyna",
    "Lima": "Peru",
    "Bogota": "Kolumbia",
    "Santiago": "Chile",
    "Montevideo": "Urugwaj",
    "Quito": "Ekwador",
    "La Paz": "Boliwia",

    # Afryka
    "Kair": "Egipt",
    "Rabat": "Maroko",
    "Algier": "Algieria",
    "Tunis": "Tunezja",
    "Nairobi": "Kenia",
    "Addis Abeba": "Etiopia",
    "Pretoria": "Republika Południowej Afryki",
    "Akra": "Ghana",
    "Lagos": "Nigeria",
    "Dakar": "Senegal",

    # Oceania
    "Canberra": "Australia",
    "Wellington": "Nowa Zelandia",
}

# Kontynenty - do podpowiedzi
KONTYNENTY = {
    "Europa": ["Polska", "Niemcy", "Francja", "Wielka Brytania", "Hiszpania",
               "Włochy", "Portugalia", "Austria", "Czechy", "Słowacja",
               "Węgry", "Rumunia", "Bułgaria", "Chorwacja", "Serbia",
               "Grecja", "Holandia", "Belgia", "Szwajcaria", "Szwecja",
               "Norwegia", "Finlandia", "Dania", "Irlandia", "Islandia",
               "Estonia", "Łotwa", "Litwa", "Ukraina", "Białoruś",
               "Rosja", "Turcja", "Słowenia", "Albania", "Czarnogóra",
               "Macedonia Północna"],
    "Azja": ["Japonia", "Chiny", "Korea Południowa", "Indie", "Tajlandia",
             "Wietnam", "Indonezja", "Filipiny", "Malezja", "Singapur",
             "Iran", "Irak", "Arabia Saudyjska", "Afganistan", "Pakistan",
             "Bangladesz", "Nepal"],
    "Ameryka Północna": ["Stany Zjednoczone", "Kanada", "Meksyk", "Kuba",
                          "Gwatemala", "Panama"],
    "Ameryka Południowa": ["Brazylia", "Argentyna", "Peru", "Kolumbia",
                            "Chile", "Urugwaj", "Ekwador", "Boliwia"],
    "Afryka": ["Egipt", "Maroko", "Algieria", "Tunezja", "Kenia", "Etiopia",
               "Republika Południowej Afryki", "Ghana", "Nigeria", "Senegal"],
    "Oceania": ["Australia", "Nowa Zelandia"],
}


# ── Funkcje pomocnicze ─────────────────────────────────

def wyczysc_ekran():
    os.system('cls' if os.name == 'nt' else 'clear')


def pisz_powoli(tekst, opoznienie=0.03):
    for znak in tekst:
        sys.stdout.write(znak)
        sys.stdout.flush()
        time.sleep(opoznienie)
    print()


def znajdz_kontynent(kraj):
    for kontynent, kraje in KONTYNENTY.items():
        if kraj in kraje:
            return kontynent
    return "Nieznany"


def animacja_samolotu():
    klatki = [
        f"{Kolor.CYAN}                          __|__\n         ------@-/  |  \\-@------{Kolor.RESET}",
        f"{Kolor.CYAN}                __|__\n   ------@-/  |  \\-@------{Kolor.RESET}",
        f"{Kolor.CYAN}      __|__\n------@-/  |  \\-@------{Kolor.RESET}",
    ]
    for klatka in klatki:
        wyczysc_ekran()
        print("\n" * 5)
        print(klatka)
        time.sleep(0.3)


def animacja_poprawna():
    print(f"{Kolor.ZIELONY}{Kolor.BOLD}{POPRAWNA_ART}{Kolor.RESET}")
    time.sleep(0.5)


def animacja_bledna():
    print(f"{Kolor.CZERWONY}{Kolor.BOLD}{BLEDNA_ART}{Kolor.RESET}")
    time.sleep(0.5)


def pokaz_wynik(poprawne, bledne, runda, imie):
    total = poprawne + bledne
    if total > 0:
        procent = int(poprawne / total * 100)
    else:
        procent = 0

    # Pasek postępu
    dlugosc = 20
    wypelnienie = int(dlugosc * procent / 100)
    pasek = "█" * wypelnienie + "░" * (dlugosc - wypelnienie)

    print(f"""
{Kolor.BOLD}{Kolor.CYAN}┌──────────────────────────────────────────┐
│  📊 WYNIK: {imie:<29s}│
├──────────────────────────────────────────┤{Kolor.RESET}
│  Runda:     {Kolor.BOLD}{runda:<28s}{Kolor.RESET}│
│  ✅ Poprawne: {Kolor.ZIELONY}{Kolor.BOLD}{poprawne:<26d}{Kolor.RESET}│
│  ❌ Błędne:   {Kolor.CZERWONY}{Kolor.BOLD}{bledne:<26d}{Kolor.RESET}│
│  📈 Procent:  {Kolor.ZOLTY}{Kolor.BOLD}{procent}%{' ' * (24 - len(str(procent)))}{Kolor.RESET}│
│  [{Kolor.ZIELONY}{pasek}{Kolor.RESET}]{' ' * (18 - dlugosc)}│
{Kolor.CYAN}└──────────────────────────────────────────┘{Kolor.RESET}
""")


def pokaz_podpowiedz(kraj):
    kontynent = znajdz_kontynent(kraj)
    pierwsza = kraj[0]
    dlugosc = len(kraj)
    print(f"  {Kolor.ZOLTY}{Kolor.BOLD}💡 Podpowiedzi:{Kolor.RESET}")
    print(f"     {Kolor.DIM}🌍 Kontynent: {kontynent}{Kolor.RESET}")
    print(f"     {Kolor.DIM}🔤 Pierwsza litera: {pierwsza}{Kolor.RESET}")
    print(f"     {Kolor.DIM}📏 Liczba liter: {dlugosc}{Kolor.RESET}")
    print()


def pokaz_podsumowanie(poprawne, bledne, imie):
    total = poprawne + bledne
    if total > 0:
        procent = int(poprawne / total * 100)
    else:
        procent = 0

    wyczysc_ekran()

    if procent >= 80:
        print(f"{Kolor.ZOLTY}{Kolor.BOLD}{TROFEUM_ART}{Kolor.RESET}")
        ocena = "🌟 MISTRZ GEOGRAFII! 🌟"
        kolor_oceny = Kolor.ZOLTY
    elif procent >= 60:
        ocena = "📚 Dobra robota! Znasz się na geografii!"
        kolor_oceny = Kolor.ZIELONY
    elif procent >= 40:
        ocena = "🗺️  Nieźle, ale jest jeszcze nad czym pracować!"
        kolor_oceny = Kolor.CYAN
    else:
        ocena = "📖 Czas otworzyć atlas! Nie poddawaj się!"
        kolor_oceny = Kolor.CZERWONY

    print(f"""
{Kolor.BOLD}{Kolor.FIOLET}╔══════════════════════════════════════════════╗
║           📋 PODSUMOWANIE QUIZU 📋           ║
╠══════════════════════════════════════════════╣{Kolor.RESET}
║                                              ║
║  Gracz:      {Kolor.BOLD}{imie:<32s}{Kolor.RESET}║
║  Pytania:    {Kolor.BOLD}{total:<32d}{Kolor.RESET}║
║  Poprawne:   {Kolor.ZIELONY}{Kolor.BOLD}{poprawne:<32d}{Kolor.RESET}║
║  Błędne:     {Kolor.CZERWONY}{Kolor.BOLD}{bledne:<32d}{Kolor.RESET}║
║  Wynik:      {Kolor.ZOLTY}{Kolor.BOLD}{procent}%{' ' * (30 - len(str(procent)))}{Kolor.RESET}║
║                                              ║
║  {kolor_oceny}{Kolor.BOLD}{ocena:<44s}{Kolor.RESET}║
║                                              ║
{Kolor.FIOLET}╚══════════════════════════════════════════════╝{Kolor.RESET}
""")


def pokaz_menu_trybu():
    print(f"""
{Kolor.BOLD}{Kolor.CYAN}┌──────────────────────────────────────────┐
│       🌍 WYBIERZ TRYB GRY 🌍            │
├──────────────────────────────────────────┤{Kolor.RESET}
│                                          │
│  {Kolor.BOLD}{Kolor.NIEBIESKI}[1]{Kolor.RESET} 🌐 Cały świat  {Kolor.DIM}(wszystkie stolice){Kolor.RESET} │
│                                          │
│  {Kolor.BOLD}{Kolor.ZIELONY}[2]{Kolor.RESET} 🇪🇺 Tylko Europa                     │
│                                          │
│  {Kolor.BOLD}{Kolor.ZOLTY}[3]{Kolor.RESET} 🎯 Szybki quiz  {Kolor.DIM}(10 pytań){Kolor.RESET}        │
│                                          │
│  {Kolor.BOLD}{Kolor.FIOLET}[0]{Kolor.RESET} 🚪 Wyjdź                           │
│                                          │
{Kolor.CYAN}└──────────────────────────────────────────┘{Kolor.RESET}
""")


# ── Główna logika gry ──────────────────────────────────

def przygotuj_pytania(tryb):
    if tryb == "europa":
        kraje_europa = KONTYNENTY["Europa"]
        pytania = {s: k for s, k in STOLICE.items() if k in kraje_europa}
    else:
        pytania = dict(STOLICE)

    lista = list(pytania.items())
    random.shuffle(lista)
    return lista


def graj_runde(stolica, kraj, numer, imie):
    wyczysc_ekran()

    # Nagłówek rundy
    print(f"\n  {Kolor.BOLD}{Kolor.FIOLET}═══ Pytanie #{numer} ═══{Kolor.RESET}\n")

    # Pokaż pytanie w ramce
    kontynent = znajdz_kontynent(kraj)
    kolory_kontynent = {
        "Europa": Kolor.NIEBIESKI,
        "Azja": Kolor.ZOLTY,
        "Ameryka Północna": Kolor.CZERWONY,
        "Ameryka Południowa": Kolor.ZIELONY,
        "Afryka": Kolor.FIOLET,
        "Oceania": Kolor.CYAN,
    }
    kolor = kolory_kontynent.get(kontynent, Kolor.BIALY)

    print(PYTANIE_RAMKA.format(kolor=kolor, stolica=stolica, reset=Kolor.RESET))

    # Pierwsza próba
    odpowiedz = input(f"  {Kolor.BOLD}Twoja odpowiedź ➤ {Kolor.RESET}").strip()

    if odpowiedz.lower() == kraj.lower():
        animacja_poprawna()
        pisz_powoli(f"  {Kolor.ZIELONY}{Kolor.BOLD}🎉 Brawo {imie}! {stolica} to stolica {kraj}!{Kolor.RESET}", 0.03)
        return True

    # Źle - daj podpowiedź i drugą szansę
    print(f"\n  {Kolor.ZOLTY}🤔 Hmm, to nie to... Masz jeszcze jedną szansę!{Kolor.RESET}\n")
    pokaz_podpowiedz(kraj)

    odpowiedz2 = input(f"  {Kolor.BOLD}Spróbuj jeszcze raz ➤ {Kolor.RESET}").strip()

    if odpowiedz2.lower() == kraj.lower():
        animacja_poprawna()
        pisz_powoli(f"  {Kolor.ZIELONY}{Kolor.BOLD}🎉 Za drugim razem! {stolica} ➜ {kraj}!{Kolor.RESET}", 0.03)
        return True

    # Źle po raz drugi
    animacja_bledna()
    pisz_powoli(f"  {Kolor.CZERWONY}Poprawna odpowiedź: {Kolor.BOLD}{kraj}{Kolor.RESET}", 0.03)
    pisz_powoli(f"  {Kolor.DIM}{stolica} jest stolicą kraju: {kraj} ({znajdz_kontynent(kraj)}){Kolor.RESET}", 0.03)
    return False


def main():
    poprawne = 0
    bledne = 0

    # Ekran tytułowy
    wyczysc_ekran()
    print(f"{Kolor.CYAN}{Kolor.BOLD}{LOGO}{Kolor.RESET}")
    time.sleep(0.5)
    print(f"{Kolor.ZOLTY}{GLOBUS_ART}{Kolor.RESET}")
    time.sleep(0.5)

    pisz_powoli(f"  {Kolor.ZOLTY}🌍 Quiz ze stolic świata!{Kolor.RESET}", 0.04)
    pisz_powoli(f"  {Kolor.DIM}Podaję stolicę - Ty mówisz jaki to kraj!{Kolor.RESET}", 0.03)
    print()

    imie = input(f"  {Kolor.BOLD}{Kolor.CYAN}✏️  Jak masz na imię? ➤ {Kolor.RESET}").strip()
    if not imie:
        imie = "Gracz"

    print()
    pisz_powoli(f"  {Kolor.ZIELONY}{Kolor.BOLD}Cześć {imie}! Sprawdźmy Twoją wiedzę! 🧠{Kolor.RESET}", 0.04)
    print()

    # Wybór trybu
    pokaz_menu_trybu()
    wybor_trybu = input(f"  {Kolor.BOLD}Wybierz tryb ➤ {Kolor.RESET}").strip()

    if wybor_trybu == "0":
        pisz_powoli(f"  {Kolor.CYAN}Do zobaczenia {imie}! 👋{Kolor.RESET}", 0.04)
        return

    if wybor_trybu == "2":
        tryb = "europa"
        pisz_powoli(f"\n  {Kolor.NIEBIESKI}🇪🇺 Tryb: Europa!{Kolor.RESET}", 0.03)
    else:
        tryb = "swiat"
        pisz_powoli(f"\n  {Kolor.ZIELONY}🌐 Tryb: Cały świat!{Kolor.RESET}", 0.03)

    szybki = wybor_trybu == "3"
    if szybki:
        pisz_powoli(f"  {Kolor.ZOLTY}🎯 Szybki quiz - 10 pytań!{Kolor.RESET}", 0.03)

    # Animacja samolotu
    animacja_samolotu()

    # Przygotuj pytania
    pytania = przygotuj_pytania(tryb)
    if szybki:
        pytania = pytania[:10]

    print(f"\n  {Kolor.FIOLET}{MAPA_ART}{Kolor.RESET}")
    pisz_powoli(f"  {Kolor.DIM}Masz 2 próby na każde pytanie. Podpowiedź po 1. błędzie!{Kolor.RESET}", 0.03)
    pisz_powoli(f"  {Kolor.DIM}Wpisz 'q' aby zakończyć w trakcie gry.{Kolor.RESET}", 0.03)
    input(f"\n  {Kolor.DIM}Naciśnij ENTER aby rozpocząć...{Kolor.RESET}")

    # Pętla gry
    for i, (stolica, kraj) in enumerate(pytania, 1):
        wynik = graj_runde(stolica, kraj, i, imie)

        if wynik:
            poprawne += 1
        else:
            bledne += 1

        # Pokaż wynik
        pokaz_wynik(poprawne, bledne, str(i), imie)

        # Opcja wyjścia
        kontynuuj = input(f"  {Kolor.DIM}ENTER = następne pytanie | 'q' = koniec ➤ {Kolor.RESET}").strip()
        if kontynuuj.lower() == 'q':
            break

    # Podsumowanie
    pokaz_podsumowanie(poprawne, bledne, imie)
    pisz_powoli(f"  {Kolor.CYAN}Dzięki za grę {imie}! Do zobaczenia! ✈️{Kolor.RESET}", 0.04)


# ── Start ──────────────────────────────────────────
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {Kolor.CYAN}Do zobaczenia! ✈️{Kolor.RESET}\n")
