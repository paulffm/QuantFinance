from pandas_datareader import data as pdr

def getData(stocks, start, end, col='Close'):
    '''
    :param stocks:
    :param start:
    :param end:
    :param col:
    :return:
    '''
    stockdata = pdr.get_data_yahoo(stocks, start=start, end=end)
    stockdata = stockdata[col]
    return stockdata

def mean_std(stockdata):
    '''
    :param stockdata:
    :return:
    '''

    try:
        returns = stockdata.pct_change
    except:
        print('Input must be pandas object!')
    mean_returns = returns.mean()
    covMatrix = returns.cov()

    return mean_returns, covMatrix




