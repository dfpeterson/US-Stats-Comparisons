# US Stats Comparisons Todo  

## Architecture & Refactoring  

- [x] Generate Stats for a date  
- [x] Generate comparison to most recent data (negation)  
- [x] Subtraction logic  
  - [x] Test interval
- [x] Addition logic  
  - [x] Test logic  
- [x] See if I can convert the dates to datetime objects and make a getter with YYYY-MM-DD (is there a dateimte limit?)  
- [ ] Refactor code into multiple files  
  - [x] Split into files  
  - [x] Create generic population/delta class  
  - [x] Create generic GDP/delta class  
  - [ ] Regenerate data for generic classes  
- [ ] Lint code  
  - [ ] Replace markdown with proper functions  
  - [ ] Consistent quote use  
  - [ ] Add typing  
  - [ ] Docstrings (with data formats)  
- [ ] Try polars or duckdb  

### Data sets and handlers

- [ ] Clean up preprocessing scripts  
  - [ ] Move them into repository  
  - [ ] Add web data pulling capability  
  - [ ] Backfill historical data (1600–1800)  
- [ ] Consolidate shared utilities (parsing, date alignment, sources)  
- [ ] "No Data" handlers and ability to turn on/off dashboard features when there is no data  

---

## Economy & Daily Life

- [ ] Stock market  

### GDP

- [x] US and World GDP  
  - [x] Add to deltas  
- [x] Add a currency symbol and placement (with defaults)  

### Inflation and Price Levels

- [x] Add inflation data  
  - [ ] Add a currency symbol and placement (with defaults)
  - [ ] Baseline dollar amount in currency of choice

### Prices & Wages

- [ ] Add food commodity prices (beef, corn, staples)  
- [ ] Add wages (if sources are available)  

### Economic Visualizations

- [ ] Inflation graph of +/- 10y  

---

## Government & Politics

### Executive Branch

- [x] US Presidents  
  - [x] Resize portraits
  - [x] Generate inaugurations csv
  - [x] Add class to us_stats
  - [ ] The President's party
  - [ ] x days into y term
- [ ] The Vice Presidents
  - [ ] The Vice Presidents' party

### Legislative Branch

- [ ] Congressional makeup (and number)  
  - [ ] Number of seats over time  
  - [ ] Composition by party  

### Judicial Branch

- [ ] Justices  
  - [ ] Who appointed each justice  
  - [ ] How long they had been serving at the time  
- [ ] Major Supreme Court rulings  

### Constitutional Development

- [x] Constitutional Amendments  
  - [ ] A visual representation of the constitutional amendments  

### Government Eras

- [ ] The colonial, confederate and federal systems  

---

## Population & Society

- [x] US and World population  
  - [x] Add to deltas  
- [ ] Native peoples tracker  
- [ ] Immigration data  
- [ ] Urban vs. rural breakdown  
- [ ] Demographic patterns (as data allows)  

---

## Historical Context & Events

- [ ] Major inventions  
- [ ] Wars  
  - [ ] The Revolutionary War  
  - [ ] The Civil War period  
- [ ] Tallest building tracker  
- [ ] End of slavery indicator  
- [ ] The alcohol prohibition period  
- [ ] Who can vote tracker  

---

## Geography & Environment

- [x] Number of States  
  - [x] Last state to join the union
- [ ] Map integrations  
- [ ] Territorial expansion timeline  
- [ ] State boundary evolution  
- [ ] Environmental events (storms, droughts, disasters)  

---

## Visualizations

### US Flags  

- [x] Add images  
- [x] Add to state admissions as a 1st pass  
- [x] Create a flags file (since flags are synched to 4th of July)  
- [x] Create a flag class  
- [ ] See if there is a realistic image alternative  

### Graphic Visualizations

- [ ] Waffle or chart of population/gdp
- [ ] Congressional makeup  
- [ ] Stock market graph

---

## Documentation

- [ ] Add data attributions  
- [ ] Add language about data estimates  
- [ ] Add DATA_SOURCES.md  
- [ ] Add ESTIMATES_AND_LIMITS.md  
- [ ] Expand documentation  
- [ ] Add architecture diagram to docs  
- [ ] Finalize README  
