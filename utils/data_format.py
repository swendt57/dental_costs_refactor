import copy


def restructure_dental_json(data):
    for elem in data:
        if elem['area'] == 'sd':
            elem['city'] = elem['city'] = 'San Diego'
        elif elem['area'] == 'tj':
            elem['city'] = elem['city'] = 'Tijuana'

        if elem['state'] == 'ca':
            elem['state'] = elem['state'] = 'CA'
        elif elem['state'] == 'tj':
            elem['state'] = elem['state'] = 'Baja California'

        if elem['mock_data']:
            elem['mock_data'] = elem['mock_data'] = 'Mock Data'
        elif not elem['mock_data']:
            elem['mock_data'] = elem['mock_data'] = 'Actual Data'

        elem['fake_data'] = elem.pop('mock_data')

    expanded_json = expand_data(data)

    return expanded_json


def expand_data(data):
    new_json = []

    # create duplicate of each dentist for each procedure
    for x in range(len(data)):
        for y in range(5):
            new_json.append(copy.deepcopy(data[x]))

    procedures = ['Adult Cleaning', 'Composite Filling', 'Extraction', 'Root Canal', 'Porcelain Crown']
    procedure_abbr = ['cleaning', 'filling', 'extraction', 'root_canal', 'crown']

    # each dentist copy has one of the five procedures with the cost
    main_index = 0
    for cycle in range(len(data)):
        proc_index = 0
        for procedure in range(len(procedures)):
            new_json[main_index]['procedure'] = procedures[procedure]
            new_json[main_index]['cost'] = new_json[main_index][procedure_abbr[proc_index]]
            if proc_index + 1 < 5:
                proc_index = proc_index + 1
            else:
                proc_index = 0
            main_index = main_index + 1

    return new_json

