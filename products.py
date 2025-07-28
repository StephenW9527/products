# 二維清單:清單中的清單
# 二維清單可以用來表示矩陣或表格數據


products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '產品名稱' in line:  # 跳過表頭
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)


while True:
    name = input("請輸入產品名稱（或輸入 'q' 結束）: ")
    if name.lower() == 'q':
        break
    price = input("請輸入產品價格: ")
    price = int(price)  # 將價格轉換為整數
    # p = []
    # p.append(name)
    # p.append(price)
    # products.append(p)
    products.append([name, price])  # 也可以這樣寫 = 10~13行
    print(f"已添加產品: {name}, 價格: {price}")
print("目前產品清單:", products)

# 顯示所有產品
print("所有產品清單:")
for product in products:
    print(product)  # product 是一個清單

    # 也可以使用index來顯示產品名稱和價格
    print(f"產品名稱: {product[0]}, 價格: {product[1]}")


# 顯示產品數量
print(f"產品數量: {len(products)}")


with open('products.csv', 'w', encoding='utf-8') as f:
    # 寫入產品清單到 CSV 檔案
    f.write('產品名稱,價格\n')  # 寫入表頭
    for product in products:
        f.write(product[0] + ',' + str(product[1]) + '\n')
