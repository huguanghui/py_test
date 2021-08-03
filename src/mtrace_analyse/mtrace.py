#!/usr/bin/env python3

import argparse
from ast import Param


def main():
    parser = argparse.ArgumentParser(description='Process mtrace log.')
    parser.add_argument('-i', '--input', required=True, help='input log file')
    args = parser.parse_args()


if __name__ == "__main__":
    main()
