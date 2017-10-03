import re

def ExtractId(text):
    """
    Extracts wine id from url like "http:\/\/www.cellartracker.com\/wine.asp?iWine=1" 
    """
    if not text: return None
    array_str = text.split("iWine=")
    return int(array_str[1]) if len(array_str) > 1 else None

def FindYear(text):
    """
    Extracts year in the wine name if it exists
    """
    try:
        m = re.search(r"\s*(\d{4})\s*", text)
        return int(m.group(0)) if m else None
    except:
        return None

