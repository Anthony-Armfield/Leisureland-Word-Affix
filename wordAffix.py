

prefix = '>'
suffix = '</a>'

with open('G:\Work Stuff\Technode\LeisurelandRVCenter\Python Programs\source.txt', 'r') as src:
    with open('G:\Work Stuff\Technode\LeisurelandRVCenter\Python Programs\dest.txt', 'w') as dest:
       for line in src:
           dest.write('%s%s%s\n' % (prefix,line.rstrip('\n'),suffix))

