# -*- coding: utf-8 -*-
# @Time    : 2018/7/8
# @Author  : Clark Du
# @简介    : receive
# @File    : mq_rcv.py

from stompest.async import Stomp
from stompest.protocol import StompSpec
from stompest.config import StompConfig
from stompest.async.listener import SubscriptionListener
from twisted.internet import reactor, defer
import json
import logging
from time import clock


class Transformer(object):
    QUEUE_IN = "/queue/inq"
    QUEUE_OUT = "/queue/outq"

    def __init__(self, config=None):
        if config is None:
            config = StompConfig("tcp://localhost:61613")
        self.config = config

    @defer.inlineCallbacks
    def run(self):
        client = Stomp(self.config)
        yield client.connect()
        headers = {
            StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL,
            'activemq.prefetchSize': '500'
        }
        client.subscribe(self.QUEUE_IN, headers, listener=SubscriptionListener(self.add,
                         errorDestination=self.QUEUE_OUT))

    def add(self, client, frame):
        data = frame.body
        # print data


def main():
    # logging.basicConfig(level=logging.DEBUG)
    Transformer().run()
    reactor.run()


main()