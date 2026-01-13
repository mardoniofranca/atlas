import os
import django
import pandas as pd
from django.db import transaction
import sys

# 🔹 inicializa o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tupa.settings")
django.setup()

from siteweb.models import Cliente

def importar_clientes():
    # Verificar se já existem clientes no banco
    if Cliente.objects.exists():
        print("⚠️  Já existem clientes no banco de dados. Pular importação.")
        return
    
    # arquivo excel - ajuste o caminho para o Heroku
    ARQUIVO_EXCEL = "db/clientes.xlsx"
    
    # Verificar se arquivo existe
    if not os.path.exists(ARQUIVO_EXCEL):
        print(f"Arquivo não encontrado: {ARQUIVO_EXCEL}")
        print(" Dica: No Heroku, você pode usar um arquivo em um storage externo (S3) ou base64")
        return
    
    try:
        # ler excel
        df = pd.read_excel(ARQUIVO_EXCEL)
        print(f"Excel lido com sucesso: {len(df)} registros")
    except Exception as e:
        print(f" Erro ao ler Excel: {e}")
        return
    
    # Preencher valores nulos
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
        "uf": "NI",
    })
    
    clientes = []
    
    for indice, linha in df.iterrows():
        try:
            # Criar cliente - NÃO passe o campo 'id', ele será gerado automaticamente
            cliente = Cliente(
                nome=str(linha["nome"])[:200],
                lideranca=str(linha["lideranca"])[:200],
                fone=str(linha["fone"])[:50],
                endereco=str(linha["endereco"]),
                numero=str(linha.get("numero", "0"))[:20],
                email=str(linha["email"])[:100],
                bairro=str(linha.get("bairro", "Sem Informação"))[:100],
                cidade=str(linha["cidade"])[:100],
                uf=str(linha.get("uf", "NI"))[:20],
                zona=str(linha["zona_eleitoral"])[:20],
                secao=str(linha["secao"])[:20],
                ativo=int(linha.get("ativo", 1)),
                dia_aniv=int(linha["diaAniversario"]),
                mes_aniv=int(linha["mesAniversario"]),
                ano_aniv=int(linha["anoAniversario"]),
            )
            clientes.append(cliente)
            
            # Progresso
            if (indice + 1) % 100 == 0:
                print(f"Processados {indice + 1} registros...")
                
        except Exception as e:
            print(f" Erro na linha {indice + 1}: {e}")
            print(f"   Dados da linha: {dict(linha)}")
            continue
    
    # Importar para o banco
    if clientes:
        try:
            print(f" Salvando {len(clientes)} registros no banco...")
            
            with transaction.atomic():
                # Usar ignore_conflicts=True para evitar erros de duplicação
                Cliente.objects.bulk_create(clientes, batch_size=100, ignore_conflicts=True)
            
            print(f" Importação concluída com sucesso!")
            print(f"   Registros importados: {len(clientes)}")
            print(f"   Total no banco: {Cliente.objects.count()} clientes")
            
        except Exception as e:
            print(f"\n Erro ao salvar no banco: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(" Nenhum cliente válido para importar!")

if __name__ == "__main__":
    importar_clientes()