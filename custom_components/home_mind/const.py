"""Constants for Home Mind integration."""

DOMAIN = "home_mind"
CONF_API_URL = "api_url"
CONF_API_TOKEN = "api_token"
CONF_USER_ID = "user_id"
CONF_CUSTOM_PROMPT = "custom_prompt"

DEFAULT_API_URL = "http://localhost:3100"
DEFAULT_USER_ID = "default"
DEFAULT_TIMEOUT = 120  # Claude with tool use can take 60+ seconds

API_CHAT_ENDPOINT = "/api/chat"
API_HEALTH_ENDPOINT = "/api/health"
# Set to "invalid" by a server whose generated token is not in use yet, when a
# request carried some other token: it still answers, so the setup has to look.
TOKEN_STATUS_HEADER = "X-Home-Mind-Token"

NIVES_URL = "https://github.com/hoornet/nives"
