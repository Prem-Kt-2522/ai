rwp_examples = [
    {'Alt': 'Y', 'Bar': 'N', 'Fri': 'N', 'Hun': 'Y', 'Pat': 'S', 'Price': '$$$', 'Rain': 'N', 'Res': 'Y', 'Type': 'F', 'Est': '0-10', 'ans': 'Y'},
    {'Alt': 'Y', 'Bar': 'N', 'Fri': 'N', 'Hun': 'Y', 'Pat': 'F', 'Price': '$', 'Rain': 'N', 'Res': 'N', 'Type': 'T', 'Est': '30-60', 'ans': 'N'},
    {'Alt': 'N', 'Bar': 'Y', 'Fri': 'N', 'Hun': 'N', 'Pat': 'S', 'Price': '$', 'Rain': 'N', 'Res': 'N', 'Type': 'B', 'Est': '0-10', 'ans': 'Y'}
]
total_exp = len(rwp_examples)
def tot(attribute, value):
    return sum(1 for ex in rwp_examples if ex[attribute] == value)
def getProbab(attribute, attribval, value):
    count = sum(1 for ex in rwp_examples if ex[attribute] == attribval and ex['ans'] == value)
    total_ans_value = tot('ans', value)
    return count / total_ans_value if total_ans_value != 0 else 0
def calculate_probability(attribute, values):
    for val in values:
        total_attribute_value = tot(attribute, val)
        if total_attribute_value == 0:
            print(f"No data for {attribute} = {val}")
            continue 
        for ans in ['Y', 'N']:
            prob = (getProbab(attribute, val, ans) * tot('ans', ans) / total_attribute_value) * 100
            print(f"{ans}: Will Wait {prob:.2f}% if {attribute} = {val}")
def main():
    conditions = {
        'Alt': ['Y', 'N'], 
        'Est': ['0-10', '10-30', '30-60', '>60'],
        'Pat': ['S', 'N', 'F'], 
        'Type': ['T']
    }
    for attr, vals in conditions.items():
        print(f"\nProbability for Will Wait based on {attr}:")
        calculate_probability(attr, vals)
main()
