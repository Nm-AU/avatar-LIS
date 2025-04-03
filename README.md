# Avatar 3D per Lingua dei Segni Italiana (LIS)
## Tecnologie utilizzate e riferimenti
* Riferimento segni LIS: progetto [Spread the Sign](https://spreadthesign.com/it.it/search/), gestito dall'associazione no-profit [European Sign Language Center](https://www.signlanguage.eu/en/)
* Per creazione segni: [HamNoSys](https://www.sign-lang.uni-hamburg.de/dgs-korpus/hamnosys-97.html) e lo [strumento HamNoSys Palette](https://www.fdr.uni-hamburg.de/record/9725#.YgKI8hNKhpI)
* Rappresentazione segni in formato machien readable: [SigML](https://vh.cmp.uea.ac.uk/index.php/SiGML)
* Per traduzione da HamNoSys a  SigML: [strumento HamNoSys2SigML](https://github.com/carolNeves/HamNoSys2SiGML)
* Per animazione Avatar 3D: Librerie [CWASA](https://vh.cmp.uea.ac.uk/index.php/CWASA_Release_Notes)

## Descrizione
L'applicazione è stata sviluppata a partire dalle librerie fornite da CWASA e modificata in base alle esigenze. L'Avatar 3D viene animato a partire dalla rappresentazione.
### Struttura
```
.
|__ pagina web avatar e librerie CWASA
|
|__hamnosys (Rappresentazione in HamNoSys dei segni)
|   
|__sigml (Rappresentazione in SigML dei segni)
|
|__demo (file sigml di prova per animazione Avatar)
```
## Istruzioni per l'uso
È necessaria l'installazione di Python e di un browser per poter visualizzare e interagire con la webapp.
Per poter creare i Segni tramite notazione HamNoSys è possibile utilizzare lo strumento [strumento HamNoSys Palette](https://www.fdr.uni-hamburg.de/record/9725#.YgKI8hNKhpI). Qualora si volesse evitare l'applicativo per la creazione dei segni, è disponibile anche un font, ma questo è rilasciato solo per sistema operativo MacOS.

Per la traduzione da notazione HamNoSys a SigML è necessario installare lo strumento [HamNoSys2SigML](https://github.com/carolNeves/HamNoSys2SiGML)
Viene fornito un scritp python (create_sigml.py) che può essere utilizzato per concatenare diversi segni. Lo script legge un file in input contenente le parole che si volgiono concatenare, e.g., per creare un frase; va a cercarle nella cartella contenente i segni in HamNoSys; concatena tutte le rappresentazioni e le trasforma in notazione SigML richiamando lo script HamNoSys2SigML.

Per far partire l'avatar basterà, una volta scaricato il repository, entrare nella directory principale e eseguire il seguente comando:
```bash
python -m server.http 8000
```
Dopo di che collegarsi, da un browser, all'indirizzo 
```
http://localhost:8000
```
L'applicazione di default leggerà il conentuo del file demo/demo.sigml per l'animazione.