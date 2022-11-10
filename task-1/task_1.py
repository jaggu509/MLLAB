import pandas as pd

data = pd.read_csv('cardata.csv', names = ["brand", "price"])
print(data)

cars = {
    'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
    'Price': [32000, 35000, 37000, 45000]
}

df = pd.DataFrame(cars, columns = ["Brand","Price"])

export_excel = df.to_excel("exported.xlsx", index = None, header = True)
