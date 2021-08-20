# VicenzaInnovationLab: Earth Observation Web App

![logo InnovationLab Vicenza](webapp/static/img/logo-innovationlab.png)

Questo repository contiene il codice Python necessario per l'elaborazione dei dati e per generare tre Web App. È dedicato all'utilizzo dei dati aperti Earth Observation nel territorio vicentino e racchiude tre time:

1. [Inquinamento luminoso](http://dash-multipage.eu-south-1.elasticbeanstalk.com/inquinamento-luminoso)
2. [Potenziale del fotovoltaico](http://dash-multipage.eu-south-1.elasticbeanstalk.com/fotovoltaico)
3. [Pressione antropica](http://dash-multipage.eu-south-1.elasticbeanstalk.com/pressione-antropica)

> Il progetto è parte del Programma Operativo Regionale del Fondo Europeo di Sviluppo Regionale (POR FESR 2014 - 2020) del Veneto, nell'ambito del bando dell'azione 231 volto alla "costituzione di Innovation Lab diretti al consolidamento/sviluppo del network Centri P3@-Palestre Digitali e alla diffusione della cultura degli Open Data."

![logo of participants](webapp/static/img/logos.png)

## Sommario

- [Metodologia](#metodologia)
- [Struttura del repository](#struttura-del-repository)
- [Uso](#uso)
- [Contatti](#contatti)
- [Licenza](#licenza)

## Metodologia

Le web app sono sviluppate con Python Dash, un Framework per la creazione di applicazioni analitiche Web. Per creare queste app con i grafici interattivi abbiamo usato la seguente metodologia:

1. Il territorio di ogni comune è definito dal dataset dei limiti amministrativi pubblicato dall'Istat.
2. I dati satellitari vengono ottenute ed elaborate nella piattaforma Big Data che si chiama Google Earth Engine.
3. Incrociando i dati satellitari con i limiti amministrativi, per ogni territorio comunale vengono calcolate le statistiche zonali tramite il software libero QGIS: i caratteri come media, mediana, deviazione standard, min e max che descrivono i valori estratti dalle immagini e rilevanti solo per questo comune.
4. Ottenute le statistiche, possiamo tracciare i grafici. Per semplificare la rappresentanza dei fenomeni abbiamo scelto i caratteri media e deviazione standard.

## Struttura del repository

* `/data`
  * `/input`
    * `ghm.tif` - gHM (Global Human Modification Index) o l'indice della pressione antropica che fornisce una misura cumulativa della modifica umana delle terre a livello di risoluzione di 1 km<sup>2</sup>. I valori gHM variano da `0,0` a `1,0` e sono calcolati stimando la proporzione di una determinata posizione (pixel) che viene modificata. Licenza [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Ottenuto tramite [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/CSP_HM_GlobalHumanModification). Attributo: *Kennedy, C.M., J.R. Oakleaf, D.M. Theobald, S. Baurch-Murdo, and J. Kiesecker. 2019. Managing the middle: A shift in conservation priorities based on the global human modification gradient. Global Change Biology 00:1-16. https://doi.org/10.1111/gcb.14549.*
    * `istat_codici_prov.csv` - Codici statistici e denominazioni delle ripartizioni sovracomunali dall'Istat. L'encoding è stato convertito in UTF-8. Ottenuto tramite https://www.istat.it/it/archivio/6789
    * `istat_comuni2021.zip` - archivio ZIP che contiene uno Shapefile dall'Istat di limiti amministrativi di tutti i comuni italiani, riproiettati in EPSG:4326 con una correzione di geometrie corrotte. L'encoding è stato convertito in UTF-8. Fonte: https://www.istat.it/it/archivio/222527
    * `istat_pop2019.csv` - i dati Istat del censimento della popolazione 2019. L'encoding è stato convertito in UTF-8. Ottenuto tramite http://dati-censimentipermanenti.istat.it.
    * `pvout.tif` - potenziale solare fotovoltaico annuo, **kWh/m<sup>2</sup>**. Licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attributo: *I dati ottenuti dalla Global Solar ATLAS 2.0, una Web App gratuita, sviluppata e gestita dalla società SolarGis s.r.o. a nome del Gruppo della Banca mondiale, utilizzando i dati di Solargis, con finanziamenti forniti dal programma di assistenza per il settore dell'energia (ESMAP). Per ulteriori informazioni: https://globalsolaratlas.info*
    * `viirs.tif` - immagine composita di radianza mediana annua, **nW/(cm<sup>2</sup>×sr)**, creata dai dati dell'osservazione notturna della Terra **VIIRS Stray Light Corrected Nighttime Day/Night Band Composites Version 1** tramite [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG).
    * `worldpop.tif` - WorldPop Global Project Population Data: popolazione residenziale stimata per 2020 su una grigliata di 100x100 m. Licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attributo: www.worldpop.org
* `processing`
  * `vector_prep.py` - crea un nuovo dataset georeferenziato `data/output/istat_com_pop.json` che contiene le colonne necessarie come i nomi di comuni, popolazione, ecc.
  * `raster_stats.py` - calcola le statistiche zonali su raster tematici d'input. 
* `webapp` - contiene i file pronti per essere installati su un server web. Il file principale è `webapp/application.py`.

## Uso

Abbiamo usato Windows per questo sviluppo, quindi l'istruzione è valida per questo sistema. Però funziona anche su Linux e Mac.

Il repositorio consiste da due distinte parti. La prima è la web app (HTML, CSS e JS). La seconda è lo script in Python per aggiornarla. Abbiamo testato questo con Python 3.8, ma funzionano anche le versioni non inferiori a 3.6.

1. Prima di tutto installa **Microsoft Visual C++** 14.0 (o maggiore). Scaricalo con lo strumento ["Microsoft C++ Build Tools"](https://visualstudio.microsoft.com/visual-cpp-build-tools/). 
   
2. Bisogna installare le seguenti librerie in ordine. Puoi usare la cartella ` processing/depenencies` che contiene i file necessari (Python Wheels) compatibili con la versione specifica del Python e architettura dell'OS: in questo caso è Windows x64, Python 3.7 o Python 3.8. Altrimenti scarica i Wheel dall'[Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

```
pip install processing\dependencies\GDAL-3.2.2-cp39-cp39-win_amd64.whl
pip install processing\dependencies\pyproj-3.0.1-cp39-cp39-win_amd64.whl
pip install processing\dependencies\Fiona-1.8.18-cp39-cp39-win_amd64.whl
pip install processing\dependencies\Shapely-1.7.1-cp39-cp39-win_amd64.whl
pip install processing\dependencies\geopandas-0.9.0-py3-none-any.whl
pip install processing\dependencies\Rtree-0.9.7-cp39-cp39-win_amd64.whl
pip install processing\dependencies\rasterio-1.2.1-cp39-cp39-win_amd64.whl
   
pip install requests rasterstats
```

L'ultima libreria viene installata dall'internet, dunque non si specifica nessun file.

### Aggiustamenti manuali

Si possono aggiornare i dataset vettoriali, usati dalle Web App, con i script dalla cartella `processing`. Ad es., se cambiano coordinate dei confini amministrativi di comuni.

## Contatti

- Sito
  aziendale: [VicenzaInnovationLab](https://https://www.comune.vicenza.it/uffici/cms/innovationlabvicenza.php/)
- Sviluppatore: [Yaroslav Vasyunin](https://www.linkedin.com/in/vasyunin)
- Project
  Link: [https://github.com/VicenzaInnovationLab/innovationlab-3webapps](https://github.com/VicenzaInnovationLab/innovationlab-3webapps)

## Licenza

Questo progetto è concesso in licenza sotto la GNU GPL versione 3: vedi il file [LICENSE](LICENSE) per dettagli. Per quanto riguarda le licenze dei dati, vedi la sezione [Struttura del ripositorio](#struttura-del-ripositorio).
