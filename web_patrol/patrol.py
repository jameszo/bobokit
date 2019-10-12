#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util

def go(mission_file):
    logger.info("Receive mission: " + mission_file)
    try:
        mission = json.load(mission_file)
    except Exception as e:
        logger.error("Not understood Sir!", e)
        raise e
    else:
        logger.info("Understood Sir!")

    if check_equip(mission["equipment"]):
        logger.info("Equipment checked!")
    else:
        logger.error("Equipment checked failed.")

    go_for(mission["territory"])
    logger.info("Go Go Go!")

def check_equip(equipment):
    return True
