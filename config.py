# Trading Configuration Settings

TRADING_SETTINGS = {
    'symbol': 'BTCUSD',  # Trading pair
    'timeframe': '1h',  # Timeframe for trading
    'strategy': 'mean_reversion',  # Strategy to use
    'risk_management': {
        'stop_loss': 0.02,  # Stop loss percentage
        'take_profit': 0.05,  # Take profit percentage
    },
    'amount': 0.1  # Amount to trade
}