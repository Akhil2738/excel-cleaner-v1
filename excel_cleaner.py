import pandas as pd

def clean_excel(input_file, output_file):
    df = pd.read_excel(input_file)

    # Drop completely empty rows
    df.dropna(how="all", inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Trim spaces in text columns
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()

    # Save cleaned file
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    clean_excel("input.xlsx", "clean_output.xlsx")
