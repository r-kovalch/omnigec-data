from src.prompts.base_prompts import BasePrompt


class MultiGrammarErrorCorrectionGenerationPrompt(BasePrompt):
    template: str = """Correggete il seguente testo rendendolo grammaticalmente corretto.
Correggete tutti gli errori ortografici, di punteggiatura, stilistici, grammaticali, lessicali e sintattici.
Se non ci sono errori, ripetere semplicemente il testo originale.
Generare {num_corrections} versioni distinte del testo corretto con le relative spiegazioni.
Sfuggire a tutti i doppi apici e ad altri caratteri speciali nella risposta usando due backslash.
Ad esempio, invece di una linea di separazione, utilizzare \\n; invece di " use \\".
Per favore, non rimuovere i simboli tecnici come i link internet, i tag, ecc. da altre lingue (principalmente dall’inglese).


Formato della risposta in JSON:
[{{
    "correction": "testo corretto",
    "explanation": "spiegazione della correzione"
}}, ...]

Esempi:

1. Testo in ingresso:
   28/05/2011. Egregio Signore, sto scrivendo per annurciarsi l'intenzione mia di frequentare uno di loro corsi relevanti, cioé il corso estivo al mare. Sono un insegnante quindi fortunamente ho una vacanze di due mesi dal Luglio al Agosto. Penso che questo corso sia il migliore per me tanto sarò libero in questi mesi e mi piace essere in un paese mediterranae d'estate. Vorrei iscrivermi per una vacanze-studio di -unreadable- settimane.dal 10 July al 28 July Potrebbero informarmi che in quale modo sono abbinate questi corsi? Perché ho i progetti di prendere un alloggio a Roma nella casa di mia nonna. Tanto non bisognò di prenotare un alloggio. Anche posso usare la sua macchina per viaggiare. Avete menziato la possibilità di fare una vacanza in Cliento. Posso andare lì quando io stesso voglio fare un vacanze o è un periodo deciso. In attesa nel suo risposto Cordiali saluti, Michele Rossi

   Correzioni:
   [("28/05/2011. Egregio Signore, sto scrivendo per annunciarvi la mia intenzione di frequentare uno dei loro corsi rilevanti, cioè il corso estivo al mare. Sono un insegnante, quindi fortunatamente ho una vacanza di due mesi da luglio ad agosto. Penso che questo corso sia il migliore per me, tanto sarò libero in questi mesi e mi piace essere in un paese mediterraneo d'estate. Vorrei iscrivermi a una vacanza-studio di -unreadable- settimane dal 10 luglio al 28 luglio. Potrebbero informarmi in quale modo sono abbinati questi corsi? Perché ho il progetto di prendere un alloggio a Roma, nella casa di mia nonna. Tanto non c'\\è bisogno di prenotare un alloggio. Anche posso usare la sua macchina per viaggiare. Avete menzionato la possibilità di fare una vacanza nel Cilento. Posso andare lì quando io stesso voglio fare una vacanza o c'\\è un periodo deciso? In attesa della sua risposta, cordiali saluti, Michele Rossi", "Rettificati errori ortografici (es. \\\"annurciarsi\\\" in \\\"annunciarvi\\\", \\\"vacanze\\\" in \\\"vacanza\\\") e uniformato l'uso delle preposizioni; inoltre, corrette le incoerenze di punteggiatura e maiuscole."),
    ("28/05/2011. Egregio Signore, le scrivo per comunicare la mia intenzione di partecipare a uno dei vostri corsi rilevanti, ossia il corso estivo al mare. In qualità di insegnante, dispongo di una vacanza di due mesi da luglio ad agosto. Ritengo che questo corso sia il migliore per me, in quanto sarò libero in quel periodo e amo trascorrere l'estate in un paese mediterraneo. Vorrei iscrivermi a una vacanza-studio di -unreadable- settimane dal 10 luglio al 28 luglio. Potrebbe informarmi su come sono organizzati questi corsi? Ho in programma di prendere un alloggio a Roma, nella casa di mia nonna, così da non dover prenotare. Inoltre, posso usare la sua macchina per viaggiare. Avete indicato la possibilità di fare una vacanza nel Cilento: posso andarci liberamente o esiste un periodo prestabilito? In attesa di una sua risposta, cordiali saluti, Michele Rossi", "Riformulata la comunicazione per una maggiore chiarezza e correttezza stilistica, con ulteriori precisazioni su punteggiatura e uso delle preposizioni."),
    ("28/05/2011. Egregio Signore, scrivo per annunciarvi la mia intenzione di frequentare uno dei vostri corsi, in particolare il corso estivo al mare. Essendo insegnante, ho la fortuna di avere una vacanza di due mesi da luglio ad agosto. Credo che questo corso sia il più adatto a me, dato che sarò libero in quel periodo e desidero trascorrere l'estate in un paese mediterraneo. Desidero iscrivermi a una vacanza-studio di -unreadable- settimane dal 10 luglio al 28 luglio. Potreste informarmi riguardo alla modalità di abbinamento dei corsi? Ho in programma di prendere un alloggio a Roma, presso la casa di mia nonna, così da non dover prenotare. Inoltre, posso usufruire della sua macchina per viaggiare. Avete indicato la possibilità di una vacanza nel Cilento: posso scegliere liberamente il periodo oppure è già definito? In attesa di un vostro cortese riscontro, cordiali saluti, Michele Rossi", "Variata la struttura della frase e adottato un lessico più formale, correggendo ortografia e punteggiatura.")]
   
2. Testo in ingresso:
   Città X, 24.11.2011 Ciao Franco, Grazie per la tua invitazione. Certo voglio venire a Città Y per questo grande incontro AS Roma contro la Lazio. È sempre uno spettacolo grandioso... ancora più quando vince la Roma! Penso di prendere Easyjet già venerdì sera, così arriverò alle ore 20.30. Mandami un messagio se verrai incontrarmi all'aeroporto! Se vuoi rimango fino a martedì mattina. Ci vediamo, forza Roma Michele P.S. Come va tuo padre? Ha trovato un nuovo impiego?

   Correzioni:
   [("Città X, 24.11.2011 Ciao Franco, grazie per la tua invitazione. Certo che voglio venire a Città Y per questo grande incontro AS Roma contro la Lazio. È sempre uno spettacolo grandioso... Ancora di più quando vince la Roma! Penso di prendere Easyjet già venerdì sera, così arriverò alle ore 20.30. Mandami un messaggio se verrai a incontrarmi all'aeroporto! Se vuoi, rimango fino a martedì mattina. Ci vediamo, forza Roma Michele P. S. Come va tuo padre? Ha trovato un nuovo impiego?", "Aggiunta la particella \\\"che\\\" dopo \\\"Certo\\\", corretto \\\"messagio\\\" in \\\"messaggio\\\" e migliorata la punteggiatura complessiva."),
    ("Città X, 24.11.2011 Ciao Franco, grazie per l'invito. Confermo la mia partecipazione a Città Y per l'incontro tra AS Roma e Lazio. È sempre uno spettacolo grandioso, ancor più quando vince la Roma! Prenoterò un volo Easyjet per venerdì sera, con arrivo previsto alle ore 20.30. Fammi sapere se ci incontreremo all'aeroporto. Rimango disponibile fino a martedì mattina. A presto, forza Roma, Michele.", "Riformulata la comunicazione per rendere il messaggio più fluido e formale, correggendo errori ortografici e di punteggiatura."),
    ("Città X, 24.11.2011. Ciao Franco, grazie per la tua invitazione. Desidero confermare la mia partecipazione a Città Y per l'incontro tra AS Roma e Lazio. L'evento è sempre uno spettacolo grandioso, specialmente quando la Roma trionfa! Ho intenzione di prendere Easyjet venerdì sera, con arrivo alle ore 20.30. Ti prego di mandarmi un messaggio se ci incontreremo all'aeroporto. Se necessario, posso rimanere fino a martedì mattina. Ci vediamo, forza Roma, Michele.", "Correzioni apportate alla struttura delle frasi e alla punteggiatura, con modifiche per migliorare la chiarezza del testo.")]
   ]
   
3. Testo in ingresso:
   Cara Daniela, Come stai? E come state la tua famiglia, tutto a posto? Ti piace la città Città X? Io voglio andare a Città X per la prossima settimana, va bene per te? Io vengo con il bus e restare 3 giorni. A la sera andiamo al cinema. Puoi chiamarmi al NR. 0345-11111111. Aspetto la tua telefonata. Ci vediamo a presto Cari saluti Maria

   Correzioni:
   [("Cara Daniela, come stai? E come sta la tua famiglia, tutto a posto? Ti piace la città di Città X? Io voglio andare a Città X per la prossima settimana, va bene per te? Io vengo con il bus e resto 3 giorni. La sera andiamo al cinema. Puoi chiamarmi al nr. 0345-11111111. Aspetto la tua telefonata. Ci vediamo presto. Cari saluti, Maria", "Correzioni: normalizzata la capitalizzazione, sostituito \\\"state\\\" con \\\"sta\\\" e \\\"restare\\\" con \\\"resto\\; inoltre, sistemata la punteggiatura."),
    ("Cara Daniela, come stai? E come sta la tua famiglia, tutto a posto? Ti piace la città di Città X? Ho intenzione di visitare Città X la prossima settimana, se per te va bene. Arriverò in autobus e rimarrò per 3 giorni. La sera andremo al cinema. Puoi contattarmi al nr. 0345-11111111. Aspetto una tua telefonata. A presto, cari saluti, Maria.", "Ristrutturato il testo per maggiore chiarezza e correttezza formale, con la sostituzione di forme verbali errate."),
    ("Cara Daniela, come stai? E come sta la tua famiglia, tutto bene? Ti piace Città X? Vorrei recarmi a Città X la prossima settimana, se sei d'accordo. Viaggerò in bus e rimarrò per 3 giorni. La sera potremmo andare al cinema. Puoi chiamarmi al nr. 0345-11111111. Aspetto la tua telefonata. A presto, cari saluti, Maria.", "Semplificata la struttura del testo e corrette le imprecisioni grammaticali, mantenendo un tono colloquiale ma corretto.")]
   ]
   
4. Testo in ingresso:
   Ciao Piero + Anna Sono a Città X dove provo di seguire un corso di italiano. Nel mio corso si trova gente di quasi tutto il mondo. Ci sono ragazzi inglesi, francesi e anche russi. Allora non imparo solo l'italiano. Nel tempo libero andiamo con bus o in treno per vedere altre citté e paesini. È sempre molto divertimento. tanti saluti e bacini x Anna Michele

   Correzioni:
   [("Ciao Piero e Anna, sono a Città X dove provo a seguire un corso di italiano. Nel mio corso c'\\è gente proveniente da quasi tutto il mondo: ci sono ragazzi inglesi, francesi e anche russi, quindi non imparo solo l'italiano. Nel tempo libero andiamo in autobus o in treno a vedere altre città e paesini. C'\\è sempre molto divertimento. Tanti saluti e bacini a Anna, Michele", "Sostituito il simbolo \\\"+\\\" con \\\"e\\\", corretto \\\"provo di seguire\\\" in \\\"provo a seguire\\\" e migliorato il lessico e la punteggiatura."),
    ("Ciao Piero e Anna, sono a Città X dove seguo un corso di italiano. In questo corso si incontrano persone da tutto il mondo, inclusi ragazzi inglesi, francesi e russi, per cui l'apprendimento non si limita all'italiano. Nel tempo libero, utilizziamo autobus o treni per visitare altre città e paesini. È sempre molto divertente. Un caro saluto e bacini ad Anna, Michele", "Ristrutturata la frase per chiarezza, correggendo \\\"divertimento\\\" in \\\"divertente\\\" e ottimizzando l'uso di termini formali."),
    ("Ciao Piero e Anna, mi trovo a Città X dove sto frequentando un corso di italiano. Durante il corso incontro persone di diverse nazionalità, tra cui inglesi, francesi e russi, il che mi permette di apprendere non solo l'italiano. Nel tempo libero, prendiamo il bus o il treno per esplorare altre città e paesini. È sempre molto divertente. Tanti saluti e un bacino per Anna, Michele", "Modificata la struttura del testo per maggiore coerenza, correggendo errori lessicali e migliorando la punteggiatura.")]
   ]
   
5. Testo in ingresso:
   Egregia Signora Gabriella Favati, Mi chiamo Michele Rossi. Sono aggettivo di nazionalità X e uno studente. Quest'anno è l'ultimo anno nel mio liceo. Vorrei andare al'università di legge. Allora devo studiare lingue straniere per punti e perchè vorrei lavorare all'estero anche. Ho studiato englese per 6 anni e ho scritto un test lingua e anche un'esame di maturita. Un anno fa cominciavo studiare l'italiano. L'italiano più bello che englese, ma anche più difficile. Attualmente io non uso le queste lingue spesso solo quando andiamo all'estero (per esempio: Italia) con la mia famiglia o la mia classe. Ma nel futuro - come Le ho detto - vorrei lavorare all'estero e ci naturalmente devo usare le lingue straniere. Spero che con le lingue straniere possa lavorare all'estero, possa incontrare e conoscere persone straniere, possa parlare molta gente nel mondo. Certo adesso devo studiare le lingue straniere perché bisogno i punti per l'università. L'educazione delle lingue in Paese X secondo me è buono. Si vuole studiare lingue straniere qui può imperare. Sero che Le abbia potere aiutare. Se ha altri domandi solo me scrive un'altra lettera. 2012.01.02 Distinti saluti, Michele Rossi

   Correzioni:
   [("Egregia Signora Gabriella Favati, mi chiamo Michele Rossi. Sono aggettivo di nazionalità X e uno studente. Quest'anno è l'ultimo anno del mio liceo. Vorrei andare all'università di legge. Devo studiare le lingue straniere per ottenere punti e perché vorrei anche lavorare all'estero. Ho studiato l'inglese per 6 anni e ho sostenuto un test di lingua e un esame di maturità. Un anno fa ho cominciato a studiare l'italiano. L'italiano è più bello dell'inglese, ma anche più difficile. Attualmente uso queste lingue solo quando andiamo all'estero (per esempio: Italia) con la mia famiglia o la mia classe. In futuro, come Le ho detto, vorrei lavorare all'estero e, naturalmente, dovrò usare le lingue straniere. Spero che, grazie alle lingue straniere, io possa lavorare all'estero, incontrare e conoscere persone straniere e comunicare con molte persone nel mondo. Certamente, adesso devo studiare per accumulare i punti necessari per l'università. L'educazione delle lingue in Paese X, secondo me, è buona. Se si vuole studiare lingue straniere qui, si può farlo. Spero di essere stato d'aiuto. Se ha altre domande, mi scriva un'altra lettera. 2012.01.02 Distinti saluti, Michele Rossi", "Correzioni: sistemati errori ortografici (es. \\\"englese\\\" in \\\"inglese\\\"), ristrutturata la frase per chiarezza e corrette le incongruenze grammaticali."),
    ("Egregia Signora Gabriella Favati, mi chiamo Michele Rossi. Sono aggettivo di nazionalità X e studente. Concludendo il liceo quest'anno, desidero iscrivermi all'università di legge. Pertanto, devo studiare le lingue straniere per ottenere i crediti necessari e perché ambisco a lavorare all'estero. Ho studiato l'inglese per 6 anni, sostenuto un test di lingua e superato l'esame di maturità. Un anno fa ho iniziato a studiare l'italiano, che ritengo più bello seppur più complesso dell'inglese. Attualmente uso queste lingue solo durante viaggi all'estero con la mia famiglia o classe. Tuttavia, in futuro, come Le ho comunicato, intendo lavorare all'estero e usare regolarmente le lingue straniere. 2012.01.02 Distinti saluti, Michele Rossi", "Correzioni: revisione completa della struttura del testo, correzione degli errori grammaticali e miglioramento della coerenza espositiva."),
    ("Egregia Signora Gabriella Favati, mi chiamo Michele Rossi. Sono aggettivo di nazionalità X e studente. Quest'anno concluderò il liceo e intendo iscrivermi all'università di legge. Per questo motivo, devo approfondire lo studio delle lingue straniere, sia per ottenere crediti che per poter lavorare all'estero. Ho studiato l'inglese per 6 anni, superato un test di lingua e l'esame di maturità. Un anno fa ho iniziato a studiare l'italiano, che considero più affascinante dell'inglese, sebbene più impegnativo. Attualmente, uso queste lingue solo in occasioni di viaggi all'estero con la mia famiglia o classe; tuttavia, in futuro vorrei utilizzarle costantemente. 2012.01.02 Distinti saluti, Michele Rossi", "Correzioni: migliorata la struttura logica e coerenza del discorso, corrette le imprecisioni lessicali e adeguata la punteggiatura.")]

Testo in ingresso: {text}
Correzioni:"""


class GrammarErrorCorrectionAggregationPrompt(BasePrompt):
    template: str = """Aggregare le correzioni grammaticali proposte in un testo finale grammaticalmente corretto.
Dal testo originale e da un elenco di {num_corrections} varianti di correzione, unire tutte le modifiche utili di queste versioni per creare un testo finale sintatticamente corretto.
Eliminare tutti gli errori ortografici, di punteggiatura, stilistici, grammaticali, lessicali e sintattici.
Includere spiegazioni per le correzioni aggregate e per le correzioni grammaticali generali.
Concentratevi esclusivamente sulle correzioni suggerite e non cercate di modificare in modo indipendente il testo originale.
Se non ci sono errori, restituire il testo originale.
Nella risposta, tutti i doppi apici e gli altri caratteri speciali devono essere sfuggiti utilizzando due backslash.
Ad esempio, utilizzare \\n per una linea nuova e \\" per una doppia citazione.
Per favore, non rimuovere i simboli tecnici come i link internet, i tag, ecc. da altre lingue (principalmente dall’inglese).


Formato delle correzioni proposte:
[{{
    "correction": "testo corretto",
    "explanation": "spiegazione della correzione"
}},...]

[Output only JSON]
Formato di risposta in JSON:
{{
    "correction": "testo corretto",
    "explanation": "spiegazione della correzione"
}}

Testo originale: {text}
Correzioni proposte: {possible_corrections}
Testo corretto:"""
    input_variables: list[str] = ["text", "possible_corrections", "num_corrections"]

