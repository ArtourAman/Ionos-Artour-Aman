# Telegram API Configuration
API_ID = ""  
API_HASH = ""  
BOT_TOKEN = ""  
SESSION_STRING = "="

# Channel Configuration
SOURCE_CHANNEL = []  # Source channel ID
TARGET_CHANNEL = []  # Target channel ID

# Forward Timing Configuration
FORWARD_DELAY_MIN = 10  # Minimum delay between forwards in seconds
FORWARD_DELAY_MAX = 15  # Maximum delay between forwards in seconds
BATCH_SIZE = 360       # Number of videos before taking a break
BATCH_BREAK_MIN = 300  # Minimum break time after batch (5 minutes in seconds)
BATCH_BREAK_MAX = 900  # Maximum break time after batch (15 minutes in seconds)
DAILY_SLEEP_HOURS = 16 # Hours to run before taking long break
DAILY_BREAK_HOURS = 1  # Hours to sleep after running DAILY_SLEEP_HOURS
