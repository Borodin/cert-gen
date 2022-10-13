# Certificate generator
This is a simple PDF certificate generator from CSV file

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python3 main.py
  -t TEMPLATE, --template=template.html
  -c CSV, --csv=students.csv
```

## Example
```bash
python3 main.py -t template.html -c students.csv
```
```bash
python3 main.py -c "https://docs.google.com/spreadsheets/d/1rp7c39yX3K84ImV8UQQrb3RXk99LgDz1ykCCYEJ0USo/edit?usp=sharing"
```


## Run in Docker

```bash
docker build -t sert-gen .
docker run -it --rm -v $(pwd):/app sert-gen -c students.csv
```