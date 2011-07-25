# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jul 24, 2011 6:51:29 PM$"

def display(i):
    if i == 10: return 'LF'
    if i == 13: return 'CR'
    if i == 32: return 'SPACE'
    return chr(i)

if __name__ == "__main__":
#
# countletters.py
#
    from sys import argv
    infile = open(argv[1], 'r')
    text = infile.read()
    infile.close()

    counts = 128 * [0]

    for letter in text:
        counts[ord(letter)] += 1

    outFileName = argv[1].split('_')
    outfile = open(outFileName[0]+'_counts.dat', 'w')
    outfile.write("%-12s%s\n" % ("Character", "Count"))
    outfile.write("=================\n")

    for i in range(len(counts)):
        if counts[i]:
            outfile.write("%-12s%d\n" % (display(i), counts[i]))

    outfile.close()