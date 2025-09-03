"""Wrapper for the shared trading script using local data directory."""

from pathlib import Path
import sys

# Allow importing the shared module from the repository root
sys.path.append(str(Path(__file__).resolve().parents[1]))

from trading_script import main


if __name__ == "__main__":
    from pathlib import Path
    csv_path = Path("Start Your Own/chatgpt_portfolio_update.csv").resolve()
    data_dir = Path("Start Your Own").resolve()  # or Path.cwd() if main expects repo root
    main(str(csv_path), data_dir)

