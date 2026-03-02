
## Varierende albedo  ulike steder på jorda

Da vi reduserte den utgående varmestrålingen med faktoren $\epsilon$, kunne vi å tilpasse modellen til dagens klima. Imidlertid påvirker ikke støv,aerosoler og klimagasser bare varmen som stråler ut fra jorda (som vi måler med parameteren $\epsilon$),  men også hvor mye som absorberes av jordoverflaten (målt med parametren albedoen $\alpha$). 

Aerosoler og støv kan blokkere og spre sollys før det når jordoverflaten. På den måten endrer de hvor mye solenergi jorda faktisk tar imot. De påvirker også jordas albedo, altså hvor mye av sollyset som reflekteres tilbake til verdensrommet.

Det er vanskelig å måle nøyaktig hvor stor denne effekten er, fordi det krever mange og avanserte målinger. I vår forenklede modell antar vi derfor at albedoen henger sammen med temperaturen: Når temperaturen er lav, er albedo høy (for eksempel 0.7), fordi is og snø reflekterer mye sollys. Når temperaturen er høy, er albedo lav (for eksempel 0,3), fordi mindre is gjør overflaten mørkere og mer sollys absorberes. Hvorhvit man kan steke et egg på en mørk overflate på en varm sommerdag er diskutabelt, men effekten er den samme. 


![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/egg.png)

Vi innfører derfor albedoen $\alpha$ som en funskjon av temperaturen $T$. Albedoen er lav for overflate dekket av vann (havet absorberer mye innkommen varme), mens er høy for is (da det er en lys overflate som reflekterer mye av den innkommende strålingen). 

En temperaturavhenig formel er gitt ved

$$
\alpha(T) = 0.7 - 0.4 \frac{e^{(T - 265)/5}}{1 + e^{(T - 265)/5}}
$$

som gir $\alpha(T)$ = 0.7 for $T<250$ og $\alpha(T)$ = 0.3 for $T>280$. 

Plottet nedenfor viser dette.

![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/variere_a.png)

Vi har nå et utrykk for albedoen $\alpha$ som en funksjon av temperaturen $T$, $\alpha$ $(T)$. Dette gir oss følgene utrykk for innkommende og utgående energi fra jorda. 


$$E_{\text{in}} =  \pi R^{2} S (1- \alpha (T)) $$


 $$E_{\text{ut}} 
 = 4\pi R^2 \epsilon \sigma T^4  
$$

Differensiallikningen, som bekriver tempeaturendringen som proposjonal til energi-ubalansen blir dermed:

$$f(T) = C\frac{dT}{dt} = (1-\alpha (T)) Q - \epsilon \sigma T^{4}.$$

Denne likningen lar seg ikke løse numerisk, men vi ønsker allikvel å drøfte de ulike funksjonsverdiene til $f(T)$. I plottet er det tegnet to grafer, en rosa for $E_{\text{inn}}$ og en blå graf for $E_{\text{ut}}$.


![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/drivhuseffekt.png)
### Temperaturer der $T$ $\in [233, 265]$ 
Av figuren ser vi at den blå grafen ligger over den rosa for $T$ $\in [233, 265]$ , som tilsier at $E_{\text{ut}}$ > $E_{\text{inn}}. Dette gir negative verdier for $f(T)$, slik at temperaturen på jorda vil avta. Temperaturen vil fortsette å synke til den når skjæringspunktet mellom de to kurvene ved $T$ = 233 K. Her er $E_{\text{ut}}$ = $E_{\text{inn}}$ , slik at punktet representerer et termisk likevektspunkt. Dette tilsvarer en temperatur på -40 grader Celsius. 

### Temperaturer der $T$ $\in [265, 288]$ 

I dette intervallet ser vi at $E_{\text{ut}}$ < $E_{\text{inn}}$ , som gir postive verdier for $f(T)$, og dermed en positiv  temperaturendring. Temperaturen vil derfor øke, fremt il $f(T)$ = 0 ved $T$ = 288 K. Dette punktet tilsvarer jordens likevektstempertur ved omtrent 16 grader Celsius. 

### En lav verdi for albedo murliggjør istider


![yayayaya](https://github.com/ragnhild-thielemann/Klimamodeller/blob/main/images/isbre.png)
Når jordens temperatur er lav og overflaten dekkes av is og snø, øker albedoen kraftig, slik at en stor del av den innkommende solstrålingen reflekteres tilbake til verdensrommet. Som vi ser i figuren, vil dette føre til at utgående energi $E_{\text{ut}}$ overstiger innkommende energi 
$E_{\text{ut}}$ , og temperaturen fortsetter å synke eller holde seg lav. Denne positive tilbakekoblingen gjør at lave temperaturer kan vedvare over lange perioder, slik det var under istidene, der jorden i praksis “fanget” seg selv i et kaldt klimaregime.