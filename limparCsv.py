import os
import sys

arquivo_para_limpar =sys.argv[1] 
print(arquivo_para_limpar)
arquvo_para_salvar ="./arquivos_limpos/"+ arquivo_para_limpar.replace(".txt", "_arquivo_limpo.csv")

print(arquvo_para_salvar)
conteudo_para_salvar="cod_cidade;cidade\n"

with open(arquivo_para_limpar, "r") as file:
    conteudo_arq_original =( file.read()
    .replace('\n','')
    .replace("\"","")
    .replace(",{code:","")
    .replace(",name:",";")
    .replace("}","\n")
    .replace("[{code:","")
    .replace("]",'')
     )

    conteudo_para_salvar+= conteudo_arq_original

with open(arquvo_para_salvar,"w") as file:
    file.write(conteudo_para_salvar)


