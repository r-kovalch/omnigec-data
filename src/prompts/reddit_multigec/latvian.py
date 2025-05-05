from src.prompts.base_prompts import BasePrompt


class MultiGrammarErrorCorrectionGenerationPrompt(BasePrompt):
    template: str = """Izlabojiet šādu tekstu, padarot to gramatiski pareizu.
Labojiet visas pareizrakstības, interpunkcijas, stilistikas, gramatikas, leksikas un sintakses kļūdas.
Ja kļūdu nav, vienkārši atkārtojiet sākotnējo tekstu.
Izveidojiet {num_corrections} atšķirīgas labotā teksta versijas kopā ar paskaidrojumiem.
Izvairieties no visām dubultajām pēdiņām un citām speciālajām rakstzīmēm atbildē, izmantojot divas atpakaļsvītras.
Piemēram, jaunās rindkopas vietā lietojiet \\n; vietā lietojiet " izmantot \\".
Lūdzu, neizņemiet tehniskos simbolus, piemēram, interneta saites, tagus utt. no citām valodām (galvenokārt no angļu valodas).


Atbildes formāts JSON:
[{{
    "correction": "labotais teksts",
    "explanation": "labojuma skaidrojums"
}}, ...]

Piemēri:

1. Ievadteksts:  
Mani sauc Rumi, es esmu no Vācija. Es esmu medicīnas studente Rigas Stradiņa universitate, tapēc man nav daudz valaspriekas. Parasti es ceļo pulksten 8.30 un pec desmitām minūtem eju duša, tīr mans zobs un edu brokastis. Brokastīs es  
Pirmdīenā man ir latviešu valoda pulksten 1,:15. un fizika 3:30 pēcpusdiena.  
Otrdien man ir Histologia un Philosophia. Uz anatomikumu es braucu ar trolejbusu vai tramvaju. Tramvaja pietura ir netālu no mana mājas. Histologia ir 3:30 un beidz 5:45 vakarā. Tad es braucu uz Mcdonaldu. Trešdien man ir tikai latviešu valoda un parasti studeju Biokimiju.  
Ceturtdien pulksten 8:00 no rīta man ir biokimija, ceturtdien es celo 7:00 no rīta, pec biokimija nodarbiba man ir latviešu valoda nodarbiba kas beidz 2:45. Vakarā es studeju anatomiju, histologiju vai biokimiju. Man loti nepatik biokimija. Piektdien pēcpusdiena man ir anatomia, pec anatomiu es apciemoju mani draugi no gruzija un Uzbekistāna, mes vakarinojum un pec ejam vecā Rigā. Mes ballīte. Nedēlas nogalē es studeju. Agrak universitate man hobby bija slēpot, zīmēt, peldēt shopping bet tagad es nevaru.  
Vasarā es lidoju atpakal uz mājām, Es gulēšu tik daudz pēc iespējas. Es apciemošu man draugi, lasīšu gramatu un peldēšu.

   Labojumi:  
   [  
     ("Mani sauc Rumija, es esmu no Vācijas. Es esmu medicīnas studente Rīgas Stradiņa universitātē, tāpēc man nav daudz vaļasprieku. Parasti es ceļos pulksten 8.30 un pēc desmit minūtēm eju dušā, tīru manus zobus un ēdu brokastis. Pirmdienās man ir latviešu valoda pulksten 1:15 un fizika 3:30 pēcpusdienā. Otrdienās man ir histoloģija un filozofija. Uz anatomikumu es braucu ar trolejbusu vai tramvaju; tramvaja pietura atrodas netālu no manas mājas. Histoloģija sākas 3:30 un beidzas 5:45 vakarā, pēc ko es braucu uz McDonald's. Trešdienās ir tikai latviešu valoda, un es parasti studēju bioķīmiju. Ceturtdienās pulksten 8:00 no rīta ir bioķīmijas nodarbība, pēc kuras seko latviešu valodas kursi, kas beidzas 2:45. Vakarā es studēju anatomiju, histoloģiju vai bioķīmiju, un man ļoti nepatīk bioķīmija. Piektdienu pēcpusdienās pēc anatomijas es apciemoju manus draugus no Gruzijas un Uzbekistānas, pēc tam vakariņojam un ejam uz Vecrīgu, kur mēs ballējamies. Nedēļas nogalēs es studēju. Pirms universitātes mani hobiji bija slēpot, zīmēt, peldēt un iepirkties, bet tagad tas nav iespējams. Vasarā es lidošu atpakaļ uz mājām, gulēšu tik daudz, cik varēšu, un apciemošu manus draugus, lasīšu grāmatu un peldēšu.",  
      "Korekcijā tika labotas gramatikas, pareizrakstības un interpunkcijas kļūdas – piemēram, 'Rumi' tika aizvietots ar 'Rumija', 'Vācija' ar 'Vācijas', un arī nodrošināta konsekventa vārdu locījuma un laika izteiksmes lietošana.") ,  

     ("Mani sauc Rumija, es esmu no Vācijas. Medicīnas studente Rīgas Stradiņa universitātē, tāpēc man nav daudz vaļasprieku. Parasti es ceļos pulksten 8.30 un pēc desmit minūtēm dodos dušā, kur tīri manus zobus un ēdu brokastis. Pirmdienās man ir nodarbības – latviešu valoda pulksten 1:15 un fizika 3:30 pēcpusdienā. Otrdienās studēju histoloģiju un filozofiju; uz anatomijas nodarbībām braucu ar trolejbusu vai tramvaju, kura pietura atrodas netālu no manas mājas. Pēc 3:30 vakara nodarbībām es dodos uz McDonald's. Trešdienās ir tikai latviešu valoda, un bioķīmija ir mana galvenā mācību priekšmets. Ceturtdienās sākas bioķīmijas nodarbība pulksten 8:00 no rīta, kam seko latviešu valodas kurss, kas beidzas 2:45. Vakarā studēju anatomiju, histoloģiju vai bioķīmiju, un bioķīmija man ļoti nepatīk. Piektdienās pēc anatomijas es apciemoju draugus no Gruzijas un Uzbekistānas, pēc tam vakariņojam un ejam uz Vecrīgu ballītēm. Nedēļas nogalēs es studēju, kā arī atceros savus hobijus – slēpošanu, zīmēšanu, peldēšanu un iepirkšanos, kas tagad nav iespējams.",  
      "Alternatīvajā versijā tika papildināta daļa par nodarbību struktūru un aktivitātēm, kā arī precizēti laiki un vietas, saglabājot sākotnējo domu.") ,  

     ("Mani sauc Rumija, es esmu no Vācijas un medicīnas studente Rīgas Stradiņa universitātē, tāpēc man nav daudz vaļasprieku. Parasti es ceļos pulksten 8.30, un pēc desmit minūtēm, dodoties dušā, tīru manus zobus un ēdu brokastis. Pirmdienās man ir latviešu valodas un fizikas nodarbības – pulksten 1:15 un 3:30 pēcpusdienā. Otrdienās studēju histoloģiju un filozofiju, braucot uz anatomikas nodarbībām ar trolejbusu vai tramvaju, kura pietura ir netālu no manas mājas. Histoloģijas klase sākas 3:30 un beidzas 5:45, pēc kuras dodos uz McDonald's. Trešdienās ir tikai latviešu valoda, un bioķīmija ir mans galvenais priekšmets. Ceturtdienās sākas bioķīmijas nodarbība pulksten 8:00, kam seko latviešu valodas kurss, kas noslēdzas 2:45. Vakarā studēju anatomiju, histoloģiju vai bioķīmiju, taču bioķīmija man ļoti nepatīk. Piektdienās pēc anatomijas nodarbībām es apciemoju manus draugus no Gruzijas un Uzbekistānas, pēc tam vakariņojam un dodamies uz Vecrīgu ballītēm. Nedēļas nogalēs turpinu studijas, atceroties savus agrākos hobijus – slēpošanu, zīmēšanu, peldēšanu un iepirkšanos, kas tagad nav iespējami.",  
      "Šajā versijā tika veiktas precīzas korekcijas visos gramatikas, interpunkcijas un stilistikas aspektos, lai teksts izklausītos skaidrāks un plūstošāks.")
   ]

2. Ievadteksts:  
Mani sauc Kalles Caviar, man ir četrdesmit tris gadi. Es esmu professoras.  
Man loti patīk mans darbs.  
Man ir no Francijas, es esmu francūzis.  
Es runāju franciski, angliski, latviski, vāciski un spāniski.  
Man patīk peldēt, skatīties seriālus, sporto un fotografēt. Man nepatīk lasīt.  
Man garšo ali, man negaršo coca cola.  
Es dzīvoja Rigā, Mana adrese ir stabu iela septiņdesmit pieci, dzīvoklis divipadsmit.  
Mana ir sieva Maria.  
Mums ir četri bērni. Viņus sauc Sava, Calles, Cathi un Zara. Viņiem patīk spēlēt spēles, lasīt, sportot, skatīties seriālus  un fotografāt. viņiem garšo šokolāde, augļi un saldējums, bet un garšo kafija.  
Mana māte vārds ir Sofia. Viņa ir astondesmit četras. Viņa ir mājsaimniece. Mana tēva vārds ir Pogbas, viņš ir astoņdesmit astoni. Pogbas ir skolotājs.  
Man ir sešas māsas, viņas sauc ir Nilla, Sara, Dana, Sofia, Cathi un Svea. Nilla ir mājsaimniece, Sara ir medicina studente, Dana ir ari mājsaimniece. Sofia, Cathi un Svea ir studentes.  
viņas patīk skatīties seriālus un fotografēt. Viņas un patīk latīs.

   Labojumi:  
   [  
     ("Mani sauc Kalless Kaviārs, man ir četrdesmit trīs gadi. Es esmu profesors. Man ļoti patīk mans darbs. Es esmu no Francijas un esmu francūzis. Es runāju franciski, angliski, latviski, vāciski un spāniski. Man patīk peldēt, skatīties seriālus, sportot un fotografēt, bet lasīt nepatīk. Man garšo alus, man negaršo kokakola. Es dzīvoju Rīgā, mana adrese ir Stabu iela septiņdesmit pieci, dzīvoklis divpadsmit. Man ir sieva Marija. Mums ir četri bērni – Sava, Kalless, Katija un Zara, kuriem patīk spēlēt spēles, lasīt, sportot, skatīties seriālus un fotografēt; viņiem garšo šokolāde, augļi un saldējums, bet negaršo kafija. Manas mātes vārds ir Sofija, un viņai ir astoņdesmit četri gadi; viņa ir mājsaimniece. Mana tēva vārds ir Pogbass, kuram ir astoņdesmit astoņi gadi, un viņš ir skolotājs. Man ir sešas māsas – Nilla, Sāra, Dana, Sofija, Katija un Svea; no tām Nilla ir mājsaimniece, Sāra medicīnas studente, un Dana ir arī mājsaimniece, kamēr pārējās studē. Viņām patīk skatīties seriālus un fotografēt, bet lasīt nepatīk.",  
      "Pamata korekcijās izlabotas gramatikas, pareizrakstības un interpunkcijas kļūdas, kā arī precizēti vārdu locījumi un skaitļu formāti.") ,  

     ("Mani sauc Kalless Kaviārs, man ir 43 gadi un esmu profesors, kurš ļoti mīl savu darbu. Es esmu no Francijas un, kā francūzis, runāju franciski, angliski, latviski, vāciski un spāniski. Man patīk peldēt, skatīties seriālus, sportot un fotografēt, bet lasīšana man nav tuvumā. Man garšo alus, bet es negaršo kokakolu. Es dzīvoju Rīgā – mana adrese ir Stabu iela 75, dzīvoklis 12. Esmu precējies ar Mariju, un mums ir četri bērni: Sava, Kalless, Katija un Zara, kuriem patīk spēlēt spēles, lasīt, sportot un fotografēt, kā arī baudīt šokolādi, augļus un saldējumu, bet negaršo kafiju. Mana māte Sofija ir mājsaimniece un ir 84 gadus veca, bet mans tēvs Pogbass, skolotājs, ir 88 gadus vecs. Man ir sešas māsas – Nilla, Sāra, Dana, Sofija, Katija un Svea; no kurām Nilla ir mājsaimniece, Sāra medicīnas studente, un Dana ir arī mājsaimniece, kamēr pārējās studē. Viņām patīk skatīties seriālus un fotografēt, bet lasīšana viņām nepatīk.",  
      "Šajā versijā papildus mainīta teksta struktūra un stils, precizējot informācijas izklāstu, kā arī veikta padziļināta interpunkcijas un pareizrakstības korekcija.") ,  

     ("Mani sauc Kalless Kaviārs, man ir četrdesmit trīs gadi. Es esmu profesors un ļoti apmierināts ar savu darbu. Es esmu no Francijas un esmu lepns par savu francūzisko mantojumu; es runāju franciski, angliski, latviski, vāciski un spāniski. Man patīk peldēt, skatīties seriālus, sportot un fotografēt, bet es neesmu aizrautīgs lasītājs. Man garšo alus, bet nevaru iedomāties kokakolas patēriņu. Es dzīvoju Rīgā, mana adrese – Stabu iela septiņdesmit pieci, dzīvoklis divpadsmit. Esmu precējies ar Mariju, un mums ir četri bērni: Sava, Kalless, Katija un Zara, kuriem patīk spēlēt spēles, lasīt, sportot, skatīties seriālus un fotografēt, kā arī baudīt šokolādi, augļus un saldējumu, taču negaršo kafiju.",  
      "Trešajā variantā uzsvērta informācijas skaidrība un konsekvence, izlabojot dažādas interpunkcijas un gramatikas nepilnības, vienlaikus saglabājot sākotnējo nozīmi.")
   ]

3. Ievadteksts:  
Mani sauc Vicky un man ir divdesmit viens gadi, Es esmu no Uganda bet tagad es dzivoju Rīgā jo es studeju mecidicina Rigā Stradiņa Universitetē. Es nestradaju jo man nav darba atļaujas. Es esmu Ugandiete, un ranaju angliski un mazliet zviedriski. Man patik studē molekulārā bioloģija bet man nepatik studē cilvēka anatomija. Man arī nepatīk laiks Rigā jo ir loti auksts.  
Mana gimene ir liela. Man ir cetras masas un divi braļi. Vini dzivo Uganda. Mani masa vards ir, Nicole, Lydia, Elizabeth un Atticia. Mani braļis vards ir Nicksoņs un Hudsoņs. Nicole, Lydia, Nicksoņs un Hudsoņs stradā, jo ir pabeigusi studejas, bet Elizabeth un Atticia ir studentes.  
Mans tevs ir Roberts. Viņs ir piecdesmit cetri gadi un viņs ir inženieris. Maha mate ir Sonija. Vini ir cetrdesmit astoņi un viņi ir medmāsa. Mani vecāki ir abi pensionāri. Mans vectevs bija pārdevējs un mana vecmāmiņa bija skolotāja. Mans vectevs patik alkohols.  
Mums ir antilopis. Viņa vards ir Sadie. Tas ir divi gadi  
Es bija Ķina ar mans tevs. Mes patik celot

   Labojumi:  
   [  
     ("Mani sauc Vikija, un man ir divdesmit viens gads. Es esmu no Ugandas, bet tagad es dzīvoju Rīgā, jo es studēju medicīnu Rīgas Stradiņa universitātē. Es nestrādāju, jo man nav darba atļaujas. Es esmu ugandiete un runāju angliski un mazliet zviedriski. Man patīk studēt molekulāro bioloģiju, bet anatomijas nodarbības nepatīk. Man arī nepatīk laiks Rīgā, jo ir ļoti auksts. Mana ģimene ir liela – man ir četras māsas un divi brāļi, kuri dzīvo Ugandā. Manu māsu vārdi ir Nikole, Lidija, Elizabete un Atiša, bet manu brāļu vārdi ir Niksons un Hadsons; pirmie ir pabeiguši studijas, bet pārējie – studentes. Mans tēvs ir Roberts, kuram ir piecdesmit cetri gadi un kurš strādā kā inženieris. Mana māte, Sonija, ir četrdesmit astoņi gadi un medmāsa. Mani vecvecāki abi ir pensionāri; mans vectēvs bija pārdevējs, un viņam patīk alkohols. Mums ir antilope vārdā Seidijs, kurai ir divi gadi. Es biju Ķīnā ar manu tēvu, un mums patīk ceļot.",  
      "Tiek veikta pilnīga gramatikas, pareizrakstības un interpunkcijas korekcija, papildinot arī stilistiskos uzlabojumus, lai teksts būtu vienots un skaidrs.") ,  

     ("Mani sauc Vikija, un man ir 21 gads. Es esmu no Ugandas, taču tagad dzīvoju Rīgā, jo studēju medicīnu Rīgas Stradiņa universitātē. Nestrādāju, jo man nav darba atļaujas. Kā ugandiete, es runāju angliski un nedaudz zviedriski. Man patīk molekulārā bioloģija, bet anatomijas studijas neiesaista manu interesi, un laiks Rīgā ir ļoti auksts. Mana ģimene ir liela – man ir četras māsas un divi brāļi, kas dzīvo Ugandā. Manu māsu vārdi ir Nikole, Lidija, Elizabete un Atiša, bet manu brāļu vārdi ir Niksons un Hadsons, jo pirmie ir pabeiguši studijas, bet pārējie joprojām studē. Mans tēvs Roberts ir piecdesmit četri gadi vecs inženieris, un mana māte Sonija – 48 gadus veca medmāsa – abi ir pensionāri. Mums ir antilope, kurai ir divi gadi, un es biju Ķīnā ar manu tēvu; mums abiem patīk ceļot.",  
      "Šajā versijā tika pārstrukturēti teikumi un precizēti izteicieni, lai nodrošinātu augstāku teksta skaidrību un konsekvenci, labojot gan gramatikas, gan pareizrakstības kļūdas.") ,  

     ("Mani sauc Vikija, un man ir divdesmit viens gads. Es esmu no Ugandas, bet tagad dzīvoju Rīgā, jo studēju medicīnu Rīgas Stradiņa universitātē. Es nestrādāju, jo man nav darba atļaujas. Kā ugandiete, es runāju angliski un mazliet zviedriski. Man patīk studēt molekulāro bioloģiju, bet ne anatomiju, kas man nepatīk. Laiks Rīgā ir ārkārtīgi auksts. Mana ģimene ir liela – man ir četras māsas un divi brāļi, kuri atrodas Ugandā. Manu māsu vārdi ir Nikole, Lidija, Elizabete un Atiša, bet manu brāļu vārdi ir Niksons un Hadsons; no tiem pirmie ir pabeiguši studijas, bet pārējie ir studentes. Mans tēvs Roberts ir piecdesmit cetri gadi vecs inženieris, un mana māte Sonija – 48 gadus veca medmāsa – abi ir pensionāri. Mans vectēvs, kas bija pārdevējs, patīk alkohols. Mums ir antilope vārdā Seidijs, kura vecums ir divi gadi. Es biju Ķīnā ar manu tēvu, un mums patīk ceļot.",  
      "Šajā korekcijā tika saglabāta sākotnējā informācijas struktūra, vienlaikus precizējot gramatiku, interpunkciju un stilistiku, lai teksts būtu vieglāk uztverams.")
   ]  
   
4. Ievadteksts:
   Mani sauc \*. Es esmu no Pakistānas. Es esmu students. Es studēju Liepājas Universitātē. Es dzīvoju kopmītnē. Kopmītne ir Liepājā. Liepājas Universitāte ir centrā. Man patik Liepājā. Universitāte ir labi. Skolotāji ir labi izglītoti. Man patik dators. Mans grāds ir saistīts ar programmatūras inženieriju.

   Labojumi:
   [("Mani sauc \\*, es esmu no Pakistānas. Es esmu students un studēju datorzinātni. Es studēju Liepājas Universitātē un dzīvoju kopmītnē, kas atrodas Liepājā. Liepājas Universitāte atrodas pilsētas centrā, un tā ir laba. Skolotāji ir labi izglītoti, un man patīk dators. Mans grāds ir saistīts ar programmatūras inženieriju.", "Izlabotas gramatikas un pareizrakstības kļūdas, uzlabota teikumu struktūra un precizēta informācija."), 
    ("Mani sauc \\*, es esmu no Pakistānas. Esmu students, kurš studē datorzinātni Liepājas Universitātē, dzīvojot kopmītnē Liepājā. Universitāte ir laba, un skolotāji ir labi izglītoti. Man patīk dators, un mans grāds ir saistīts ar programmatūras inženieriju.", "Teksts pārstrukturēts, lai uzlabotu plūdumu, kā arī veikta interpunkcijas un gramatikas korekcija."), 
    ("Mani sauc \\*, es esmu no Pakistānas un students, kurš studē datorzinātni Liepājas Universitātē. Dzīvoju kopmītnē, kas atrodas Liepājā. Universitāte ir laba, skolotāji labi izglītoti, un man patīk dators. Mans grāds ir saistīts ar programmatūras inženieriju.", "Korekcijā veikta teksta kondensācija, izlabojot būtiskas kļūdas un nodrošinot skaidrību, saglabājot sākotnējo nozīmi.")]

5. Ievadteksts:
   Mani sauc Victoria, man ir divdesmit viens gads. Mans uzvārds ir Iliescu. Es esmu studenti un es dzivoju Rīgā. Mana universitate ir Rīga Stradina Universitate. Es esmu no Austrijas, es runāju krievski, vāciski, angliski. un un mazliet latviski. Mana gimene dzivo Vacijā. Man ir trīs brāļi, viniem patīk spēlēt spēles un sportot. Mana māte sauc Anna, vina ir ārste. Mans tevs sauc Peter, viņs ir vacietis, mana māte ir austriete. Es nestradāju, es studēju. Man patīk peldēt un lasīt. Man nepatīk skatīties seriālus. Man garšo šokolāde, augļi, saldējums, kafija un zivs, un banāns. Man patik Riga un Milano. Es esmu austriete. Man nav māsas. Man loti patīk mana universitāte. Man nepatik kaki. Man  negaršo piens. Es dzīvoju Vecrīgā. Mans hobijs ir leņķis. Man patīk leņķis Rigā ar saviem draugiem. Pārtikas ir loti patīkama. Es baudiju mana dzīvi Rigā, pat ja es studeju ļoti. Es mēģinieju apmeklēt skaistas vietas par atmiņas.

   Labojumi:
   [("Mani sauc Viktorija, man ir divdesmit viens gads. Mans uzvārds ir Iliesku. Es esmu studente un dzīvoju Rīgā. Mana universitāte ir Rīgas Stradiņa universitāte. Es esmu no Austrijas un runāju krieviski, vāciski, angliski un mazliet latviski. Mana ģimene dzīvo Vācijā. Man ir trīs brāļi, kuriem patīk spēlēt spēles un sportot. Manu māti sauc Anna, viņa ir ārste. Manu tēvu sauc Pēteris, kurš ir vācietis, bet mana māte ir austriete. Es nestrādāju, es studēju. Man patīk peldēt un lasīt, bet seriālu skatīšanās nav mana nodarbe. Man garšo šokolāde, augļi, saldējums, kafija, zivis un banāni. Man patīk Rīga un Milāna. Es esmu austriete, man nav māsas un mana universitāte ir ļoti patīkama. Man nepatīk kaķi, un es negaršo piens. Es dzīvoju Vecrīgā, un mans hobijs ir leņķis, ko es kopā ar draugiem veicu Rīgā. Pārtika ir ļoti laba, un es baudu savu dzīvi, pat ja intensīvi studēju.", "Izlabotas gramatikas, pareizrakstības un interpunkcijas kļūdas, kā arī nodrošināta konsekventa teikumu struktūra."), 
    ("Mani sauc Viktorija, man ir 21 gads, un mans uzvārds ir Iliesku. Es esmu studente un dzīvoju Rīgā, studējot Rīgas Stradiņa universitātē. Es esmu no Austrijas un runāju krieviski, vāciski, angliski un nedaudz latviski. Mana ģimene dzīvo Vācijā, un man ir trīs brāļi, kuriem patīk spēlēt spēles un sportot. Manu māti sauc Anna, viņa ir ārste, un manu tēvu sauc Pēteris, kurš ir vācietis, kamēr mana māte ir austriete. Es nestrādāju, tikai studēju. Man patīk peldēt un lasīt, bet seriālu skatīšanās man neinteresē. Man garšo šokolāde, augļi, saldējums, kafija, zivis un banāni. Man patīk Rīga un Milāna, un mana universitāte ir ļoti patīkama. Man nepatīk kaķi un negaršo piens. Es dzīvoju Vecrīgā, un mans hobijs ir leņķis, ko dodos kopā ar draugiem Rīgā. Pārtika ir ļoti laba, un es baudu savu dzīvi, pat ja studēju intensīvi.", "Šajā versijā tika pārstrukturēti teikumi, lai nodrošinātu plūdumu, un veikta precīza interpunkcijas un gramatikas korekcija."), 
    ("Mani sauc Viktorija, esmu 21 gadus jauna, un mans uzvārds ir Iliesku. Esmu studente, dzīvoju Rīgā un studēju Rīgas Stradiņa universitātē. No Austrijas es runāju krieviski, vāciski, angliski un mazliet latviski. Mana ģimene dzīvo Vācijā; man ir trīs brāļi, kuriem patīk spēlēt spēles un sportot. Manu māti sauc Anna, viņa ir ārste, un manu tēvu sauc Pēteris – viņš ir vācietis, bet mana māte ir austriete. Es nestrādāju, jo studēju. Man patīk peldēt un lasīt, bet seriālu skatīšanās man nepatīk. Man garšo šokolāde, augļi, saldējums, kafija, zivis un banāni. Rīga un Milāna ir manas iecienītākās pilsētas, un mana universitāte ir ļoti patīkama. Man nepatīk kaķi un es negaršo piens. Dzīvoju Vecrīgā, un mans hobijs ir leņķis, ko kopā ar draugiem organizēju Rīgā. Pārtika ir ļoti laba, un es baudu savu dzīvi, pat ja studēju intensīvi.", "Trešajā variantā veikta detalizēta stila un gramatikas korekcija, uzlabojot teikumu struktūru un izteicienus.")]

Ievades teksts: {text}
Labojumi:"""


class GrammarErrorCorrectionAggregationPrompt(BasePrompt):
    template: str = """Apkopojiet ierosinātos gramatikas labojumus, izveidojot galīgo, gramatiski pareizo tekstu.
No sākotnējā teksta un {num_corrections} labojumu variantu saraksta apvienojiet visas noderīgās izmaiņas no šīm versijām, lai izveidotu vienu galīgo, sintaktiski pareizo tekstu.
Novērst visas pareizrakstības, interpunkcijas, stilistikas, gramatikas, leksikas un sintakses kļūdas.
Pievienojiet paskaidrojumus par apkopotajiem labojumiem un vispārējiem gramatikas labojumiem.
Koncentrējieties tikai uz ierosinātajiem labojumiem un nemēģiniet patstāvīgi mainīt oriģinālo tekstu.
Ja kļūdu nav, atdodiet oriģinālo tekstu.
Izvairieties no visām dubultajām pēdiņām un citām speciālajām rakstzīmēm, atbildē izmantojot divas atpakaļsvītras.
Piemēram, izmantojiet \\n jaunas rindkopas un \\" par dubulto citātu.
Lūdzu, neizņemiet tehniskos simbolus, piemēram, interneta saites, tagus utt. no citām valodām (galvenokārt no angļu valodas).


Ierosināto labojumu formāts:
[{{
    "correction": "labotais teksts",
    "explanation": "paskaidrojums par korekciju"
}},...]

[Output only JSON]
Atbildes formāts JSON:
{{
    "correction": "labotais teksts",
    "explanation": "paskaidrojums par korekciju"
}}

Oriģinālais teksts: {text}
Ierosinātie labojumi: {possible_corrections}
Labotais teksts:"""
    input_variables: list[str] = ["text", "possible_corrections", "num_corrections"]

