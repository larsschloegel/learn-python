import random

class ZorkDeutsch:
    def __init__(self):
        self.aktuelle_raum = "vor_dem_haus"
        self.inventar = []
        self.spieler_leben = True
        self.lampe_an = False
        self.bewegungen = 0
        
        # Räume definieren
        self.raeume = {
            "vor_dem_haus": {
                "beschreibung": "Sie stehen vor einem weißen Haus mit verschlossener Vordertür. Ein kleiner Briefkasten steht hier.",
                "ausgaenge": {"norden": "wald", "sueden": "sued_vom_haus", "osten": "ost_vom_haus", "westen": "west_vom_haus"},
                "gegenstaende": ["briefkasten", "blaettchen"]
            },
            "wald": {
                "beschreibung": "Sie befinden sich in einem Wald. Pfade führen in alle Richtungen.",
                "ausgaenge": {"sueden": "vor_dem_haus", "norden": "lichtung", "osten": "wald", "westen": "wald"},
                "gegenstaende": []
            },
            "lichtung": {
                "beschreibung": "Sie sind auf einer kleinen Lichtung im Wald. Ein Gitter führt nach unten.",
                "ausgaenge": {"sueden": "wald", "unten": "keller_eingang"},
                "gegenstaende": []
            },
            "keller_eingang": {
                "beschreibung": "Sie stehen vor einem dunklen Kellertunnel. Ohne Licht können Sie nicht weitergehen.",
                "ausgaenge": {"oben": "lichtung", "norden": "dunkler_tunnel"},
                "gegenstaende": []
            },
            "dunkler_tunnel": {
                "beschreibung": "Es ist stockdunkel hier. Sie könnten von einem Troll gefressen werden.",
                "ausgaenge": {"sueden": "keller_eingang", "norden": "schatzkammer"},
                "gegenstaende": [],
                "dunkel": True
            },
            "schatzkammer": {
                "beschreibung": "Eine prächtige Schatzkammer! Hier liegt ein funkelnder Diamant!",
                "ausgaenge": {"sueden": "dunkler_tunnel"},
                "gegenstaende": ["diamant"],
                "dunkel": True
            },
            "sued_vom_haus": {
                "beschreibung": "Sie befinden sich südlich des weißen Hauses.",
                "ausgaenge": {"norden": "vor_dem_haus", "westen": "west_vom_haus"},
                "gegenstaende": []
            },
            "ost_vom_haus": {
                "beschreibung": "Sie befinden sich östlich des weißen Hauses. Ein Fenster ist hier.",
                "ausgaenge": {"westen": "vor_dem_haus", "sueden": "sued_vom_haus"},
                "gegenstaende": ["fenster"]
            },
            "west_vom_haus": {
                "beschreibung": "Sie befinden sich hinter dem weißen Haus. Eine Küchentür ist hier.",
                "ausgaenge": {"osten": "vor_dem_haus", "norden": "kueche"},
                "gegenstaende": []
            },
            "kueche": {
                "beschreibung": "Sie sind in der Küche des weißen Hauses. Ein Sack mit Knoblauch hängt hier.",
                "ausgaenge": {"sueden": "west_vom_haus", "osten": "wohnzimmer"},
                "gegenstaende": ["knoblauch", "messer"]
            },
            "wohnzimmer": {
                "beschreibung": "Ein gemütliches Wohnzimmer mit einem großen Orientteppich in der Mitte.",
                "ausgaenge": {"westen": "kueche", "unten": "keller"},
                "gegenstaende": ["teppich", "lampe"]
            },
            "keller": {
                "beschreibung": "Ein dunkler Keller unter dem Haus.",
                "ausgaenge": {"oben": "wohnzimmer"},
                "gegenstaende": [],
                "dunkel": True
            }
        }
        
        # Spezielle Gegenstände
        self.gegenstaende_info = {
            "lampe": {"tragbar": True, "beschreibung": "Eine Messinglampe"},
            "diamant": {"tragbar": True, "beschreibung": "Ein funkelnder Diamant von unschätzbarem Wert!"},
            "knoblauch": {"tragbar": True, "beschreibung": "Ein Bund Knoblauch"},
            "messer": {"tragbar": True, "beschreibung": "Ein scharfes Elfenmesser"},
            "blaettchen": {"tragbar": True, "beschreibung": "Ein kleines Blättchen mit Text"},
            "briefkasten": {"tragbar": False, "beschreibung": "Ein kleiner Briefkasten"},
            "teppich": {"tragbar": False, "beschreibung": "Ein großer Orientteppich"},
            "fenster": {"tragbar": False, "beschreibung": "Ein geschlossenes Fenster"}
        }

    def zeige_raum(self):
        raum = self.raeume[self.aktuelle_raum]
        print(f"\n{raum['beschreibung']}")
        
        # Prüfe ob Raum dunkel ist
        if raum.get('dunkel', False) and not self.lampe_an:
            print("Es ist zu dunkel, um etwas zu sehen.")
            return
            
        if raum['gegenstaende']:
            print("Sie sehen hier:", ", ".join(raum['gegenstaende']))
        
        ausgaenge = list(raum['ausgaenge'].keys())
        print(f"Ausgänge: {', '.join(ausgaenge)}")

    def gehe(self, richtung):
        raum = self.raeume[self.aktuelle_raum]
        
        if richtung in raum['ausgaenge']:
            neue_raum = raum['ausgaenge'][richtung]
            
            # Prüfe auf dunklen Tunnel ohne Licht
            if neue_raum == "dunkler_tunnel" and not self.lampe_an:
                print("Es ist zu gefährlich, ohne Licht in die Dunkelheit zu gehen!")
                return
                
            self.aktuelle_raum = neue_raum
            self.bewegungen += 1
            self.zeige_raum()
        else:
            print("Sie können nicht in diese Richtung gehen.")

    def nimm(self, gegenstand):
        raum = self.raeume[self.aktuelle_raum]
        
        if raum.get('dunkel', False) and not self.lampe_an:
            print("Es ist zu dunkel, um etwas zu sehen.")
            return
            
        if gegenstand in raum['gegenstaende']:
            if self.gegenstaende_info.get(gegenstand, {}).get('tragbar', True):
                raum['gegenstaende'].remove(gegenstand)
                self.inventar.append(gegenstand)
                print(f"Sie nehmen {gegenstand}.")
            else:
                print(f"Sie können {gegenstand} nicht mitnehmen.")
        else:
            print(f"Hier ist kein {gegenstand}.")

    def untersuche(self, gegenstand):
        if gegenstand == "briefkasten":
            print("Der Briefkasten ist leer, bis auf ein kleines Blättchen.")
        elif gegenstand == "blaettchen":
            print("Auf dem Blättchen steht: 'Willkommen bei ZORK! Ihre Lampe wird schwächer.'")
        elif gegenstand == "teppich":
            print("Unter dem Teppich befindet sich eine Falltür!")
            if "falltuer" not in self.raeume["wohnzimmer"]["gegenstaende"]:
                self.raeume["wohnzimmer"]["gegenstaende"].append("falltuer")
        elif gegenstand in self.gegenstaende_info:
            print(self.gegenstaende_info[gegenstand]["beschreibung"])
        else:
            print("Das ist nichts Besonderes.")

    def inventar_zeigen(self):
        if self.inventar:
            print("Sie tragen:", ", ".join(self.inventar))
        else:
            print("Sie tragen nichts.")

    def lampe_schalten(self, an_aus):
        if "lampe" in self.inventar:
            if an_aus == "an":
                self.lampe_an = True
                print("Die Lampe ist jetzt an.")
            elif an_aus == "aus":
                self.lampe_an = False
                print("Die Lampe ist jetzt aus.")
        else:
            print("Sie haben keine Lampe.")

    def verarbeite_befehl(self, befehl):
        befehl = befehl.lower().strip()
        woerter = befehl.split()
        
        if not woerter:
            return
            
        kommando = woerter[0]
        
        # Bewegungsbefehle
        if kommando in ["norden", "n", "nord"]:
            self.gehe("norden")
        elif kommando in ["sueden", "s", "sued"]:
            self.gehe("sueden")
        elif kommando in ["osten", "o", "ost"]:
            self.gehe("osten")
        elif kommando in ["westen", "w", "west"]:
            self.gehe("westen")
        elif kommando in ["oben", "hoch"]:
            self.gehe("oben")
        elif kommando in ["unten", "runter"]:
            self.gehe("unten")
        
        # Aktionsbefehle
        elif kommando in ["nimm", "nehme", "hole"]:
            if len(woerter) > 1:
                self.nimm(woerter[1])
            else:
                print("Was möchten Sie nehmen?")
        
        elif kommando in ["untersuche", "betrachte", "schaue", "schau"]:
            if len(woerter) > 1:
                self.untersuche(woerter[1])
            else:
                self.zeige_raum()
        
        elif kommando in ["inventar", "inv", "i"]:
            self.inventar_zeigen()
        
        elif kommando == "lampe":
            if len(woerter) > 1:
                self.lampe_schalten(woerter[1])
            else:
                print("Lampe an oder aus?")
        
        elif kommando in ["hilfe", "help", "?"]:
            self.zeige_hilfe()
        
        elif kommando in ["quit", "q", "ende", "beenden"]:
            print("Auf Wiedersehen!")
            self.spieler_leben = False
        
        else:
            print("Das verstehe ich nicht. Versuchen Sie 'hilfe' für eine Liste der Befehle.")

    def zeige_hilfe(self):
        print("""
Verfügbare Befehle:
- Bewegung: norden/n, sueden/s, osten/o, westen/w, oben, unten
- Aktionen: nimm [gegenstand], untersuche [gegenstand], schaue
- Ausrüstung: inventar/i, lampe an/aus
- System: hilfe, quit/q
        """)

    def spiel_starten(self):
        print("ZORK - Die deutsche Ausgabe")
        print("==========================")
        print("Sie sind ein Abenteurer, der vor einem weißen Haus steht.")
        print("Ihr Ziel ist es, Schätze zu finden und das Geheimnis zu lösen.")
        print("Tippen Sie 'hilfe' für Befehle.\n")
        
        self.zeige_raum()
        
        while self.spieler_leben:
            try:
                befehl = input("\n> ")
                self.verarbeite_befehl(befehl)
                
                # Prüfe Gewinnbedingung
                if "diamant" in self.inventar and self.aktuelle_raum == "vor_dem_haus":
                    print("\nGlückwunsch! Sie haben den Diamanten gefunden und sind zurück zum Haus!")
                    print(f"Sie haben das Spiel in {self.bewegungen} Zügen gewonnen!")
                    break
                    
            except KeyboardInterrupt:
                print("\nAuf Wiedersehen!")
                break

# Spiel starten
if __name__ == "__main__":
    spiel = ZorkDeutsch()
    spiel.spiel_starten()