import os
import glob
import json

script_dir = os.path.dirname(os.path.realpath(__file__))

for path in glob.glob(os.path.join(script_dir, 'raw/vocab', '*.txt')):
    entries = []

    with open(path, 'r') as f:
        lines = f.readlines()

        for line in lines[1:]:
            cur = line.split()

            entry = {
                'id': cur[0],
                'level': cur[1],
                'word': cur[3],
                'definition': ' '.join(cur[4:])
            }

            entries.append(entry)

    print 'Finished processing {0} entries in {1}.'.format(len(entries), path)

    out_path = os.path.join(script_dir, 'data')

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    with open(os.path.join(out_path, 'vocab.json'), 'w') as f:
        json.dump(entries, f, indent=4, separators=(',', ': '), encoding='utf-8', ensure_ascii=False)
