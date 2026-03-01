# Klimamodeller

# Innledning

Energibalansemodeller representerer en sentral og klassisk tilnærming innen klimafysikk. De bygger på fundamentale fysiske lover, særlig strålingsfysikk og Stefan–Boltzmanns lov, og gir en matematisk beskrivelse av hvordan jorden oppnår en likevekt mellom absorbert og utstrålt energi. Til tross for at modellene er sterkt forenklede – ved at jorden behandles som et svart legeme og komplekse prosesser i atmosfære, hav og biosfære utelates – gir de viktig innsikt i de grunnleggende mekanismene bak drivhuseffekten og klimafølsomhet.

Oppgaven vil kombinere matematisk modellering med klimafaglig drøfting. Vi vil undersøke hvordan endringer i sentrale parametere, som albedo og effektiv emissivitet, påvirker systemets likevekt, og diskutere hvilke styrker og begrensninger som ligger i denne typen modeller. På denne måten søker vi å belyse hvordan enkle matematiske strukturer kan bidra til forståelsen av komplekse klimaprosesser.

Oppgaven innledes med en svært forenklet klimamodell, der jorden behandles som et svart legeme og kun den grunnleggende energibalansen mellom innkommende og utgående stråling analyseres. Deretter utvides modellen trinnvis ved først å inkludere albedoeffekten, som beskriver hvor stor andel av solstrålingen som reflekteres tilbake til verdensrommet. Til slutt innarbeides drivhuseffekten, som tar hensyn til atmosfærens evne til å absorbere og reemittere infrarød stråling.

Oppgaven tar utgangspunkt i notatet [Flath & Co: "Energy Balance Models"](https://www.uio.no/studier/emner/matnat/math/MAT1020/v26/mat1020flatharticle.pdf). 

# Modelering av klimamodeller
## 1 - Jorden som et svart legme


![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/energibalanse.png)

Energibalansen viser forholdet mellom hvor  mye energi som kommer inn mot jordoverflaten og hvor mye som sendes ut. Fra figuren nedenfor, ser vi at omtrent halvparten av den innkommende energien fra sola reflekteres eller tas opp i atmosfæren. Den resterende delen absorberes av jordoverflaten, og bidrar til å varme opp bakken og havene. I den enkleste klimamodellen ser vi på jorda som et sort legme som absorberer all innkommen stråling. 
 Når vi vidrere i teksten utvider modellen, legger vi til  parametern albedo $\alpha$, slik at vi tar hensyn til at jordoverflaten reflekterer noe av den innkommende strålingen. 



#### Enheter 
- Lengde, meter ($m$)
- Energi, watt ($W$); 1 watt = 1 joule per sekund
- Temperatur, Kelvin ($K$): Et objekt som holder 0 $K$ befinner seg på det absolutte nullpunkt, og har dermed ingen termisk energi. Kelvin-skalaen starter altså ved det absolutte nullpunktet, som representerer den lavest mulige temperaturen i naturen.


#### Fysiske parametere
| Parameter | Forklaring | Verdi|
|-----------|-------|------|
| $R$   | Jordens radius |6371 $10^{3}$ m  |
| $S$  | Energitettheten fra Sola. Energitettheten er definert som mengden energi som kommer gjennom et areal på 1 $m^{2}$. For innkommen solenergi er dette  | 1367.7 $Wm^{2}$|
| $\sigma$  | Stefan–Boltzmann konstant | 5.67 $10^{-8}$|



### Bygge modellen
#### Innkommende energi
![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/flat_jord.png)


Sett fra sola vil jorda være en disk (se illutrasjonen ovenfor). Jordas areal derfor være gitt ved A = $\pi$ $R^{2}$. 
Energifluksen fra sola er gitt ved $S$, slik at total innkommen energi fra sola vil være gitt ved


$E_{\text{in}}$ = $A_{\text{jorda}}$ $S$ = $\pi$ $R^{2}$ $S$


![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/utg%C3%A5ende%20str%C3%A5ling.png)

Den totale innkommende energien treffer jordens overflate som vist i illustrasjonen ovenfor. En del av strålingen reflekteres tilbake til verdensrommet, mens resten absorberes av jordoverflaten – omtrent 50 %. Denne absorbert energien varmer opp jordkloden og er grunnlaget for den termiske energien som senere sendes ut som varmestråling.

#### Utgående energi
Alle fysiske legemer emitterer energi i form av elektromagnetisk stråling, og den totale strålingsmengden øker med legemets temperatur. Da jorda har blitt varmet opp av den innkommende solstrålingen, vil den derfor skille ut termisk energi. 

For et ideelt svart legeme (som vi i denne enkle modellen anser jorda for å være) beskrives denne sammenhengen av Stefan–Boltzmanns lov, som angir at strålingsfluksen er proporsjonal med den fjerde potens av temperaturen, 
uttrykt som 


$$F_{\mathrm{SB}}(T)=\sigma T^4$$, der $\sigma$  er Stefan–Boltzmanns konstant. 


Når denne loven anvendes på Jorden, tar man utgangspunkt i at planetens totale overflateareal er A = 4
$\pi$ $R^{2}$ (altså overflaten til en kule). Dette innebærer at den samlede energien Jorden stråler ut til verdensrommet, forutsatt at den oppfører seg som et tilnærmet svart legeme, kan beskrives ved uttrykket 


$$E_{\text{ut}} = A_{\text{jorda}}
F_{\mathrm{SB}}(T) = \sigma T^4 4\pi R^2
$$


Dersom den innkommende strålignen er større enn den utgående, vil temperaturen på  jorda øke. Motsatt, dersom innkommende energi er lavere enn energien jorda sender ut, vil temepaturen avta. Likvekten, der 
$$E_{\text{inn}} = E_{\text{ut}}$$ er der temperaturen holdes konstnat, og omtales gjerne som $termisk$  $likevekt$

Med de matematiske utrykkene vi har funnet, gir dette 


$\pi$ $R^{2}$ $S$ = 4 $\sigma$ $T^4$ $\pi$ $R^2$. 


Når vi løser dette med hensyn på temperaturen $T$, får vi 


$$T = \left(\frac{\frac{1}{4}S}{\sigma}\right)^{1/4}\. $$ 


Med de numeriske verdiene vi jobber med, får vi da 


$$T = \left(\frac{1376.6/4}{5.67*10^{-8}}\right)^{1/4}\. $$ = 276.6 $K$. Dette tilsvarer rundt 5.5 grader Celsius. 


## 2- Verdi for albedo

Når vi innfører albedo, $\alpha$ , tar vi hensyn til hvor stor andel av solstrålingen som faktisk absorberes av Jorden, og hvor mye som reflekteres tilbake til verdensrommet. En gjennomsnittlig global albedo på  0.3 innebærer at rundt 30% av den innkommende solenergien reflekteres, mens de resterende 70% absorberes av jordoverflaten. Dette gir oss et nytt utrykk for innkommende energi, mens utgående termisk energi fra jorda holdes konstant. 


$E_{\text{in}}$ =  $\pi$ $R^{2}$ $S$ (1- $\alpha$ ) 


 $$E_{\text{ut}} = A_{\text{jorda}}
F_{\mathrm{SB}}(T) = \sigma T^4 4\pi R^2
$$

Igjen løser vi 
$$E_{\text{inn}} = E_{\text{ut}}$$ for å finne termisk likevekt. Når vi løser dette med hensyn på $T$, slik at vi får temperaturen jorden stabiliserer seg på, får vi 


$$T = \left(\frac{\frac{1}{4}S \cdot (1-\alpha)}{\sigma}\right)^{1/4}\. $$ 

Når vi setter inn de numeriske verdiene og parametere får vi:

$$T = \left(\frac{\frac{1}{4} \cdot 1367.6 \cdot 0.7}{5.68 \cdot10^{-8}}\right)^{1/4}\. $$ = 254.9 K = -19 C. 

Til tross for at modellen nå inkluderer en ekstra parameter som gjør den mer realistisk, ser vi at temperaturanslaget beveger seg enda lenger bort fra den observerte middeltemperaturen på 16 grader. Dette viser at albedo $\alpha$ alene ikke er derfor ikke nok til å forklare Jordens faktiske temperatur, og at viktige prosesser fortsatt mangler i modellen. 

## 3 - Drivhuseffekten

Vi legger nå til en ny parameter $\epsilon$ , som betegner drifhuseffekten. Dette er en konstant (0 < $\epsilon$ < 1), som måler hvor mye av den utgående stråligen fra jorda som absorberes av atmosfæren. En lav verdi for $\epsilon$ tilsvarer en høy andel drivhusgasser i atmorfæren (da en liten andel av den utgående strålingen fra jorda slipper gjennom atmosfæ
ren)

Vi legger til den nye parameteren i utrykkene for innkommende og utgående stråling, som gir: 


$E_{\text{in}}$ =  $\pi$ $R^{2}$ $S$ (1- $\alpha$ ) 


 $$E_{\text{ut}} 
 = 4\pi R^2 \epsilon \sigma T^4  
$$

Igjen løser vi for temperaturen $T$, som gir 

$$T = \left(\frac{\frac{1}{4}S \cdot (1-\alpha)}{\sigma \epsilon}\right)^{1/4}\. $$ 

Når vi prøver oss frem med numeriske verdier, ser vi at en $\epsilon$ = 0.66 gir en likeveksttempeatur på $$T_{\text{1}}$$ = 288 $K$ , som tilsvarer jordas likevektstempeatur på 16 grader. 

En avtakende verdi av parameteren $\epsilon$ (som kommer av økt andel drivhusgasser i atmosfæren)
fører til en økning i jordens likevektstemperatur.

Modellen predikerer dermed at en økning i konsentrasjonen av drivhusgasser – som effektivt reduserer den utgående strålingen til verdensrommet – vil føre til en økning i jordens temperatur.




Jorden varmes opp av innkommende ultrafiolett solstråling (bølgelengde på mindre enn 0.4 $\mu\$ m), og sender deretter ut energi i form av infrarød varmestråling (bølgelengde 
bølgelengde 3 - 100 $\mu\$ m)).

heiehei

