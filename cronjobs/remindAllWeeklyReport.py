# -*- coding: utf-8 -*-
import datetime

lastMon = datetime.datetime.now() - datetime.timedelta(days=7)
#print lastMon.strftime("%Y-%m-%d")
print ".\n.\n  ▶ ▶ ▶ 記得填 Weekly Report https://wiki.mozilla.org/FirefoxOS/DeviceQA/{0}WeeklyReport\n.\n".format(lastMon.strftime('%Y-%m-%d'))

