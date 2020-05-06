
def make_file():
    file = 'pre_post.sh'
    values = []

    feature_cols = ['pregnant', 'glucose', 'bp',
                    'insulin', 'bmi', 'pedigree', 'age']

    for feature in feature_cols:
        values.append(input(f'Enter value for {feature}: '))

    cmd = f'curl -d \'{{"pregnant":{values[0]},"glucose":{values[1]},"bp":{values[2]},"insulin":{values[3]},"bmi":{values[4]},"pedigree":{values[5]}, "age": {values[6]}}}\' -H \"Content-Type: application/json\" -X POST http://127.0.0.1:5000/predict/sample'

    with open(file=file, mode='w') as f:
        f.write(cmd)

make_file()
