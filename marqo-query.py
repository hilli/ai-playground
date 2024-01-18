#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pip install marqo
import marqo
import pprint

mq = marqo.Client(url="http://localhost:8882")

results = mq.index("my-first-index").search(
    q="What did Hansel and Grethel do?",
)

# let's print out the results:
pprint.pprint(results)
