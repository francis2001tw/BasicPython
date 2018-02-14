# pip

#[POINT 1]
from tqdm import tqdm

output = []
for item in tqdm(range(10000000)):
    output.append(item)

print(len(output))
