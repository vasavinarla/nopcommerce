
import logging

def Logger():
    # debug,info,warn,error,critical
    logging.basicConfig(filename=r"./logs/automation.log",
                        level=logging.INFO,
                        format="%(asctime)s : %(levelname)s : %(message)s",
                        filemode="w",
                        force=True)

    logger = logging.getLogger()
    return logger