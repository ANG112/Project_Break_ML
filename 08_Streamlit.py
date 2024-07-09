
# ------ IMPORTACIÓN DE LIBRERÍAS --------
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import joblib


# ------- FUNCIONES -------------

def porc_cluster(df_cluster, k):
    dicc_cluster = {}
    for i in range(k):
        dicc_cluster[f'cluster_{i}'] = (df_cluster['Cluster']==i).sum()/ (len(df_cluster)*100)*100

    porc_cluster_df = pd.DataFrame(dicc_cluster, columns=['cluster_1','cluster_2','cluster_0'],index=[0])
    return porc_cluster_df

def create_pie_chart(data, title, figsize=(4, 4)):  # Aumentar el tamaño para mejor visualización
    fig, ax = plt.subplots(figsize=figsize)
    colors = plt.cm.viridis(np.linspace(0, 1, data.shape[0]))  # Cambiar la paleta de colores
    wedges, texts, autotexts = ax.pie(data, labels=data.index, colors=colors, autopct='%1.1f%%',
                                       pctdistance=0.85, labeldistance=1.05)  # Ajustar distancias
    plt.setp(autotexts, size=8, weight="bold")  # Hacer los porcentajes más legibles
    plt.setp(texts, size=8)  # Ajustar el tamaño de las etiquetas
    ax.set_title(title)
    plt.tight_layout()
    return fig

def describe_cluster(df_cluster, k):
    cluster_descriptions = {}
    for num in range(k):
        cluster_df = df_cluster.loc[df_cluster['Cluster'] == num]
        temp = cluster_df.describe().loc['50%'].T.round(2)
        temp['cluster_type'] = f'cluster_{num}'
        cluster_descriptions[f'cluster_{num}'] = temp
    cluster_df = pd.DataFrame(cluster_descriptions, columns=['cluster_1','cluster_2','cluster_0'])
    return cluster_df

def format_numbers(x):
    if isinstance(x, float):
        return f"{x:.1f}"
    return x


def create_bar_chart(data, title, column_name, figsize=(4,3)):
    fig, ax = plt.subplots(figsize=figsize)
    colors = plt.cm.viridis(np.linspace(0, 1, data.shape[0]))
    ax.bar(data.index, data[column_name], color=colors)
    ax.set_title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

def crear_grafico_radar_multiples(stats_list, etiquetas_multi, colores, titulo, leyenda_multi, figsize=(6,6)):
    # Número de variables que tenemos
    num_vars = len(etiquetas_multi)

    # Ángulos de cada eje en el plot de radar (dividimos el círculo completo en partes iguales)
    angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # El gráfico es circular, así que necesitamos cerrar el círculo
    stats_list = [stats + stats[:1] for stats in stats_list]
    angulos += angulos[:1]

    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(polar=True))
    
    # Dibujar las líneas de los ejes
    for stats, color in zip(stats_list, colores):
        ax.fill(angulos, stats, color=color, alpha=0.25)
        ax.plot(angulos, stats, color=color, label=leyenda_multi[colores.index(color)])  # Añadir leyendas con colores

    # Añadir etiquetas a los ejes
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Añadir etiquetas a los ejes
    ax.set_thetagrids(np.degrees(angulos[:-1]), etiquetas_multi)

    # Añadir título
    ax.set_title(titulo, size=18, color='black', y=1.1)  # Ajuste del título

    # Añadir leyenda
    legend = ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    for handle in legend.legendHandles:
        handle.set_linewidth(3.0)  # Asegurar que las líneas de la leyenda sean visibles

    plt.tight_layout(pad=3.0)  # Ajuste del layout

    return fig


# ------- CARGA DE DATOS --------
df_cluster = pd.read_csv('./data/df_cluster.csv', index_col=0)



# ------- CARGA DE MODELOS --------
cluster_model = joblib.load('./models/kmeans_pipeline.joblib')


# ------- VARIABLES/ CONSTANTES -----------
k = 3



# --------- PREPARACIÓN DATOS ---------

# Configuración tabla por % de clientes en cada clúster
porc_cluster_df = porc_cluster(df_cluster, k)

# Configuración de la tabla con los valores medios de las características de los clientes
cluster_df = describe_cluster(df_cluster,k)
tabla2 = cluster_df.loc[cluster_df.index.str.contains('Income|Kidhome|Teenhome|Household_members|age')]
tabla2 = tabla2.map(format_numbers)



# ------ SET_CONFING ---------

st.set_page_config(
    page_title='Customer_Engineering',
    page_icon=':💶:',
    layout = 'wide'
)


# ------ PÁGINA 1: DASHBOARD ------------

def pagina_dashboard(tabla2):
    st.header('DASHBOARD CLÚSTER CLIENTES')
    
    # -- Primera fila --
    st.subheader('Información básica')
    col1, col2 = st.columns([1,2])

    with col1:
        st.write('% clientes por clúster')
        porcentajes = porc_cluster_df.iloc[0]
        fig = create_pie_chart(porcentajes, '% de clientes vs clúster',figsize=(3,3))
        st.pyplot(fig, use_container_width=True)

    with col2:
        st.write('Caract. principales clientes')    
        st.table(tabla2)

    # -- Segunda fila --
    st.subheader('Información CORE negocio')
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    figsize = (4, 3)
    with col1:
        st.write('Total Amount')
        cluster_df_transposed = cluster_df.T
        #fig, ax = plt.subplots(figsize= figsize)
        #ax.bar(cluster_df_transposed.index, cluster_df_transposed['Total_amount'])
        #st.pyplot(fig, use_container_width=True)
        fig = create_bar_chart(cluster_df.T, 'Total Amount', 'Total_amount')
        st.pyplot(fig, use_container_width=True)

    with col2:
        st.write('Num. Avg. Purchase')
        #fig, ax = plt.subplots(figsize= figsize)
        #ax.bar(cluster_df_transposed.index, cluster_df_transposed['Total_purchase'])
        #st.pyplot(fig, use_container_width=True)

        fig = create_bar_chart(cluster_df.T, 'Num. Avg. Purchase', 'Total_purchase')
        st.pyplot(fig, use_container_width=True)

    with col3:
        st.write('Avg. Amount')
        #fig, ax = plt.subplots(figsize= figsize)
        #ax.bar(cluster_df_transposed.index, cluster_df_transposed['Median_amount_purchase'])
        #st.pyplot(fig, use_container_width=True)

        fig = create_bar_chart(cluster_df.T, 'Avg. Amount', 'Median_amount_purchase')
        st.pyplot(fig, use_container_width=True)

    with col4:
        st.write('Recency')
        #fig, ax = plt.subplots(figsize= figsize)
        #ax.bar(cluster_df_transposed.index, cluster_df_transposed['Recency'])
        #st.pyplot(fig, use_container_width=True)

        fig = create_bar_chart(cluster_df.T, 'Recency', 'Recency')
        st.pyplot(fig, use_container_width=True)

    # -- Tercera fila --
    st.subheader('Comparativa productos y canales de compra')
    col1, col2 = st.columns(2)
   
    with col1:
        st.write('Producto')
        # Creo el df específico con las cantidades de los productos
        grafico_mnt = cluster_df.loc[cluster_df.index.str.contains('Mnt')]
        # Creo listas provisionales que albergarán características de la función
        stats_list = []
        leyenda_multi = []

        for elemento in grafico_mnt:
            temp_stats= grafico_mnt[elemento].values.tolist()
            temp_label = elemento
            stats_list.append(temp_stats)
            leyenda_multi.append(elemento)
            etiquetas_multi = grafico_mnt.index.to_list()
        
        colores = ['red','blue', 'yellow', 'green', 'orange']
        

        fig = crear_grafico_radar_multiples(stats_list,etiquetas_multi,colores,'Cantidades por producto', leyenda_multi, figsize=(10,6))
        st.pyplot(fig)
    with col2:
        st.write('Canales')
        grafico_purchase = cluster_df.loc[cluster_df.index.str.contains('Purchase')]
        # Creo listas provisionales que albergarán características de la función
        stats_list = []
        leyenda_multi = []
        for elemento in grafico_purchase:
            temp_stats= grafico_purchase[elemento].values.tolist()
            temp_label = elemento
            stats_list.append(temp_stats)
            leyenda_multi.append(elemento)
        
        etiquetas_multi = grafico_purchase.index.to_list()
        colores = ['red','blue', 'yellow', 'green', 'orange']

        fig = crear_grafico_radar_multiples(stats_list,etiquetas_multi,colores,'Canales de compra', leyenda_multi, figsize=(10,8))
        st.pyplot(fig)

    

# ------- PÁGINA 2: SELECCIÓN DE CLIENTES------
def seleccion_clientes():
    st.header('SELECCIÓN DE CLIENTES')
    # Ordenar los valores únicos del clúster de mayor a menor
    clusters_ordenados = sorted(df_cluster['Cluster'].unique(), reverse=True)

    # Usar los valores ordenados para el botón de opción
    cluster_to_filter = st.radio('Selecciona un clúster:', clusters_ordenados)
    filtered_df = df_cluster[df_cluster['Cluster'] == cluster_to_filter]
    # Filtrar el DataFrame
    filtered_df = df_cluster[df_cluster['Cluster'] == cluster_to_filter]

    # Mostrar la tabla filtrada con barras de desplazamiento si es necesario
    st.dataframe(filtered_df, width=1700, height=500)

    # Función para convertir el DataFrame filtrado a CSV
    def convert_df_to_csv(df):
        return df.to_csv().encode('utf-8')

    # Botón de descarga para el DataFrame filtrado
    csv = convert_df_to_csv(filtered_df)
    st.download_button(
        label="Descargar datos filtrados como CSV",
        data=csv,
        file_name='datos_filtrados.csv',
        mime='text/csv',
    )



# ------- PÁGINA 3: PREDICTOR CLÚSTER------
def segmentador():
    st.header('PREDICTOR CLÚSTER')

    # Crear un formulario para introducir datos
    with st.form('input_form'):
    # Aquí puedes añadir campos para que el usuario introduzca los datos
        input_data = st.text_input('Introduce tus datos aquí:')
        submitted = st.form_submit_button('Predecir')

        if submitted:
            # Aquí procesarías los datos introducidos y harías la predicción
            prediction = cluster_model.predict([input_data])
            st.write(f'El clúster predicho es: {prediction}')

    # O permitir la subida de un archivo CSV
    uploaded_file = st.file_uploader('Sube tu archivo CSV aquí:', type='csv')
    if uploaded_file is not None:
        # Aquí leerías el archivo y harías la predicción
        data_to_predict = pd.read_csv(uploaded_file)
        predictions = cluster_model.predict(data_to_predict)
        st.write('Predicciones de clúster:')
        st.write(predictions)

# ------- PÁGINA 4: PREDICTOR CAMPAÑAS------
def pred_campañas():
    st.header('PREDICTOR CAMPAÑAS')



# ------- SIDEBAR ---------
pagina = st.sidebar.selectbox('Menú',['Dashboard','Selección clientes', 'Predictor Clúster', 'Predictor Campañas'])

# Llama a la función que corresponde a la página seleccionada
if pagina == 'Dashboard':
    pagina_dashboard(tabla2)
elif pagina == 'Selección clientes':
    seleccion_clientes()
elif pagina == 'Predictor Clúster':
    segmentador()
elif pagina == 'Predictor Campañas':
    pred_campañas()
