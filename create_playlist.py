import os
import sys

relative = True

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} /path/to/folder")
    sys.exit(1)

folder_path = sys.argv[1]

if not os.path.isdir(folder_path):
    print("Error: The specified path is not a valid directory.")
    sys.exit(1)

# select training videos
target_filenames = {
    '01.mkv',
}

all_files = []
training_files = []

for f in os.listdir(folder_path):

    if f.startswith('.'):
        continue

    if not f.endswith('.mkv'):
        continue

    full_path = os.path.abspath(os.path.join(folder_path, f))

    if relative:
        full_path = os.path.relpath(full_path, start=os.getcwd())
    if os.path.isfile(full_path):
        all_files.append(full_path)
        if f in target_filenames:
            training_files.append(full_path)

with open('playlist.list', 'w') as pl:
    for path in all_files:
        pl.write(path + '\n')

with open('training.list', 'w') as tr:
    for path in training_files:
        tr.write(path + '\n')

print(f"Wrote {len(all_files)} files to playlist.list")
print(f"Wrote {len(training_files)} files to training.list")
