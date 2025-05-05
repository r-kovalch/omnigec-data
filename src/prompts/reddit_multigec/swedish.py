from src.prompts.base_prompts import BasePrompt

class MultiGrammarErrorCorrectionGenerationPrompt(BasePrompt):
    template: str = """Korrigera följande text så att den blir grammatiskt korrekt.
Korrigera alla stavfel, skiljetecken, stilistiska, grammatiska, lexikala och syntaktiska fel.
Om texten inte innehåller några fel, upprepa originaltexten.
Generera {num_corrections} olika versioner av den korrigerade texten med tillhörande förklaringar.
Escapea alla dubbla citattecken och andra specialtecken i svaret med två bakåtsnedstreck.
Till exempel, använd \\n för en ny rad och \\" istället för ett dubbelt citattecken.
Vänligen ta inte bort tekniska symboler, såsom internetlänkar, taggar, etc. från andra språk (främst engelska).


Svarformat i JSON:
[{{
    "correction": "korrigerad text",
    "explanation": "förklaring till korrigeringen"
}}, ...]

Exempel:

1. Inmatad text:
   Jag kommer från Peru och vi har ett ordspråk som säger att man ofta träffar någons kläder men säger farväl till någons personlighet. Och jag håller med om det. Jag tror att kläder spelar viktig roll i ens liv men jag har min egen åsikt om det. När jag träffar person första gången fäster jag min uppmärksamheten på mans utseende och det inkluderar både kläder och hur man ser ut i allmänhet. Det är inte viktig för mig om kläderna är trendiga och nya men de behöver vara rena och prydliga. 
   Jag tror att det är bra när man har sin egen stil och klär sig inte bara enligt modefluga men väljer kläder som passar figur och man känner sig bekväm i dem. 
   Jag tror att i Sverige finns bra möjlighet att uttrycka sig genom kläder eftersom man kan ha på sig nästan vad man vill. Det är inte samma i landet som jag kommer från. I Peru klär sig människor mycket lika och om man har någonting ovanligt på sig då fäster det mycket uppmärksamhet i samhället (och det är inte en bra sak). 
   Också jag gillar att i Sverige finns många affärer när man kan handla kläder även begagnade. Det tillåter att spara pengar och är mycket miljövänligt. 
   Å ena sidan är det viktigt att ha sin egen stil men å andra sidan är det relevant att anpassa sig till normer på arbetsplatsen eller i samhället. Om det finns någon klädkod då behöver man följa den eftersom det visar respekt för andra människor. Om dina kläder gör folk obekväma där man bor eller arbetar då behöver man undvika göra så och anpassa sin stil.

   Korrigeringar:
   [("Jag kommer från Peru och vi har ett ordspråk som säger att man ofta träffar någons kläder men säger farväl till någons personlighet. Och jag håller med om det. Jag tror att kläder spelar en viktig roll i ens liv, men jag har min egen åsikt om det. När jag träffar en person för första gången fäster jag uppmärksamheten på personens utseende, vilket inkluderar både kläder och hur man ser ut i allmänhet. Det är inte viktigt för mig om kläderna är trendiga och nya, men de behöver vara rena och prydliga.", "Lagt till nödvändiga artiklar, rättat prepositioner och justerat skiljetecken för bättre läsbarhet."), 
   ("Jag kommer från Peru och vi har ett ordspråk som säger att man ofta bedömer någon utifrån deras kläder men glömmer bort personens verkliga karaktär. Jag håller med om detta. Jag anser att kläder spelar en viktig roll i ens liv, men jag har min egen uppfattning. När jag möter någon för första gången fokuserar jag på personens utseende, inklusive kläder och helhetsintryck. Det är inte avgörande för mig att kläderna är trendiga och nya, utan att de är rena och prydliga.", "Omstrukturerat meningarna för att förbättra flytet och korrigerat grammatiska fel.")]

2. Inmatad text:
   Tjena Maria! hur är läget? 
   Jag läste din sms för att ge bort pengar till Anna som bröllopspresent. men det låter inte en bra present. Vi kan köpa den tavlan istället som hon ville köpa den förre veckan. 
   Jag tänker det låter bättre present till henne eftersom hon gillar mycket den. Dessutom blir hon glad och minnas alltid oss när hon ser den tavlan. 
   Om du är håller med min förslag vi kan köpa den imorgon. 

   Korrigeringar:
   [("Tjena Maria! Hur är läget? Jag läste ditt sms om att ge bort pengar till Anna som bröllopspresent, men det låter inte som en bra idé. Vi kan köpa den där tavlan istället, som hon ville ha förra veckan. Jag tycker att det verkar vara en bättre present till henne eftersom hon verkligen gillar den. Dessutom blir hon glad och kommer alltid att minnas oss när hon ser tavlan. Om du håller med om mitt förslag kan vi köpa den imorgon.", "Justerat ordföljd, korrigerat grammatiska misstag och förbättrat meningsbyggnaden."), 
   ("Hej Maria! Hur är läget? Jag såg ditt sms om att ge pengar till Anna som bröllopspresent, men det verkar inte vara en bra present. Istället kan vi köpa den tavla hon önskade förra veckan. Jag anser att det skulle vara en bättre present, eftersom hon gillar den mycket. Dessutom kommer hon att bli glad och alltid minnas oss när hon ser tavlan. Om du instämmer i mitt förslag kan vi köpa den imorgon.", "Förbättrat klarhet, rättat stavfel och justerat meningsstrukturen för bättre flyt.")]

Inmatad text: {text}
Korrigeringar:"""
    input_variables: list[str] = ["text", "num_corrections"]


class GrammarErrorCorrectionAggregationPrompt(BasePrompt):
    template: str = """Sammanfoga de föreslagna grammatiska korrigeringarna till en slutgiltig, grammatiskt korrekt text.
Utifrån originaltexten och en lista med {num_corrections} versioner av korrigeringar, kombinera alla användbara ändringar från dessa versioner och skapa en slutgiltig, syntaktiskt korrekt text.
Ta bort stavfel, skiljeteckenfel, stilistiska, grammatiska, lexikala och syntaktiska fel.
Lägg till en förklaring för de aggregerade korrigeringarna samt den övergripande grammatikkorrigeringen.
Fokusera enbart på de föreslagna korrigeringarna och försök inte att självständigt korrigera originaltexten.
Om inga fel finns, returnera originaltexten.
Escapea alla dubbla citattecken och andra specialtecken i svaret med två bakåtsnedstreck.
Till exempel, använd \\n för en ny rad och \\" istället för ett dubbelt citattecken.
Vänligen ta inte bort tekniska symboler, såsom internetlänkar, taggar, etc. från andra språk (främst engelska).


Format för de föreslagna korrigeringarna:
[{{
    "correction": "korrigerad text",
    "explanation": "förklaring av korrigeringen"
}},...]

[Output only JSON]
Svarformat i JSON:
{{
    "correction": "korrigerad text",
    "explanation": "förklaring av korrigeringen"
}}

Originaltext: {text}
Föreslagna korrigeringar: {possible_corrections}
Korrigerad text:"""
    input_variables: list[str] = ["text", "possible_corrections", "num_corrections"]


