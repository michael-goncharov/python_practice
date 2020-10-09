import argparse, re, collections

parser = argparse.ArgumentParser(description='This script finds 10 most common ip addresses in log')
parser.add_argument("log_name", help="path to the log file")
args = parser.parse_args()  

def extractIPs(fileContent):
    pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)([ (\[]?(\.|dot)[ )\]]?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})"
    ips = [each[0] for each in re.findall(pattern, fileContent)]   
    for item in ips:
        location = ips.index(item)
        ip = re.sub("[ ()\[\]]", "", item)
        ip = re.sub("dot", ".", ip)
        ips.remove(item)
        ips.insert(location, ip) 
    return ips

myFile = open(args.log_name)
fileContent = myFile.read()

IPs = extractIPs(fileContent)

print(collections.Counter(IPs).most_common(10))