import pandas as pd
import sqlite3 as sql

# arquivo excel
ARQUIVO_EXCEL = "db/clientes.xlsx"

# banco sqlite
BANCO = "db.sqlite3"

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
    "ativo": 1
})

# conexão com banco
con = sql.connect(BANCO)
cur = con.cursor()

# percorre cada linha do excel
for _, linha in df.iterrows():
    cur.execute("""
        INSERT INTO siteweb_cliente (
            nome, fone, cidade, email, ativo, endereco, lideranca,
            ano_aniv,dia_aniv,mes_aniv,
                secao,zona
         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)
    """, (
        linha.get("nome"),
        linha.get("fone"),
        linha.get("cidade"),
        linha.get("email"),
        linha.get("ativo", 1),
        linha.get("endereco"),
        linha.get("lideranca"),
        linha.get("anoAniversario"),
        linha.get("diaAniversario"),
        linha.get("mesAniversario"),
        linha.get("secao"),
        linha.get("zona_eleitoral")
    ))

con.commit()
con.close()

print("Importação concluída com sucesso!")
