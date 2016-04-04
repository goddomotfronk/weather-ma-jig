#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests as req

class Weather:
    DARK_SKY_URL = 'https://api.forecast.io'

    def __init__(self, lat=None, lng=None, units=None, api_key=None):
        self._lat, self._long, self._units, self._key  = (lat, lng, units, api_key)
        self.get_weather()

    def __getattr__(self, attr):
        return self._forecast.get(attr)

    def get_weather(self):
        url = "%s/forecast/%s/%s,%s?units=%s" % (Weather.DARK_SKY_URL, self._key, self._lat, self._long, self._units)
        self._forecast = req.get(url).json()
        return self

    def get_current(self):
        return self._forecast.get('currently')

    def get_today(self):
        return self._forecast.get('daily').get('data')[0]
