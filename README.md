# Vis ur og citater
Dette projekt omdanner din raspberry pi med display ind til et ur og skifter tilfældig citater hver 10 sekundt. Som staret automatisk når du tænder den.
Citater kommer fra en txt 

![RaspberryPI med Ur og Citater](image/PimedURCitat.png)


# Forudsætninger for projekt

## Materialer 
- Raspberry med display

# Opsætning

Hent **citater.py** og **citater.txt** og lig den i /home/user fx /home/mg/citater.py som jeg brugerflade

# Opsætning af systemd til automatisk kørsel af Python-script ved opstart

Dette dokument beskriver, hvordan du opsætter **systemd** til at køre et Python-script (f.eks. **citater.py**) automatisk ved opstart af din Raspberry Pi.

## Forudsætninger for automatisk opstart
- Du har en Raspberry Pi med en korrekt installeret Python 3.
- Du har et Python-script (f.eks. `citater.py`), som du ønsker at køre ved opstart.
- Du har adgang til en terminal og root-rettigheder på Raspberry Pi.

## Trin 1: Opret systemd servicefil

1. Åbn terminalen og opret en ny systemd-servicefil:

```bash
   sudo nano /etc/systemd/system/citater.service
```

Indsæt følgende indhold i servicefilen:
```bash
[Unit]
Description=Viser citater og klokken på touchscreen
After=graphical.target

[Service]
ExecStartPre=/bin/sleep 10
ExecStart=/usr/bin/python3 /home/mg/citater.py
WorkingDirectory=/home/mg
StandardOutput=inherit
StandardError=inherit
Restart=always
User=mg
Environment=DISPLAY=:0
Environment=XDG_RUNTIME_DIR=/run/user/1000

[Install]
WantedBy=graphical.target
```
## Forklaring:

**After=graphical.target**: Sørger for, at servicen først starter, når den grafiske brugerflade er klar.

**ExecStartPre**=/bin/sleep 10: Tilføjer en 10-sekunders forsinkelse før scriptet starter, så systemet er klar.
**ExecStart**: Kører Python-scriptet.

**Environment=DISPLAY=:0** og 

**XDG_RUNTIME_DIR=/run/user/1000:** Sikrer, at scriptet har adgang til skærmen.
Gem og luk filen: CTRL + X, derefter Y og ENTER.

## Trin 2: Aktivér og start systemd-servicen

Genindlæs systemd og aktiver servicen:

```bash
sudo systemctl daemon-reload
```

sudo systemctl enable citater.service
Start servicen:
sudo systemctl start citater.service
Bekræft, at servicen kører:
sudo systemctl status citater.service

## Trin 3: Test automatisk opstart

Genstart din Raspberry Pi for at teste, om servicen starter automatisk ved opstart:
sudo reboot
Efter reboot, tjek om servicen kører:
sudo systemctl status citater.service
Fejlfinding

Hvis servicen ikke starter korrekt, kan du se systemd-loggen for eventuelle fejl:
journalctl -u citater.service -b
Hvis du får fejlmeddelelsen XDG_RUNTIME_DIR is invalid or not set in the environment, sørg for, at miljøvariablerne er korrekt indstillet i systemd-servicefilen.
Ekstra tips

Hvis du vil ændre forsinkelsen før scriptet starter, kan du justere ExecStartPre=/bin/sleep 10 til en anden værdi.
Sørg for, at din Python-skript ikke indeholder fejl og fungerer korrekt, når du kører det manuelt.
Denne guide hjælper dig med at sikre, at dit script automatisk starter ved opstart og kører stabilt på din Raspberry Pi.


### **Kort forklaring på filens indhold:**
- **Installation**: Forklarer, hvordan du opretter og konfigurerer systemd-servicefilen.
- **Fejlfinding**: Giver tips til, hvordan man kan debugge eventuelle problemer, der opstår, f.eks. hvis systemet ikke starter scriptet korrekt.
- **Test**: Forklarer, hvordan man kan sikre, at servicen starter korrekt efter en genstart.

Slut Slut





