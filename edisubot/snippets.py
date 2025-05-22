from html import escape
from telebot.util import quick_markup

snip = {
    "Copertura al 100%": 
    {'testo':"""\
Negli ultimi 8 anni circa siamo riusciti ad ottenere la copertura totale delle borse.\
Anche quest'anno, come Alter.POLIS, CollettivaMente e Studenti Indipendenti, \
abbiamo chiesto garanzie alla Regione ed a parole ci è stato detto che l'intenzione è la copertura al 100%. \
La reale situazione sarà nota solo verso dicembre, con il numero di richieste e lo stanziamento effettivo dei fondi. \
Come sempre vigileremo sull'operato della Regione
"""},

    "Differenza tra standard e conferma":
    {'testo':"""\
<b>Differenza tra domanda standard e domanda di conferma benefici per merito</b>

Se l'anno precedente hai ricevuto i benefici (posto letto e/o borsa), con la domanda di conferma ottieni \
sicuramente i benefici per cui fai richiesta (e che avevi già ricevuto). Hai la precedenza rispetto alla domanda standard.
Puoi fare domanda di conferma solo se hai il numero di crediti richiesto (per questo si chiama "per merito")
"""},

    "Rinuncia al posto letto dopo le graduatorie definitive":
    {'testo':"""\
<b>Rinuncia al posto letto dopo le graduatorie definitive</b>

La rinuncia al posto letto successivamente alle graduatorie definitive può comportare la perdita \
della borsa di studio da fuori sede completa. Per maggiori dettagli leggi a pagina 19 del bando.

In sintesi, se rifiuti poiché assegnatariз nelle graduatorie definitive di servizio abitativo o negli \
esiti della dichiarazione di interesse, diventi pendolare (ai fini dell'importo della borsa).

Per tutti gli altri casi, ti rimando alla pagina 19 o premi il pulsante sotto
""",
    'markup':quick_markup({
        'Tabella riassuntiva importi borsa':{'url': 'https://t.me/edisubotimmagini/6'}
    })},

    "CFU necessari durante l'anno per gli anni successivi":
    {'testo':"""\
<b>CFU necessari durante l'anno per gli anni successivi</b>

La borsa EDISU è destinata a coloro che rispettano i requisiti economici (cioè ISEE e ISP sotto una certa soglia) \
e i requisiti di merito (devono aver totalizzato un tot di CFU negli anni precedenti).

Per i primi anni non è naturalmente possibile valutare il merito essendo che lo studente non ha ancora sostenuto esami. \
Per cui lo studente deve ottenere 20 CFU entro il 10 agosto successivo per poter ottenere la seconda rata della borsa \
(o 20 CFU entro Novembre per non dover restituire la prima rata).

Questo discorso non si applica per gli anni successivi poichè per questi è possibile valutare il merito \
basandosi sugli anni precedenti. Per cui se al momento di fare domanda per anni successivi hai i CFU richiesti, \
risultando assegnatario hai diritto ad entrambe le rate della borsa.
"""},

    "Elenco corsi STEM" :
    {'testo':r"""\
<b> Elenco corsi STEM</b>

https://www.edisu.piemonte.it/sites/default/files/risorse/documentazione/Bandi_di_concorso/2023-2024/Elenco%20Corsi%20STEM%20a.a.%202023-24.pdf
"""},

    "Dichiarazione di domicilio a titolo oneroso":
    {'testo':"""\
<b>Dichiarazione di domicilio a titolo oneroso</b>

La dichiarazione di domicilio a titolo oneroso va fatta da tutti lз studentз fuori sede che NON sono ospiti \
delle residenze EDISU e non abbiano accettato (o dichiarato l'interesse) mediante Opzione Einaudi.
Serve per confermare lo status di fuori sede e va fatta a partire dal 19 Ottobre.

La scadenza per presentare tale dichiarazione dipende dall'anno d'iscrizione, per maggiori dettagli vedi pag 38 o clicca il pulsante in basso.
     
Il contratto da caricare deve avere le caratteristiche indicate all'articolo 8 del bando.
""",
    'markup': quick_markup({'Scadenze per la dichiarazione di domicilio a titolo oneroso':\
                            {'url': 'https://t.me/edisubotimmagini/7'}})},
    
    "Differenza tra locativo e diverso titolo oneroso":
    {'testo':"""\
Dichiarazione di domicilio a titolo locativo: hai una casa in affitto, e quindi contratto di locazione \
registrato presso l'agenzia delle entrate.

Dichiarazione di domicilio a diverso titolo oneroso: stai in collegio/convitto, non hai un contratto \
locativo e il contratto che fai con la struttura non viene registrato presso l'agenzia delle entrate. \
Possibilmente ogni volta che versi soldi ti viene pure dato uno scontrino/fattura/ricevuta fiscale.
"""},

    "Date erogazione rate borsa di studio":
    {'testo':"""\
Le date di erogazione delle rate della borsa di studio dipendono dall'anno d'iscrizione e dal quando è \
stato caricato l'iban sul portale edisu.

Va precisato che per i primi anni la ricezione della seconda rata dipende dal conseguimento dei 20 cfu, \
requisito di merito necessario per il mantenimento della borsa per i soli primi anni.

(art 13 comma 5) Le studentesse e gli studenti che non conseguono i 20 cfu entro il 10 agosto 2024 perdono \
il diritto a ricevere la seconda rata di borsa. Possono, tuttavia, mantenere il diritto alla sola prima rata di borsa \
conseguendo almeno 20 crediti entro il 30 novembre 2024. È inoltre necessario che tali crediti siano regolarmente registrati
dal proprio Ateneo con data uguale o anteriore al 30 novembre 2024.

Il periodo di erogazione per gli anni successivi è il seguente:
1. la prima rata, pari al 50%% dell'importo totale, viene erogata a partire da fine dicembre 2023;
2. la seconda rata, pari al restante 50%% dell'importo totale, viene erogata a partire da fine giugno 2024, con accredito su IBAN da metà luglio 2024.   

Di seguito ecco le immagini riassuntive tratte dal bando con i periodi di erogazione:
""",
    'markup': quick_markup({
        'Prima rata per i primi anni':{
            'url': 'https://t.me/edisubotimmagini/8'
            },
        'Seconda rata per i primi anni': {
            'url': 'https://t.me/edisubotimmagini/9'
            }
        }, 1)
    },

    "Importi borse di studio":
    {'testo':f"""\
<b>Importi borse di studio</b>

Per gli studentз iscrittз a tempo pieno (full time), l'importo della borsa di studio dipende dal proprio ISEE \
ricalcolato dalla tipologia di borsa (in sede, pendolare, fuori sede)
""",
    'markup':quick_markup(
        {
            'In sede':{'url': 'https://t.me/edisubotimmagini/2'},
            'Pendolare':{'url': 'https://t.me/edisubotimmagini/3'},
            'Fuori sede':{'url': 'https://t.me/edisubotimmagini/4'},
            'Fuori sede ospite di residenza edisu':{'url': 'https://t.me/edisubotimmagini/5'}
            }, 1
        )},

    "Rimborso tassa regionale per il diritto allo studio":
    {'testo':"""\
Puoi chiedere il rimborso esclusivamente della quota della tassa regionale per il diritto allo studio universitario (€ 140,00), \
non invece gli eventuali importi aggiuntivi come le spese di bollo virtuale o altri oneri.
Gli studenti che hanno versato esclusivamente il MAV per l'importo di 16,00 € non devono compilare la richiesta di rimborso.

Tutti i dettagli nel bando nella sezione inerente il proprio anno o al sito https://www.edisu.piemonte.it/it/servizi/borse-di-studio-e-altri-contributi/tassa-regionale-il-diritto-allo-studio-universitario
"""
},

    "Allegato A2":
    {'testo':r"""
<a href='https://www.edisu.piemonte.it/sites/default/files/risorse/documentazione/Bandi_di_concorso/2023-2024/Allegato%20A2%20-%20Merito%20domanda%20standard%20iscrizione%20full-time.pdf'>Allegato A2 contenente i requisiti di merito per le domande standard di anni successivi, per i vari corsi di laurea</a>"""}
}