import pandas as pd
import random

# Laptop brands and models
companies = {
"Dell":["XPS 13","XPS 15","Inspiron 15","Inspiron 14","G15 Gaming","Alienware M15"],
"HP":["Pavilion 15","Victus 16","Envy 13","Omen 16","EliteBook 840"],
"Lenovo":["ThinkPad X1","Legion 5","IdeaPad Slim 3","Yoga 7i","Legion 7"],
"Asus":["TUF F15","ROG Strix G15","VivoBook 15","ZenBook 14","ROG Zephyrus G14"],
"Acer":["Aspire 7","Nitro 5","Swift 3","Predator Helios 300","Aspire Lite"],
"Apple":["MacBook Air M1","MacBook Air M2","MacBook Air M3","MacBook Pro 14","MacBook Pro 16"]
}

# CPU options
cpu_options = {
"Dell":["i3","i5","i7","i9"],
"HP":["i3","i5","i7","i9"],
"Lenovo":["i3","i5","i7","Ryzen5","Ryzen7"],
"Asus":["i5","i7","Ryzen7","Ryzen9"],
"Acer":["i3","i5","i7","Ryzen5"],
"Apple":["M1","M2","M3"]
}

gpu_options = ["Intel","AMD","Nvidia","AppleGPU"]

rows = []

for i in range(400):

    company = random.choice(list(companies.keys()))
    model = random.choice(companies[company])

    laptop_name = company + " " + model

    cpu = random.choice(cpu_options[company])

    ram = random.choice([8,16,32])
    ssd = random.choice([256,512,1024])
    hdd = random.choice([0,500,1000])

    gpu = random.choice(gpu_options)

    screen = random.choice([13.3,14,15.6,16,17])

    weight = round(random.uniform(1.1,2.7),2)

    os = "MacOS" if company=="Apple" else "Windows"

    # Base CPU prices
    base_price = {
    "i3":30000,
    "i5":40000,
    "i7":65000,
    "i9":95000,
    "Ryzen5":42000,
    "Ryzen7":70000,
    "Ryzen9":100000,
    "M1":85000,
    "M2":120000,
    "M3":150000
    }

    price = base_price.get(cpu,40000)

    # Add feature costs
    price += ram * 1500
    price += ssd * 5

    if gpu == "Nvidia":
        price += 12000

    if gpu == "AMD":
        price += 4000

    price += random.randint(-5000,5000)

    rows.append([
        laptop_name,
        company,
        ram,
        ssd,
        hdd,
        cpu,
        gpu,
        screen,
        weight,
        os,
        price
    ])

columns = [
"LaptopName",
"Company",
"RAM",
"SSD",
"HDD",
"CPU",
"GPU",
"ScreenSize",
"Weight",
"OS",
"Price"
]

df = pd.DataFrame(rows,columns=columns)

df.to_csv("dataset.csv",index=False)

print("Dataset generated successfully with",len(df),"laptops")