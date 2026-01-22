#step 1 Notes:
#o pandas é utilizado para importar e manipular os dados e ele fica instalado no computador através do comando pip install pandas, então não é necessário instalar toda vez que for utilizar
#o pd é um apelido padrão para o pandas, utilizado para facilitar a escrita do código
#o display(tabela) é utilizado para exibir a tabela de forma mais legível
#o display(tabela.info()) é utilizado para exibir informações sobre a tabela, como tipos de dados e valores nulos. É importante tratar valores nulos antes de utilizar os dados para treinar um modelo de Machine Learning ou fazer análise dos dados.

#step 2 Notes:
#LableEncoder é utilizado para transformar dados categóricos em numéricos, pois modelos de Machine Learning geralmente trabalham melhor com dados numéricos.
#EXEMPLO: Profissão (Engenheiro, Médico, Professor) -> (0, 1, 2)
#fit_transform é um método que ajusta o codificador aos dados e transforma os dados em uma única etapa.
#É necessário criar um codificador para cada coluna categórica que se deseja transformar.
# Cria um codificador para transformar valores categóricos (texto) em números
# codificador_profissao = LabelEncoder()

# Aprende os valores únicos da coluna 'Profissão' e converte cada um em um número inteiro
# tabela['Profissão'] = codificador_profissao.fit_transform(tabela['Profissão'])
# Funciona como uma tabela de banco de dados: cada profissão recebe um ID numérico,
# substituindo o texto pelo número correspondente para facilitar o processamento
#36
