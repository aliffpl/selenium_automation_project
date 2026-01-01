import pytest
from config import REPORTS_DIR

if __name__ == '__main__':
	# Basic run with HTML report generation
	pytest_args = [
		'-q',
		'--html=' + str(REPORTS_DIR / 'report.html'),
		'--self-contained-html'
	]
	pytest.main(pytest_args)

