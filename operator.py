print("Welcome to your wallet")


# Get user inputs
investor_name = input("Enter your name: ")
amount_to_invest = float(input("Enter amount to invest: "))

# Calculate wallet balance
wallet_balance  = (amount_to_invest * 0.5) + amount_to_invest
print("Wallet balance: ", wallet_balance)

# Allow investor to withdraw funds
amount_to_withdraw = float(input("Enter amount to withdraw: "))

# Calculate final balance
if amount_to_withdraw >= wallet_balance:
    print("Insufficient Funds")
else:
    vat_deduction = 0.07 * wallet_balance
    wallet_balance -= (amount_to_withdraw + vat_deduction)
    print("Withdrawal successful, your account has been debited with", amount_to_withdraw, "and 7% VAT has been deducted.")
    print("Final balance: ", wallet_balance)
