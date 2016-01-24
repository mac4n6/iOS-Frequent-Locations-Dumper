# iOS Frequent Locations Dumper
Dump the contents of the StateModel#.archive files located in /private/var/mobile/Library/Caches/com.apple.routined/

##Usage:
`python dump_freq_locs.py -output {k, c, e} <StateModel#.archive>`

##Output Options:
* k - KML
* c - CSV
* e - Everything (KML & CSV)

##Dependencies:      
* hexdump.py: https://pypi.python.org/pypi/hexdump    
* ccl_bplist.py: https://github.com/jorik041/ccl-bplist

##Sample Output:
sample_dump_freq_locs.txt - Sample script output

##Related Information:
http://www.mac4n6.com/blog/2015/12/20/parsing-the-ios-frequent-locations

 

