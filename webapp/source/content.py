bando = """
> Il progetto è parte del Operativo Regionale del Fondo Europeo di Sviluppo Regionale (POR FESR 2014 - 2020) del Veneto, nell'ambito del bando dell'azione 231 volto alla "costituzione di Innovation Lab diretti al consolidamento/sviluppo del network Centri P3@-Palestre Digitali e alla diffusione della cultura degli Open Data."
"""

body = dict(

viirs=dict(

meta_description="""
La web app che stima, sulla base di immagini satellitari notturne, l'inquinamento luminoso nei comuni italiani.
""",

fa_icon="fa fa-moon-o",

first_img="![Light pollution](static/img/light-pollution.jpg)",

second_img="![NASA - Immagine notturna dell'Italia](static/img/italy-night-200px.jpg)",

title="Inquinamento luminoso",

filler="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas ac erat in varius. Mauris blandit neque metus, nec mattis justo dapibus ut. Curabitur in nulla felis. Nam posuere fermentum mattis. Sed ut turpis sapien. Etiam sapien justo, feugiat at enim ut, venenatis elementum mauris. In hac habitasse platea dictumst. Duis vel tristique justo. Morbi erat nunc, viverra eget maximus eget, mollis sed felis. Nullam nibh lorem, porta at tellus vitae, condimentum convallis mauris. Maecenas nec neque vitae arcu blandit aliquet. Duis sodales ut turpis non aliquet. Mauris vitae tellus nulla. Vivamus malesuada aliquam tortor.
""",

intro1="""
L'**inquinamento luminoso** è l'alterazione dei livelli di illuminazione naturale notturna causata da fonti di luce antropiche. I livelli di illuminazione naturale sono regolati da fonti naturali celesti: la luna, le emissioni atmosferiche naturali (Airglow), le stelle,  la Via Lattea e la luce zodiacale. La luce artificiale sparsa nell'atmosfera rilancia la luminanza del cielo notturno e colpisce anche i siti incontaminati: è facilmente osservabile durante la notte a centinaia di chilometri dalla sua fonte. Oltre a ostacolare le osservazioni astronomiche, la luminosità artificiale del cielo notturno rappresenta una profonda alterazione di un'esperienza umana fondamentale - l'opportunità per ogni persona di vedere e riflettere il cielo notturno. Inoltre, l'inquinamento luminoso causa conseguenze ecologiche globali, causando  problemi di salute pubblica e sprechi di energia e denaro (1).
""",

intro2="""
I satelliti di osservazione della Terra consentono il monitoraggio del pianeta durante la notte. Stime dell'Associazione Internazionale Dark-Sky, basata sul lavoro da immagini satellitari, mostrano che le città fanno "brillare" inutilmente miliardi di dollari direttamente nel cielo ogni anno (2). I satelliti sono in grado di dimostrare il crescente inquinamento luminoso artificiale, lo sviluppo di nuove fonti di illuminazione (come LED), e la continua crescita in estensione e radianza delle aree artificialmente illuminate (3). I grafici qui sotto sono basati sull'analisi delle immagini satellitari americane Suimi-NPP (4) e ci aiutano a capire, in modo quantitativo, come il problema dell'inquinamento luminoso tocca il territorio vicentino e oltre. I grafici mettono diversi comuni a confronto, mostrando la quantità di luce irradiata nel cielo.
""",

interp="""
- Ogni grafico mostra i singoli comuni come "bolle". Le loro dimensioni dipendono proporzionalmente dalla popolazione. Ad esempio, la "bolla" di Vicenza è più grande di quella di Creazzo.
- Sull'asse X, ci sono i valori medi di quanta luce è stata emessa nel cielo sopra il territorio di un singolo comune, come misurato dal satellite. Sono espressi in *nanowatt diviso per centimetro quadrato per steradiante*. Maggiore è il valore X, maggiore è l'inquinamento luminoso medio. I valori X più grandi di 10 corrispondono  ad un alto livello di inquinamento del cielo. In queste condizioni le persone non sperimentano mai una vera notte, in quanto è mascherata da un crepuscolo artificiale.
- Sull'asse Y, c'è una deviazione standard (STD), che mostra la dispersione della quantità di luce all'interno di un comune. Una bassa STD indica che i valori tendono ad essere vicini alla media, mentre una STD elevata indica che i valori sono distribuiti su un range più ampio.
- Ad esempio, rispetto ad altri comuni della provincia di Vicenza, Rossano Veneto ha una MEDIA elevata con una bassa STD, il che significa che l'intero territorio del comune è illuminato in un modo uniformemente alto. Diversamente il comune di Vicenza ha sia un'elevata MEDIA sia un'alta STD, il che significa che la parte centrale di Vicenza è altamente illuminata, mentre la zona periferica più scura.
- Su ogni grafico, i comuni di interesse sono provvisti di nominativo e sono evidenziati nel colore giallo. Per vedere le informazioni basta porre il cursore del mouse su una "bolla".
""",

comment1="",
comment2="",
comment3="",

workflow="""
Per creare questi grafici abbiamo usato la seguente metodologia:

1. Il territorio di ogni comune è definito dal dataset dei limiti amministrativi pubblicato dall'Istat (5).
2. Le immagini satellitari notturne **VIIRS** (4) vengono ottenute ed elaborate nella piattaforma Big Data che si chiama [Google Earth Engine](https://earthengine.google.com/).
3. Incrociando le immagini notturne con i limiti amministrativi, per ogni territorio comunale vengono calcolate le *statistiche zonali* tramite il software libero [QGIS](https://www.qgis.org/): i caratteri come *media*, *mediana*, *deviazione standard*, *min* e *max* che descrivono i valori estratti dalle immagini e rilevanti solo per questo comune.
4. Ottenute le statistiche, possiamo tracciare i grafici. Per semplificare la rappresentanza del fenomeno dell'inquinamento luminoso abbiamo scelto i caratteri *media* e *deviazione standard*.
""",

refs="""
1. Falchi, Fabio, Pierantonio Cinzano, Dan Duriscoe, Christopher C.M. Kyba, Christopher D. Elvidge, Kimberly Baugh, Boris A. Portnov, Nataliya A. Rybnikova, and Riccardo Furgoni. 2016. “The New World Atlas of Artificial Night Sky Brightness.” Science Advances 2 (6): 1–26. [doi:10.1126/sciadv.1600377](https://doi.org/10.1126/sciadv.1600377).
2. Smith, Malcolm. 2009. “Time to Turn off the Lights.” Nature 457 (7225): 27–27. [doi:10.1038/457027a](https://doi.org/10.1038/457027a).
3. Levin, Noam, Christopher C.M. Kyba, Qingling Zhang, Alejandro Sánchez de Miguel, Miguel O. Román, Xi Li, Boris A. Portnov, et al. 2020. “Remote  Sensing of Night Lights: A Review and an Outlook for the Future.” Remote Sensing of Environment 237 (September 2019). [doi:10.1016/j.rse.2019.111443](https://doi.org/10.1016/j.rse.2019.111443).
4. Le immagini notturne della Terra di pubblico dominio "VIIRS Stray Light Corrected Nighttime Day/Night Band Composites Version 1", ottenute e elaborate tramite [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG).
5. Istat. Limiti amministrativi di tutti i comuni italiani: https://www.istat.it/it/archivio/222527
""",

credits="""
- La web app è sviluppata con Python Dash, un Framework per la creazione di applicazioni analitiche Web.
- Icone realizzate da [Freepik](https://www.freepik.com) da [www.flaticon.com](https://www.flaticon.com/).
- Foto dell'inquinamento luminoso: [Yan Yu Chen](https://www.flickr.com/photos/darkyanyu/5505836856/), licenza [CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/)
"""

),

pvout=dict(
fa_icon="fa fa-solar-panel",
meta_description="""
La web app che compare i comuni italiani per il suo potenziale fotovoltaico.
""",

first_img="![Panelli fotovoltaici su un tetto](static/img/vicenza-fotovoltaici-capannone-300px.png)",

second_img="",

title="Potenziale del fotovoltaico",

filler="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas ac erat in varius. Mauris blandit neque metus, nec mattis justo dapibus ut. Curabitur in nulla felis. Nam posuere fermentum mattis. Sed ut turpis sapien. Etiam sapien justo, feugiat at enim ut, venenatis elementum mauris. In hac habitasse platea dictumst. Duis vel tristique justo. Morbi erat nunc, viverra eget maximus eget, mollis sed felis. Nullam nibh lorem, porta at tellus vitae, condimentum convallis mauris. Maecenas nec neque vitae arcu blandit aliquet. Duis sodales ut turpis non aliquet. Mauris vitae tellus nulla. Vivamus malesuada aliquam tortor.
""",

intro1="""
Il sole è la maggiore fonte al mondo di energia rinnovabile. Per più di mezzo secolo, gli scienziati hanno provato innumerevoli opzioni e metodi di ottenimento e utilizzo dell'energia solare. Inizialmente le tecnologie sono state costose e inefficaci. Però non avendo mai smesso di migliorare nel corso degli anni, oggi hanno portato a sviluppi attraenti ed economici.
""",

intro2="""
I grafici qui sotto sono realizzati sui dati World Bank del **potenziale di energia solare** (1). Sono utili per comprendere il potenziale teorico e pratico dell'energia solare per i paesi e le regioni, incluso il territorio vicentino. I grafici mettono diversi comuni a confronto, mostrando l'output elettrico fotovoltaico.
""",

interp="""
- Ogni grafico mostra i singoli comuni come "bolle". Le loro dimensioni dipendono proporzionalmente dalla popolazione. Ad esempio, la "bolla" di Vicenza è più grande di quella di Creazzo.
- Sull'asse X, ci sono i valori medi di quanta energia può essere prodotta in un anno dal territorio di un singolo comune. Sono espressi in *Kilowatt diviso per ora annui*. Maggiore è il valore X, maggiore è il potenziale di energia.
- Sull'asse Y, c'è una deviazione standard (STD), che mostra la dispersione della quantità di energia producibile all'interno di un comune. Una bassa STD indica che i valori tendono ad essere vicini alla media, mentre una STD elevata indica che i valori sono distribuiti su un range più ampio.
- Ad esempio, rispetto ad altri comuni della provincia di Vicenza, Lastebasse ha una MEDIA bassa però un'alta STD, il che significa che l'intero territorio del comune è illuminato dal sole in un modo non uniforme, a causa della sua posizione tra le montagne. Al contrario, il comune di Vicenza e i comuni contermini hanno elevate MEDIE e basse STD, il che significa che il territorio è adatto alla produzione dell'energia solare.
- Su ogni grafico, i comuni di interesse sono provvisti di nominativo e sono evidenziati nel colore giallo. Per vedere le informazioni basta porre il cursore del mouse su una "bolla".
""",

comment1="",
comment2="*Nota bene: nel grafico sopra, il valore della deviazione standard per il comune di Livorno non è attendibile a causa di un'anomalia nei dati satellitari.*",
comment3="",

workflow="""
Per creare questi grafici abbiamo usato la seguente metodologia:

1. Il territorio di ogni comune è definito dal dataset dei limiti amministrativi pubblicato dall'Istat (2).
2. Incrociamo i dati del potenziale del fotovoltaico (2) con i limiti amministrativi. Per ogni territorio comunale vengono calcolate *statistiche zonali* tramite il software libero [QGIS](https://www.qgis.org/): *media*, *mediana*, *deviazione standard*, *min* e *max* che descrivono i valori estratti dal dataset fotovoltaico sottostente e rilevante solo per questo comune.
3. Ottenute le statistiche possiamo tracciare i grafici. Per semplificare la rappresentanza del potenziale fotovoltaico scegliamo i caratteri *media* e *deviazione standard*.
""",

refs="""
1. I dati del potenziale solare fotovoltaico annuo, licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). *I dati ottenuti dalla Global Solar ATLAS 2.0, una Web App gratuita, sviluppata e gestita dalla società SolarGis s.r.o. a nome del Gruppo della Banca mondiale, utilizzando i dati di Solargis, con finanziamenti forniti dal programma di assistenza per il settore dell'energia (ESMAP). Per ulteriori informazioni: https://globalsolaratlas.info*
2. Istat. Limiti amministrativi di tutti i comuni italiani: https://www.istat.it/it/archivio/222527
""",

credits="""
- La web app è sviluppata con Python Dash, un Framework per la creazione di applicazioni analitiche Web.
- Icone realizzate da [Freepik](https://www.freepik.com) da [www.flaticon.com](https://www.flaticon.com/).
"""

),

ghm=dict(

fa_icon="fa fa-globe-europe",

meta_description="""
La web app che stima il livello della **pressione antropica* in comuni italiani.
""",

first_img="![Vista di VIcenza dall'alto](static/img/vicenza-300px.jpg)",

second_img="![Tre Cime di Lavaredo](static/img/mountains-300px.jpg)",

title="Pressione antropica",

filler="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas ac erat in varius. Mauris blandit neque metus, nec mattis justo dapibus ut. Curabitur in nulla felis. Nam posuere fermentum mattis. Sed ut turpis sapien. Etiam sapien justo, feugiat at enim ut, venenatis elementum mauris. In hac habitasse platea dictumst. Duis vel tristique justo. Morbi erat nunc, viverra eget maximus eget, mollis sed felis. Nullam nibh lorem, porta at tellus vitae, condimentum convallis mauris. Maecenas nec neque vitae arcu blandit aliquet. Duis sodales ut turpis non aliquet. Mauris vitae tellus nulla. Vivamus malesuada aliquam tortor.
""",

intro1="""
 La **pressione antropica**, o **antropizzazione**, è l'opera di trasformazione dell'ambiente naturale attuata dall'uomo per soddisfare le proprie esigenze e migliorare la qualità della vita, spesso, però, a scapito dell'equilibrio ecologico (1). Gli umani hanno drammaticamente trasformato la biosfera terrestre, riducendo la biodiversità globale e la stabilità degli ecosistemi. Il problema di antropizzazione è estremamente attuale nel momento in qui si tratta dell'Italia e della pianura Padano-veneta in particolare. Un numero crescente di iniziative internazionali mira a riconciliare lo sviluppo con la conservazione della natura. Il nodo cruciale per il successo di queste iniziative è una completa comprensione dell'attuale condizione ecologica dei terreni e delle loro distribuzioni spaziali (2).
""",

intro2="""
I grafici qui sotto sono realizzati sui dati *Global Human Modification Index* (gHM), che forniscono una misura cumulativa della modifica umana di terreni. Questa misura è basata sulla modellazione delle estensioni fisiche di 13 stressanti antropogeni e dei loro impatti stimati (3). I grafici mettono i diversi comuni italiani, incluso il territorio vicentino, a confronto, mostrando il livello della pressione antropica.
""",

interp="""
- Ogni grafico mostra i singoli comuni come "bolle". Le loro dimensioni dipendono proporzionalmente dalla popolazione. Ad esempio, la "bolla" di Vicenza è più grande di quella di Creazzo.
- I valori dell'indice gHM variano da `0,0` a `1,0`, dove `1` corrisponde al massimo livello del cambiamento.
- Sull'asse X è rappresentata la media (MEDIA) dell'indice gHM per ogni singolo comune.
- Sull'asse Y, c'è una deviazione standard (STD), che mostra la dispersione dell'indice gHM all'interno di un comune. Una bassa STD indica che i valori tendono ad essere vicini alla media, mentre una STD elevata indica che i valori sono distribuiti su un range più ampio.
- Ad esempio, rispetto ad altri comuni della provincia di Vicenza, Asiago ha una MEDIA bassa però un'alta STD, il che significa che nonostante l'intero territorio del comune è generalmente poco modificato, esista una differenza tra la parte abitata e le periferie. Al contrario, il comune di Vicenza ha un'elevata MEDIA e una bassa STD, il che significa che l'intero territorio è altamente modificato con poche variazioni.
- Su ogni grafico, i comuni di interesse sono provvisti di nominativo e sono evidenziati nel colore giallo. Per vedere le informazioni basta porre il cursore del mouse su una "bolla".
""",

comment1="",
comment2="",
comment3="",

workflow="""
Per creare questi grafici abbiamo usato la seguente metodologia:

1. Il territorio di ogni comune è definito dal dataset dei limiti amministrativi pubblicato dall'Istat (4).
2. I dati  **gHMI** (3) vengono ottenuti ed elaborati nella piattaforma Big Data che si chiama [Google Earth Engine](https://earthengine.google.com/).
3. Incrociando i dati gHMI con i limiti amministrativi, per ogni territorio comunale vengono calcolate le *statistiche zonali* tramite il software libero [QGIS](https://www.qgis.org/): *media*, *mediana*, *deviazione standard*, *min* e *max* che descrivono i valori estratti dalle immagini e rilevanti solo per questo comune.
4. Ottenute le statistiche, possiamo tracciare i grafici. Per semplificare la rappresentanza del fenomeno della pressione antropica usiamo i caratteri *media* e *deviazione standard*.
""",

refs="""
1. [Dizionario di italiano Sabatini Coletti - antropizzazione](https://dizionari.corriere.it/dizionario_italiano/A/antropizzazione.shtml)
2. *Kennedy, C.M., J.R. Oakleaf, D.M. Theobald, S. Baurch-Murdo, and J. Kiesecker. 2019. Managing the middle: A shift in conservation priorities based on the global human modification gradient. Global Change Biology 00:1-16. https://doi.org/10.1111/gcb.14549.*
3. Global Human Modification Index (gHM) o l'indice della pressione antropica che fornisce una misura cumulativa della modifica umana delle terre a livello di risoluzione di 1 km². I valori gHM variano da `0,0` a `1,0` e sono calcolati stimando la proporzione di una determinata posizione (pixel) che viene modificata. Licenza [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Ottenuto tramite [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/CSP_HM_GlobalHumanModification).
4. Istat. Limiti amministrativi di tutti i comuni italiani: https://www.istat.it/it/archivio/222527
""",

credits="""
- La web app è sviluppata con Python Dash, un Framework per la creazione di applicazioni analitiche Web.
- Icone realizzate da [Freepik](https://www.freepik.com) da [www.flaticon.com](https://www.flaticon.com/).
- Foto "Vedute aeree di Vicenza": [Comune di Vicenza](https://www.flickr.com/photos/comunedivicenza/6115937240/in/album-72157627306867866/), tutti i diritti riservati.
"""
)

)
