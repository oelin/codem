import yaml
import os
import re



def populateBuildDirectory(search_locations, rule):
    print(search_locations)

    for location in [*search_locations, *(rule.get('include') or [])]:
        os.system(f'cp -r {location} {output_location}')


    for path, folders, files in os.walk(output_location):
        should_process = not not files

        if not should_process:
            continue

        for file in files:
            compileTarget(path, file, rule)


def compileTarget(path, file, rule):
    from_extension = rule.get('from')
    to_extension = rule.get('to')

    joined_path = path + '/' + file

    print(f'[*] compiling target {joined_path}...')

    try:
        with open(joined_path, 'r') as target_file:
            content = target_file.read()
    except:
        return 

    if joined_path.endswith(from_extension):
        with open(joined_path.replace(from_extension, to_extension), 'w') as target_file:

            codeblocks = find_codeblocks(content)
            target_file.write(''.join(codeblocks))

            os.system(f'rm -rf {joined_path}')


def find_codeblocks(content):
    codeblocks = filter(lambda segment: segment.startswith('js'), content.split('```'))
    codeblocks = map(lambda segment: segment[2:], codeblocks)

    return codeblocks


def executeRule(rule):
    name = rule.get('name')
    search_locations = rule.get('locations')

    print(f'[*] executing rule {name}...')
    populateBuildDirectory(search_locations, rule)


with open('./codem.yaml') as file:
    configuration = yaml.safe_load(file)


output_location = configuration.get('output') or 'codemoutput'
os.system(f'rm -rf {output_location}')

print(f'[*] creating build directory {output_location}...')

os.mkdir(output_location)

for rule in configuration.get('rules'):
    executeRule(rule)
