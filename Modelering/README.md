
# Mot en varmere normaltilstand
## Behovet for en dynamisk modell

I første del av oppgaven analyserte vi temperaturer under betingelsen $E_{\text{inn}}$ = $E_{\text{ut}}$ , altså situasjoner med termisk likevekt. Vi undersøkte da hvilken temperatur som oppstår når den innkommende og utgående energien er i balanse. 
Når vi nå videreutvikler modellen, ser vi på hva som skjer dersom $E_{\text{inn}}$ $\neq$ $E_{\text{ut}}$. 


Dersom $E_{\text{inn}}$  > $E_{\text{ut}}$ , mottar jorden mer energi enn den stråler ut, og temperaturen vil derfor øke. Tilsvarende vil temperaturen synke dersom $E_{\text{inn}}$  > $E_{\text{ut}}$ , fordi systemet da taper energi. 

Dette leder til videre spørsmål: Vil temperaturen fortsette å øke (eller avta) så lenge ubalansen består, eller vil den etter hvert stabilisere seg på et nytt nivå? Hva representerer egentlig forskjellen 
 $E_{\text{inn}}$  - $E_{\text{ut}}$ ? Og hvor raskt vil temperaturen endre seg når det oppstår en slik ubalanse? 
 
 For å kunne besvare disse spørsmålene er det ikke tilstrekkelig med en ren likevektsbetraktning; vi trenger en mer avansert, dynamisk modell som beskriver hvordan temperaturen utvikler seg over tid.

### En dynamisk modell.

Den enkleste formen for en dynamisk modell for temperaturendringene, er at temperaturendringen er proposjonal med energi-ubalansen. Dette gir følgene utrykk for endringen i temperaturen $T$ over tiden $t$

$$\frac{dT}{dt} = k (E_{\text{inn}} -E_{\text{ut}})$$

Vi bruker utrykkene for $E_{\text{inn}}$ og $E_{\text{ut}}$ vi utledet i første del av oppgaven. For å gjøre utrykket enklere å jobbe med, setter vi parametern Q = $\frac{1}{4} S$ , samt dividerer hele utrykket på $\pi$ $R^{2}$. Dette gir følgene $temperature$ $evolution$ $equation$, eller temperaturutviklingslikning, i mangel på et bedre norsk ord. 

$$C\frac{dT}{dt} = (1-\alpha) Q - \epsilon \sigma T^{4}.$$

Dette gjenkjenner vi som en  ordinary differential equation (ODE), der temperaturen $T$ er en funksjon av tiden $t$. Konstanten $C$ er Jordas varmekapasitet, som knytter tempeaturen til energitettheten. Konstanten C måles i Joule per Kelvin $\frac{J}{K}$
### Dagens nivå for klimagasser i atmosfæren
#### $\epsilon$ = 0.6
![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/dT_dt1.png)

I scriptet 
[modelering_av_differensiallikningen.py](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/Modelering/modelering_av_differensiallikningen.py) modelerer vi plottet vist ovenfor, med en $\epsilon$ = 0.60. Den vertikale aksen viser hastigheten som temperaturen endrer seg med, altså $\frac{dT}{dt}$ . Den angir hvor raskt jordens temperatur øker eller synker som følge av en energiu-balanse.

Vi observerer også det stjernemerkede punktet, som markerer nullpunktet til $f(T)$, altså når endringen i temperaturen er lik 0. Dette er likevektstemperaturen, der den innkommende og utgående energien balanserer hverandre (det vi i tidligere oppgaver så på som termisk likevekt, der $E_{inn}$ = $E_{ut}$ . Verdien tilsvarer den samme løsningen som tidligere i oppgaven, T = 288 K, og representerer jordens nåværende klimastatus. 

Av figuren ser vi at $f(T)$ er negativ når temperaturen (K) er høyere enn 288 K.
Dermed vil temperaturendringen ($\frac{dT}{dt}$)være negativ, så tempeaturen vil avta mot likevekten på 288 K. Tilsvarende ser vi at ved lavere tempeaturer enn 288 K, vil $\frac{dT}{dt}$ være positiv, så tempraturen vil øke, til den stabiliserer seg på 288 K. 


### Endring i nivået for klimagasser i atmosfæren
#### $\epsilon$ = 0.5

![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/to_verdier_for_epsilon.png)


Dersom vi reduserer verdien til parameteren epsilon $\epsilon$ , ved å øke nivået av klimagasser i atmosfæren vil vi få et nytt utrykk for $f(T)$. I [ulike_verdier_for_epsilon.py](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/Modelering/ulike_verdier_for_epsilon.py) reduserer vi verdiene til $\epsilon$ = 0.5. 

Differensiallikningen $f(T)$, som beskriver temperaturendringen $\frac{dT}{dt}$ som en funksjon av tempeaturen $T$, gir oss: 

$$f(T) = C\frac{dT}{dt} = (1-\alpha) Q - \epsilon \sigma T^{4}.$$

Vi ser at dersom vi øker andelen drivhusgasser i atmosfæren (og dermed resuserer paramteren $\epsilon$, alt annet likt, vil funksjonsverdiene $f(T)$ bli høyere for alle temperaturer $T$. Dette kommer frem i plottet nedenfor, som ligger høyere opp i diagrammet for alle temperaturer $T$. 


Når vi reduserer parameteren $\epsilon$ , modellerer vi en sterkere drivhuseffekt. Det betyr at atmosfæren slipper ut mindre varmestråling, og jorda mister energi saktere enn før. Resultatet er at systemet får et positivt energioverskudd ved den gamle likevektstemperaturen.

Energibalansen vil derfor jobbe mot en høyere likevektstemperatur. Så lenge innstrålt energi er større enn utstrålt energi (altså $f(T)$ > 0), vil temperaturen fortsette å øke. Temperaturen stiger helt til utstrålingen igjen er stor nok til å balansere innstrålingen. Først da får vi en ny likevekt der $f(T)$ = 0, eller $E_{inn}$ = $E_{ut}$

I dette tilfellet skjer det ved omtrent 303 K (30 °C). Det betyr at systemet fortsatt søker mot balanse, men balansepunktet er forskjøvet til et høyere temperaturnivå. 
### Med andre ord: klimaet stabiliserer seg rundt en varmere normaltilstand.