# detectEncrypted

Command line arguments:
  -d, --dir: specifies the path to directory where to look for encrypted/compressed files. Default - current directory.
  -c, --confidence: specifies the threshold level of confidence (in percents from 0 to 100) to treat a certain file as encryped/compressed. Default - 80%.
  -s: all files in the program output should be sorted by confidence level descending (from high to low).
  +s: all files in the program output should be sorted by confidence level ascending (from low to high).
  -p, --print-confidence: print the confidence level along with the file name.
  -h, --help: print help message for all available options (feel free to copy-paste this text).
