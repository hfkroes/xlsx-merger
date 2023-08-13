# xlsx-merger
Python script to easily merge multiple excel sheets by exact matching of column records

# Installation
Clone the github page:
```
git clone https://github.com/HectorKroes/xlsx-merger
```
And install the required python libraries:
```
pip install -r requirements.txt
```
# Utilization
To execute the script:
```
merger.py [input_file] [output_file] [columns_to_be_matched] 
```
As an example, if I want to merge different sheets in the file `a.xlsx` matching `var1` and `var2` generating a new file `b.xlxs`, I would do:
```
merger.py a.xlsx b.xlsx var1 var2
```
All matched variables should be divided by a space.
