
## Descripción variables

| Nombre de Columna       | Descripción                                           |
|-------------------------|-------------------------------------------------------|
| ID                      | Identificador único para cada cliente                 |
| Year_Birth              | Año de nacimiento del cliente                         |
| Education               | Nivel educativo del cliente                           |
| Marital_Status          | Estado civil del cliente                              |
| Income                  | Ingresos anuales del cliente                          |
| Kidhome                 | Número de niños pequeños en el hogar del cliente      |
| Teenhome                | Número de adolescentes en el hogar del cliente        |
| Dt_Customer             | Fecha en que el cliente se unió                       |
| Recency                 | Número de días desde la última compra                 |
| MntWines                | Cantidad gastada en vino en los últimos 2 años        |
| MntFruits               | Cantidad gastada en frutas en los últimos 2 años      |
| MntMeatProducts         | Cantidad gastada en carne en los últimos 2 años       |
| MntFishProducts         | Cantidad gastada en pescado en los últimos 2 años     |
| MntSweetProducts        | Cantidad gastada en dulces en los últimos 2 años      |
| MntGoldProds            | Cantidad gastada en oro en los últimos 2 años         |
| NumDealsPurchases       | Número de compras realizadas con descuento            |
| NumWebPurchases         | Número de compras realizadas a través del sitio web de la empresa |
| NumCatalogPurchases     | Número de compras realizadas utilizando un catálogo   |
| NumStorePurchases       | Número de compras realizadas directamente en tiendas  |
| NumWebVisitsMonth       | Número de visitas al sitio web de la empresa en el último mes |
| AcceptedCmp3            | 1 si el cliente aceptó la oferta en la 3ra campaña, 0 en caso contrario |
| AcceptedCmp4            | 1 si el cliente aceptó la oferta en la 4ta campaña, 0 en caso contrario |
| AcceptedCmp5            | 1 si el cliente aceptó la oferta en la 5ta campaña, 0 en caso contrario |
| AcceptedCmp1            | 1 si el cliente aceptó la oferta en la 1ra campaña, 0 en caso contrario |
| AcceptedCmp2            | 1 si el cliente aceptó la oferta en la 2da campaña, 0 en caso contrario |
| Complain                | 1 si el cliente se quejó en los últimos 2 años, 0 en caso contrario    |
| Z_CostContact           | Costo de contacto del cliente (valor constante)       |
| Z_Revenue               | Ingresos por el cliente (valor constante)             |
| Response                | 1 si el cliente aceptó la oferta en la última campaña, 0 en caso contrario |




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


#### Categóricas-target

- Education-target:
    - Distribución aceptación oferta (1):
        - Graduation: 47% de (1) vs el 50% del total de clientes
        - PhD: 29% de (1) vs el 22% del total de clientes
    - 

- Martial_Status- target:
    - Married: 28% de (1) vs el 38% del total de clientes
    - Together: 17% de (1) vs el 26% del total de clientes
    - Single: 31% de (1) vs el 20% del total de clientes **INSIGTH**
    - Diveroced: 14% de (1) vs el 10% del total de clientes **INSIGTH**


#### Numéricas-target

- Year_Birth vs Response, age vs Response: (una de las dos sobra)
    - La distribución de 0 y 1 por años de nacimiento son prácticamente iguales.
    - pvalor = 0.68 (no significativa)

- Income vs Response:
    - A mayor ingresos, mayor aceptación de las ofertas
    - pvalor = 0.00 (significativa)

- Kidhome vs Response y Teenhome vs Response: (tienen una distribución muy parecida. Una sobra?)
    - A pesar de tener un pvalor de 0.00, visualmente no hay diferencia en la distribución (no significativa)

- Recency vs Response:
    - Los que tienen una recency inferior parece que responden mejor a las ofertas **INSIGTH**
    - pvalor = 0.00 (significativa)

- MntWines vs Response, MntFruits vs Response, MntMeatProducts vs Response, MntFishProducts vs Response, MntSweetProducts vs Response, MntGoldProds vs Response, Total_amount vs Response:
    - A mayor gasto, más aceptación de las ofertas
    - pvalor = 0.00 (significativa)

- NumDealsPurchases vs Response:
    - La distribución es prácticamente igual
    - pvalor = 0.706 (no significativa)

- NumWebPurchases vs Response:
    - Distribuciones diferentes.
    - pvalor de 0.00 (significativa)

- NumCatalogPurchases vs Response:
    - Distribuciones diferentes.
    - pvalor de 0.00 (significativa) 

- NumStorePurchases vs Response:
    - Distribuciones diferentes.
    - pvalor de 0.00 (significativa) 

- NumWebVisitsMonth vs Response:
    - La distribución es prácticamente igual
    - pvalor = 0.137 (no significativa)

- customes_seniority vs Response:
    - Supuestamente es significativo, pero veo la distribución casi igual.
    - En el gráfico de caja y bigotes, a mayor antigüedad, mayor acceptación oferta. **INSIGHT**
    - pvalor = 0.00 (significativa)

Household_members vs Response:
    - A menor nº de miembros en familia, mayor addeptación.
    - pvalor de 0.00 (significativa) 

Total_purchase vs Response:
    - La distribución es muy parecida, si bien hay ligeras diferencias al principio.
    - pvalor de 0.00 (significativa) 

Median_amount_purchase vs Response: HAY QUE ARREGLAR ESTA VARIABLE!!!!! tiene inf
    - 

Total_cmp vs Response, Total_%_cmp vs Response: (Una de las dos sobra.)
    - Distribuciones diferentes
    - pvalor de 0.00 (significativa) 

 





Perfil de Cluster: Crea perfiles detallados para cada cluster identificando las características comunes de los clientes dentro de cada grupo. Esto puede incluir la edad promedio, ingresos, comportamiento de compra, y cualquier otra métrica relevante que hayas utilizado para la segmentación.

Visualización de Datos: Utiliza gráficos y visualizaciones para mostrar cómo se distribuyen los clusters y cuáles son sus características distintivas. Los gráficos de barras, los diagramas de dispersión y los mapas de calor pueden ser particularmente útiles.

Interpretación de Resultados: Proporciona una narrativa clara sobre lo que cada cluster representa. Por ejemplo, podrías tener un cluster de “clientes leales de alto valor” o “clientes ocasionales sensibles al precio”.

Acciones de Marketing: Basándote en los perfiles de cluster, sugiere acciones de marketing específicas. Por ejemplo, podrías recomendar una campaña de correo electrónico dirigida para un cluster o una promoción especial para otro.

Evaluación de la Segmentación: Explica cómo la segmentación puede mejorar las estrategias de marketing y ventas, y cómo se pueden medir los resultados.

Documentación: Prepara una documentación detallada que explique el proceso de modelado, incluyendo la selección del número de clusters y las métricas utilizadas para evaluar el modelo.




RandonForest Amount
Mejor modelo y parámetros: {'criterion': 'absolute_error', 'max_depth': 12, 'min_samples_leaf': 12, 'min_samples_split': 3, 'n_estimators': 100}
Mejor resultado del recall para la clase positiva: -201.78001463155096







