# Klimamodeller
Beskrivelse av klimamodeller i MAT1020

Vi tar utgangpunkt i notatet [Flath & Co: "Energy Balance Models"](https://www.uio.no/studier/emner/matnat/math/MAT1020/v26/mat1020flatharticle.pdf). Denne oppgaven vil være drøftinger og refleksjoner rundt klimamodellene som bygges vises frem i notatet. 


# Modelering av klimamodeller
## Jorden som et svart legme


![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/energibalanse.png)

Energibalansen viser forholdet mellom hvor  mye energi som kommer inn mot jordoverflaten og hvor mye som sendes ut. Fra figuren nedenfor, ser vi at omtrent halvparten av den innkommende energien fra sola reflekteres eller tas opp i atmosfæren. Den resterende delen absorberes av jordoverflaten, og bidrar til å varme opp bakken og havene. I den enkleste klimamodellen ser vi på jorda som et sort legme som absorberer all innkommen stråling. 
 Når vi vidrere i teksten utvider modellen, legger vi til  parametern albedo $\alpha$, slik at vi tar hensyn til at jordoverflaten reflekterer noe av den innkommende strålingen. 
![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/utg%C3%A5ende%20str%C3%A5ling.png)


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

$$T = \left(\frac{1376.6/4}{5.67*10^{-8}}\right)^{1/4}\. $$ = 276.6 $K$. Dette tilsvarer rundt 5.5 grader Celsius. Da vi vet at jordas gjennomsnittstemperatur er på 16 grader Celsius, blir tempeaturestimatet med denne svært forenklede modellen alt for lavt. 

## Verdi for albedo

Når vi innfører albedo, $\alpha$ , tar vi hensyn til hvor stor andel av solstrålingen som faktisk absorberes av Jorden, og hvor mye som reflekteres tilbake til verdensrommet. En gjennomsnittlig global albedo på  0.3 innebærer at rundt 30% av den innkommende solenergien reflekteres, mens de resterende 70% absorberes av jordoverflaten. Dette gir oss et nytt utrykk for innkommende energi, mens utgående termisk energi fra jorda holdes konstant. 


$E_{\text{in}}$ =  $\pi$ $R^{2}$ $S$ (1-$\alpha$) 


 $$E_{\text{ut}} = A_{\text{jorda}}
F_{\mathrm{SB}}(T) = \sigma T^4 4\pi R^2
$$

Igjen løser vi 
$$E_{\text{inn}} = E_{\text{ut}}$$ for å finne termisk likevekt. Når vi løser dette med hensyn på $T$, slik at vi får temperaturen jorden stabiliserer seg på, får vi 


$$T = \left(\frac{\frac{1}{4}S(1-\alpha)}{\sigma}\right)^{1/4}\. $$ 

Når vi setter inn de numeriske verdiene og parametere får vi:

$$T = \left(\frac{\frac{1}{4}1467.6*0.7}{5.68*10^{-8}}\right)^{1/4}\. $$ 

I den enkleste klimamodellen anser vi jorden som et svart legeme. Dette betyr at den absorberer all innkommende stråling som treffer overflaten.

Jorden varmes opp av innkommende ultrafiolett solstråling (bølgelengde på mindre enn 0.4 $\mu\$ m), og sender deretter ut energi i form av infrarød varmestråling (bølgelengde 
bølgelengde 3 - 100 $\mu\$ m)).

heiehei

