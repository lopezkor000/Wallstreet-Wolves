import pandas as pd

def safeReturns(buy:float, history:list):
  return round((buy // float(history[0])) * float(history[-1]), 2)

def timeTravelerReturns(price_history:list, starting_money:float):
    """
    Time traveler strategy: maximize profit by buying before rises and selling before drops.
    
    Args:
        price_history (list of float): Closing prices.
        starting_money (float): Starting amount of money.

    Returns:
        final_money (float): Money after the end of trading.
        trade_log (list of str): Log of actions taken.
    """
    wallet = starting_money
    shares = 0
    trade_log = []

    for i in range(len(price_history) - 1):
        today_price = price_history[i]
        tomorrow_price = price_history[i + 1]

        if tomorrow_price > today_price:
            # Tomorrow price goes up → buy today
            shares_to_buy = int(wallet // today_price)
            if shares_to_buy > 0:
                wallet -= shares_to_buy * today_price
                shares += shares_to_buy
                trade_log.append(f"Day {i}: Bought {shares_to_buy} shares at ${today_price:.2f}")
        elif tomorrow_price < today_price:
            # Tomorrow price goes down → sell today
            if shares > 0:
                wallet += shares * today_price
                trade_log.append(f"Day {i}: Sold {shares} shares at ${today_price:.2f}")
                shares = 0
        else:
            # Prices equal → do nothing
            trade_log.append(f"Day {i}: No action at ${today_price:.2f}")

    # Sell any leftover shares on the last day
    if shares > 0:
        wallet += shares * price_history[-1]
        trade_log.append(f"Day {len(price_history)-1}: Sold {shares} shares at ${price_history[-1]:.2f}")
        shares = 0

    return round(wallet, 2), trade_log

stable = 'KO'
moderate = 'BBY'
volatile = 'ENPH'

wallet = 1_800.00

data = list(pd.read_csv(f'data/{stable}.csv')['Close'])
print(f'{stable}, BDay money returns:   -Patient {safeReturns(wallet, data)}    -TimeTraveler {timeTravelerReturns(data, wallet)[0]}')

data = list(pd.read_csv(f'data/{moderate}.csv')['Close'])
print(f'{moderate}, BDay money returns:   -Patient {safeReturns(wallet, data)}    -TimeTraveler {timeTravelerReturns(data, wallet)[0]}')

data = list(pd.read_csv(f'data/{volatile}.csv')['Close'])
print(f'{volatile}, BDay money returns:   -Patient {safeReturns(wallet, data)}    -TimeTraveler {timeTravelerReturns(data, wallet)[0]}')
