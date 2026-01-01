from pathlib import Path

# Base test configuration
BASE_URL = "https://demoqa.com"

# Driver options
DEFAULT_BROWSER = "chrome"

# Timeouts (seconds)
IMPLICIT_WAIT = 0
EXPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 20

# Paths
PROJECT_ROOT = Path(__file__).parent
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

# Test user data (for demo forms)
TEST_USER = {
	"first_name": "Test",
	"last_name": "User",
	"email": "redacted@example.com",
	"current_address": "REDACTED_ADDRESS",
}
