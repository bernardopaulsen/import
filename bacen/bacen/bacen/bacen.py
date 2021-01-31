import pandas as pd

def get(number : int, start : tuple, end : tuple) -> pd.DataFrame:
    """
    Gets data from Bacen Time Series Management System API

    Parameters
    ----------
    number : integer
        Serie\'s number on Bacen SGS

    start : tuple
        Initial date for the series, (YYYY,M,D)

    end : tuple
        Final date for the series, (YYYY,M,D)

    Returns
    -------
    object : pandas.series

    """

    def add_zero(n):
        return str(n) if n >= 10 else f'0{n}'
    
    def tuple_to_string(date):
        year  = date[0]
        month = add_zero(date[1])
        day   = add_zero(date[2])
        return f'{day}/{month}/{year}'

    start_str = tuple_to_string(start)
    end_str   = tuple_to_string(end)
    
    url = 'http://api.bcb.gov.br/dados'
    url += '/serie/bcdata.sgs.{}'.format(number)
    url += '/dados?formato=csv&'
    url += '&dataInicial={}&dataFinal={}'.format(start_str, end_str)
    df = pd.read_csv(url,
        sep=';', index_col=0, parse_dates=True, decimal=',', dayfirst = True)

    return df


