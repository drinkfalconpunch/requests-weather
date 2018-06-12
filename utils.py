import datetime

date_format = '%Y-%m-%d'
time_format = '%H:%M:%S'
datetime_format = ' '.join([date_format, time_format])

def unixtime_to_readable(unixtime, datetime_format=datetime_format):
    return datetime.datetime.fromtimestamp(unixtime).strftime(datetime_format)

def unixtime_to_date_and_time(unixtime, datetime_format=datetime_format):
    dtime = unixtime_to_readable(unixtime, datetime_format)
    return datetime_to_date_and_time(dtime, datetime_format)

def datetime_to_date_and_time(dtime, datetime_format=datetime_format):
    stripped_datetime = datetime.datetime.strptime(dtime, datetime_format)
    return {'date': stripped_datetime.date().isoformat(), 'time': stripped_datetime.time().isoformat()}

def replace_in_dict(src: dict, search_key=None, replace_func=None):
    for key, value in src.items():
        if isinstance(value, dict):
            replace_in_dict(value, search_key=search_key, replace_func=replace_func)
        elif isinstance(value, list):
            for data in value:
                if isinstance(data, (list, dict)):
                    replace_in_dict(data, search_key=search_key, replace_func=replace_func)
                else:
                    continue
        elif key==search_key and replace_func:
            src[key] = replace_func(value)
        else:
            continue


