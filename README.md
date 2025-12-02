# US Stats Comparisons Dashboard

This project is an interactive **Streamlit dashboard** that visualizes historical U.S. and world data to provide a quick, approachable snapshot of what life looked like at different points in time. It brings together population trends, economic indicators, government structure, and major historical context. The goal isn’t to create a comprehensive reconstruction of history, but to make it easy to compare “then and now” using real data presented clearly and transparently.

Working with historical data comes with challenges and limits. Many early-period datasets involve estimates, reconstructed figures, or gaps in the record. Likewise, different groups—such as enslaved people, Indigenous nations, and communities at the margins of documented life—had customs and systems of value that weren’t always captured by the record keepers of the time or don’t map neatly onto modern frameworks. A continuing goal of this project is to acknowledge these limits while still presenting data in a way that is readable, honest, and helpful for modern comparison.

---

## Dashboard Overview

The dashboard is organized into themed sections. Some features are already implemented, while others are planned for future versions.

---

## Implemented Features

- Population comparisons (U.S. & World)  
- GDP data integration  
- Historical U.S. flags  
- State admissions + flag synchronization  
- U.S. presidents  

---

## Future Features (Planned / In Progress)

### 1. Economy & Daily Life

- Commodity prices (beef, corn, staples)  
- Wages & income indicators  
- Cost of living metrics  
- Inflation/deflation visualizations  
- GDP delta visualizations  
- Trade, production, and market indicators  
- Historical stock market timeline  

### 2. Government & Politics

- Presidents:  
  - Party affiliation  
  - Vice Presidents + party  
- Congress:  
  - Congressional makeup (House/Senate composition)  
  - Seat counts over time  
- Supreme Court:  
  - Justices  
  - Major rulings  
- Constitutional amendments:  
  - Text + interpretation  
  - Timeline visualization  
- Major legislation timeline  
- Government eras (colonial → confederate → federal)  

### 3. Population & Society

- End of slavery indicator  
- Voting rights eligibility timeline  
- Immigration indicators  
- State populations  
- Urban vs. rural breakdown  
- Demographic patterns (as data allows)  
- Indicators for Indigenous communities  
- Indicators for enslaved populations  

### 4. Historical Context & Events

- Major wars (Revolutionary → Civil War → modern)  
- Major inventions & technologies  
- Tallest building timeline  
- Prohibition indicator  
- Major historical events & milestones  
- Additional era markers  

### 5. Geography & Environment

- State & territorial boundaries over time  
- Streamlit map integrations  
- U.S. land expansion timeline  
- Environmental indicators (weather extremes, disasters, major environmental events)  

---

## Tech Stack

- **Python**  
- **Streamlit**  
- **Pandas** (exploring Polars/DuckDB)  
- Modular class-based data models  
- CSV source datasets (with future web scraping planned)

---

## Running the App

```bash
streamlit run app/app.py

```
