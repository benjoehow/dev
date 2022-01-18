from datetime import datetime
import calendar

def get_nyse_open_timestamp(date = datetime.today()):
    
    """
    Return the Unix timestamp of the opening of the
    New York Stock Exchange (NYSE) for a given day.
    
    Parameters
    ----------
    date: datetime.datetime, default: datetime.datetime.today()
          The datetime object for the date to calculate the Unix 
          timestamp for.
          
    Returns
    -------
    int
    Unix timestamp for date 
    
    """
    
    market_open = datetime(date.year, date.month, date.day,
                           13, 30, 0, 0)
    return calendar.timegm(market_open.utctimetuple())