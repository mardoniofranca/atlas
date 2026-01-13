from django.conf import settings

from django.db import models

from django.utils import timezone


ESTADOS_BRASIL = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]



class Cliente(models.Model):
    id          = models.AutoField(primary_key=True)  # Adicione esta linha   
    cpf         = models.CharField(max_length=11,default='99999999999',null=True)
    nome        = models.CharField(max_length=200)
    lideranca   = models.CharField(max_length=200,default='Não informado',null=True)
    fone        = models.CharField(max_length=50,default='Não informado',null=True)
    endereco    = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    numero      = models.CharField(max_length=20,default='Não informado',null=True)
    email       = models.CharField(max_length=100,default='Não informado',null=True)
    bairro      = models.CharField(max_length=100,default='Não informado',null=True)
    cidade      = models.CharField(max_length=100,default='Não informado',null=True)
    uf          = models.CharField(max_length=20,choices=ESTADOS_BRASIL,default='CE',null=True)

    zona        = models.CharField(max_length=20,default='Não informado',null=True)
    secao       = models.CharField(max_length=20,default='Não informado',null=True)
    ativo       = models.IntegerField(default=1)
    dia_aniv    = models.IntegerField(default=0)
    mes_aniv    = models.IntegerField(default=0)
    ano_aniv    = models.IntegerField(default=0)
    observacao  = models.CharField(max_length=300, blank=True, null=True)


    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())

        super().save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
    



class Cliente_Hist(models.Model):
    OPERACAO_CHOICES = (
        ('ALTERACAO', 'Alteração'),
        ('EXCLUSAO', 'Exclusão'),
    )

    id = models.AutoField(primary_key=True)  # Adicione esta linha

    cliente_id_original     = models.IntegerField()
    nome                    = models.CharField(max_length=200)
    lideranca               = models.CharField(max_length=200,default='Não informado')

    fone                    = models.CharField(max_length=50)
    endereco                = models.CharField(max_length=200)
    complemento             = models.CharField(max_length=200, blank=True, null=True)

    numero                  = models.CharField(max_length=20)
    email                   = models.CharField(max_length=100)
    bairro                  = models.CharField(max_length=100)
    cidade                  = models.CharField(max_length=100)
    uf                      = models.CharField(max_length=20,choices=ESTADOS_BRASIL,default='CE',null=True)
    zona                    = models.CharField(max_length=20)
    secao                   = models.CharField(max_length=20)
    ativo                   = models.IntegerField(default=1)
    dia_aniv                = models.IntegerField()
    mes_aniv                = models.IntegerField()
    ano_aniv                = models.IntegerField()
    observacao              = models.CharField(max_length=300, blank=True, null=True)

    
    operacao    = models.CharField(max_length=10, choices=OPERACAO_CHOICES)
    data_hora   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.nome} - {self.operacao} - {self.data_hora}'
