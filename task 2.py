import csv
 
def track_portfolio():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 145,
        "MSFT": 330
    }
 
    portfolio = {}
    total_investment = 0
 
    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' when you finish entering stocks.\n")
 
    while True:
        stock_name = input("Enter stock name: ").upper()
 
        if stock_name == "DONE":
            break
 
        if stock_name not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue
 
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
 
        cost = stock_prices[stock_name] * quantity
        total_investment += cost
 
        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity
 
        print(f"Added {quantity} shares of {stock_name} (₹{cost})\n")
 
    # Display summary
    print("\n----- Portfolio Summary -----")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        print(f"{stock}: {qty} shares x {price} = {qty * price}")
    print(f"\nTotal Investment Value: {total_investment}")
 
    # Optional: save to file
    save_choice = input("\nDo you want to save the result? (yes/no): ").lower()
    if save_choice == "yes":
        file_type = input("Save as .txt or .csv? ").lower()
 
        if file_type == "csv":
            with open("portfolio_summary.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price", "Total"])
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    writer.writerow([stock, qty, price, qty * price])
                writer.writerow([])
                writer.writerow(["Total Investment", "", "", total_investment])
            print("Saved as portfolio_summary.csv")
 
        else:
            with open("portfolio_summary.txt", "w") as f:
                f.write("----- Portfolio Summary -----\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    f.write(f"{stock}: {qty} shares x {price} = {qty * price}\n")
                f.write(f"\nTotal Investment Value: {total_investment}\n")
            print("Saved as portfolio_summary.txt")
 
 
if __name__ == "__main__":
    track_portfolio()