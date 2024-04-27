import pandas as pd
from sklearn import preprocessing


class DataProcessor:
    def __init__(self):
        pass

    def prompt_data_path(self):
        """Prompt user to input data path."""
        data_path = input("Please enter the path to your data file: ")
        return data_path

    def determine_data_type(self, df):
        """Determine data types of columns."""
        data_types = df.dtypes.to_dict()
        return data_types

    def read_data(self, file_path):
        """Read data from specified path, handling potential errors."""
        try:
            df = pd.read_csv(file_path)
            return df
        except FileNotFoundError:
            print("Error: File not found. Please check the path and try again.")
            return None
        except pd.errors.ParserError:
            print("Error: Invalid file format. Please ensure it's a valid CSV file.")
            return None

    def basic_analysis(self, df):
        """Perform basic analysis on data."""
        head = df.head()
        data_types = self.determine_data_type(df)
        summary_statistics = df.describe()
        return head, data_types, summary_statistics

    def handle_missing_values(self, df, strategy='mean'):
        """Handle missing values in the DataFrame, with strategy flexibility."""
        # Iterate through columns
        for col in df.columns:
            # Handle missing values for numeric columns
            if df[col].dtype in ['int64', 'float64']:
                if strategy == 'mean':
                    df[col].fillna(df[col].mean(), inplace=True)
                elif strategy == 'median':
                    df[col].fillna(df[col].median(), inplace=True)
                elif strategy == 'mode':
                    df[col].fillna(df[col].mode()[0], inplace=True)
                elif strategy == 'ffill':
                    df[col].fillna(method='ffill', inplace=True)
                elif strategy == 'bfill':
                    df[col].fillna(method='bfill', inplace=True)
            # Handle missing values for object columns
            elif df[col].dtype == 'object':
                df[col].fillna(df[col].mode()[0], inplace=True)
            # Handle missing values for other data types
            else:
                pass  # You can add handling for other data types if needed
        return df

    def encode_categorical_data(self, df, columns):
        """Encode categorical data using one-hot encoding."""
        encoded_df = pd.get_dummies(df, columns=columns, drop_first=False)
        return encoded_df

    def label_encode_categorical_data(self, df, columns):
        """Label encode categorical data."""
        encoder = preprocessing.LabelEncoder()
        for column in columns:
            df[column] = encoder.fit_transform(df[column])
        return df


# Example Notebook (replace with your actual script path)
from your_script import DataProcessor  # Replace with the path to your script

# Create DataProcessor object
data_processor = DataProcessor()

# User input for data path
data_path = data_processor.prompt_data_path()

# Read data with error handling
df = data_processor.read_data(data_path)
if df is not None:  # Check if data was read successfully

    # Basic analysis
    head, data_types, summary_statistics = data_processor.basic_analysis(df)
    print("Head of the data:")
    print(head)
    print("\nData types:")
    print(data_types)
    print("\nSummary statistics:")
    print(summary_statistics)

    # Choose strategy for handling missing values (example)
    chosen_strategy = input("Choose a strategy for handling missing values (mean, median, mode, ffill, bfill): ")

    # Handle missing values
    df = data_processor.handle_missing_values(df.copy(), strategy=chosen_strategy)

    # Choose columns for categorical encoding (example)
    categorical_columns = ['column1', 'column2']  # Replace with actual column names

    # One-hot encoding
    encoded_df_onehot = data_processor.encode_categorical_data(df.copy(), categorical_columns)

    
