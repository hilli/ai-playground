#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pip install marqo
import marqo

mq = marqo.Client(url="http://localhost:8882")

try:
    mq.delete_index("my-first-index")
    mq.create_index("my-first-index", model="hf/e5-base-v2")
except:
    mq.create_index("my-first-index", model="hf/e5-base-v2")
finally:
    print("Index created")

hansel = open("training/hansel_and_grethel.txt", "r").read()

mq.index("my-first-index").add_documents(
    [
        {
            "Title": "Hansel and Grethel",
            "Description": hansel,
            "_id": "hansel_and_grethel",
        },
        {
            "Title": "Extravehicular Mobility Unit (EMU)",
            "Description": "The EMU is a spacesuit that provides environmental protection, "
            "mobility, life support, and communications for astronauts",
            "_id": "article_591",
        },
    ],
    tensor_fields=["Description"],
)