# Basic Data Pre-processing
* Manually pre-processing data without using addition module (numpy, pandas, ...).
* Support command line only.

|FUNCTIONALITY                                                                                 |         FILE           |
|---                                                                                           |:---:                   |
|1. List attributes with missing values.                                                       |     [list_missing.py](list_missing.py)    | 
|2. Count the number of samples with missing values.                                           |    [count_missing.py](count_missing.py)    |
|3. Impute data using mean or median (for numeric attributes) or mode (for nominal attributes).|        [impute.py](impute.py)       |
|4. Remove attributes with amount of missing values exceeds the threshold.                     |  [remove_attributes.py](remove_attributes.py)  |
|5. Remove samples with amount of missing values exceeds the threshold.                        |    [remove_samples.py](remove_samples.py)   |
|6. Remove duplicate samples.                                                                  |     [remove_clone.py](remove_clone.py)    |
|7. Normalize a numeric attribute using min-max scaling or standardization                     |      [normalize.py](normalize.py)      |
|8. Calculate the input math expression of numeric attributes.                                 | [evaluate_attributes.py](evaluate_attributes.py) |