import os
API_V1_BASE_ROOT = '/mlcb/api/v1'

DB_ENV_LIST = ["DB_HOST", "DB_PASS", "DB_PORT", "DB_NAME", "DB_USER"]
SSH_ENV_LIST = ['ssh_password', 'ssh_username', 'ssh_hostname', 'ssh_port']

SSH_DB_URL = 'postgresql://{DB_USER}:{DB_PASS}@{SHH_TUNNEL}/{DB_NAME}'
DB_URL = 'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

REQ_LIB_PATH = 'requirements.txt'

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 45
NUM_SESSION_CODE_CHAR = 6

ALGORITHM = "HS256"

DB_SCHEMA = os.getenv('SCHEMA')

SUPPORTED_LANGS = [
  "en",
  "es",
  "fr",
  "de",
  "zh",
  "ja",
  "ko",
  "ru",
  "ar",
  "hi",
  "pt",
  "it",
  "nl",
  "sv",
  "fi",
  "tr",
  "pl",
  "vi",
  "th",
  "id",
  "ms",
  "fa",
  "he",
  "el",
  "cs",
  "hu",
  "ro",
  "da",
  "no",
  "sk",
  "sl",
  "bg",
  "hr",
  "sr",
  "et",
  "lv",
  "lt"
]

MAX_LENGTH_PER_STR = 1000

# ws broadcast types
WS_MESSAGE = 'message'

TRANSCRIPTS_BODY = {
  "body": {
    "user1": {
      "REPLACE_WITH_USER1_USERNAME": {
        "transcript_text": [],
        "source_lang": ""
      }
    },
    "user2": {
      "REPLACE_WITH_USER2_USERNAME": {
        "transcript_text": [],
        "source_lang": ""
      }
    }
  },
  "info": {
    "user1": "",
    "user2": "",
    "user1_lang": "",
    "user2_lang": ""
  }
}
