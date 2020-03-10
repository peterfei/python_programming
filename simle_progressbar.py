#--coding utf8--

import sys,time

def progressbar(count,total,suffix=''):
    barLength=20
    filledLength = int(round(barLength*count/float(total)))

    percent = round(100.0*count /float(total),1)
    bar = '='*filledLength +'-'* (barLength - filledLength)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))
    sys.stdout.flush()

for i in range(10):
	time.sleep(1)
	progressbar(i, 10)

