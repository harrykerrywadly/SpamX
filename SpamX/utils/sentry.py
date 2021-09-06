import sentry_sdk
from sentry_sdk.integrations.redis import RedisIntegration

from SpamX.config import get_str_key
from SpamX.utils.logger import log

log.info("Starting sentry.io integraion...")

sentry_sdk.init(get_str_key("SENTRY_API_KEY"), integrations=[RedisIntegration()])
