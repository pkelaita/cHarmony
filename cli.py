import argparse
from bscanner import bscan_file


def run_cli():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=True)
    ap.add_argument('-o', '--output', required=False, action='store_true')
    ap.add_argument('-r', '--resize', required=False)
    args = vars(ap.parse_args())

    print(args)
    bscan_file(args['image'], args['resize'], args['output'])


if __name__ == '__main__':
    run_cli()
