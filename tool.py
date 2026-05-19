import pandas as pd
import numpy as np

def age_to_age_range(age):
    if 20 <= age <= 30:
        return '20-30'
    elif 31 <= age <= 40:
        return '31-40'
    elif 41 <= age <= 50:
        return '41-50'
    elif 51 <= age <= 60:
        return '51-60'
    else:
        return 'Other'

def zip_code_to_prefix(zip_code):
    return str(zip_code)[:3]

def suppress_sensitive_info(diagnosis):
    return '*'

def anonymize_column(data, column_name, method):
    if method == 'Suppression':
        if column_name == 'Diagnosis':
            data[column_name] = data[column_name].apply(suppress_sensitive_info)
        else:
            data[column_name] = data[column_name].apply(suppress_sensitive_info)
    elif method == 'Generalization':
        if column_name == 'Age':
            data[column_name] = data[column_name].apply(age_to_age_range)
        elif column_name == 'Zip Code':
            data[column_name] = data[column_name].apply(zip_code_to_prefix)

    return data


if __name__ == "__main__":
    # Create a sample dataset (replace with your actual data)
    columns = ["Name", "Age", "Zip Code", "Diagnosis"]
    data = pd.DataFrame({
        "Name": ["John", "Alice", "Bob"],
        "Age": [25, 42, 55],
        "Zip Code": [98101, 90210, 12345],
        "Diagnosis": ["Cancer", "Diabetes", "Hypertension"]
    })

    # Anonymize the dataset
    anonymized_data = anonymize_column(data, column_name="Age", method="Generalization")
    anonymized_data = anonymize_column(anonymized_data, column_name="Zip Code", method="Generalization")
    anonymized_data = anonymize_column(anonymized_data, column_name="Diagnosis", method="Suppression")

    # Print the anonymized dataset
    print(anonymized_data)
