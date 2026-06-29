import sqlite3
import os

db_path = "database/data/mn_criminal_defense.db"

def clear_screen():
    os.system('clear')

def show_menu():
    clear_screen()
    print("=" * 50)
    print("MN CRIMINAL DEFENSE RESEARCH DATABASE")
    print("=" * 50)
    print("\n1. View all cases")
    print("2. Search cases by keyword")
    print("3. View database statistics")
    print("4. Add a new statute")
    print("5. View all statutes")
    print("6. Exit")
    print("\n" + "=" * 50)

def view_all_cases():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, case_name, citation, date_filed FROM cases LIMIT 10")
    results = cursor.fetchall()
    conn.close()
    
    clear_screen()
    print("=" * 50)
    print("ALL CASES")
    print("=" * 50)
    
    if results:
        for row in results:
            print(f"\nID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Citation: {row[2]}")
            print(f"Date: {row[3]}")
    else:
        print("\nNo cases in database yet.")
    
    print("\n" + "=" * 50)
    input("Press Enter to continue...")

def search_cases():
    keyword = input("\nEnter search keyword: ")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, case_name, citation FROM cases WHERE case_name LIKE ? OR citation LIKE ? LIMIT 10",
        (f"%{keyword}%", f"%{keyword}%")
    )
    results = cursor.fetchall()
    conn.close()
    
    clear_screen()
    print("=" * 50)
    print(f"SEARCH RESULTS FOR: {keyword}")
    print("=" * 50)
    
    if results:
        for row in results:
            print(f"\nID: {row[0]}")
            print(f"Case: {row[1]}")
            print(f"Citation: {row[2]}")
    else:
        print("\nNo cases found.")
    
    print("\n" + "=" * 50)
    input("Press Enter to continue...")

def view_stats():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM cases")
    case_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM statutes")
    statute_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM precedents")
    precedent_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM defense_arguments")
    defense_count = cursor.fetchone()[0]
    
    conn.close()
    
    clear_screen()
    print("=" * 50)
    print("DATABASE STATISTICS")
    print("=" * 50)
    print(f"\nCases: {case_count}")
    print(f"Statutes: {statute_count}")
    print(f"Precedents: {precedent_count}")
    print(f"Defense Arguments: {defense_count}")
    print("\n" + "=" * 50)
    input("Press Enter to continue...")

def add_statute():
    clear_screen()
    print("=" * 50)
    print("ADD NEW STATUTE")
    print("=" * 50)
    
    code = input("\nStatute Code (e.g., 609.52): ")
    chapter = input("Chapter (e.g., 609): ")
    section = input("Section (e.g., 52): ")
    title = input("Title: ")
    statute_type = input("Type (felony/misdemeanor): ")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO statutes (statute_code, chapter, section, title, full_text, statute_type)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (code, chapter, section, title, title, statute_type))
        conn.commit()
        print("\n✅ Statute added successfully!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    conn.close()
    input("Press Enter to continue...")

def view_statutes():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, statute_code, title, statute_type FROM statutes LIMIT 10")
    results = cursor.fetchall()
    conn.close()
    
    clear_screen()
    print("=" * 50)
    print("ALL STATUTES")
    print("=" * 50)
    
    if results:
        for row in results:
            print(f"\nID: {row[0]}")
            print(f"Code: {row[1]}")
            print(f"Title: {row[2]}")
            print(f"Type: {row[3]}")
    else:
        print("\nNo statutes in database.")
    
    print("\n" + "=" * 50)
    input("Press Enter to continue...")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            view_all_cases()
        elif choice == "2":
            search_cases()
        elif choice == "3":
            view_stats()
        elif choice == "4":
            add_statute()
        elif choice == "5":
            view_statutes()
        elif choice == "6":
            clear_screen()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
