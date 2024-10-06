import random 
from typing import List, Tuple

# Ger värde till korten, korten har sina respektive värde.
# Ess har två möjliga värden (1, 14).
Kort_värde = {
    "Ess": [1, 14], "Kung": 13, "Dam": 12, "Knekt":11,
    "10": 10, "9": 9, "8": 8, "7":7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
    }

# Definiera kort som en typ
Kort = Tuple[str, int] 

# Den här klassen hanterar kortleken och dess funktionalitet.
class Kortlek: 

    def __init__(self) -> None:
        # Skapar en ny kortlek med alla kort genom att anropa skapa_kortlek-funktionen.
        self.kortlek: List[Kort] = self.skapa_kortlek()

    def skapa_kortlek(self) -> List[Tuple[str, int]]:
        # Skapar en ny kortlek med alla kort som tupler (kortnamn, värde). 
    
        kortlek: List[Tuple[str, int]] = []
        # Loopa genom alla kort i Kort_värde.
        for kort_namn, kort_värde in Kort_värde.items():
            # Om kortet har fler värden (som Ess), lägg till varje värde separart.
            if isinstance(kort_värde, list):
                for värde in kort_värde:
                    kortlek.append((kort_namn, värde))
            
            else: 
                # Lägg till kortet med sitt värde i kortleken.
                kortlek.append((kort_namn, kort_värde))
        
        return kortlek

    def dra_kort(self) -> Tuple[str, int]:
        # Drar ett kort slumpmässigt från kortleken.
        # Om kortleken är tom, skapas en ny kortlek.
       
        if not self.kortlek:
            print("Kortleken är slut! Skapar en ny!")
            self.kortlek = self.skapa_kortlek()
        # Välj ett kort slumpmässigt och ta bort det från kortleken. 
        kort = random.choice(self.kortlek)
        self.kortlek.remove(kort)
        return kort

# Den här klassen hanterar spelet 21, som ikluderar spelarens och datorns turer samt poängberäkningen. 
class Tjugoett:
    def __init__(self):                 
    # Skapar spelarens och datorns händer som listor av kort.
         
        self.spelarens_hand: List[Tuple[str, int]] = []           # Spelarens kort
        self.datorns_hand: List[Tuple[str, int]] = []             # Datorns kort
        self.kortlek = Kortlek()                                  # Skapa en instans av Kortlek för att dra kort

    def dra_kort(self) -> Kort:            
    # Drar ett kort från kortleken genom att använda Kort_värde. 
           
        return self.kortlek.dra_kort()

    def räkna_summan(self, hand: List[Kort]) -> int:
    # Beräknar summan av kortens värde i handen.
    # Hanterar också att Ess kan ha två olika värden dvs 1 eller 14.
        
        summa = sum(kort[1] for kort in hand)
        antal_ess = sum(1 for kort in hand if kort[0] == "Ess")   # Räkna antal Ess i handen.
 
        while summa > 21 and antal_ess > 0:  
            # Om summan är större än 21, justera värdet av Ess till 1.                     
            summa -= 13
            antal_ess -= 1
        return summa


    def spelarens_tur(self) -> None:
    # Hanterar spelarens tur, spelaren får välja att dra fler kort. 
        while True:                                               
            # Dra ett kort och lägg det i spelarens hand.    
            kort = self.dra_kort()
            self.spelarens_hand.append(kort)
            print(f"Du har dragit {kort[0]} med värdet {kort[1]}.")
            # Beräkna spelarens totala poäng. 
            din_poäng = self.räkna_summan(self.spelarens_hand)
            print(f"Din totala poäng är: {din_poäng}")

            # Om spelarens poäng blir mer än 21, förlorar spelaren.
            if din_poäng > 21:
                print("Du har överstigit 21. Du förlorar!")
                return
            # Spelaren får välja om hen vill dra ett till kort.
            while True:
                choice: str = input("Vill du dra ett till kort? (Ja eller Nej): ").lower()
                if choice in ["ja", "nej"]:
                    break
                else:
                    print("Felaktigt svar! Var god skriv 'ja' eller 'nej'")
            # Om spelaren inte vill dra flera kort, avsluta spelarens tur. 
            if choice != "ja":
                break

        
    def datorns_tur(self) -> None:
    # Hanterar datorns tur där den drar kort tills den når minst 17 poäng. 
        while True:
            # Datorns drar ett kort och lägger det i sin hand.
            kort = self.dra_kort()
            self.datorns_hand.append(kort)
            # Beräkna datorns poäng.
            datorns_poäng = self.räkna_summan(self.datorns_hand)
            print(f"Datorn har dragit {kort[0]} med värdet {kort[1]}. Datorns poäng är: {datorns_poäng}")
            # Om datorns poäng blir mer är 21, vinner spelare. 
            if datorns_poäng > 21:
                print("Datorn har överstigit 21. Du vinner!")
                return
            # Om datorns poäng är 17 eller mer, stannar den.
            elif datorns_poäng >= 17:
                print("Datorn stannar!")
                break

    def bestämma_vinnaren(self) -> None:
    # Bestämmer vinnaren genom att jämföra deras(spelarens och datorns) poäng. 
        spelarens_poäng = self.räkna_summan(self.spelarens_hand)
        datorns_poäng = self.räkna_summan(self.datorns_hand)

        print(f"Spelarens hand: {spelarens_poäng} poäng, Datorns hand: {datorns_poäng} poäng.")

        # Vinnare baserat på reglerna för 21.
        if datorns_poäng > 21 or (spelarens_poäng <= 21 and spelarens_poäng > datorns_poäng): 

            print("Datorn har överstigit 21. Good job! Du vinner!")

        elif spelarens_poäng == datorns_poäng:
            print("Det blev oavgjort!")

        else:
            print("Datorn vinner!")

    def spela(self) -> None:
    # Börja av att spela en omgång av 21.
        print("Välkommen till spelet 21!")
        

        # Spelarens tur startar.
        self.spelarens_tur()
        # Om spelarens poäng är 21 eller mindre, gåt turen vidare till datorn.
        if self.räkna_summan(self.spelarens_hand) <= 21:
            self.datorns_tur()
        # Efter att båda har kört, bestämms vinnaren.
        self.bestämma_vinnaren()
                    
# Huvudprogrammet som låter spelaren spela flera omgångar.
if __name__ == "__main__":
    while True:
        # Starta en ny omgång av spelet.
        spel = Tjugoett()
        spel.spela()
        # Fråga om spelaren vill spela igen. 
        while True:
            spela_igen: str = input("Vill du spela igen? (Ja eller Nej): ").lower()
            if spela_igen == "ja":
                print("Spelet börjar om! Here we go!")
                break
            elif spela_igen== "nej":
                print("Tack för att du spelade! Untill next time!")
                exit()
            else:
                print("Felaktigt svar! Var god skriv 'ja' eller 'nej'.")
                
    spel = Tjugoett()
    spel.spela()