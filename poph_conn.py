import os
import django

# 🔹 Inicializa o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tupa.settings")
django.setup()

from siteweb.models import Cliente

def atualizar_todos_para_fortaleza():
    """
    Atualiza todos os registros para cidade=FORTALEZA e uf=CE.
    AVISO: Isso modifica TODOS os registros da tabela.
    """
    
    print("⏳ Atualizando cidade e UF para todos os clientes...")
    
    # Atualiza todos os registros de uma vez (eficiente)
    # Não usa .update() em um QuerySet vazio, aplica diretamente no manager
    rows_updated = Cliente.objects.all().update(
        cidade='FORTALEZA',
        uf='CE'
    )
    
    print(f" Concluído! {rows_updated} registros foram atualizados.")
    print(f"   - cidade definida como: 'FORTALEZA'")
    print(f"   - uf definido como: 'CE'")

if __name__ == "__main__":
    atualizar_todos_para_fortaleza()