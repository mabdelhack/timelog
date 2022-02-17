import datetime as tm


def timestamp(time='now', fmt=None):
    """Creates a timestamp for your logging needs. If you don't provide time it uses current time. If you don't
    provide a format it uses [year][month][day]_[hour][minute]. If you want your own format, you can either use the
    datetime library format or you can use one of the following options [year2second, month2second, month2minute,
    year2minute] for a compact representation of (%Y)%m%d_%H%M(%S). It's always better to go in this order since it can
    be sorted directly by date."""
    if fmt is None:
        fmt = "%Y%m%d_%H%M"
    elif isinstance(fmt, list):
        if fmt == 'year2second':
            fmt = "%Y%m%d_%H%M%S"
        elif fmt == 'month2second':
            fmt = "%m%d_%H%M%S"
        elif fmt == 'month2minute':
            fmt = "%m%d_%H%M"
        elif fmt == 'year2minute':
            fmt = "%Y%m%d_%H%M"
    if time != 'now':
        assert (isinstance(time, tm.datetime) | isinstance(time, tm.time) | isinstance(time, tm.date))
        tmstmp = tm.datetime.strftime(time, fmt)
    else:
        tmstmp = tm.datetime.now().strftime(fmt)

    return tmstmp


if __name__ == '__main__':
    print(timestamp())
    print(timestamp(time=tm.datetime.strptime('18/09/19 01:55:19', '%d/%m/%y %H:%M:%S'), fmt="%Y%m%d_%H%M%S"))
    print(timestamp(time=tm.datetime.strptime('18/09/20', '%d/%m/%y'), fmt="%Y%m%d"))
