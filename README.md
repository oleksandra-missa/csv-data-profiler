# CSV Data Profiler

A simple command-line tool written in Python for profiling `.csv` files.

## 📋 Features
- Displays basic stats: count, mean, median, std, min, max
- Shows data types and null value counts
- Outputs column-level summaries

## 🚀 Usage
```bash
python profiler.py sample_data/employees.csv
```

## 📁 Sample Files
- `employees.csv`: Basic employee dataset
- `sales.csv`: Sales data with dates and regions

## 🛠️ Requirements
- pandas

Install with:

```bash
pip install pandas
```

## 🔧 Example Output
```bash
$ python profiler.py sample_data/sales.csv

Dataset: sample_data/sales.csv
----------------------------------------
Shape: (5, 3)

Column: Date
 - Type: datetime64[ns]
 - Missing: 0

Column: Sales
 - Type: float64
 - Missing: 1
 - Mean: 235.0
 - Median: 235.0

Column: Region
 - Type: object
 - Missing: 0
 - Unique Values: 4
```

