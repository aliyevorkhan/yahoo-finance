# yahoo-finance

### List of Companies:
* PD
* ZUO
* PINS
* ZM
* PVTL (!)
* DOCU
* CLDR
* RUN

### Completed tasks
1. Tried to scrapping all listed companies historical data above with MAX Period. 
2. Successfully scrapped all companies historical data with MAX Period except PVTL.
3. Added to sqlite3 database
4. Added FastAPI service for serving data
5. Added sample request.py to getting companies data from FastAPI 

### Install requirements
```bash
pip3 install -r requirements.txt
```

### Scrap datas and start server
```bash
python3 scrap.py
```
### GET REQUEST to server with sample below
```bash
python3 request.py
```
