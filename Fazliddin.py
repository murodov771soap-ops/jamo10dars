from matplotlib import pyplot as plt


turlar = ["iPhone", "Zaryadnik", "Chexol", "Steklo", "Yolkira", "Oziq-ovqat"]
xarajat = [3500000, 160000, 18000, 23750, 50000, 100000]


bo_laklar = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

plt.pie(
    xarajat, 
    labels=turlar, 
    autopct="%1.1f%%", 
    startangle=90, 
    explode=bo_laklar
)

plt.title("Xarajatlar Diagrammasi")
plt.show()