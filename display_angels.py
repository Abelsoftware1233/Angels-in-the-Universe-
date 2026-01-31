import json

# De data die we hebben verzameld
celestial_data = {
    "entities": [
        {
            "name": "Hourglass Nebula (MyCn18)",
            "span_ly": 0.5,
            "distance_ly": 8000,
            "feature": "Lijkt op een alziend oog",
            "meaning": "Goddelijke waakzaamheid / Raquib"
        },
        {
            "name": "Celestial Angel (S106)",
            "span_ly": 2.0,
            "distance_ly": 2000,
            "feature": "Symmetrische vleugels",
            "meaning": "Engelen die de horizon vullen"
        },
        {
            "name": "Pillars of Creation (M16)",
            "span_ly": 5.0,
            "distance_ly": 7000,
            "feature": "Gigantische oprijzende figuren",
            "meaning": "Kosmische schaal van engelen"
        },
        {
            "name": "Hand of God (PSR B1509)",
            "span_ly": 150.0,
            "distance_ly": 17000,
            "feature": "Vorm van een hand",
            "meaning": "Uitvoerders van goddelijke wil"
        }
    ]
}

def toon_onderzoek_tabel(data):
    print(f"{'NAAM NEVEL':<25} | {'GROOTTE (LJ)':<15} | {'AFSTAND (LJ)':<15} | {'BETEKENIS'}")
    print("-" * 85)
    for entity in data['entities']:
        print(f"{entity['name']:<25} | {entity['span_ly']:<15} | {entity['distance_ly']:<15} | {entity['meaning']}")

if __name__ == "__main__":
    print("--- Echo AI: Onderzoek naar Kosmische Engelen ---\n")
    toon_onderzoek_tabel(celestial_data)
