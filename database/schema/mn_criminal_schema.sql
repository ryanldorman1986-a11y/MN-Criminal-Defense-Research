CREATE TABLE IF NOT EXISTS cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_name TEXT NOT NULL,
    citation TEXT UNIQUE NOT NULL,
    case_number TEXT,
    court TEXT NOT NULL,
    date_filed DATE NOT NULL,
    date_decided DATE,
    judge_name TEXT,
    full_text TEXT,
    summary TEXT,
    case_type TEXT,
    crime_category TEXT,
    outcome TEXT,
    defendant_name TEXT,
    source TEXT,
    source_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    downloaded_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS statutes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statute_code TEXT UNIQUE NOT NULL,
    chapter TEXT NOT NULL,
    section TEXT NOT NULL,
    title TEXT NOT NULL,
    full_text TEXT NOT NULL,
    statute_type TEXT,
    max_penalty TEXT,
    years_imprisonment INTEGER,
    revisor_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS precedents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    precedent_category TEXT NOT NULL,
    defense_principle TEXT NOT NULL,
    defense_value TEXT NOT NULL,
    holding TEXT NOT NULL,
    times_cited INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(id)
);

CREATE TABLE IF NOT EXISTS defense_arguments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    argument_type TEXT NOT NULL,
    argument_name TEXT NOT NULL,
    was_successful BOOLEAN NOT NULL,
    outcome TEXT,
    strategy_explanation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(id)
);

CREATE TABLE IF NOT EXISTS hearings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    hearing_type TEXT NOT NULL,
    hearing_date DATE,
    status TEXT,
    outcome TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(id)
);

CREATE INDEX idx_cases_court ON cases(court);
CREATE INDEX idx_cases_date_filed ON cases(date_filed);
CREATE INDEX idx_cases_citation ON cases(citation);
CREATE INDEX idx_statutes_code ON statutes(statute_code);
CREATE INDEX idx_precedents_defense_value ON precedents(defense_value);
CREATE INDEX idx_defense_args_case ON defense_arguments(case_id);
