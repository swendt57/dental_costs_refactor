import json
import copy


 # 'static/data/combined_flat.json'


def restructure_dental_json(path):
    with open(path) as infile:
        data = json.load(infile)

    for elem in data:
        print(elem)
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

        # if hasattr('mock_data'):
        #     elem['fake_data'] = elem.pop('mock_data')

        # data.append(elem)

    # with open('static/data/test_out.json', 'w') as outfile:
    #     json.dump(data, outfile)


def copy_elements(path):
    with open(path) as infile:
        data = json.load(infile)

    new_json = []

    for x in range(len(data)):
        for y in range(5):
            new_json.append(copy.deepcopy(data[x]))

    procedures = ['Adult Cleaning', 'Composite Filling', 'Extraction', 'Root Canal', 'Porcelain Crown']
    procedure_abbr = ['cleaning', 'filling', 'extraction', 'root_canal', 'crown']

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

    f = open("static/data/final_out.json", "w")
    f.write(json.dumps(new_json, indent=4))  # write pretty json to the file
    f.close()




# restructure_dental_json('static/data/test_in.json')