import re
from collections import Counter
import operator
import argparse, pathlib

def log_reader(args):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    data = dict()
    with args.logfile as f:
        log = f.read()
        iplist = re.findall(myregex,log)
        count = Counter(iplist)
        for i, c in count.items():
            data.update({i: c})
    for key, value in sorted(data.items(), key=operator.itemgetter(1),reverse=True)[:10]:
        print("%s: %s" % (key, value))

parser = argparse.ArgumentParser(description="Finds 10 most common ip addresses in log", add_help=False)
parser.add_argument('logfile', type=argparse.FileType('r'), help = 'Path to the log file')
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Show this help message and exit.')
args = parser.parse_args()
log_reader(args)
