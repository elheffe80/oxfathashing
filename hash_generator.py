# Solution to: https://www.0xf.at/play/20
# run in same directory as their wordlist.txt
 
import hashlib
import sys 

testcase = "1801992782aa0c9ff82af0d52cff4610"
print "Finding hash: " + testcase
a = [line.strip() for line in open('wordlist.txt')]
b = a
hashfile = open('hashes.txt','w')
count = 1
print "Total iterations required: " + str(len(a))
for line in a:
	aword = line
	for line in b:
		bword = line
		mword = aword + bword
		m = hashlib.md5(mword).hexdigest()
		hashfile.write(mword)
		hashfile.write(': ')
		hashfile.write(m)
		hashfile.write('\n')
		if m == testcase:
			break
			print "Solution: " + aword + bword
	if m == testcase:
		print "Solution: " + aword + bword
		break
	percent = float(count) / float(len(a))
	hashes = '#' * int(round(percent * 20))
	spaces = ' ' * (20 - len(hashes))
	sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))) + " " + str(count) + "/"+str(len(a)))
	sys.stdout.flush()
	count = count + 1
