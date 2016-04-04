#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

from weathermajig import emoji
from weathermajig import cache

reload(sys)
sys.setdefaultencoding('utf8')

def output_verbose(forecast, place, units, **kargs):
    out = kargs

    current = forecast.get_current()
    today = forecast.get_today()

    temp = "%s" % current.get('temperature') + units
    time = datetime.fromtimestamp(current.get('time'))
    high = '%s' % today.get('temperatureMax') + units
    low = '%s' % today.get('temperatureMin') + units

    return '''
{date}
Forecast for {place}
---
CURRENTLY: {cur_temp}
HIGH: {high}
LOW: {low}
{icon} {conditions}
    '''.format(
            date = time.strftime('%a %D %r'),
            place = place,
            cur_temp = temp,
            high = high,
            low = low,
            icon = out.get('icon'),
            conditions = out.get('summary'),
        )

def output_short(out):
    if (len(out.get('summary')) > 10):
        out['summary'] = "%s…" % out['summary'][:10]

    return '%s %s [%s]' % (
        out.get('icon'),
        out.get('summary'),
        out.get('temp'))

def make(conf, forecast):
    current = forecast.get_current()
    units = '°F' if conf.get('units') == 'us' else '°C';
    out = {
        'temp': "%s" % int(round(current.get('temperature'))) + units,
        'icon':  "%s"   % emoji.icon(current.get('icon')),
        'summary': "%s" % current.get('summary'),
    }

    if (conf.get('verbose')):
        out = output_verbose(forecast, conf.get('place'), units, **out)
    else:
        out = output_short(out)

    cache.write(conf, out)
    print out
