import argparse
from core.core import run_signal_encryption
from core.services import test_services

def main():
    parser = argparse.ArgumentParser(description="EagleEye CLI Tool")
    parser.add_argument("--encrypt", action="store_true", help="Run signal encryption")
    parser.add_argument("--test-services", action="store_true", help="Test external services connectivity")

    args = parser.parse_args()

    if args.encrypt:
        run_signal_encryption()

    if args.test_services:
        test_services()

if __name__ == "__main__":
    main()