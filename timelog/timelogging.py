import datetime as tm


def timelogging(time='now', fmt=None):
    """Creates a timelog for your logging needs. If you don't provide time it uses current time. If you don't
    provide a format it uses [year][month][day]_[hour][minute]. If you want your own format, you can either use the
    datetime library format or you can use one of the following options [year2second, month2second, month2minute,
    year2minute] for a compact representation of (%Y)%m%d_%H%M(%S). It's always better to go in this order since it can
    be sorted directly by date."""
    format_dict = {
        'year2second': "%Y%m%d_%H%M%S",
        'month2second': "%m%d_%H%M%S",
        'month2minute': "%m%d_%H%M",
        'year2minute': "%Y%m%d_%H%M",
        'year2day': "%Y%m%d",
        'month2day': "%m%d",
    }
    if fmt is None:
        fmt = "%Y%m%d_%H%M"
    elif fmt in format_dict.keys():
        fmt = format_dict[fmt]
    if time != 'now':
        assert (isinstance(time, tm.datetime) | isinstance(time, tm.time) | isinstance(time, tm.date))
        tmstmp = tm.datetime.strftime(time, fmt)
    else:
        tmstmp = tm.datetime.now().strftime(fmt)

    return tmstmp


if __name__ == '__main__':
    print(timelogging())
    print(timelogging(fmt='month2minute'))
    print(timelogging(time=tm.datetime.strptime('18/09/19 01:55:19', '%d/%m/%y %H:%M:%S'), fmt="%Y%m%d_%H%M%S"))
    print(timelogging(time=tm.datetime.strptime('18/09/20', '%d/%m/%y'), fmt="%Y%m%d"))
