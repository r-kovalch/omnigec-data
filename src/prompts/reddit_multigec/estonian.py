from src.prompts.base_prompts import BasePrompt


class MultiGrammarErrorCorrectionGenerationPrompt(BasePrompt):
    template: str = """Parandage järgmine tekst, et see oleks grammatiliselt korrektne.
Parandage kõik õigekirja-, kirjavahemärgistamis-, stiili-, grammatilised, leksikaalsed ja süntaktilised vead.
Kui vigu ei ole, korrake originaalteksti.
Looge {num_corrections} parandatud teksti erinevad versioonid koos selgitustega.
Eemaldab kõik topeltlause- ja muud erimärgid vastuses kahe kaldkriipsuga.
Näiteks kasutage uue joone asemel märki \\n; „ asemel kasutage vabastatud märki \\“.
Palun ärge eemaldage tehnilisi sümboleid, nagu internetilingid, sildid jms teistest keeltest (peamiselt inglise keelest).


Vastuse vorming JSONis:
[{{
    "correction": "parandatud tekst",
    "explanation": "selgitus korrektsiooni kohta"
}}, ...]

Näited:

1.  Sisestatud tekst:
    Tere, Liina.
    Kirjutan Sulle, sest mul on suur brobleem.
    Minu külmkapp on katki ja vaja remontida.
    Ma oskan, et sinu abikaasa on väga hea maister.
    Võib-olla ta saab aidata minule.
    Kui teil on vaba aeg, helista palun mulle telefonil --- või tulge mulle külla aadressil Luha ---, Tallinnas.
    Head aega.
    Sinu sõbranna, Olga.

    Parandus:
    [("Tere, Liina! Kirjutan Sulle, sest mul on suur probleem. Minu külmkapp on katki ja seda on vaja remontida. Ma tean, et sinu abikaasa on väga hea meister. Võib-olla ta saab mind aidata. Kui teil on vaba aega, helistage palun mulle telefonil --- või tulge mulle külla aadressil Luha ---, Tallinn. Head aega! Sinu sõbranna Olga.", "Parandati õigekirja- ja grammatikavead ('brobleem' → 'probleem', 'vaja remontida' → 'seda on vaja remontida') ning muudetud sõnavalik ('oskan' → 'tean') ja formaalne kõnepruuk (nt 'helista' → 'helistage')."),
    ("Tere, Liina! Kirjutan Sulle, sest mul on suur probleem. Minu külmkapp on katki ning seda tuleb remontida. Ma usun, et sinu abikaasa on väga osav meister, kes saab mind aidata. Kui Teil on vaba aega, palun helistage mulle või tulge külla aadressil Luha ---, Tallinn. Head aega! Sinu sõbranna, Olga.", "Alternatiivne variant, kus väljendeid täpsustati ja ühendussõna 'ning' lisati, et parandada lausete sidusust ning muuta tekst selgemaks."),
    ("Tere, Liina! Kirjutan Sulle, sest mul on suur probleem. Minu külmkapp on katki ja vajab remonti. Tean, et sinu abikaasa on väga hea meister ning võib-olla oskab ta mind aidata. Kui Teil on vaba aega, helistage palun mulle telefonil --- või tulge külla aadressil Luha ---, Tallinn. Head aega! Sinu sõbranna Olga.", "Kohandatud lauseehitus ja sõnavalik, et vältida mitmetähenduslikkust ning tagada ühtlane stiil.")]
    
2.  Sisestatud tekst:
    Tere, Peeter!
    Mul on väike problem.
    Mul on vaja sinu appi.
    Mul kodumasin läks katki, tilgub.
    Tulge palun minu juurde koju ja vaata, võib teha remonti või ei.
    Väga kahju tuleb, kui ei saa teha.
    Ta vaatas ja tegid kõik korras.
    Ma olin väga rahul.
    Selle pärast ma annan sõbrale palju õunad, kurgid ja tomatid, ja ütlesin "Suur tänu".
    Väga tubli poeg (mees)
    
    Parandus:
    [("Tere, Peeter! Mul on väike probleem. Mul on vaja sinu abi. Mul läks kodumasin katki, see tilgub. Tule palun minu juurde koju ja vaata, kas saab remonti teha või mitte. Väga kahju, kui remonti ei saa teha. Sa vaataksid ja teeksid kõik korda. Ma oleksin väga rahul. Selle tõttu annaksin ma sõbrale palju õunu, kurke ja tomateid ning ütleksin "Suur tänu". Väga tubli poeg (mees)!", "Parandati õigekirja- ja grammatikavead ('problem' → 'probleem', 'appi' → 'abi') ning täpsustati lauseehitus ja väljendid (nt 'tilgub' eelduseks lisati 'see')."),
    ("Tere, Peeter! Mul on väike probleem. Mul on vaja sinu abi. Kodumasin läks katki ja see tilgub. Palun tule minu juurde koju ja vaata, kas remont on võimalik teha. On väga kahju, kui remonti ei saa korraldada. Ootaksin, et sa vaataksid ja teeksid kõik korda. Ma oleksin väga rahul. Seetõttu annaksin sõbrale palju õunu, kurke ja tomateid ning ütleksin "Suur tänu". Väga tubli poeg (mees)!", "Muudetud lause struktuuri ja väljendit, et tagada tekstis selgus ja korrektsus."),
    ("Tere, Peeter! Mul on väike probleem ja mul on vaja sinu abi. Minu kodumasin on katki ning see tilgub. Tule palun minu juurde koju ja kontrolli, kas saab remonti teha. On tõesti kahju, kui remonti ei osata teha. Ma oleksin väga rahul, kui sa vaataksid ja parandaksid kõik vead. Sellepärast annaksin ma sõbrale palju õunu, kurke ja tomateid ning ütlen "Suur tänu". Väga tubli poeg (mees)!", "Parandatud lauseehitus ja sõnavalik, et muuta tekst sujuvamaks ja selgemaks, säilitades samas algse sõnumi.") ]
    
3.  Sisestatud tekst:
    Ma tahan müüa autod.
    Minu auto välimus on punane BMW.
    See auto maksab viis tuhat eurod.
    Te saate autot näha 14. mail.
    Me saame kohtuda teie kodu ääres.
    Te saate mulle helistada numbrile ---.
    Minu eesnimi on Julia.
    See auto on uus ja korralik
    Sõidab auto kiiresti.
    Ma müüan seda autod, sest mulle kingitakse uue autod
    
    Parandus:
    [("Ma tahan müüa autot. Minu auto on punane BMW. See auto maksab viis tuhat eurot. Te saate autot näha 14. mail. Me saame kohtuda teie kodu juures. Te saate mulle helistada numbril ---. Minu eesnimi on Julia. See auto on uus ja korralik. Auto sõidab kiiresti. Ma müün seda autot, sest mulle kingitakse uus auto.", "Parandati õigekirja- ja grammatikavead ('autod' → 'autot', 'eurod' → 'eurot'), muudetud kääned ja täpsustatud lauseehitus."),
    ("Ma soovin müüa autot. Minu auto, mis on punane BMW, maksab viis tuhat eurot. Autot saab näha 14. mail. Kohtume teie kodu juures ning te võite mulle helistada numbrile ---. Minu eesnimi on Julia. Auto on uus, korralik ja sõidab kiiresti. Müün seda autot, sest mulle kingitakse uus auto.", "Alternatiivne variant, kus sõnastust muudetud, et tekst oleks voolavam ja selgem."),
    ("Ma tahan müüa autot. Minu auto on punane ja tegemist on BMW-ga. Auto hind on viis tuhat eurot. Te saate autot näha 14. mail. Kohtume teie kodu juures, kus te saate mulle helistada numbril ---. Minu eesnimi on Julia. Auto on uus, korralik ja sõidab kiiresti. Ma müün seda autot, sest mulle kingitakse uus auto.", "Korrigeeritud grammatikavead ning sõnastuse ühtlustamine, et tagada loogiline ja korrektne esitlus.") ]
    
4.  Sisestatud tekst:
    Tere, minu kallis Anton!
    Tahan sulle teatada, et ma soovin müüa oma autot.
    See on suur must autot BMW X6.
    Auto hind on 25 000 eurot.
    Autot saab näha Fama Keskuses esmapäevast kuni pühapäevani kell 12.00.
    Kui miski ei laabu, siis helista mulle.
    Julia
    
    Parandus:
    [("Tere, minu kallis Anton! Tahan sulle teatada, et ma soovin müüa oma autot. See on suur must auto, BMW X6. Auto hind on 25 000 eurot. Autot saab näha Fama Keskuses esmaspäevast kuni pühapäevani kell 12.00. Kui miski ei laabu, siis helista mulle. Julia", "Parandati vigu väljendis 'must autot' -> 'must auto' ning 'esmapäevast' -> 'esmaspäevast', et tagada korrektne käänamine ja sõnavalik."),
    ("Tere, kallis Anton! Soovin teatada, et ma müün oma autot. Tegemist on suure musta BMW X6-ga, mille hind on 25 000 eurot. Autot saab näha Fama Keskuse aegadel esmaspäevast kuni pühapäevani kell 12.00. Kui midagi ei laabu, helista mulle. Julia", "Alternatiivne variant, kus muudetud sõnastust ja lauseehitust, et tekst oleks voolavam ning selgem. Muudetud 'minu kallis Anton' -> 'kallis Anton' ja täpsustatud väljend 'müüa oma autot' -> 'müün oma autot'."),
    ("Tere, minu kallis Anton! Annan teada, et soovin müüa oma autot. See on suur must BMW X6, mille hind on 25 000 eurot. Autot saab vaadata Fama Keskuses esmaspäevast kuni pühapäevani kell 12.00. Kui midagi läheb valesti, siis palun helista mulle. Julia", "Kohandatud lauseehitus ja sõnavalik: 'teatan' asendatud 'annan teada', 'vaadata' asendatud 'näha', et väljendada selgemat mõtet ning parandada grammatilisi ebakõlasid.") ]

5.  Sisestatud tekst:
    Kevadel ma kaisin Kaanari saartel.
    Ma kaisin lennukuga.
    Ma elasin viietärnuhotellis.
    Ma magisin, sõin ja kaisin rannas.
    Ma kaisin seal iga aasta.
    Mulle väga meeldib seal.
    loodus on väga ilus.
    Päike päistas.
    ilm oli palav.
    Reis läks maksma umbes 1000 euro inimesekohta.
    
    Parandus:
    [("Kevadel käisin ma Kanaari saartel. Ma käisin lennukiga. Ma elasin viietärnihotellis. Ma magasin, sõin ja käisin rannas. Ma käin seal igal aastal. Mulle väga meeldib seal viibida. Loodus on väga ilus. Päike paistis. Ilm oli palav. Reis läks maksma umbes 1000 eurot inimese kohta.", "Parandati mitmed õigekirja- ja grammatikavead ('kaisin' → 'käisin', 'Kaanari' → 'Kanaari', 'ilm oli palav' → 'Ilm oli palav') ning täpsustati lause struktuur."),
    ("Kevadel käisin ma Kanaari saartel. Lennukiga reisides elasin ma viietärnihotellis. Ma magasin, sõin ja käisin rannas. Käin seal iga aasta, sest mulle meeldib seal viibida. Loodus on väga ilus, päike paistis ja ilm oli palav. Reis maksis umbes 1000 eurot inimese kohta.", "Alternatiivne variant, kus laused on ühendatud sujuvamaks, säilitades samas algse sõnumi ja parandades käänete järjepidevust."),
    ("Kevadel käisin ma Kanaari saartel. Kasutasin lennukit ja elasin viietärnihotellis. Seal magasin, sõin ja käisin rannas, mida külastan igal aastal. Loodus oli väga ilus, päike paistis ning ilm oli palav. Reis hind oli umbes 1000 eurot inimese kohta.", "Parandatud lauseehitus ja sõnavalik, et tagada selgus ning ühtlus kogu tekstis.")]
    
6.  Sisestatud tekst:
    Mina reisin tihti komandeeringus ja puhkas.
    Minu viimasne reis oli Minskis Valgevenes.
    Ma tegelen reklaamiga.
    Minskis mul on palju klientid.
    Veel minu vanemad elavad siis, ma käisin külla nende juurde.
    Mulle meeldib reisida Valgevenes!

    Parandus:
    [("Mina reisin tihti komandeeringutele ja puhkamise ajal. Minu viimane reis oli Minskisse, Valgevenesse. Ma tegelen reklaamiga ning Minskis on mul palju kliente. Kui minu vanemad veel elavad, käisin ma nende juures külas. Mulle meeldib reisida Valgevenesse!", "Parandati õigekirja- ja stiilivead ('komandeeringus' → 'komandeeringutele', 'puhkas' → 'puhkamise ajal', 'klientid' → 'kliente') ning täpsustati asukohanimede kääned."),
    ("Reisin tihti komandeeringutele ja puhkamise ajal. Minu viimane reis viis mind Minskisse, Valgevenesse, kus tegelen reklaamiga. Minskis on mul palju kliente ja kui mu vanemad elavad veel, käisin nende juures külas. Mulle meeldib reisida Valgevenesse!", "Alternatiivne variant, kus lauseehitus on muudetud selgemaks ning sõnavalik parandatud."),
    ("Ma reisin sageli komandeeringutele ja puhkan samal ajal. Minu viimane reis oli Minskisse, Valgevenesse. Tegelen reklaamiga ning Minskis on mul arvukalt kliente. Kui mu vanemad elavad veel, käisin kindlasti nende juures külas. Mulle meeldib reisida Valgevenesse!", "Kohandatud väljendid ja lause struktuur, et parandada teksti voolavust ja grammatilist korrektsust.")]
    
7.  Sisestatud tekst:
    Eelkõige mulle meeldib suvest palju, kuna see on puhkus ja ilm on soe, kus saab puhata pikka aega ja lõõgastuda korralikult.
    Suvi on juba üsna lähedal.
    Soome suvi on täis igasugust mönus nähtavust, tegemist ja kogemist.
    Aga mina kavatsen olla hea meelega seal ajal kodumaal, kus on võimalik meeldivat vähe aega sugulastega.
    Juuni ja koos sellega ka puhkuse ühtlustuvad lausa ähvardav kiirusega, mis on peaaegu kõigile ilouutinen.
    Vietän tund aega koos sõpradega väljas hengaten.
    Käesoleva õpingute lõpus, et ma olen kavatsenud käia välismaal, eriti kodumaal Türgis.
    Vähemalt praegune kava tundub, et minnakse kuhugi.
    Kui seotuna kodumaale saab olema palju ära teha.
    Tegelikult ma tahan ujuda meres, kus saab nautida ainult päikest ja ka sölta.
    Kui ainult jöuaks on hea lahkuda, käiksime.
    Seega söpradega ma tahan olla väljäs kuigi mängivad meeldivat vörkpall.
    Ma tahan käia inimestega juuni messidel.
    St kavatsen teha ekskursioone.
    Sel suvel tutvud ka uute inimestega, kes olid enne teadmata.
    Aga söprade abil kavatseme külastada shoppailemasa väga palju.
    Seal kodumaal meeldiva rannikul tahaksin köndida kogu aeg.
    Lühidalt öeldes ma tahan veeta puhkusepäevade täieliklut.
    Türgis ma ka piip paigutada imetlema vaatamisväärsusi.
    Samalla ajal toimub kindlasti pikini kodanikel.
    Ka traditsioonlised toidud saavad maitseb äärmiselt maitsvaid alt kui kunagi varem.
    Sel suvel olen kavatsenud käia filmis palju, kui ainult önnestub.
    Sisenedes tagasi soome minu on kavatsus valmistada just järgmise l öppeaastal öppida.
    Kui jöuan välismaal puhkuse järel saan minna löpuks tööle.
    
    Parandus:
    [("Eelkõige meeldib mulle suvi, sest see tähendab puhkusperioodi ja soojat ilma, mis võimaldab pikka aega puhata ning korralikult lõõgastuda. Suvi on juba üsna lähedal. Soome suvi on täis erinevaid huvitavaid nähtusi, tegevusi ja kogemusi. Mina kavatsen hea meelega veeta selle aja kodumaal, kus saab meeldivat aega sugulastega. Juuni ja puhkused lähenevad kiiresti, mis tekitab rõõmu paljude seas. Vietan tund aega koos sõpradega väljas. Õpingute lõpus kavatsen külastada välismaad, eriti Türgit. Praeguse kava kohaselt tundub, et minnakse kuhugi, kus on palju teha. Tegelikult tahan ujuda meres, kus saab nautida päikest ja ringi sõita. Kui ainult jõuaks, käiksime koos. Seega tahan sõpradega olla väljas ja isegi võrkpalli mängida. Soovin käia juunis messidel ning teha ekskursioone. Sel suvel tutvun ka uute inimestega, kes olid varem teadmata. Lisaks kavatseme sõpradega külastada palju poode. Kodumaa meeldival rannikul tahaksin kõndida kogu aeg. Lühidalt öeldes tahan veeta ideaalsed puhkusepäevad. Türgis kavatsen imetleda vaatamisväärsusi ning samal ajal toimub kindlasti ka piknik. Traditsioonilised toidud maitsevad sel suvel kindlasti paremini kui kunagi varem. Saabudes tagasi Soome, on mu kavatsus valmistuda järgmise õppeaasta alguseks. Puhkuse järel, kui välismaalt naasen, saan lõpuks tööle minna.", "Parandati laiaulatuslikult grammatilisi, stiili- ja õigekirjavigu; ühtlustati sõnavalik ning parandati lause struktuurid, et tekst oleks loetavam ja sisuliselt sidus."),
    ("Mulle meeldib suvi eelkõige, sest see tähistab puhkusperioodi ja soojemat ilma, mis võimaldab pikemat puhkeaega ja korralikku lõõgastumist. Suvi on juba üsna lähedal ning Soome suvi pakub palju erinevaid kogemusi ja tegevusi. Mina kavatsen veeta selle aja kodumaal, et nautida meeldivat aega sugulastega. Juuni ja puhkused lähenevad kiiresti, mis rõõmustab paljusid. Vietan tund aega koos sõpradega väljas. Õpingute lõpus kavatsen käia välismaal, eriti Türgis. Praeguse kava järgi tundub, et minnakse kuhugi, kus on palju teha. Tegelikult tahan ujuda meres, kus saab päikest nautida ja ümbrust avastada. Kui midagi läheb valesti, käiksime koos. Seega tahan sõpradega olla väljas, mängides ka võrkpalli. Soovin käia juunis messidel ja teha ekskursioone. Sel suvel tutvun ka uute inimestega, kes olid varem teadmata, ning plaanime külastada mitmeid poode. Kodumaa meeldival rannikul tahaksin kõndida kogu aeg. Lühidalt öeldes tahan veeta täiuslikud puhkusepäevad. Türgis kavatsen imetleda vaatamisväärsusi, samal ajal kui toimub kindlasti ka piknik kodanike seas. Traditsioonilised toidud maitsevad kindlasti äärmiselt hästi kui kunagi varem. Saabudes tagasi Soome, on mu kavatsus valmistuda järgmise õppeaasta alguseks. Puhkuse järel, kui naasen välismaalt, olen valmis tööle minema.", "Alternatiivne variant, kus teksti sõnastust on veidi lihtsustatud ning lauseehitus on korrigeeritud, et tagada selgus ja ühtlus."),
    ("Eelkõige meeldib mulle suvi, sest see tähendab puhkusperioodi ja soojemat ilma, mis võimaldab pikemat puhkeaega ning korralikku lõõgastumist. Suvi on juba üsna lähedal ning Soome suvi on täis mitmekesiseid nähtusi, tegevusi ja kogemusi. Mina kavatsen hea meelega veeta selle aja kodumaal, et nautida kvaliteetaega sugulastega. Juuni ja puhkused lähenevad lausa ähvardavalt kiiresti, mis rõõmustab paljusid. Vietan tunni koos sõpradega väljas. Õpingute lõpus olen kavatsenud käia välismaal, eriti Türgis, kus plaanin teha mitmeid ekskursioone. Praeguse kava järgi tundub, et minnakse kuhugi, kus on palju ülesandeid. Tegelikult tahan ujuda meres, kus saab päikest nautida ja ümbrust avastada. Kui ainult jõuaks, käiksime koos. Seega tahan sõpradega olla väljas, mängides isegi võrkpalli. Soovin käia juunis messidel ning tutvuda uute inimestega, kes olid varem teadmata. Samuti kavatseme sõpradega külastada palju poode ja nautida meeldivat kõndimist kodumaa rannikul. Lühidalt öeldes tahan veeta ideaalsed puhkusepäevad. Türgis kavatsen imetleda vaatamisväärsusi ning samal ajal toimub kindlasti ka piknik. Traditsioonilised toidud maitsevad sel suvel äärmiselt hästi kui kunagi varem. Saabudes tagasi Soome, valmistun järgmise õppeaasta alguseks ning puhkusjärgse tööle asumisega.", "Variant, kus on säilitatud algse teksti mõte, parandatud grammatika, sõnavalik ja lauseehitus, et tekst oleks selge ja ühtlane.") ]


Sisestatud tekst: {text}
Parandus:"""


class GrammarErrorCorrectionAggregationPrompt(BasePrompt):
    template: str = """Koondage väljapakutud grammatilised parandused lõplikuks, grammatiliselt korrektseks tekstiks.
Ühendage algtekstist ja {num_corrections} parandusvariantide nimekirjast kõik nende versioonide kasulikud muudatused, et luua üks lõplik, süntaktiliselt korrektne tekst.
Kõrvaldage kõik õigekirja-, kirjavahemärgistamis-, stiili-, grammatilised, leksikaalsed ja süntaktilised vead.
Lisage selgitused agregeeritud paranduste ja üldiste grammatiliste paranduste kohta.
Keskenduge ainult soovitatud parandustele ja ärge püüdke iseseisvalt muuta algset teksti.
Kui vigu ei ole, tagastage originaaltekst.
Eraldage oma vastuses kõik topeltlause- ja muud erimärgid kahe kaldkriipsu abil.
Näiteks kasutage \\n uue joone jaoks ja \\“ topeltlause jaoks.
Palun ärge eemaldage tehnilisi sümboleid, nagu internetilingid, sildid jms teistest keeltest (peamiselt inglise keelest).


Kavandatud paranduste vorming:
[{{
    "correction": „parandatud tekst",
    "explanation": „selgitus paranduse kohta"
}},...]

[Väljund ainult JSON]
Vastuse vorming JSONis:
{{
    "correction": "corrected text",
    "explanation": "selgitus paranduse kohta"
}}

Originaaltekst: {text}
Parandusettepanekud: {possible_corrections}
Parandatud tekst:"""
    input_variables: list[str] = ["text", "possible_corrections", "num_corrections"]
