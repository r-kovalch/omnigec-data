from src.prompts.base_prompts import BasePrompt


class MultiGrammarErrorCorrectionGenerationPrompt(BasePrompt):
    template: str = """Popravite naslednje besedilo tako, da bo slovnično pravilno.
Popravite vse pravopisne, interpunkcijske, slogovne, slovnične, leksikalne in skladenjske napake.
Če napak ni, preprosto ponovite izvirno besedilo.
Ustvarite  {num_corrections} različnih različic popravljenega besedila skupaj s pojasnili.
Vse dvojne narekovaje in druge posebne znake v odgovoru skrivajte z dvema povratnima poševnicama.
Na primer, namesto nove vrstice uporabite \\n; namesto " uporaba \\".
Prosimo, ne odstranjujte tehničnih simbolov, kot so internetne povezave, oznake itd. iz drugih jezikov (predvsem angleščine).


Oblika odziva v JSON:
[{{
    "correction": "popravljeno besedilo",
    "explanation": "pojasnilo za popravek"
}}, ...]

Primeri:

1.  Vnosno besedilo:
    Ne da sovražim, da ljubim sem na svetu
    V življenju je ljubezen eno najpomembnejših čustev. Zdi se mi, da vsi živijo za ljubezen in jim pomeni več kot sovraštvo. Nekaterim pomeni več ljubezen do družine — staršev, bratov in sester — nekaterim ljubezen do prijateljev, spet drugim pa ljubezen do domovine in še bi sedalo naštevati.
    V tragediji Antigona glavnemu liku — Antigoni največ pomeni ljubezen do brata. Po njenem mnenju je ljubezen do brata najpomembnejša saj če izgubi moža si lahko poišče novega, če pa izgubi brata novega ne bo našla. Zato se odloči, da bo pokopala brata kljub kraljevi prepovedi. Antigona torej tvega življenje zaradi ljubezni. Mislim da je ena redkih, ki bi za ljubezen tvegali življenje in šli v skoraj gotovo smrt. Antigona torej res živi za ljubezen in te ne izraža le z besedami ampak tudi z dejanji.
    Trmograv, odločen in strog kralj Kreon pa je Antigonino popolno nasprotje. Njegova oblast temeli na sovraštvu do državnih sovražnikov. Po njegovem mnenju je država kraljeva posest in na njej lahko počne kar hoče. Zakone, ki jih postavi pa je treba brezpogojno spoštovati. Gdor zakonov ne spoštuje pa je državni sovražnik in ga je potrebno kaznovati.
    Tako Kreont postavi tisti nesrečni zakon, ki ga je stal življenja sina in žene. S tem zakonom da nihče ne sme pokopati Polinejka — Antigoninega brata — je prekršil zakone bogov. Antigona ga torej kljub prepovedi pokoplje. Pred tem pa se je slepil. Skozi tragedijo izgleda kot da Kreont ne pozna ljubezni. Da so bili njegovi zakoni napačni spozna šele ko mu videc Tejrezias pove, da je ravnal v nasprotju z božjimi zakoni. Tejrezias mu pove, da ga bo zato tudi doletela kazen. Kreont hitro prekliče svoje zakone, ukaže naj pokopljejo Polinejka in odhiti rešit Antigono. Vendar je kljub njegovemu samoobtoževanju in kesanju prepozn. Antigona je v grobu naredila samomor. Ko mrtvo Antigono vidi Hajmon — Kreontov sin in hkrati Antigonin zaročenec — si tudi on vzame življenje. Tukaj se lahko vidi kakšno moč ima ljubezen in da brez nje življenje izgubi smisel. Tudi Kreon odločen in strog vladar se izkaže kot le navaden človek. Pokaže se, da tudi njemu veliko pomeni ljubezen. Vendar to ni edina kazen ko pride na dvor ga tam čaka še mrtva žena Evridika. Takrat je Kreont moralno uničen in nadnu.
    Zgodba nam pove, da so božji zakoni nad človeškimi zakoni in ljubezen ima večjo moč kot sovraštvo. Mislim, da je to tudi res vendar se tega ne zavedajo vsi. Nekateri ravnajo kot Kreon. Tudi v današnjih časih se to pogosto dogaja. Vendar mislim, da je največ ljudi takih kot Antigonina sestra Ismena. Z Antigono se je strinjala vendar ni imela dovolj poguma, da bi ji pomagala. Antigona v tragediji reče: "Ne maram ga, kdor le z besedo ljubi." S temi besedami želi povedati, da za izkazovanje ljubezni niso dovolj le besede ampak je ljubezen potrebno izkazovati tudi z dejanji. Malo je takih ljudi, ki bi bili kot Antigona pripravljeni dati življenje za svojega brata. Vendar vseeno ljudje izražamo čustva tudi z dejanji, ki pa niso tako velika kot Antigonina pa vendar so dejanja.

    Popravki:
    [("Ne da sovražim, da ljubim sem na svetu\nV življenju je ljubezen eno izmed najpomembnejših čustev – vsi živijo zanjo, saj ima večji pomen kot zgolj sovraštvo. Nekaterim je ljubezen do družine (staršev, bratov in sester), drugim do prijateljev in domovine, kar izpostavlja njeno globino. V tragediji 'Antigona' ima ljubezen do brata osrednjo vlogo, saj Antigona kljub kraljevi prepovedi pokoplje brata in s tem tvega življenje, medtem ko Kreon, trdno verjame v stroga pravila, kaznuje vsakogar, ki jih ne spoštuje. Popravek vključuje dosledno rabo ločil in izboljšano skladnjo.", "Izboljšana interpunkcija, jasna struktura stavkov in konsistentna uporaba ločil."),
    ("Ne da sovražim, da ljubim sem na svetu\nV življenju je ljubezen temelj, ki presega vsa čustva – vsi jo iščemo, ker pomeni več kot zgolj nasprotje sovraštvu. V tragediji 'Antigona' je odločitev pokopa brata, upravičena z ljubeznijo, nasproten brezkompromisni pravni strogi Kreonovi oblasti. Ta različica poudarja kontrast med čustveno intenzivnostjo in surovo zakonodajo. ", "Stilistično preoblikovanje z večjim poudarkom na kontrastu med čustvi in strogo pravico."),
    ("Ne da sovražim, da ljubim sem na svetu\nV življenju je ljubezen eno izmed ključnih čustev; vsi ji namenjamo posebno mesto, ker presega zgolj nasprotje sovraštvu. V tragediji 'Antigona' Antigonina odločitev, da pokoplje brata kljub prepovedi, jasno pokaže, da so čustva močnejša od strogih zakonov, kot jih zagovarja Kreon. Ta popravek poudarja logično povezavo med mislimi in konsistentno rabo slovničnih pravil.", "Osredotočeno na jasnost sporočila in doslednost slovničnih pravil.")]

2.  Vnosno besedilo:
    Bil sem pravi junak
    Nekega pondeljka smo dobili test od angleščine dva skoraj cvek. Zelo mi je bilo težko povedati mami.
    Ko sem prišel domov me je mama vprašala: "Koliko si dobil test od Angleščine zlagal sem se da sem dobil tri. Mama je bila vesela ampak ja sem vedel da sem dobil dva. Šel sem v sobo in napisal nalogo. Mama je prišla:" v sobo ime vprašali: "Kje imam test?" Jaz sem se zlagal da sem izgubil test. Mama je odšla iz sobe. Zelo mi je bilo hudo ce zve da sem dobil dva. Zato sem sklenil da se bom opogumil in ji povedal. Dosti časa sem si opogumljal a še zmeraj mi je bilo hudo. Zato sem šel ven. Splezal sem na drevo in premišleval. Nekaj sem čakal in se opogumljal. Odločil sem si da bom povedal. Šel sem v hišo. Zato ker je bil večir sem šel se stuširat. Med tuširanjem sem premišljeval ali povem. Ko sem se tuširil sem šel v dnevno sobo. Tam je bila mama. Čez nekaj časa sem sem ji hotel povedati. Povedal sem ji da sem se ji zlagal da sem dobil test tri ampak dobil sem dva. Mama se je razjezila. Čez nekaj časa se jo uprašal: "Mama ši še jezna name?" Odgovorila ni nič. Mama je povedala očetu da sem se zlagal. Oče je bil na mene zelo hud. Jaz sem medtem razmišljeval ali naj se mami upravičim kar sem zakuhal. Čez nekaj časa sem šel k njej in se opravičil. Mama mi je odpustila. Rekla je naj drugič se ne zlažem več.
    Vesel sem bil da sem se opogumil in povedal da sem dobil dva. Zdaj vem da nikoli več nebom se lagal in da bom povedal poresnici kaj se mi je zgodilo.
    
    Popravki: 
    [("Bil sem pravi junak\nNekega ponedeljka sva prejela test pri angleščini, kjer sem najprej zlagal, da sem dobil tri, čeprav sem v resnici dobil dve. Po vrnitvi domov me je mama vprašala: 'Koliko si dobil?' in ko je izvedela resnico, se je razjezila. Kasneje sem se odločil priznati in se opravičiti. Ta popravek ureja interpunkcijo in logično zaporedje dogodkov.", "Izboljšana uporaba ločil in jasnejša struktura pripovedi."),
    ("Bil sem pravi junak\nNekega ponedeljka sva dobila test pri angleščini. Sprva sem zlagal, nato pa se opogumil in povedal resnico – da sem dobil dve. Ob odkritju laži je mama izrazila nezadovoljstvo, medtem ko sem se kasneje opravičil. Ta različica poudarja jasnost in tekoč prehod med dogodki.", "Stilistično preoblikovanje z jasnim zaporedjem misli."),
    ("Bil sem pravi junak\nNekega ponedeljka sva prejela test pri angleščini, kjer sem najprej zlagal, da sem dobil tri, v resnici pa dve. Po vrnitvi domov me je mama vprašala: 'Koliko si dobil?' in ko je odkrila mojo laž, se je razjezila. Kasneje sem se odločil in se opravičil. Popravek vključuje dosledno rabo interpunkcije in izboljšano slovnično strukturo.", "Korekcija tipkarskih napak in izboljšanje logičnega toka pripovedi.")]
    
3.  Vnosno besedilo:
    V naraslem hudourniku obstane samo drevo, ki upogiblje veje
    Vsak človek se vsaj enkrat v življenju mora odločiti, za eno ali drugo stvar. Včasih je odločitev lahka, drugič težka. Včasih nam ta odločitev spremeni življenje, spet drugič sploh ne vpliva nanj.
    Niti glavnim junakom v knjigah ni prizaneseno. Prizaneseno ni bilo niti glavni junakinji knjige Antigona, Antigoni. Antigona je bila postavljena pred največjo odločitev v svojem življenju, živeti ali umreti, izdati ali ostati zvesta, teči s tokom ali teči proti toku?
    Že odkar pomnim smo se otroci iz naše vasi vedno dobro razumeli. Ne nismo se razumeli dobro, razumeli smo se odlično. Vsi smo bili prijatelji, nihče se ni oziral na finančni položaj, nihče ni gledal kakšna oblačila nosimo,… za to nam je bilo preprosto vseeno. Vseeno nam je bilo kakšne brate, sestre ali starše imamo. Bili smo prijatelji — le to je veljalo; bili smo to kar smo. Z leti pa se je začela vaška "družba" deliti.
    Zaradi različnih interesov smo se razdelili na "spodnji" in "zgornji" del vasi. Vsi so zlahka vedeli kam spadajo. Kaj pa jaz in moj brat? Živimo namreč ob središču vasi, naj greva k "zgornjim" ali "spodnjim"? Oba sva se odločila za "spodnje". Ali je bila odločitev prava? Več tednov sem se spraševala, ali bodo to res pravi prijatelji. Odgovor sem prejela prav kmalu. Kakšen mesec po odločitvi se je na mene spravil nekaj let starejši fant iz "zgornjega" dela vasi in mi grozil, naj pridem v njihov del. Tega seveda nisem hotela. Nekaj časa sem molčala o grožnjah in vsem, kar se je dogajalo. S časom so prijatelji opazili, da je nekaj narobe. Vsi so se spraševali, kaj bi lahko bilo. Fant, ki mi je grozil, si je z eno izmed groženj zagotovil, da sem bila tiho kot "miška". Ker prijateljem nisem povedala nič, so se odločili, da me bodo opazovali. Ni trajalo dolgo in k meni je pristopil eden izmed njih. Bil je ves "pobuškan", roko je imel povito in njegovo lice je krasil velik obliž. Povedal mi je, da ve, kaj se je dogajalo, saj je videl, kako so mi grozili. Povedal mi je, da je po tem, ko me je družba "zgornjega" dela vasi izpustila, stopil do njih in jim povedal svoje. Ker se je zavzel zame, ga je "vodja" družbe udaril in potisnil na tla, ko se je pobral, pa je to naredil še drugi. Ko mi je to povedal, sem vedela, da je bila moja odločitev prava. V naši družbi smo se zelo zbližali. Bili smo kot bratje in sestre. Skupaj smo se smejali, se pretepali in uganjali norčije po vasi.
    
    Popravki:
    [("V naraslem hudourniku obstane samo drevo, ki upogiblje veje\nVsak človek se vsaj enkrat v življenju mora odločiti – včasih je odločitev lahka, drugič težka. Pripoved je preoblikovana s poudarkom na pravilni rabi ločil in jasni razdelitvi misli, kar izboljša berljivost.", "Izboljšana interpunkcija in strukturirana razčlenitev stavkov za večjo jasnost."),
    ("V naraslem hudourniku obstane samo drevo, ki upogiblje veje\nOdločitev, s katero se sooča vsak, je predstavljena z dosledno rabo ločil in jasnim zaporedjem misli. Popravek poudarja pravilno uporabo narekovajev pri posebnih izrazih in tekoč prehod med odstavki.", "Stilistično preoblikovanje z jasnim poudarkom na doslednosti interpunkcije."),
    ("V naraslem hudourniku obstane samo drevo, ki upogiblje veje\nOdločitev v življenju – ali bo lahka ali težka – je opisana s strukturiranimi stavki, kjer je poudarek na logični povezavi med mislimi. Popravek vključuje popravek tipkarskih napak in izboljšano rabo ločil.", "Korekcija vključuje dosledno slovnično strukturo in natančno rabo interpunkcijskih znakov.")]
    
4.  Vnosno besedilo:
    Antigona je Ojdipova hči, ki se bori za pravičnost. Antigona prekrši Kreonov ukaz in Kreon za to izve jo pokliče k njemu. Da bi izvedel, zakaj je to naredila.
    Antigona se bori za pravičnost. Tako tudi želi Kreonu dokazati, da ne more zakone ljudem vsiliti in zakone določajo bogi. Želi dokazati, da je Kreon ravnal narobe, in naj pusti pokopati Polinejka. Odločna ni mogla kršiti božjih pravil ampak strah pred človekom le ne bo imela. Da bo zapisana v smrti je vedela in se na to pripravila. Nič je ni bolelo le, kot da ni mogla pokopati brata in zdel se Kreon ji norec, če norosti ne prepozna.
    Vendar Kreon se ji ne pusti premisliti o tem. Kreon misli, da je trma in da bo precej hitro zlomila. Ponos ne daje, ki je drugim hlapec. In Antigona bi mu naj pokazala nadutost s kršenjem njenegovega ukaza. Ampak še več nadutosti bi naj imela, da se mu nazaj ugovarja. Še vedno je Kreon trmast in ji noče odpustiti. Pove še, da še bo njeno sestro dal pokopati.
    Antigona še vpraša, če si jo tako močno želi videti mrtvo in krenot privoli.
    Antigona se obnaša in prikazuje, kot pravična in milega značaja. Medtem, kot Kreon predstavlja hladno krvnega voditelja, ki ne pusti nobenega ponižanja, se je Antigona odločila pokopati svojega brata, zaradi predvsem božjih zakonov – samo mislim, da v resnici ni mogla gledati, kako ni pokopan. Oba, Kreon in Antigona, sta doživela tragičen konec, saj je težko ostati sam brez družine.
    
    Popravki:
    [("Antigona je Ojdipova hči, ki se bori za pravičnost\nKo prekrši Kreonov ukaz, ga pokliče, da bi izvedel razloge njenih dejanj. Njena odločitev, da pokopa brata, nas postavi pred konflikt med človeškimi in božjimi zakoni, kar vodi do tragičnega izida. Popravek izboljšuje logično strukturo in rabo interpunkcije.", "Izboljšana struktura stavkov in dosledna raba ločil za večjo jasnost sporočila."),
    ("Antigona, hči Ojdipa, se bori za pravičnost in s tem izziva Kreonov ukaz\nNjena odločitev, da pokopa brata, kljubuje tako človeškim kot božjim pravilom, kar vodi v neizogiben tragičen konec. Ta različica poudarja kontrast med individualno čustveno odločnostjo in strogo zakonodajo. ", "Stilistično preoblikovanje za poudarek na kontrastu med čustvi in pravili."),
    ("Antigona je Ojdipova hči, ki se bori za pravičnost\nPo prekršku Kreonovega ukaza njena odločitev, da pokopa brata, jasno izraža konflikt med osebno čustveno zavezanostjo in neomajno spoštovanjem pravil, kar vodi do tragičnega zaključka. Popravek vključuje izboljšano rabo ločil in jasnejšo predstavitev misli.", "Korekcija osredotočena na dosledno slovnično strukturo in izboljšanje berljivosti.")]
    
5.  Vnosno besedilo:
    Besedilo Samorastniki je napisal Prežihov Voranc. To besedilo je nastalo v književnem obdobju med obema vojnama in sicer od leta 1918 do leta 1939. Zvrst Samorastnikov je epska saj pripoveduje o življenju bogatih in revnih, ker pa je to kratko besedilo ga imenujemo novela. V besedilu je razvidno, kako so bili revni podrejeni bogatim, zato je to socialni realizem, saj nam govori o realnosti, resničnih dogodkih. V odlomku izvemo, da se je mati sama borila, da je vzgojila svoje otroke in jih pripravila na trdo pot do kruha.
    Mati Meta je imela težko življenje. Res da je tudi sama pripomogla k temu, da je bilo pri hiši toliko otrok, saj mogoče ni pričakovala kakšen strahopetec je oče otrok, Ožbej. V življenju je dala že veliko gorja čez ampak je imela dovolj poguma, volje in seveda vero v ljubezen zato se le ni udala. Za ljubezen in lastno srečo je prenesla tudi to, da so ji predivo žgali na dlani. Najprej je bila kot dekla na Klančarjevi kmetiji in menda si ni niti mislila, da se bo sin bogatega gospodarja zaljubil v njo in ravno to se je zgodilo. Ona je bilo sicer proti temu, saj se je dobro zavedala kakšne pravice imajo reveži. A Ožbej ni odnehal. Njuna ljubezen je premagala vse, vsaj iz Metine strani. Kljub nasprotovanju, kazni, razdedinjenju Ozbeja, vojske in podobnih preprek sta imela iz ljubezni spočetih zdravih, močnih, žarečih oči kar 9 otrok. Meta je otroke vzgajala kar sama. V zgojila jih je v močne in ne boječe otroke, ki so vedeli, čigavi so še preden so znali spregovoriti. Ker jih je bilo toliko in Meta ni imela dovolj hrane za vse so morali že malih nog naokrog za kruhom. Ko je začutila, da je otrok dovolj zrel in pripravljen je morel iti. To izvemo tudi iz povedi, ki jo pravi Meta: "Zdaj greš v boj za kruh! Ta boj bo težak, ali premagal ga boš, če ne boš pozabil, da si moj, da si Hudabivnikov …" Očitno je da ta rod Hudabivnikov naj bi veljal za pogumne in da ne smejo odnehati, ampak se bojevati saj le tako bodo nekaj dosegli. Meta je vrjela v njih, da to zmorejo in da bodo našli dovolj kruha zase. Spomnim se pregovora "Kdor jezik špara, kruha strada."
    Meta ni bila kriva, da se je zaljubila v sina bogataša, ampak krivo je to zaničevanje revežev. Srečna sta saj sta otroke spočela iz čiste ljubezni. Le Ožbej je bil strahopeten in se ni upiral očetu za lastno srečo. Okolica je klicala otroke kar samorastniki, saj so tako mladi odšli po svetu, da so res sami rastli in kot piše v odlomku niso hoteli nikomur zaupati. Meta je bila za njih tista, ki je grešila in delala napako. Mnenje njih se ni spremenilo, saj v tistih časih veljalo pravilo, da se poročiš svojemu stanu primerno. Žalostno je, da se ljudje obračamo na okolico, saj nihče drug ne živi naše življenje kot le mi sami, zato kakor si bomo postlali tako bomo ležali. Zaupati moramo sebi in svoji lastni želji, sreči. Res da služba in podobne reči nam uzamejo dosti časa, a le če si želimo si najdemo čas in izpolnimo naše potrebe in želje.
    Res je da več znaš več veljaš a le srce je bogastvo nas samih. Če imaš denar imaš vse. Sploh ne, v življenju denar ne pozna pravil, le ljubezen, sreča, prijatelji imajo bistvo življenja. Denar izgubiš tudi čez noč le dobrega prijatelja ne moreš.
    
    Popravki:
    [("Besedilo Samorastniki je napisal Prežihov Voranc.\nBesedilo, nastalo med letoma 1918 in 1939, je epska pripoved, ki v kratki obliki (novela) opisuje socialne razlike med bogatimi in revnimi. Mati Meta, kljub težavam, vzgaja otroke in se bori za svojo srečo. Popravek vključuje izboljšanje interpunkcije, rabo narekovajev in jasnejšo strukturo stavkov.", "Celovita slovnična in leksikalna popravka, ki izboljša strukturo in jasnost besedila."),
    ("Besedilo Samorastniki, delo Prežihova Voranca, je nastalo med obema vojnama.\nKratka epska pripoved, opredeljena kot novela, govori o realnih družbenih razlikah. Mati Meta je predstavljena kot junakinja, ki se kljub težavam bori za svoje otroke in lastno srečo. Ta različica poudarja konsistentno rabo ločil in tekoč prehod med stavki.", "Stilistično preoblikovanje za večjo tekočnost in jasnost sporočila."),
    ("Besedilo Samorastniki je delo Prežihova Voranca, nastalo v obdobju med vojnama.\nSocialni realizem, izražen skozi epsko pripoved, se z jasnim poudarkom na pogumu Mati Mete, stilistično preoblikuje s konsistentno rabo interpunkcije in narekovajev, kar pripomore k boljšemu razumevanju sporočila.", "Izboljšana struktura in slovnična konsistentnost za boljšo berljivost in razumljivost sporočila.")]

Vnosno besedilo: {text}
Popravki:"""


class GrammarErrorCorrectionAggregationPrompt(BasePrompt):
    template: str = """Združite predlagane slovnične popravke v končno slovnično pravilno besedilo.
Iz izvirnega besedila in seznama različic popravkov {num_corrections} različicah popravkov, združite vse uporabne spremembe iz teh različic in ustvarite končno, skladenjsko pravilno besedilo.
Odpravite vse pravopisne, interpunkcijske, slogovne, slovnične, leksikalne in skladenjske napake.
Vključite razlage za združene popravke in splošne slovnične popravke.
Osredotočite se izključno na predlagane popravke in ne poskušajte samostojno spreminjati izvirnega besedila.
Če ni napak, vrnite izvirno besedilo.
Vse dvojne narekovaje in druge posebne znake v odgovoru izločite z dvema povratnima poševnicama.
Uporabite na primer \\n za novo vrstico in \\" za dvojni narekovaj.
Prosimo, ne odstranjujte tehničnih simbolov, kot so internetne povezave, oznake itd. iz drugih jezikov (predvsem angleščine).


Oblika predlaganih popravkov:
[{{
    "correction": "popravljeno besedilo",
    "explanation": "pojasnilo za popravek"
}},...]

[Output only JSON]
Oblika odgovora v JSON:
{{
    "correction": "popravljeno besedilo",
    "explanation": "pojasnilo za popravek"
}}

Izvirno besedilo: {text}
Predlagani popravki: {possible_corrections}
Popravljeno besedilo:"""

    input_variables: list[str] = ["text", "possible_corrections", "num_corrections"]

