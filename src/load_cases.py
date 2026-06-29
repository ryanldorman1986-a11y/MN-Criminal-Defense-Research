import requests
import sqlite3
from pathlib import Path

db_path = "database/data/mn_criminal_defense.db"

def download_cases(query, limit=10):
    print(f"Downloading cases for: {query}")
    
    url = "https://www.courtlistener.com/api/rest/v3/opinions/"
    params = {
        "court": "mnctapp",
        "q": query,
        "limit": limit
    }
    
    headers = {
        "User-Agent": "MN-Criminal-Defense-Research/1.0"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            cases = data.get('results', [])
            print(f"Found {len(cases)} cases")
            return cases
        else:
            print(f"API returned: {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def store_cases(cases):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    count = 0
    for case in cases:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO cases 
                (case_name, citation, court, date_filed, source, source_url)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                case.get('case_name', 'Unknown'),
                case.get('citation', 'Unknown'),
                'Minnesota Court of Appeals',
                case.get('date_filed', ''),
                'courtlistener',
                case.get('absolute_url', '')
            ))
            count += 1
        except Exception as e:
            pass
    
    conn.commit()
    conn.close()
    print(f"Stored {count} cases")

if __name__ == "__main__":
    cases = download_cases("Minnesota criminal", limit=5)
    if cases:
        store_cases(cases)
    else:
        print("Could not download cases")
