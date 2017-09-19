import sys, os
import ast
from tqdm import tqdm


with open(sys.argv[1], 'r') as checksum_results_file:
    checksum_results = ast.literal_eval(checksum_results_file.read())
    checksum_results_file.close()
    # print({k: v for k, v in checksum_results.items() if not v})
    for checksum_result in {k: v for k, v in checksum_results.items() if not v}:
        if os.path.isfile(checksum_result[0:-4] + '_files.xml'):
            os.remove(checksum_result[0:-4] + '_files.xml')
        if os.path.isfile(checksum_result):
            print(checksum_result)
            os.remove(checksum_result)
