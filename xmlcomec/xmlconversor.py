import pandas as pd
import xml.etree.ElementTree as ET

# Load Excel file into a Pandas DataFrame
excel_filepan = pd.ExcelFile('your_excel_file.xlsx')

# Define the XML root element
root = ET.Element('root')

# Iterate through each sheet and create XML elements
for sheet_name in excel_file.sheet_names:
    sheet_data = excel_file.parse(sheet_name)
    
    for _, row in sheet_data.iterrows():
        # Create a new element based on sheet name
        if sheet_name == 'Residente_PNatural':
            element = ET.SubElement(root, 'personaNaturalResidente')
        elif sheet_name == 'Residente_PJuridica':
            element = ET.SubElement(root, 'personaJuridicaResidente')
        elif sheet_name == 'Residente_SinPJuridica':
            element = ET.SubElement(root, 'personaSinPJuridica')
        elif sheet_name == 'Residente_SinNaturaleza':
            element = ET.SubElement(root, 'personaSinNaturaleza')
        elif sheet_name == 'NoResidente':
            element = ET.SubElement(root, 'noResidente')
        elif sheet_name == 'NoResidenteDeuda':
            element = ET.SubElement(root, 'noResidenteDeuda')
        
        # Add child elements based on column names
        for column_name, value in row.items():
            child_element = ET.SubElement(element, column_name)
            child_element.text = str(value)

# Create an ElementTree object and write to an XML file
tree = ET.ElementTree(root)
tree.write('output.xml', encoding='UTF-8', xml_declaration=True)
