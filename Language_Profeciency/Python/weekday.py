#!/usr/bin/env python3
# coding: utf-8
import calendar
import datetime
import sys


def main():
    month, day, year = map(int, input().split(' '))
    print(calendar.day_name[datetime.datetime(year, month, day).weekday()].upper())

    return 0


if __name__ == '__main__':
    sys.exit(main())

