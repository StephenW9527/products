# 二維清單:清單中的清單
# 二維清單可以用來表示矩陣或表格數據


import os


def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:  # 讀取檔案
        for line in f:
            if '產品名稱' in line:  # 跳過表頭
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    return products

# 添加產品


def add_product(products):
    while True:
        name = input("請輸入產品名稱（或輸入 'q' 結束）: ")
        if name.lower() == 'q':
            break
        price = input("請輸入產品價格: ")
        price = int(price)  # 將價格轉換為整數
        # product = []
        # product.append(name)
        # product.append(price)
        # products.append(product)
        products.append([name, price])  # 也可以這樣寫 = 10~13行
        print(f"已添加產品: {name}, 價格: {price}")
    print("目前產品清單:", products)
    return products

# 顯示所有產品


def show_products(products):
    print("所有產品清單:")
    for product in products:
        print(product)  # product 是一個清單

        # 也可以使用index來顯示產品名稱和價格
        print(f"產品名稱: {product[0]}, 價格: {product[1]}")
    print(f"產品數量: {len(products)}")

# 寫入檔案


def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        # 寫入產品清單到 CSV 檔案
        f.write('產品名稱,價格\n')  # 寫入表頭
        for product in products:
            f.write(product[0] + ',' + str(product[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print("檔案已存在，將讀取現有的產品清單。")
        products = read_file('products.csv')  # 讀取檔案
        products = add_product(products)  # 添加產品
        show_products(products)  # 顯示產品
        write_file('products.csv', products)  # 寫入檔案
    else:
        print("檔案不存在，將創建新的產品清單。")


main()
