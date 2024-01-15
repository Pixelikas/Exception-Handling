# Cria variável para armazenar um arquivo de texto
nomeArquivo = 'arquivoUm.txt'

# Comando para abrir o arquivo (tentativa)
try:
    # Lê o arquivo se ele existir, com o parâmetro "r" (read)
    arquivo = open(nomeArquivo, 'r')

# Exceção caso o arquivo não seja encontrado
except FileNotFoundError:
    # Cria o arquivo caso ele não seja encontrado, com o parâmetro "a" (append)
    arquivo = open(nomeArquivo, 'a')

# Nenhuma exceção confirmada (nesse caso, encontrou o arquivo)
else:
    # Mostra na tela mensagem avisando que o arquivo existe
    print(f"Arquivo {nomeArquivo} já existe")

# Comando para finalizar
finally:
    # Fecha o arquivo
    arquivo.close()