# Testausdokumentti

    Yksikkötestauksen kattavuusraportti.
    Mitä on testattu, miten tämä tehtiin?
    Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
    Miten testit voidaan toistaa?
    Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.


Testaus on ideaalitapauksessa suoritettava ohjelma. Tällöin testi on helposti toistettavissa, mikä helpottaa toteutuksen tekoa jo varhaisessa vaiheessa. Ainakin yksikkötestit tulee suorittaa ohjelmallisesti, ja niiden kattavuus tulee raportoida automaattisella välineellä. Yksikkötesteillä tulee testata kaikki paitsi käyttöliittymä, suorituskykytestit ja mahdollisesti tiedostojen luku ja kirjoittaminen riippuen projektista.

Mieti mitä oman sovelluksesi toiminnan oikeellisuus tarkoittaa. Reitinhakualgoritmin tulee löytää lyhin reitti, ja reitin ja sen etsinnän etenemisen pitää olla sen kaltainen kuin on tarkoitus. Labyrintin tai luolaston tulee yleensä olla yhtenäinen. Miinaharavabotti ei saa koskaan osua miinaan silloin, kun ruutua pidetään turvallisena. Pakatun tiedoston koon täytyy olla odotusten mukainen, ja sen tulee purkautua alkuperäiseksi - tai näyttää / kuulostaa oikealta, jos kyseessä on häviöllinen pakkaus. Shakkibotti ei saa tehdä laittomia siirtoja, ja sen on osattava tehdä matti, mikäli se on mahdollista sillä laskentasyvyydellä, jota käytetään. Jos kattava oikeellisuustesti vie liikaa aikaa, kannattaa laittaa yksikkötesteihin vain pari edustavaa testitapausta, ja tehdä lisäksi erillinen testiohjelma.

Suorituskykytestaus vie yleensä niin paljon aikaa, että sitä ei kannata tehdä automaattisilla testeillä ohjelman käynnistyksen yhteydessä. Jos yksikkötestien suorittamiseen menee useita minuutteja, ne tulee helposti ohitettua. Vastaavasti jos suorituskykytestien ajamiseen menee alle minuutti, on aika todennäköistä, että testit eivät ole riittäviä. Kokonaisuus täytyy yleensä testata itse kokeilemalla, raportoidaan mitä on kokeiltu. Testeissä saa käyttää mitä tahansa apukirjastoa. Testikattavuus tulee laskea automaattisesti. Huomaa silti, että kattavuuslaskenta on vain apuväline. On hyvin mahdollista tuottaa 100% kattavuus huonosti testatulle koodille. Tavoitteena on havaita kaikki virheet ohjelman toiminnassa. Kannattaa kirjoittaa mahdollisimman pieniä yksikkötestejä mahdollisimman paljon. Ideana on, että jos koodissa on virhe, tulisi vähintään yhden testin havaita se, ja virheen kohta koodissa tulisi olla mahdollisimman selkeä. Tämä on tärkeää, jotta virheiden korjaaminen on tehokasta.
