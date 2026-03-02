# Klimamodeller
![Modelering](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/forside.png)
## Innledning

Energibalansemodeller representerer en sentral og klassisk tilnærming innen klimafysikk. De bygger på fundamentale fysiske lover, særlig strålingsfysikk og Stefan–Boltzmanns lov, og gir en matematisk beskrivelse av hvordan jorden oppnår en likevekt mellom absorbert og utstrålt energi. Til tross for at modellene er sterkt forenklede – ved at jorden behandles som et svart legeme og komplekse prosesser i atmosfære, hav og biosfære utelates – gir de viktig innsikt i de grunnleggende mekanismene bak drivhuseffekten og klimafølsomhet.

Oppgaven vil kombinere matematisk modellering med klimafaglig drøfting. Vi vil undersøke hvordan endringer i sentrale parametere, som albedo og effektiv emissivitet, påvirker systemets likevekt, og diskutere hvilke styrker og begrensninger som ligger i denne typen modeller. På denne måten søker vi å belyse hvordan enkle matematiske strukturer kan bidra til forståelsen av komplekse klimaprosesser.

Oppgaven innledes med en svært forenklet klimamodell, der jorden behandles som et svart legeme og kun den grunnleggende energibalansen mellom innkommende og utgående stråling analyseres. Deretter utvides modellen trinnvis ved først å inkludere albedoeffekten, som beskriver hvor stor andel av solstrålingen som reflekteres tilbake til verdensrommet. Til slutt innarbeides drivhuseffekten, som tar hensyn til atmosfærens evne til å absorbere og reemittere infrarød stråling.

Oppgaven tar utgangspunkt i notatet [Flath & Co: "Energy Balance Models"](https://www.uio.no/studier/emner/matnat/math/MAT1020/v26/mat1020flatharticle.pdf). 

## Oppbyggning av  oppgaven

Dette prosjektet er organisert i tre undermapper på GitHub.

#### Utlede likningene for energibalansen
I den første delen utleder vi likningene for energibalansen. Forklaring og tilhørende kode finnes i mappen 
[Utlede_likningene](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/Utlede_likningene). Her antar vi at alle parametere er konstante. Dette gir den mest grunnleggende modellen for å beregne jordens likevektstemperatur.

#### Modelering temperaturendringene som en differensiallikning

I del to av prosjektet studerer vi temperaturutviklingen over tid ved å betrakte den som proporsjonal med energiubalansen i systemet. Dersom jorden mottar mer energi enn den stråler ut, vil temperaturen øke, og dersom den stråler ut mer enn den mottar, vil temperaturen synke. Vi antar derfor at temperaturendringen er proporsjonal med differansen mellom innkommende og utgående stråling. Dette leder naturlig til en differensiallikning som beskriver hvordan temperaturen endrer seg over tid. Dette finnes i mappen [Modelering](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/Modelering) ser vi på hva som skjer når vi varierer mengden drivhusgasser i atmosfæren, der vi modelerer temperaturendrignene ved  differensiallikninger. 


#### La parametrene albedo $\alpha$ og drivhusgasser $\epsilon$ variere
I tredje del av prosjektet, i mappen [Variere_albedoen](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/Variere_albedoen)

I del tre av prosjektet utvider vi modellen ytterligere ved å la både albedoen og andelen drivhusgasser variere. Albedo $\alpha$ er et mål på hvor stor andel av den innkommende solstrålingen som reflekteres tilbake til verdensrommet. Når albedoen endres, påvirker det dermed energibalansen direkte. I denne delen undersøker vi hvordan temperaturutviklingen påvirkes når både drivhuseffekten og refleksjonsevnen til jorden får variere, noe som gir en mer dynamisk og realistisk klimamodell.