from html import escape
snip = {
    "Copertura al 100%": 
    """\
Negli ultimi 8 anni circa siamo riusciti ad ottenere la copertura totale delle borse.\
Anche quest'anno, come Alter.POLIS, CollettivaMente e Studenti Indipendenti, \
abbiamo chiesto garanzie alla Regione ed a parole ci è stato detto che l'intenzione è la copertura al 100%. \
La reale situazione sarà nota solo verso dicembre, con il numero di richieste e lo stanziamento effettivo dei fondi. \
Come sempre vigileremo sull'operato della Regione
""",
    "Differenza tra standard e conferma":
    """\
<b>Differenza tra domanda standard e domanda di conferma benefici per merito</b>

Se l'anno precedente hai ricevuto i benefici (posto letto e/o borsa), con la domanda di conferma ottieni \
sicuramente i benefici per cui fai richiesta (e che avevi già ricevuto). Hai la precedenza rispetto alla domanda standard.
Puoi fare domanda di conferma solo se hai il numero di crediti richiesto (per questo si chiama "per merito")
""",
    "Rinuncia al posto letto dopo le graduatorie definitive":
    """\
<b>Rinuncia al posto letto dopo le graduatorie definitive</b>

La rinuncia al posto letto successivamente alle graduatorie definitive può comportare la perdita \
della borsa di studio da fuori sede completa. Per maggiori dettagli leggi a pagina 23 del bando.

In sintesi, se rifiuti poiché assegnatariз nelle graduatorie definitive di servizio abitativo o negli \
esiti della dichiarazione di interesse, diventi in sede (ai fini dell'importo della borsa).

Per tutti gli altri casi, ti rimando alla pagina 23.
""",
    "CFU necessari durante l'anno per gli anni successivi":
    """\
<b>CFU necessari durante l'anno per gli anni successivi</b>

La borsa EDISU è destinata a coloro che rispettano i requisiti economici (cioè ISEE e ISP sotto una certa soglia) \
e i requisiti di merito (devono aver totalizzato un tot di CFU negli anni precedenti).

Per i primi anni non è naturalmente possibile valutare il merito essendo che lo studente non ha ancora sostenuto esami. \
Per cui lo studente deve ottenere 20 CFU entro il 10 agosto successivo per poter ottenere la seconda rata della borsa \
(o 20 CFU entro Novembre per non dover restituire la prima rata).

Questo discorso non si applica per gli anni successivi poichè per questi è possibile valutare il merito \
basandosi sugli anni precedenti. Per cui se al momento di fare domanda per anni successivi hai i CFU richiesti, \
risultando assegnatario hai diritto ad entrambe le rate della borsa.
""",
    "Elenco corsi STEM" :
    """\
<b> Elenco corsi STEM</b>

https://www.edisu.piemonte.it/sites/default/files/risorse/bandi/2022/ELENCO%20CORSI%20STEM.pdf
""",
    "Dichiarazione di domicilio a titolo oneroso":
    """\
<b>Dichiarazione di domicilio a titolo oneroso</b>

La dichiarazione di domicilio a titolo oneroso va fatta da tutti lз studentз fuori che NON sono ospiti \
delle residenze EDISU e non abbiano accettato (o dichiarato l'interesse) mediante Opzione Einaudi.
Serve per confermare lo status di fuori sede e va fatta tra il 28 Ottobre e il 5 Dicembre ore 12.00

Il contratto da caricare deve avere le caratteristiche indicate all'articolo 8 del bando.
""",
    "Procedura di rifiuto": 
    """\
<b>Procedura di rifiuto</b>
Se rifiuti via mail o senza fare il check in ottieni l'importo da "studente in sede" invece di quello da \
"fuorisede con supporto abitativo".
Se rifiuti facendo check in e poi check out (cosa che si può fare nello stesso giorno) ottieni l'importo da \
"studente pendolare" invece di quello da "fuorisede con supporto abitativo".

Per gli scambi mi raccomando di non PROPORRE né ACCETTARE scambi con dietro pagamenti in denaro od altra forma, \
sono ILLEGALI e possono farvi espellere da EDISU e rischiate una denuncia alla polizia postale, \
oltre che essere moralmente sbagliati e controproducenti visto che portano a meno scambi disponibili e a \
ledere il diritto allo studio universitario.
""",
    "Differenza tra locativo e diverso titolo oneroso":
    """\
Dichiarazione di domicilio a titolo locativo: hai una casa in affitto, e quindi contratto di locazione \
registrato presso l'agenzia delle entrate.

Dichiarazione di domicilio a diverso titolo oneroso: stai in collegio/convitto, non hai un contratto \
locativo e il contratto che fai con la struttura non viene registrato presso l'agenzia delle entrate. \
Possibilmente ogni volta che versi soldi ti viene pure dato uno scontrino/fattura/ricevuta fiscale.
""",
    "Date erogazione rate borsa di studio":
    """\
Prima rata: da fine dicembre
Seconda rata: da fine giugno

Seconda rata per i primi anni
20 cfu entro il 30 aprile e autocertificazione: da fine giugno
20 cfu entro il 10 agosto: da fine novembte
20 cfu entro il 30 novembre: mai, e non devi restituire la prima
20 cfu dopo il 30 novembre: mai e devi restituire la prima
""",
    "Importi borse di studio":
    f"""\
<b>Importi borse di studio</b>

<i>Studentз IN SEDE</i>
<code>
{escape("a. ISEE <= 11813 ----------> € 2705")}
{escape("b. 11813 < ISEE <= 15749 --> € 2332")}
{escape("c. 15749 < ISEE <= 23626 --> € 1836")}

Studentesse corsi STEM
{escape("d. ISEE <= 15749 ----------> € 2829")}
{escape("e. 15749 < ISEE <= 23626 --> € 2233")}
</code>

<i>Studentз PENDOLARз</i>
<code>
{escape("a. ISEE <= 11813 ----------> € 3989")}
{escape("b. 11813 < ISEE <= 15749 --> € 3449")}
{escape("c. 15749 < ISEE <= 23626 --> € 2729")}

Studentesse corsi STEM
{escape("d. ISEE <= 15749 ----------> € 4169")}
{escape("e. 15749 < ISEE <= 23626 --> € 3305")}
</code>

<i>Studentз FUORI SEDE</i>
<code>
{escape("a. ISEE <= 11813 ----------> € 6932")}
{escape("b. 11813 < ISEE <= 15749 --> € 6008")}
{escape("c. 15749 < ISEE <= 23626 --> € 4776")}

Studentesse corsi STEM
{escape("d. ISEE <= 15749 ----------> € 7240")}
{escape("e. 15749 < ISEE <= 23626 --> € 5761")}
</code>

<i>Studentз FUORI SEDE, assegnatari di servizio abitativo in residenza EDISU</i>
<code>
{escape("a. ISEE <= 11813 ----------> € 4232")}
{escape("b. 11813 < ISEE <= 15749 --> € 3308")}
{escape("c. 15749 < ISEE <= 23626 --> € 2076")}

Studentesse corsi STEM
{escape("d. ISEE <= 15749 ----------> € 4540")}
{escape("e. 15749 < ISEE <= 23626 --> € 3061")}
</code>

""",
    "Rimborso tassa regionale per il diritto allo studio":
    """\
Puoi chiedere il rimborso esclusivamente della quota della tassa regionale per il diritto allo studio universitario (€ 140,00), \
non invece gli eventuali importi aggiuntivi come le spese di bollo virtuale o altri oneri.
Gli studenti che hanno versato esclusivamente il MAV per l'importo di 16,00 € non devono compilare la richiesta di rimborso.

Tutti i dettagli nel bando nella sezione inerente il proprio anno o al sito https://www.edisu.piemonte.it/it/servizi/borse-di-studio-e-altri-contributi/tassa-regionale-il-diritto-allo-studio-universitario
"""
}