import re
from collections import Counter

def log_reader(logfile):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(logfile) as f:
        log = f.read()
        iplist = re.findall(myregex,log)
        count = Counter(iplist)
        for i, c in count.items():
            print("IP Address " + "=> " + str(i) + " " + "Count "  + "=> " + str(c))

if __name__ == '__main__':
    log_reader(r"C:\Users\User\access_log.txt")
