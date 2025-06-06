import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/26_05/exercises/csv/students_school.csv', sep=',', encoding='utf-8')

df_copy =df.copy()


# 1. Calcule a média, mediana, moda, variância, amplitude e desvio padrão das notas de
# matemática, português e ciências;
# 2. Qual é a frequência média dos alunos por série?
# 3. Filtre os alunos com frequência abaixo de 75% e calcule a média geral deles;
# 4. Use groupby para obter a nota média por idade e matéria;
# 5. Crie a seguinte classificação:
# 	a. Nota menor que 3,0 = reprovado;
# 	b. Nota menor que 6,0 = exame;
# 	c. Nota acima de 6,0 = aprovado.
# 6. Quantos alunos possuem a nota menor que 3,0?
# 7. Quantos alunos possuem a nota menor que 5,0?
# 8. Quantos alunos possuem a nota menor que 7,0?
# 9. Quantos alunos possuem a nota menor que 9,0?
# 10. Quantos alunos possuem a nota igual a 10,0?
# 11. Qual idade tem a melhor e a pior nota em Matemática, português e ciências?


# Título da página Web
st.title('DESAFIO 5')

# Exercício 1

st.header('Exercício 1')

menu_disciplinas = st.sidebar.selectbox("Escolha uma disciplina:", ['nota_matematica', 'nota_portugues', 'nota_ciencias'])

st.subheader(f'Média de {menu_disciplinas}:', divider=True)
st.write(df[menu_disciplinas].mean())

st.subheader(f'Mediana de {menu_disciplinas}:', divider=True)
st.write(df[menu_disciplinas].median())

st.subheader(f'Moda de {menu_disciplinas}:', divider=True)
st.write(df[menu_disciplinas].mode().values[0])

st.subheader(f'Variância de {menu_disciplinas}:', divider=True)
st.write(df[menu_disciplinas].var())

st.subheader(f'Amplitude de {menu_disciplinas}:', divider=True)
st.write(df[menu_disciplinas].max() - df[menu_disciplinas].min())

st.subheader(f'Desvio Padrão de {menu_disciplinas}:', divider=True)
st.write(df[menu_disciplinas].std())

# Exercício 2

st.header('Exercício 2')
st.subheader('Frequência média por série:')

frequencia_media = df.groupby('serie')['frequencia_%'].mean()
st.write(frequencia_media)

# Exercício 3

st.header('Exercício 3')
st.subheader('Média geral dos alunos com frequência < 75%:')

alunos_frequencia_menor75 = df[df['frequencia_%'] < 75]

notas = alunos_frequencia_menor75[['nota_matematica', 'nota_portugues', 'nota_ciencias']]

st.write(notas.values.mean())

# Exercício 4

st.header('Exercício 4')
st.subheader('Nota média por idade e matéria')

nota_media_idade_matematica = df.groupby('idade')['nota_matematica'].mean()
st.write(nota_media_idade_matematica)

nota_media_idade_portugues = df.groupby('idade')['nota_portugues'].mean()
st.write(nota_media_idade_portugues)

nota_media_idade_ciencias = df.groupby('idade')['nota_ciencias'].mean()
st.write(nota_media_idade_ciencias)

# Exercício 5

def classificar(nota_media):
    if nota_media < 3:
        return 'reprovado'
    elif nota_media < 6:
        return 'exame'
    else:
        return 'aprovado'


df['nota_media_geral'] = df[['nota_matematica', 'nota_portugues', 'nota_ciencias']].mean(axis=1)
df['classificacao'] = df['nota_media_geral'].apply(classificar)

st.header('Exercício 5')
st.subheader('Classificação dos alunos:')
st.write(df[['nome', 'nota_media_geral', 'classificacao']])

# Exercícios 6-10

nota_menor3 = df[df['nota_media_geral'] < 3]
nota_menor5 = df[df['nota_media_geral'] < 5]
nota_menor7 = df[df['nota_media_geral'] < 7]
nota_menor9 = df[df['nota_media_geral'] < 9]
nota_igual10 = df[df['nota_media_geral'] == 10]

auxiliar1 = nota_menor3.value_counts()
auxiliar2 = nota_menor5.value_counts()
auxiliar3 = nota_menor7.value_counts()
auxiliar4 = nota_menor9.value_counts()
auxiliar5 = nota_igual10.value_counts()

st.header('Exercício 6-10')

st.subheader('Alunos com média geral < 3:')
st.write(auxiliar1.count())

st.subheader('Alunos com média geral < 5:')
st.write(auxiliar2.count())

st.subheader('Alunos com média geral < 7:')
st.write(auxiliar3.count())

st.subheader('Alunos com média geral < 9:')
st.write(auxiliar4.count())

st.subheader('Alunos com média geral igual a 10:')
st.write(auxiliar5.count())

# Exercício 11

st.header('Exercício 11')

st.subheader('Melhor e pior nota média por idade:')

melhor_nota = df.groupby('idade')['nota_media_geral'].max()

maior_incide = melhor_nota.idxmax()

st.text(f'A maior nota média é: {melhor_nota.values.max()} e pertence à idade: {maior_incide}')

pior_nota = df.groupby('idade')['nota_portugues'].min()

menor_indice = pior_nota.idxmax()

st.write(f'A pior nota média é : {pior_nota.values.max()} e pertence à idade: {menor_indice}')


# 2.1. Crie um histograma das notas de todas as matérias.
# 2.2. Gere um boxplot comparando notas de português por série.
# 2.3. Gere um boxplot comparando notas de matemática por série.
# 2.4. Gere um boxplot comparando notas de ciências por série.
# 2.5. Crie um gráfico de barras com a quantidade de alunos por cidade.
# 2.6. Faça um gráfico de dispersão entre frequencia_% e nota por matéria.

# Exercício 2.1

st.header('Visualizações Gráficas')
st.subheader('Exercício 2.1')

histogramas, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 25))
sns.histplot(x='nota_matematica', data=df, ax=ax1)
ax1.set_title('Histograma: Notas de Matemática')
ax1.set_xlabel('Notas em Matemática')
ax1.set_ylabel('Notas')


sns.histplot(x='nota_portugues', data=df, ax=ax2)
ax2.set_title('Histograma: Notas de Português')
ax2.set_xlabel('Notas em Português')
ax2.set_ylabel('Notas')

sns.histplot(x='nota_ciencias', data=df, ax=ax3)
ax3.set_title('Histogram: Notas de Ciências')
ax3.set_xlabel('Notas em Ciências')
ax3.set_ylabel('Notas')

st.pyplot(histogramas)

# Exercício 2.2-2.4

st.subheader('Exercício 2.2')

boxplot, (ax4, ax5, ax6) = plt.subplots(3, 1, figsize=(10, 25))

sns.boxplot(x='serie', y='nota_matematica', data=df, ax=ax4)
ax4.set_title('Dispersão: Nota de Matemática por Série')

ax4.set_xlabel('Série')
ax4.set_ylabel('Notas em Matemática')

sns.boxplot(x='serie', y='nota_portugues', data=df, ax=ax5)
ax5.set_title('Dispersão: Nota de Português por Série')
ax5.set_xlabel('Série')
ax5.set_ylabel('Notas em Português')

sns.boxplot(x='serie', y='nota_ciencias', data=df, ax=ax6)
ax6.set_title('Dispersão: Nota de Ciências por Série')
ax6.set_xlabel('Série')
ax6.set_ylabel('Notas de Ciências')

st.pyplot(boxplot)

# Exercício 2.5

st.subheader('Exercício 2.5')

countplot, ax7 = plt.subplots()
sns.countplot(x='cidade', data=df)
ax7.set_title('Gráfico de Barras: Quantidade de Alunos por Cidade')
ax7.set_xlabel('Cidades')
ax7.set_ylabel('Quantidade de Alunos')

st.pyplot(countplot)

# Exercício 2.6
# 2.6. Faça um gráfico de dispersão entre frequencia_% e nota por matéria.

st.subheader('Exercício 2.6')

scatterplot, (ax8, ax9, ax10) = plt.subplots(3, 1, figsize=(10, 25))

sns.scatterplot(x='frequencia_%', y='nota_matematica', data=df, ax=ax8, alpha=0.7)
ax8.set_title('Scatter: Frequência dos Alunos em Matemática')
ax8.set_xlabel('Frequência')
ax8.set_ylabel('Disciplina de Matemática')

sns.scatterplot(x='frequencia_%', y='nota_portugues', data=df, ax=ax9, alpha=0.7)
ax9.set_title('Scatter: Frequência dos Alunos em Português')
ax9.set_xlabel('Frequência')
ax9.set_ylabel('Disciplina de Português')

sns.scatterplot(x='frequencia_%', y='nota_ciencias', data=df, ax=ax10, alpha=0.7)
ax10.set_title('Scatter: Frequência dos Alunos em Ciências')
ax10.set_xlabel('Frequência')
ax10.set_ylabel('Disciplina de Ciências')

st.pyplot(scatterplot)
