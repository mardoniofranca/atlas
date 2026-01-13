import os
import django
import pandas as pd

# 🔹 inicializa o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tupa.settings")
django.setup()

from siteweb.models import Cliente

# arquivo excel
ARQUIVO_EXCEL = "db/clientes.xlsx"

# ler excel
df = pd.read_excel(ARQUIVO_EXCEL)

df = df.fillna({
    "nome": "Sem Informação",
    "fone": "Sem Informação",
    "cidade": "Sem Informação",
    "email": "Sem Informação",
    "endereco": "Sem Informação",
    "lideranca": "Sem Informação",
    "secao": "0",
    "zona_eleitoral": "0",
    "anoAniversario": 0,
    "diaAniversario": 0,
    "mesAniversario": 0,
    "ativo": 1,
    "numero": "0",
    "bairro": "Sem Informação",
    "cidade": "FORTALEZA",
    "uf": "CEARÁ",
})

clientes = []
# REMOVA codigo_seq se não for usar

for _, linha in df.iterrows():
    clientes.append(
        Cliente(
            nome=linha["nome"],
            lideranca=linha["lideranca"],
            fone=linha["fone"],
            endereco=linha["endereco"],
            numero=str(linha.get("numero", "0")),
            email=linha["email"],
            bairro=linha.get("bairro", "Sem Informação"),
            cidade=linha["cidade"],
            uf=linha.get("uf", "CEARÁ"),
            zona=linha["zona_eleitoral"],
            secao=linha["secao"],
            ativo=int(linha.get("ativo", 1)),
            dia_aniv=int(linha["diaAniversario"]),
            mes_aniv=int(linha["mesAniversario"]),
            ano_aniv=int(linha["anoAniversario"]),
        )
    )
    # REMOVA esta linha: codigo_seq += 1

# 🚀 grava tudo de uma vez (rápido e seguro)
Cliente.objects.bulk_create(clientes)

print("Importação concluída com sucesso!")