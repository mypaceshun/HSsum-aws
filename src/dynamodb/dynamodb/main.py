#!/usr/bin/env python3

import boto3
from pprint import pprint
from . import TABLENAME, TESTUSER


def fetch_tableobj():
    dynamodb = boto3.resource('dynamodb')
    HSsum = dynamodb.Table(TABLENAME)
    return HSsum


def add():
    # add TESTUSER
    table = fetch_tableobj()
    res = table.put_item(
            Item={
                'userName': TESTUSER,
                'displayName': 'Test User',
                'HSItems': [
                    {
                        'name': '中井りか',
                        'date': '20200828',
                        'num': 10,
                        'bu': 1,
                    },
                    {
                        'name': '中井りか',
                        'date': '20200828',
                        'num': 10,
                        'bu': 2,
                    },
                ]
            }
        )
    pprint(res)


def delete():
    # delete TESTUSER
    table = fetch_tableobj()
    res = table.delete_item(
            Key={
                'userName': TESTUSER
            }
        )
    pprint(res)


def get():
    # get TESTUSER data
    table = fetch_tableobj()
    userdata = table.get_item(
            Key={
                'userName': TESTUSER
                }
            )
    pprint(userdata)


def scan():
    # scan all data
    table = fetch_tableobj()
    pprint(table.scan())


if __name__ == '__main__':
    scan()
