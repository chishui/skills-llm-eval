import logging

DEBUG_INFO = 11


def get_logger():
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
    logging.addLevelName(DEBUG_INFO, "DEBUG_INFO")
    logger = logging.getLogger()
    logging.Logger.debug_info = debug_info

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    return logger


def debug_info(self, message, *args, **kws):
    if self.isEnabledFor(DEBUG_INFO):
        # Yes, logger takes its '*args' as 'args'.
        self._log(DEBUG_INFO, message, args, **kws)


logger = get_logger()

