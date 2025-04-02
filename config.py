# Telegram API Configuration
API_ID = "20370320"  
API_HASH = "35ee047c1a13d07951f4ce68cf1be144"  
BOT_TOKEN = "7282011617:AAF2-0vcZqteRtbS9gEwK_KoAzjSdf-iXYo"  
SESSION_STRING = "1BVtsOIkBu1h4M60EuwmxBaJNd1XgipIxR6YcYA98DG3AQuY4k7ZOF66R9zgeVuWMeevvJW2KGHprldilrifsMV41z3TDBGy-ReuRujVdvakBsJ_8GwS1Ey0wG1WkwECip2i-TlQWRZX6AFSbp4_DnaWxUT4tWSHyMS1INyY0jxGQyy7lhL9QOn3DWBPukmQ40TKUdO0fJBM0WKa1_DN2RxGY3Fq8w2yIOzW-zc0R3LX8hjv-2iyF6jJZCfrR2CuKZN9WqC338-iqVk40136Ad2h1VYZtFhZrBsEeKZC44Uz5aQirHHx25crbIAUxkAZXIp0yFpyL0w9kI5n1ggTOit4rvAxiJNQ="

# Channel Configuration
SOURCE_CHANNEL = [-1001155351611]  # Source channel ID
TARGET_CHANNEL = [-1002570648989]  # Target channel ID

# Forward Timing Configuration
FORWARD_DELAY_MIN = 10  # Minimum delay between forwards in seconds
FORWARD_DELAY_MAX = 15  # Maximum delay between forwards in seconds
BATCH_SIZE = 360       # Number of videos before taking a break
BATCH_BREAK_MIN = 300  # Minimum break time after batch (5 minutes in seconds)
BATCH_BREAK_MAX = 900  # Maximum break time after batch (15 minutes in seconds)
DAILY_SLEEP_HOURS = 16 # Hours to run before taking long break
DAILY_BREAK_HOURS = 1  # Hours to sleep after running DAILY_SLEEP_HOURS
