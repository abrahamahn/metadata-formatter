import json

json_file = 'metadata.json'
output_file = 'output.json'

with open(json_file) as f:
    data = json.load(f)

new_data = []

# Convert keys to lowercase, remove spaces, and "#" character
for item in data:
    new_item = {'id': len(new_data) + 1}
    for key, value in item.items():
        new_key = key.replace(' ', '').lower().replace('#', '')
        if key == 'Track #':
            new_key = 'track#'
            value = str(int(value))
        elif key == 'track':
            new_key = 'track#'
            value = str(int(value)) if isinstance(value, float) else value
        else:
            for i in range(len(new_key)-1):
                if new_key[i].isalpha() and new_key[i+1].isdigit():
                    new_key = new_key[:i+1] + '_' + new_key[i+1:]
        if key == 'collaborator':
            if isinstance(value, bool):
                value = str(value) if value else "0"
        if value is None:
            value = ""
        elif isinstance(value, float) and value.is_integer():
            value = str(int(value))
        new_item[new_key.replace("_", "")] = value
    new_data.append(new_item)

with open(output_file, 'w') as f:
    json.dump(new_data, f, indent=4)

print('Finished converting keys and notes to ids in', json_file)
print('Modified data saved to', output_file)