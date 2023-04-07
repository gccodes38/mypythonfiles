#get your user input
investor_name = input("Enter investors name: " )
amount_to_invest = input("Enter amount to invest: ")

#To calcute wallet balance with 50% increase 
wallet_balance = amount_to_invest * 0.5
print("wallet_balance", wallet_balance)

#Allow investor to withdraw funds
amount_to_withdraw = float(input("Enter amount to withdraw: "))

#calculate final balance with 7% vat deduction
if amount_to_withdraw > wallet_balance:
    print("insufficient funds")
else:
    vat_deduction = 0.07 * wallet_balance
    amount_withdrawn = (amount_to_withdraw + vat_deduction)
    print("amount deducted successfully, your wallet has been debited with", amount_withdrawn)
    print("final balance", wallet_balance)
    
