from src.prompts.base_prompts import BasePrompt


class MultiGrammarErrorCorrectionGenerationPrompt(BasePrompt):
    template: str = """Opravte následující text tak, aby byl gramaticky správný.
Opravte všechny pravopisné, interpunkční, stylistické, gramatické, lexikální a syntaktické chyby.
Pokud v něm nejsou žádné chyby, zopakujte původní text.
Vytvořte {num_corrections} různých verzí opraveného textu s vysvětlivkami.
Všechny dvojité uvozovky a další speciální znaky v odpovědi escapuje dvěma zpětnými lomítky.
Například místo nového řádku použijte znak \\n; místo „ použijte escapovaný znak \\“.
Prosím, neodstraňujte technické symboly, jako jsou internetové odkazy, značky atd. z jiných jazyků (převážně z angličtiny).


Formát odpovědi JSON:
[{{
    "correction": "opravený text",
    "explanation": "vysvětlení opravy"
}}, ...]

Příklady:

1. Vstupní text:
   Poslední 3 měsíce mého života byly hodně nabité událostmi a emocemi, ale teď jsem konečně našel volné hodiny a trochu energie pokračovat v psaní o svých zkušenostech s blogováním.

   Oprava:
   [("Poslední tři měsíce mého života byly nesmírně nabité událostmi a emocemi, ale nyní jsem konečně našel několik volných hodin a trochu energie, abych pokračoval v psaní o svých zkušenostech s blogováním.", "Nahrazeno číslo '3' slovem 'tři' pro jednotnost stylu; 'volné hodiny' změněno na 'několik volných hodin' pro přesnější vyjádření; doplněna spojka a čárka pro správnou interpunkci a stylistické vyvážení.")]

2. Vstupní text:
   Už zbývá jen pár minut,“ říká si určitě nejeden žák naší třídy. Vyčerpán úmornou hodinou, těší se na zaslouženou přestávku. Z hodiny se někdy stává přestávka. My se samozřejmě rychle zklidníme a hle, zvoní!

   Oprava:
   [("Rád bych vám představil místo, na kterém trávím podstatnou část svého života. Toto pro mě velice důležité místo se jmenuje sportovní (baseballový) areál a nachází se u cyklostezky mezi Českými Budějovicemi a Hlubokou nad Vltavou. Shromažďuje se zde A-tým hlubockého baseballu, přibližně dvacetičlenná parta mužů ve věku 19–30 let, kteří tomuto krásnému sportu dávají vše, co mohou. Jsem nesmírně rád, že se mi kombinací talentu a tvrdé práce podařilo stát se součástí tohoto týmu.", "Opraveny stylistické nedostatky: 'pro mne' → 'pro mě', 'veledůležité' → 'velice důležité', 'kolem cyklostezky' upraveno na přesnější 'u cyklostezky mezi ...'; upraveno vyjádření věkového rozmezí pomocí spojovníku; slovo 'stroje, mašiny' nahrazeno konkrétnějším výrazem 'týmu'.")]
   
3. Vstupní text:
   Poslední 3 měsíce mého života byly hodně nabité událostmi a emocemi, ale teď jsem konečně našel volné hodiny a trochu energie pokračovat v psaní o svých zkušenostech s blogováním.

   Oprava:
   [("„Už zbývá jen pár minut,“ říká si určitě nejeden žák naší třídy. Vyčerpán úmornou, nekonečnou hodinou, se těší na zaslouženou přestávku. U nás se z hodiny občas stává, že se již zdá být přestávka. My se samozřejmě bleskově uklidníme a hle – zvoní!", "Doplněny chybějící čárky a upraven slovosled pro plynulost; stylisticky vylepšeno vyjádření ‚z hodiny se někdy stává přestávka‘ na srozumitelnější variantu." )]
   
4. Vstupní text:
   Mark seděl na okraji lesa. V ruce držel sklenku červeného vína a pozoroval západ slunce. Chtěl být sám. Uvnitř něho se odehrával souboj emocí. V tuto chvíli nevěděl, co chce. V hlavě si přehrával útržky nedávných událostí. Napil se vína a připadal si, jako by měl v hlavě prázdno. Jak by měl tu situaci řešit? Přemýšlel a vzpomínal na dětství. Najednou se mu zdálo, že se ty doby opět odehrávají. Usmál se, vstal a šel se projít po lese.
    
   Oprava:
   [("Mark seděl na okraji lesa, v ruce držel sklenku červeného vína a pozoroval západ slunce. Chtěl být sám, neboť v něm zuřil souboj emocí. V tu chvíli ani nevěděl, co vlastně chce; v hlavě si přehrával útržky nedávných událostí. Napil se vína a cítil, jako by měl v hlavě úplné prázdno. Přemýšlel, jak by měl tuto situaci řešit, a vzpomínal na dětství. Najednou se mu zdálo, jako by se ty doby znovu odehrávaly. Usmál se, vstal a vyrazil na procházku po lese.", "Upraveny interpunkční znaménka a stylistické formulace; zjednodušeno vyjádření, aby byl text plynulejší; opraveny drobné gramatické nepřesnosti a shoda podmětu se slovesem.")]
   
5. Vstupní text:
   Při pohledu do zrcadla mě napadají otázky: Jak mě vidí ostatní? Chovám se neslušně? Co si o mně myslí rodina a kamarádi? Nakonec jsem sám se sebou spokojený? Pokusím se odpovědět.
   
   Oprava:
   [("Při pohledu do zrcadla mě napadají různé otázky: Jak mě vidí ostatní? Chovám se neslušně? Co si o mně myslí rodina a kamarádi? A nakonec – jsem sám se sebou spokojený? Pokusím se na některé z těchto otázek odpovědět.", "Doplněna interpunkce a stylisticky upravená formulace pro lepší srozumitelnost a plynulost textu.")]
   
6. Vstupní text:
   Dne 3. 11. v 15:30 proběhla po dlouhé době Spartakiáda v T-nobile areně. tuto akci pamatují jen naše babičky nebo prababičky. Uprostřed maškarního plesu se Popelka a Sněhurkou začaly prát. Sněhurce začala téct krev z nosu. Přišli jsme, a bylo to dobré.
   
   Oprava:
   [("Dne 3. 11. v 15:30 proběhla po dlouhé době spartakiáda v T‑Mobile aréně. Tuto akci si pamatují jen naše babičky a prababičky. Uprostřed tohoto maškarního plesu se Popelka se Sněhurkou začaly prát – Sněhurce začala téct krev z nosu, ale jinak vše proběhlo dobře.", "Opraveny chyby v interpunkci a pravopise (např. 'T‑nobile' → 'T‑Mobile'); doplněno spojení a upraven stylistický celek zprávy pro větší srozumitelnost.")]
 

Vstupní text: {text}
Oprava:"""


class GrammarErrorCorrectionAggregationPrompt(BasePrompt):
    template: str = """Shrňte navržené gramatické opravy textu do konečného gramaticky správného textu.
Při zadání původního textu a seznamu {num_corrections} oprav spojte všechny užitečné opravy z těchto možností a vytvořte konečný opravený, syntakticky správný text.
Opravte pravopisné, interpunkční, stylistické, gramatické, lexikální a syntaktické chyby.
K souhrnným opravám a gramatickým opravám přidejte vysvětlivky.
Zaměřte se na navrhované opravy a nepokoušejte se sami opravovat původní text.
Pokud se v textu nevyskytují žádné chyby, vraťte původní text.
Všechny dvojtečky a další speciální znaky v odpovědi uzavřete dvěma zpětnými lomítky.
Například místo nového řádku použijte znak \\n; místo " použijte escapovaný znak \\".
Prosím, neodstraňujte technické symboly, jako jsou internetové odkazy, značky atd. z jiných jazyků (převážně z angličtiny).


Formát navrhovaných oprav:
[{{
    "correction": "opravený text",
    "explanation": "vysvětlení opravy"
}},...]

[Output only JSON]
Формат відповіді у JSON:
{{
    "correction": "opravený text",
    "explanation": "vysvětlení opravy"
}}

Originální text: {text}
Navrhované opravy: {possible_corrections}
Oprava:"""
    input_variables: list[str] = ["text", "possible_corrections", "num_corrections"]
