# Klimamodeller
Beskrivelse av klimamodeller i MAT1020

Vi tar utgangpunkt i notatet [Flath & Co: "Energy Balance Models"](https://www.uio.no/studier/emner/matnat/math/MAT1020/v26/mat1020flatharticle.pdf). Denne oppgaven vil være drøftinger og refleksjoner rundt klimamodellene som bygges vises frem i notatet. 


# Modelering av klimamodeller
## Den enkleste klimamodellen


![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/energibalanse.png)

Energibalansen viser hvor mye energi som kommer inn mot og sendes ut fra jordoverflata. Omtrent halvparten av den innkommende energien fra sola reflekteres eller tas opp i atmosfæren, mens den resterende delen,når jordoverflaten og bidrar til å varme opp bakken og havene. I første del av å bygge opp klimamodellen vår, tar vi imidlertid utgangspunkt i jorda som et sort legme, så vi antar at den absorberer all innkommen stråling. 
 Når vi vidrere i teksten utvider modellen, vil vi legge til parametern albedo $\alpha$, slik at vi tar hensyn til at jordoverflaten reflekterer noe av den innkommende strålingen. 
![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/utg%C3%A5ende%20str%C3%A5ling.png)


#### Enheter 
- Lengde, meter (m)
- Energi, watt (W); 1 watt = 1 joule per sekund
- Temperatur, Kelvin (K): Et objekt som holder 0 $K$ befinner seg på det absolutte nullpunkt, og har dermed ingen termisk energi. Kelvin-skalaen starter altså ved det absolutte nullpunktet, som representerer den lavest mulige temperaturen i naturen.


#### Fysiske parametere
| Parameter | Forklaring | Verdi|
|-----------|-------|------|
| $R$   | Jordens radius |6371 $10^{3}$ m  |
| $S$  | Energitettheten fra Sola. Energitettheten er definert som mengden energi som kommer gjennom et areal på 1 $m^{2}$. For innkommen solenergi er dette  | 1367.7 $Wm^{-2}$|
| $\sigma$  | Stefan–Boltzmann konstant | 5.67 $10^{-8}$|



### Bygge modellen
#### Innkommen energi
![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/flat_jord.png)
Sett fra sola vil jorda være en disk (se illutrasjonen ovenfor). Jordas areal derfor være gitt ved A = $\pi$ $R^{2}$. 
Energifluksen fra sola er gitt ved $S$, slik at total innkommen energi fra sola vil være gitt ved

Innkommen energi(W)= $E_{\text{in}}$ = $A_{\text{jorda}}$ $S$ = $\pi$ $R^{2}$ $S$

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

$\pi$ $R^{2}$ $S$ = $\sigma$ $T^4$ 4 $\pi$ $R^2$. 
Når vi løser dette med hensyn på $T$, får vi 

$$T = \left(\frac{S/4}{\sigma}\right)^{1/4}\. $$ 

Med de numeriske verdiene vi jobber med, får vi da 

$$T = \left(\frac{1376.6/4}{5.67*10^{-8}}\right)^{1/4}\. $$ = 276.6 $K$. Dette tilsvarer rundt 5.5 grader Celsius. 





I den enkleste klimamodellen anser vi jorden som et svart legeme. Dette betyr at den absorberer all innkommende stråling som treffer overflaten.

Jorden varmes opp av innkommende ultrafiolett solstråling (bølgelengde på mindre enn 0.4 $\mu\$ m), og sender deretter ut energi i form av infrarød varmestråling (bølgelengde 
bølgelengde 3 - 100 $\mu\$ m)).
