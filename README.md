# df4loop

df4loop supports general purpose processe that requires a combination of both pandas.DataFrame and loop. Specifically, the mission of df4loop is to "speed up processing" and "make complex code intuitive" at low installation costs.

## Installation

```sh
pip install df4loop
```

## Usage

### DFIterator

DFIterator helps developers writing the following code. This is code written using `pandas.DataFrame.iterrows` for the purpose of referencing a value by row.

```py
for index, row in df.iterrows():
    tmp = row["column_1"]
```

DFIterator reproduces this process and speeds it up. Actually, DataFrame and its row `pandas.Series` are converted to lists and dictionaries to speed up. However, the usage is almost the same.

```py
from df4loop import DFIterator

df_iterator = DFIterator(df)
for index, row in df_iterator.iterrows():
    tmp = row["column_1"]
```

If you do not need to output the index, set `return_index = False`.

```py
from df4loop import DFIterator

df_iterator = DFIterator(df)
for row in df_iterator.iterrows(return_index=False):
    tmp = row["column_1"]
```

### DFGenerator

Adding columns to the DataFrame in a loop will take a long time to process. The secret to speeding up is to organize rows in a list or dictionary and then make them pandas.DataFrame at once. DFGenerator supports this process for intuitive implementation.

```py
from df4loop import DFGenerator

# When appending Rows in a dictionary, it is not necessary to specify columns.
df_generator = DFGenerator(columns=sample_df.columns.values.tolist())
for _, row in sample_df.iterrows():
    tmp_row = {
        "column_1": row["column_1"],
        "column_2": row["column_2"],
        "column_3": row["column_3"],
    }
    df_generator.append(tmp_row)
df = df_generator.generate_df()
```

```py
from df4loop import DFGenerator

df_generator = DFGenerator(columns=sample_df.columns.values.tolist())
for _, row in sample_df.iterrows():
    tmp_row = [
        row["column_1"],
        row["column_2"],
        row["column_3"],
    ]
    df_generator.append(tmp_row)
df = df_generator.generate_df()
```

