


## Resumen análisis univariable variable categóricas:

- Education: (entre los dos suman un 72% de los clientes)
    - El 50% de los clientes son Graduados
    - Seguidos de un 22% que tienen un doctorado 

- Marital Status: Entre los tres suman más del 85% de los clientes
    - El 39% es para casados (Married)
    - El 26.65% para parejas (Together)
    - el 20.5% para solteros (Single)

- AcceptedCmp (campañas anteriores, % aceptación):
    - Cmp 1: 6.76%
    - Cmp 2: 1.4%
    - Cmp 3: 7.54%
    - Cmp 4: 7.32%
    - Cmp 5: 7.54%

- Compain (quejas): prácticamente nulas

## Resumen análisis univariable numérica:

- Year_Birth:
    - Hay atípicos en la zona inferior a partir de 1940 llegando a 1899
    - Tiene una distribución bimodal

- Income:
    - Hay outliers en la zona superior con un valor de 666.666$
    - Distribución bimodal con una mediana de 51.000$

- Kidhome y Teenhome:
    - Más del 50% no tienen ni niños pequeños ni jóvenes

- Recency:
    - La mediana de días en volver a comprar está en 49 días y de 73 dias en el 75%.
    - La frecuencia de compra de los clientes es muy dispersa si bien, dentro de esta dispersión, hay cierta uniformidad en cuanto al nº de personas que realiza compras en un mismo periodo de tiempo.

- Cantidad gastada por producto (2 años):
    - MntWines: El 75% está por debajo de 508 con un máx de 1493$.
    - MntFruits: El 75% esta en 33 con un máx. de 199$
    - MntMeatProducts: el 75% está en 223 con un máx. de 1750$
    - MntFishProducts: el 75% está en 49.75 con un máx. de 259$
    - MntSweetProducts: el 75% está en 32 con un máx. de 263
    - MntGoldProds: el 75% está en 56 y el máx en 362

- Con respecto a las compras:
    - NumDealsPurchases: el 75% está en solo en 3 compras con descuento con un máximo de 15. No parece surtir mucho efecto. Revisar si ese 15 s un outliers.
    - NumWebPurchases: el 75% está en 6 con un máx de 27. Habría que ver si es un outliers.
    - NumCatalogPurchases: el 75% está en 4 compras, el máx. en 28. Revisar si es un outliers.
    - NumStorePurchases: el 75% está en 8 veces de compra en el store con un máx. de 13.
    - NumWebVisitsMonth: el 75% está en 7 con un máx. de 20. REvisar outliers.

### Las nuevas variables creadas:

- Age:
    - El 75% está por debajo de 61 años estando la mediana en 50. Hay outliers. Revisar.

- Customer_seniority:
    - Tienen entre 6 y 8 años??? de antigüedad. Me parece muy poca variación.

- Household_members:
    - La mediana y el 75% coinciden en ser 3 o menos de 3 con un máx. de 5.

- Total_amount:
    - La mediana está en 369 y el 75% en 1042, con un máximo de 2525.

- Total_purchase:
    - La mediana está en 15, el 75% en 21 con un máx. de 44.

- Median_amount_purchase:
    - El 75% está en 45. Esta variable hay que arreglarla dado que tiene NAN e inf.

- Total_cmp:
    - El 75% no ha respondido a ninguna campaña anterior.

- Total_%_cmp:
    - El 75% está en 0% de respuesta.

### Análisis bivariable entre variables:

- 'Education' vs:
    - 'Income': parece que a mayor nivel educativo, mayor ingreso 
    - 'Total:amount': Parece que a mayor nivel educativo, mayor cuantía en gasto
    - 'Total_cmp': no hay relación. Está a cero todo.












