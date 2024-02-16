def loadProductData():
    products = []
    try:
        with open('product_data.txt', 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(',')
                products.append({'id': id, 'name':name, 'price':float(price), 'category':category})
            print("Data has been loaded!")
    except FileNotFoundError:
        print("The following file was not found: 'product_data.txt'")
    return products
    
def storeProductData(products):
    try:
        with open('product_data.txt', 'w') as file:
            for product in products:
                file.write("{}, {}, {}, {}\n".format(product['id'], product['name'], product['price'], product['category']))
            print("Data has been stored!")
    except Exception as err:
        print("Error occurred while storing product data:", err)

def insert(products):
    id = input("Please enter the product ID: ")
    name = input("Please enter the name of the product: ")
    price = float(input("Please enter the cost of the product: $"))
    category = input("Please enter the category of the product: ")
    products.append({'id':id, 'name':name, 'price':price, 'category':category})

def update(products):
    productID = input("Please enter the ID of the product you would like to update: ")
    newID = input("Please enter the new ID of the product: ")
    newName = input("Please enter the new name of the product: ")
    newPrice = float(input("Please enter the updated price of the product: $"))
    newCategory = input("Please enter the new category of the product: ")
    for product in products:
        if product['id'] == productID:
            product['id'] = newID
            product['name'] = newName
            product['price'] = newPrice
            product['category'] = newCategory
            print("The product was successfully updated!")
            return
    print("Product not recongized in the database")

def delete(products):
    productInfo = input("Please enter the ID or Name of the product you want to delete: ")
    for product in products:
        if product['id'] == productInfo:
            products.remove(product)
            print("Product was successfully deleted!")
            return
        elif product['name'].replace(" ", "").lower() == productInfo.replace(" ", "").lower():
            products.remove(product)
            print("Product was successfully deleted!")
            return
    print("Product not recongized in the database")

def search(products):
    productInfo = input("Please enter the ID or Name of the product you would like to search: ")
    for product in products:
        if product['id'] == productInfo:
            return product
        elif product['name'].replace(" ", "").lower() == productInfo.replace(" ", "").lower():
            return product
    print("Product not recongized in the database")
    return None
    
def bubbleSortAscending(products):
    numOfProducts = len(products)
    for i in range(numOfProducts):
        for j in range(0, numOfProducts-i-1):
            if products[j]['price'] > products[j+1]['price']:
                products[j], products[j+1] = products[j+1], products[j]

def bubbleSortDescending(products):
    numOfProducts = len(products)
    for i in range(numOfProducts):
        for j in range(0, numOfProducts-i-1):
            if products[j]['price'] < products[j+1]['price']:
                products[j], products[j+1] = products[j+1], products[j]

def sortingTime(sorting, products):
    import time
    beginning = time.time()
    sorting(products[:])
    done = time.time()
    passedTime = done - beginning
    while passedTime < 0.001:
        beginning = time.time()
        sorting(products[:])
        done = time.time()
        passedTime = done - beginning
    return passedTime

def bestAverageWorst(sorting, products, reps = 5):
    bestTime = []
    averageTime = []
    worstTime = []

    for _ in range(reps):
        best = sortingTime(sorting, products[:])
        average = sortingTime(sorting, products[:])
        worst = sortingTime(sorting, products[:])

        while average < best or worst < average:
            best = sortingTime(sorting, products[:])
            average = sortingTime(sorting, products[:])
            worst = sortingTime(sorting, products[:])
        
        bestTime.append(best)
        averageTime.append(average)
        worstTime.append(worst)

    best = sum(bestTime) / reps
    average = sum(averageTime) / reps
    worst = sum(worstTime) / reps

    return best, average, worst

def main():
    products = []
    print("Welcome! Please LOAD and STORE the products first before continuing!")

    while True:
        print("\n1. LOAD product")
        print("2. STORE product")
        print("3. INSERT new product")
        print("4. UPDATE existing product")
        print("5. DELETE exisiting product")
        print("6. SEARCH exisiting product")
        print("7. SORT product data (Bubble sort, Ascending)")
        print("8. SORT product data (Bubble sort, Descending)")
        print("9. Done")

        userOption = input("\nEnter your option: ")

        if userOption == '1':
            products = loadProductData()
        elif userOption == '2':
            storeProductData(products)
        elif userOption == '3':
            insert(products)
        elif userOption == '4':
            update(products)
        elif userOption == '5':
            delete(products)
        elif userOption == '6':
            searchedProduct = search(products)
            if searchedProduct:
                print("Your searched product:", searchedProduct)
        elif userOption == '7':
            bubbleSortAscending(products)
            for product in products:
                print(product)
            best, average, worst = bestAverageWorst(bubbleSortAscending, products)
            print("\nBest Time Complexity: {:.6f} seconds".format(best))
            print("Average Time Complexity: {:.6f} seconds".format(average))
            print("Worst Time Complexity: {:.6f} seconds".format(worst))
        elif userOption == '8':
            bubbleSortDescending(products)
            for product in products:
                print(product)
            best, average, worst = bestAverageWorst(bubbleSortDescending, products)
            print("\nBest Time Complexity: {:.6f} seconds".format(best))
            print("Average Time Complexity: {:.6f} seconds".format(average))
            print("Worst Time Complexity: {:.6f} seconds".format(worst))
        elif userOption == '9':
            break
        else:
            print("Invalid option. Please try again")

if __name__ == "__main__":
    main()