# -*- coding: utf-8 -*-
# @Time    : 2018/7/8
# @Author  : Clark Du
# @简介    : send
# @File    : mq_unit.py

from stompest.async import Stomp
from stompest.async.listener import ReceiptListener
from stompest.config import StompConfig
from twisted.internet import task, defer
import json
import logging
from time import clock


class Producer(object):
    QUEUE = "/queue/inq"

    def __init__(self, config=None):
        if config is None:
            config = StompConfig("tcp://localhost:61613")
        self.config = config

    @defer.inlineCallbacks
    def run(self, _):
        bt = clock()
        client = Stomp(self.config)
        yield client.connect()
        client.add(ReceiptListener(1.0))
        for i in range(200000):
            yield client.send(self.QUEUE, "hello world qwertyuiopasdfghjklzxcvbnm")
        client.disconnect()
        et = clock()
        print et - bt
        yield client.disconnected


def main():
    # logging.basicConfig(level=logging.DEBUG)
    task.react(Producer().run)


main()
