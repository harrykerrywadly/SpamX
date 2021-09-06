import os
import signal

from SpamX.services.redis import redis
from SpamX.utils.logger import log


def exit_gracefully(signum, frame):
    log.warning("Bye!")

    try:
        redis.save()
    except Exception:
        log.error("Exiting immediately!")
    os.kill(os.getpid(), signal.SIGUSR1)


# Signal exit
log.info("Setting exit_gracefully task...")
signal.signal(signal.SIGINT, exit_gracefully)
