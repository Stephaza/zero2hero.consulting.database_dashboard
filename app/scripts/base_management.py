import pandas as pd
import openpyxl
from app.models.base import Base
from app.extensions import db

# Lecture Inputs
inputs = {
    'data route': './app/data/raw_data/',
    'data file': 'raw_database.xlsx',

    'selected columns': {
        'Collection ID': ['id'],
        'Objecttyp Name': ['objecttype_name'],
        'Collection': ['collection'],
        'Institution': ['institution'],
    }
}

# Get Dataset Function
def get_dataset(inputs):
    df = pd.read_excel(inputs['data route'] + inputs['data file'])
    return df

# Get Selected Columns Function
def get_selected_columns(df, inputs):
    df = df[inputs['selected columns'].keys()]
    return df

# Create Base Objects
def create_base_objects(df):
    #iterates through raw_database rows
    for index, row in df.iterrows():
        #checks for existing elements
        if Base.query.filter_by(id=row['Collection ID']).first():
            continue
        else:
            base = Base(
                id = row['Collection ID'],
                objecttype_name = row['Objecttyp Name'],
                collection = row['Collection'],
                institution = row['Institution']
            )
            db.session.add(base)
    db.session.commit()
    print('Objects Created')

if __name__ == '__main__':
    df = get_dataset(inputs)
    df = get_selected_columns(df, inputs)
    create_base_objects(df)
    print(df.head())