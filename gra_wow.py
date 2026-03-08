#!/usr/bin/env python3
# ==============================================
#  KAMIEŃ  PAPIER  NOŻYCE  -  WERSJA WOW!
#  Nauka Pythona z efektami w terminalu
# ==============================================

import random
import time
import os
import sys

# ── Kolory ANSI (działają w terminalu) ─────────────────
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

KAMIEN_ART = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPIER_ART = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

NOZYCE_ART = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

LOGO = r"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ██╗  ██╗ █████╗ ███╗   ███╗██╗███████╗███╗   ██╗           ║
║   ██║ ██╔╝██╔══██╗████╗ ████║██║██╔════╝████╗  ██║           ║
║   █████╔╝ ███████║██╔████╔██║██║█████╗  ██╔██╗ ██║           ║
║   ██╔═██╗ ██╔══██║██║╚██╔╝██║██║██╔══╝  ██║╚██╗██║           ║
║   ██║  ██╗██║  ██║██║ ╚═╝ ██║██║███████╗██║ ╚████║           ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝           ║
║                                                               ║
║        ██████╗  █████╗ ██████╗ ██╗███████╗██████╗             ║
║        ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔══██╗            ║
║        ██████╔╝███████║██████╔╝██║█████╗  ██████╔╝            ║
║        ██╔═══╝ ██╔══██║██╔═══╝ ██║██╔══╝  ██╔══██╗            ║
║        ██║     ██║  ██║██║     ██║███████╗██║  ██║             ║
║        ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝             ║
║                                                               ║
║     ███╗   ██╗ ██████╗ ███████╗██╗   ██╗ ██████╗███████╗     ║
║     ████╗  ██║██╔═══██╗╚══███╔╝╚██╗ ██╔╝██╔════╝██╔════╝     ║
║     ██╔██╗ ██║██║   ██║  ███╔╝  ╚████╔╝ ██║     █████╗       ║
║     ██║╚██╗██║██║   ██║ ███╔╝    ╚██╔╝  ██║     ██╔══╝       ║
║     ██║ ╚████║╚██████╔╝███████╗   ██║   ╚██████╗███████╗     ║
║     ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝╚══════╝     ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

WALKA_ART = r"""
        \   |   /          \   |   /
         \  |  /            \  |  /
    ------BOOM!------  ------CRASH!------
         /  |  \            /  |  \
        /   |   \          /   |   \
"""

KORONA_ART = r"""
         ♔
      ╔══════╗
      ║ZWYCIĘ║
      ║ STWO!║
      ╚══════╝
"""

CZASZKA_ART = r"""
      ☠
   ╔══════╗
   ║PRZE- ║
   ║GRANA!║
   ╚══════╝
"""


# ── Funkcje pomocnicze ─────────────────────────────────

def wyczysc_ekran():
    """Czyści terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pisz_powoli(tekst, opoznienie=0.03):
    """Wypisuje tekst litera po literze - efekt maszyny do pisania"""
    for znak in tekst:
        sys.stdout.write(znak)
        sys.stdout.flush()
        time.sleep(opoznienie)
    print()


def animacja_odliczania():
    """Animacja 3... 2... 1... WALKA!"""
    symbole = [
        (f"{Kolor.CZERWONY}{Kolor.BOLD}  ██████╗ \n  ╚════██╗\n   █████╔╝\n   ╚═══██╗\n  ██████╔╝\n  ╚═════╝ {Kolor.RESET}", "3"),
        (f"{Kolor.ZOLTY}{Kolor.BOLD}  ██████╗ \n  ╚════██╗\n   █████╔╝\n  ██╔═══╝ \n  ███████╗\n  ╚══════╝{Kolor.RESET}", "2"),
        (f"{Kolor.ZIELONY}{Kolor.BOLD}   ██╗\n  ███║\n  ╚██║\n   ██║\n   ██║\n   ╚═╝{Kolor.RESET}", "1"),
    ]

    for art, num in symbole:
        wyczysc_ekran()
        print("\n" * 5)
        print(art)
        print()
        time.sleep(0.7)

    wyczysc_ekran()
    print("\n" * 3)
    print(f"{Kolor.BG_CZERWONY}{Kolor.BIALY}{Kolor.BOLD}")
    print("  ██╗    ██╗ █████╗ ██╗     ██╗  ██╗ █████╗ ██╗")
    print("  ██║    ██║██╔══██╗██║     ██║ ██╔╝██╔══██╗██║")
    print("  ██║ █╗ ██║███████║██║     █████╔╝ ███████║██║")
    print("  ██║███╗██║██╔══██║██║     ██╔═██╗ ██╔══██║╚═╝")
    print("  ╚███╔███╔╝██║  ██║███████╗██║  ██╗██║  ██║██╗")
    print("   ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝")
    print(f"{Kolor.RESET}")
    time.sleep(0.8)


def animacja_wybuchu():
    """Animacja wybuchu przy zderzeniu"""
    klatki = [
        f"""{Kolor.ZOLTY}
              *
             ***
            *****
           *******
            *****
             ***
              *
{Kolor.RESET}""",
        f"""{Kolor.CZERWONY}
          *       *
       *     *     *
     *    *     *    *
       *     *     *
          *       *
    ·  .  ·  .  ·  .  ·
{Kolor.RESET}""",
        f"""{Kolor.ZOLTY}
      ·  ★  ·    ★  ·
    ★    ·    ★    ·    ★
      ·    ★    ·    ★
    ★  · ╔══════════╗ · ★
      ·  ║  BOOM!!  ║  ·
    ★  · ╚══════════╝ · ★
      ·    ★    ·    ★
    ★    ·    ★    ·    ★
      ·  ★  ·    ★  ·
{Kolor.RESET}""",
        f"""{Kolor.CZERWONY}
    ·    .    ·    .    ·
      .    ·    .    ·
    ·    .    ·    .    ·
      .    ·    .    ·
    ·    .    ·    .    ·
{Kolor.RESET}""",
    ]

    for klatka in klatki:
        print(klatka)
        time.sleep(0.25)


def pokaz_walke(gracz_art, komputer_art, kolor_gracz, kolor_komp):
    """Pokazuje zderzenie dwóch broni"""
    gracz_linie = gracz_art.strip().split('\n')
    komp_linie = komputer_art.strip().split('\n')

    # Wyrównaj liczbę linii
    max_linie = max(len(gracz_linie), len(komp_linie))
    while len(gracz_linie) < max_linie:
        gracz_linie.append("")
    while len(komp_linie) < max_linie:
        komp_linie.append("")

    print(f"\n  {kolor_gracz}{Kolor.BOLD}>>> TY <<<{Kolor.RESET}"
          f"                    {kolor_komp}{Kolor.BOLD}>>> KOMPUTER <<<{Kolor.RESET}\n")

    for g, k in zip(gracz_linie, komp_linie):
        print(f"  {kolor_gracz}{g:<25}{Kolor.RESET}"
              f"  {Kolor.CZERWONY}⚔{Kolor.RESET}  "
              f"{kolor_komp}{k}{Kolor.RESET}")


def pobierz_art(wybor):
    """Zwraca ASCII art dla danego wyboru"""
    if wybor == "kamien":
        return KAMIEN_ART
    elif wybor == "papier":
        return PAPIER_ART
    elif wybor == "nozyce":
        return NOZYCE_ART
    return ""


def pobierz_nazwe(wybor):
    """Zwraca ładną nazwę z emoji"""
    nazwy = {
        "kamien": f"🪨  KAMIEŃ",
        "papier": f"📄 PAPIER",
        "nozyce": f"✂️  NOŻYCE",
    }
    return nazwy.get(wybor, wybor)


def animacja_remisu():
    """Specjalna animacja remisu"""
    klatki = ["🤜🤛", "🤛🤜", "🤜🤛", "🤛🤜"]
    for klatka in klatki:
        sys.stdout.write(f"\r    {Kolor.ZOLTY}{Kolor.BOLD}  {klatka}  REMIS!  {klatka}  {Kolor.RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    print()
    print(f"""
{Kolor.ZOLTY}{Kolor.BOLD}
    ╔═══════════════════════════════╗
    ║     ⚖️   R E M I S !!  ⚖️     ║
    ║   Równe siły... jeszcze raz! ║
    ╚═══════════════════════════════╝
{Kolor.RESET}""")


def animacja_wygranej():
    """Animacja wygranej gracza"""
    print(f"""
{Kolor.ZIELONY}{Kolor.BOLD}
    ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★
    ☆                               ☆
    ★    🏆  W Y G R A Ł E Ś !! 🏆   ★
    ☆                               ☆
    ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★
{Kolor.RESET}""")

    # Fajerwerki
    for _ in range(3):
        sys.stdout.write(f"\r  {Kolor.ZOLTY}✦ ✧ ✦{Kolor.FIOLET} ★ ☆ ★{Kolor.CYAN} ✦ ✧ ✦{Kolor.ZIELONY} ★ ☆ ★{Kolor.RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(f"\r  {Kolor.FIOLET}✧ ✦ ✧{Kolor.ZOLTY} ☆ ★ ☆{Kolor.ZIELONY} ✧ ✦ ✧{Kolor.CYAN} ☆ ★ ☆{Kolor.RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
    print()


def animacja_przegranej():
    """Animacja przegranej gracza"""
    print(f"""
{Kolor.CZERWONY}{Kolor.BOLD}
    ╔═══════════════════════════════════╗
    ║                                   ║
    ║   🤖 Komputer wygrywa! 🤖        ║
    ║   Nie poddawaj się!               ║
    ║                                   ║
    ╚═══════════════════════════════════╝
{Kolor.RESET}""")


def pokaz_wynik(gracz_pkt, komputer_pkt, rundy):
    """Pokazuje aktualny wynik w ładnej ramce"""
    szerokosc = 45
    procent_g = int((gracz_pkt / max(rundy, 1)) * 100)
    procent_k = int((komputer_pkt / max(rundy, 1)) * 100)

    pasek_g = "█" * (procent_g // 5) + "░" * (20 - procent_g // 5)
    pasek_k = "█" * (procent_k // 5) + "░" * (20 - procent_k // 5)

    print(f"""
{Kolor.CYAN}╔═════════════════════════════════════════════╗
║{Kolor.BOLD}           📊 TABLICA WYNIKÓW 📊             {Kolor.RESET}{Kolor.CYAN}║
╠═════════════════════════════════════════════╣
║                                             ║
║  {Kolor.ZIELONY}🧑 Ty:       {gracz_pkt:>3} pkt  [{pasek_g}]{Kolor.CYAN}  ║
║  {Kolor.CZERWONY}🤖 Komputer: {komputer_pkt:>3} pkt  [{pasek_k}]{Kolor.CYAN}  ║
║                                             ║
║  {Kolor.ZOLTY}Rozegrane rundy: {rundy}{Kolor.CYAN}                        ║
╚═════════════════════════════════════════════╝{Kolor.RESET}
""")


def pokaz_menu():
    """Pokazuje menu wyboru"""
    print(f"""
{Kolor.BOLD}{Kolor.CYAN}┌─────────────────────────────────────────┐
│          ✊ WYBIERZ SWOJĄ BROŃ! ✊       │
├─────────────────────────────────────────┤{Kolor.RESET}
│                                         │
│  {Kolor.BOLD}{Kolor.NIEBIESKI}[1]{Kolor.RESET} 🪨  Kamień  {Kolor.DIM}- miażdży nożyce{Kolor.RESET}     │
│                                         │
│  {Kolor.BOLD}{Kolor.ZIELONY}[2]{Kolor.RESET} 📄 Papier  {Kolor.DIM}- owija kamień{Kolor.RESET}       │
│                                         │
│  {Kolor.BOLD}{Kolor.CZERWONY}[3]{Kolor.RESET} ✂️  Nożyce  {Kolor.DIM}- tną papier{Kolor.RESET}        │
│                                         │
│  {Kolor.BOLD}{Kolor.FIOLET}[0]{Kolor.RESET} 🚪 Zakończ grę                    │
│                                         │
{Kolor.CYAN}└─────────────────────────────────────────┘{Kolor.RESET}
""")


def kto_wygrywa(gracz, komputer):
    """
    Sprawdza kto wygrał rundę.
    Zwraca: 'gracz', 'komputer' lub 'remis'
    """
    if gracz == komputer:
        return "remis"

    wygrywa_gracz = {
        "kamien": "nozyce",   # kamień miażdży nożyce
        "papier": "kamien",   # papier owija kamień
        "nozyce": "papier",   # nożyce tną papier
    }

    if wygrywa_gracz[gracz] == komputer:
        return "gracz"
    else:
        return "komputer"


def pokaz_opis_wygranej(gracz, komputer, wynik):
    """Pokazuje opis jak jedna broń pokonała drugą"""
    opisy = {
        ("kamien", "nozyce"):  "💥 Kamień MIAŻDŻY nożyce!",
        ("nozyce", "papier"):  "✂️  Nożyce TNĄ papier!",
        ("papier", "kamien"):  "📄 Papier OWIJA kamień!",
    }

    if wynik == "gracz":
        opis = opisy.get((gracz, komputer), "")
        print(f"\n  {Kolor.ZIELONY}{Kolor.BOLD}{opis}{Kolor.RESET}")
    elif wynik == "komputer":
        opis = opisy.get((komputer, gracz), "")
        print(f"\n  {Kolor.CZERWONY}{Kolor.BOLD}{opis}{Kolor.RESET}")


def pokaz_podsumowanie(gracz_pkt, komputer_pkt, rundy):
    """Pokazuje końcowe podsumowanie gry"""
    wyczysc_ekran()

    print(f"""
{Kolor.CYAN}{Kolor.BOLD}
╔══════════════════════════════════════════════════╗
║                                                  ║
║          📋 PODSUMOWANIE GRY 📋                 ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║   Rozegrane rundy:    {rundy:>3}                       ║
║   Twoje wygrane:      {gracz_pkt:>3}  🏆                    ║
║   Wygrane komputera:  {komputer_pkt:>3}  🤖                    ║
║   Remisy:             {rundy - gracz_pkt - komputer_pkt:>3}  ⚖️                     ║
║                                                  ║""")

    if gracz_pkt > komputer_pkt:
        print(f"""║                                                  ║
║    🎉🏆 JESTEŚ MISTRZEM! GRATULACJE! 🏆🎉       ║
║                                                  ║""")
    elif komputer_pkt > gracz_pkt:
        print(f"""║                                                  ║
║    🤖 Komputer tym razem lepszy...                ║
║    💪 Ale następnym razem dasz radę!              ║
║                                                  ║""")
    else:
        print(f"""║                                                  ║
║    ⚖️  Idealny remis! Równe siły!                 ║
║                                                  ║""")

    print(f"""╚══════════════════════════════════════════════════╝
{Kolor.RESET}""")


# ── GŁÓWNA GRA ─────────────────────────────────────────

def main():
    """Główna pętla gry"""

    gracz_pkt = 0
    komputer_pkt = 0
    rundy = 0

    opcje = ["kamien", "papier", "nozyce"]

    # Ekran tytułowy
    wyczysc_ekran()
    print(f"{Kolor.CYAN}{Kolor.BOLD}{LOGO}{Kolor.RESET}")
    time.sleep(1)
    pisz_powoli(f"  {Kolor.ZOLTY}Witaj w najlepszej grze w terminalu!{Kolor.RESET}", 0.04)
    pisz_powoli(f"  {Kolor.DIM}Naciśnij ENTER aby rozpocząć...{Kolor.RESET}", 0.03)
    input()

    while True:
        wyczysc_ekran()

        # Pokaż wynik jeśli to nie pierwsza runda
        if rundy > 0:
            pokaz_wynik(gracz_pkt, komputer_pkt, rundy)

        # Menu wyboru
        pokaz_menu()

        # Pobierz wybór gracza
        wybor = input(f"  {Kolor.BOLD}Twój wybór ➤ {Kolor.RESET}").strip()

        # Mapowanie numerów na nazwy
        mapa = {"1": "kamien", "2": "papier", "3": "nozyce", "0": "koniec",
                "kamien": "kamien", "kamień": "kamien",
                "papier": "papier", "nozyce": "nozyce", "nożyce": "nozyce",
                "koniec": "koniec"}

        gracz = mapa.get(wybor.lower(), None)

        if gracz == "koniec":
            pokaz_podsumowanie(gracz_pkt, komputer_pkt, rundy)
            pisz_powoli(f"  {Kolor.CYAN}Dzięki za grę! Do zobaczenia! 👋{Kolor.RESET}", 0.04)
            break

        if gracz is None:
            print(f"\n  {Kolor.CZERWONY}❌ Nie rozumiem! Wybierz 1, 2, 3 lub 0{Kolor.RESET}")
            time.sleep(1.5)
            continue

        # Komputer losuje
        komputer = random.choice(opcje)

        # Animacja odliczania
        animacja_odliczania()

        wyczysc_ekran()

        # Pokaż walkę
        gracz_art = pobierz_art(gracz)
        komp_art = pobierz_art(komputer)

        print(f"\n{Kolor.BOLD}  {pobierz_nazwe(gracz)}   vs   {pobierz_nazwe(komputer)}{Kolor.RESET}")
        pokaz_walke(gracz_art, komp_art, Kolor.ZIELONY, Kolor.CZERWONY)

        time.sleep(0.5)

        # Animacja wybuchu
        animacja_wybuchu()

        # Sprawdź wynik
        wynik = kto_wygrywa(gracz, komputer)
        rundy += 1

        # Pokaż opis walki
        pokaz_opis_wygranej(gracz, komputer, wynik)

        if wynik == "remis":
            animacja_remisu()
        elif wynik == "gracz":
            gracz_pkt += 1
            animacja_wygranej()
        else:
            komputer_pkt += 1
            animacja_przegranej()

        # Pokaż aktualny wynik
        pokaz_wynik(gracz_pkt, komputer_pkt, rundy)

        input(f"  {Kolor.DIM}Naciśnij ENTER aby kontynuować...{Kolor.RESET}")


# ── Start gry ──────────────────────────────────────────
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {Kolor.CYAN}Do zobaczenia! 👋{Kolor.RESET}\n")
