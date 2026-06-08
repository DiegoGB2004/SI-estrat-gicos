
from faker import Faker
import pandas as pd, random
fake=Faker('es_MX')

rows=[]
for _ in range(500):
    rows.append({
        'cliente':fake.name(),
        'ciudad':fake.city(),
        'producto':random.choice(['Camara IP','DVR','NVR','Accesorio']),
        'ventas':random.randint(1000,20000)
    })

pd.DataFrame(rows).to_csv('data/ventas.csv',index=False)
print('Datos generados')
