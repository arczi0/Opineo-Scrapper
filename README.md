
# Opineo.pl Scrapper

Basic script to get user reviews from Opineo.pl

## Tech Stack
- Python


## Screenshots (CSV Preview)
![csv-preview](https://user-images.githubusercontent.com/48137366/211759172-e3a88b29-9ac7-49fb-a5fb-83ea699246b4.png)


## Run Locally

Clone the project

```bash
git clone https://github.com/arczi0/Opineo-Scrapper
```

Create virtual environment

```bash
python -m venv venv
```

For Windows use:
```bash
venv\Scripts\activate
```

Go to the project directory

```bash
cd Opineo-Scrapper
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run script

```bash
python scrapper.py --url <product url> --delay <requests delay>
```

