import configparser

from docx import Document


def changeDocx2(file_path, iniFile):
    document = Document(file_path)
    for paragraph in document.paragraphs:
        config = configparser.ConfigParser()
        config.read(iniFile)
        for section in config.sections():
            for key in config[section]:
                # print((f'${key}', config[section][key]))
                key2 = '${' + key + '}'
                value = config[section][key]
                if key2 in paragraph.text:
                    inline = paragraph.runs
                    for item in inline:
                        if key2 in item.text:
                            item.text = item.text.replace(key2, value)
                # paragraph.text = paragraph.text.replace(key2, config[section][key])
    document.save(file_path)


def changeDocx1(file_path, iniFile):
    template_file_path = file_path
    output_file_path = file_path

    config = configparser.ConfigParser()
    config.read(iniFile)

    template_document = Document(template_file_path)
    for section in config.sections():
        for key in config[section]:
            key2 = '${' + key + '}'  # f'$'{''{key}'}'
            # print(f'{key2} - {config[section][key]}')
            for paragraph in template_document.paragraphs:
                replace_text_in_paragraph(paragraph, key2, config[section][key])

            for table in template_document.tables:
                for col in table.columns:
                    for cell in col.cells:
                        for paragraph in cell.paragraphs:
                            replace_text_in_paragraph(paragraph, key2, config[section][key])

    template_document.save(output_file_path)


def changeDocx(template_file_path, variables):
    output_file_path = template_file_path

    template_document = Document(template_file_path)

    for variable_key, variable_value in variables.items():
        for paragraph in template_document.paragraphs:
            replace_text_in_paragraph(paragraph, variable_key, variable_value)

        for table in template_document.tables:
            for col in table.columns:
                for cell in col.cells:
                    for paragraph in cell.paragraphs:
                        replace_text_in_paragraph(paragraph, variable_key, variable_value)

    template_document.save(output_file_path)


def replace_text_in_paragraph(paragraph, key, value):
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)


