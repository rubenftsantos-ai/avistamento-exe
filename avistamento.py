
# Solicita que o usuário insira os valores das variáveis
numero_avistamento = input("Digite o número do avistamento: ")
estrada = input("Digite o nome da estrada: ")
pk = input("Digite o valor do PK: ")
descricao = input("Digite a descrição do avistamento: ")
tipificacao = input("Digite a tipificação do avistamento: ")
link = input("Digite o link do avistamento: ")

# Constrói o texto com formatação
texto_formatado = f'''
Assunto a colocar no EV: 
CTR - {numero_avistamento} / {estrada} - {pk} / {descricao}

Descrição a colocar no EV:
{tipificacao}
{descricao}
{estrada} - {pk}
Código - {numero_avistamento}
{link}
'''

# Exibe o texto formatado
print(texto_formatado)
