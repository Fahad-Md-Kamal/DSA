# https://leetcode.com/problems/richest-customer-wealth/


########################### PSUDO CODE ############################
# Declare account_total = 0
# Loop on each customer's account
# Add all account's balance to account_total
# Compare if the balance is higher than the stored one change it with new
# Return account_total
# ------------------------------   XXXXXXXX  ----------------------

def maximumWealth(accounts: list) -> int:
    account_total = 0
    for c in range(len(accounts)):
        new_balance = 0
        for b in accounts[c]:
            new_balance += b
        if new_balance > account_total:
            account_total = new_balance
    return account_total


print(maximumWealth([[1,2,3],[3,2,1]]))


# TODO: NEXT CHALLENGES
    # Minimum Number of Refueling Stops
    # Triples with Bitwise AND Equal To Zero
    # Stone Game IX
