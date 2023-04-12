# Mittausdatan tulostaminen Google Chartin avulla

Tämän demon tarkoitus on näyttää, miten mittausdataa voidaan visualisoida käyttäen Python Flaskia ja Google Chart -Javascript-kirjastoa.

Ohjelma koostuu Flask-sovelluksesta ja mittaustietoa tuottavasta sovelluksesta. Flask-sovellus ottaa vastaan sisätilapaikannusjärjestelmän tuottamaa sijaintitietoa (xyz-koordinaatit) ja näyttää tämän tiedon HTML-sivulla.

Tässä demossa ei käytetä oikeaa sisätilapaikannusjärjestelmää, vaan mittauksia simuloidaan ohjelmalla datageneratorclient.py. Tämä ohjelma generoi xyz-koordinaatteja ja lähettää simuloidun sijaintitiedon HTTP POST -metodin avulla Flask-sovellukselle. Flask-sovellus ottaa viestit vastaan, muuntaa ne Google Chartille sopivaan muotoon ja tallentaa ne listaan. Mittaukset tallennetaan tähän listaan sellaisessa muodossa, että Google Chart osaa tulostaa sijaintiedon Line Chart -muodossa suoraan.

Ohjelma datageneratorclient.py voidaan korvata sijaintitietoa tuottavalla laitteella. Flask-sovellusta voidaan myös muuttaa siten, että tiedot tallennetaan listan sijasta tietokantaan.

Ohjelma ei päivitä selainsivua automaattisesti, kun palvelin saa uutta dataa. Selainsivu täytyy päivittää itse käsin. Tiedon päivittäminen sivulle automaattisesti tehdään seuraavassa vaiheessa. Tähän voi käyttää esimerkiksi socket.io-kirjastoa.

## Tiedostot

Demo koostuu seuraavista tiedostoista:

- measserver.py: Flask-palvelinsovellus, joka ottaa vastaan mittaustietoa ja näyttää sen HTML-muodossa.
- datageneratorclient.py: simulaattoriohjelma, joka generoi mittausdataa ja lähettää sitä HTTP POST -metodin avulla Flask-sovellukselle
- readdata.py: vaihtoehtoinen simulaattoriohjelma, joka lukee tekstitiedostoon tallennettua paikkadataa ja lähettää sitä HTTP POST -metodin avulla Flask-sovellukselle
- data_2022_02_23.txt: paikkadataa sisältävä datatiedosto readdata.py-ohjelmaa varten
- templates/linechart.html: HTML-tiedosto, joka näyttää sijaintidatan graafisessa muodossa käyttäen Google Chart -Javascript-kirjastoa.

## Demon ajaminen

Kokeile ohjelmaa näin:

1. Asenna tarvittavat Python-kirjastot: 
   - pip install matplotlib
   - pip install requests
   - pip install Flask
2. Käynnistä Flask-palvelinohjelma measserver.py
3. Avaa selain ja anna url http://localhost:5000/line
4. Käynnistä simulaattoriohjelma (datageneratorclient.py tai readdata.py)




