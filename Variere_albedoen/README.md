
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

