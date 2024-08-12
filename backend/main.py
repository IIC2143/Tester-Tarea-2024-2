import os
import sys
import json
from pathlib import Path

from test_1A import test_1A
from test_1B import test_1B
from test_1C import test_1C

from test_2A import test_2A
from test_2B import test_2B
from test_2C import test_2C

from test_3A import test_3A



def main():

    current_dir = Path(__file__).resolve().parent
    target_dir = current_dir.parent / 'frontend' / 'test'
    target_dir.mkdir(parents=True, exist_ok=True)
    file_path = target_dir / 'results.json'



    #tests = [test_1A,]

    tests = [
        test_1A, test_1B, test_1C,
        test_2A, test_2B, test_2C,
        test_3A, 
    ]

    #student_user = input('Enter student username: ')

    #if not os.path.exists(student_user):
    #    os.mkdir(student_user)
    all_results = {}

    for test in tests:
        results = test()
        #path = Path(student_user) / f'{test.__name__}.json'
        #with open(path, 'w') as f:
        #    json.dump(results, f, indent=4)


        all_results[test.__name__] = results

        #score = sum(results.values())
        #total = len(results)

        #print(f'{test.__name__}: {score}/{total}')

    with open(file_path, 'w') as f:
        json.dump(all_results, f, indent=4)

if __name__ == '__main__':
    main()
