import webbrowser
import re
import sys
from colorama import init, Fore

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# ASCII art logo
logo = """
 _____                      _    
|  __ \                    | |   
| |  \/  ___    ___   _ __ | | __
| | __  / _ \  / _ \ | '__|| |/ /
| |_\ \| (_) || (_) || |   |   < 
 \____/ \___/  \___/ |_|   |_|\_\
                                 
"""

def print_logo():
    print(Fore.RED + logo)

def print_help():
    help_text = """
--- Goork Help ---
You can use the following parameters in your search query:
- (group): Group terms (e.g., '(python developers)')
- *wildcard*: Wildcard terms (e.g., '*programming*')
- "exact phrase": Exact phrases (e.g., '"python tutorial"')
- numrange: Number range (e.g., '1..100')
- -exclude: Words to exclude (e.g., '-java')
- +include: Words to include (e.g., '+python')
- logical_or: Logical OR terms (e.g., 'python | javascript')
- ~synonym: Synonyms (e.g., '~python')
- @social: Social handle (e.g., '@python')
- after: Date after (e.g., 'after:2022-01-01')
- allintitle: All in title (e.g., 'allintitle:python tutorial')
- allinurl: All in URL (e.g., 'allinurl:python.org')
- allintext: All in text (e.g., 'allintext:python documentation')
- around: AROUND term (e.g., 'python AROUND(5) javascript')
- author: Author name (e.g., 'author:John Doe')
- before: Date before (e.g., 'before:2022-01-01')
- cache: Cached pages (e.g., 'cache:python.org')
- contains: Contains (e.g., 'contains:python')
- define: Definitions (e.g., 'define:python')
- filetype: File type (e.g., 'filetype:pdf')
- inanchor: In anchor (e.g., 'inanchor:python')
- index_of: Index of (e.g., 'index of:python')
- info: Info (e.g., 'info:python')
- intext: In text (e.g., 'intext:python')
- intitle: In title (e.g., 'intitle:python')
- inurl: In URL (e.g., 'inurl:python')
- link: Link (e.g., 'link:python.org')
- location: Location (e.g., 'location:New York')
- safesearch: SafeSearch (e.g., 'safesearch:strict')
- source: Source (e.g., 'source:github')
- site: Site (e.g., 'site:python.org')
- stock: Stock (e.g., 'stock:GOOGL')
- weather: Weather (e.g., 'weather:New York')
"""
    print(Fore.RED + help_text.strip())

def parse_input(user_input):
    params = {
        'query': '',
        'group': '',
        'wildcard': '',
        'exact': '',
        'numrange': ('', ''),
        'exclude': '',
        'include': '',
        'logical_or': ('', ''),
        'synonym': '',
        'social': '',
        'after': '',
        'allintitle': '',
        'allinurl': '',
        'allintext': '',
        'around': ('', '', ''),
        'author': '',
        'before': '',
        'cache': '',
        'contains': '',
        'define': '',
        'filetype': '',
        'inanchor': '',
        'index_of': '',
        'info': '',
        'intext': '',
        'intitle': '',
        'inurl': '',
        'link': '',
        'location': '',
        'safesearch': '',
        'source': '',
        'site': '',
        'stock': '',
        'weather': ''
    }

    patterns = {
        'group': r'\(.*?\)',
        'wildcard': r'\*.*?\*',
        'exact': r'"[^"]+"',
        'numrange': r'\d+\.\.\d+',
        'exclude': r'-\w+',
        'include': r'\+\w+',
        'logical_or': r'\w+\s*\|\s*\w+',
        'synonym': r'~\w+',
        'social': r'@\w+',
        'after': r'after:\S+',
        'allintitle': r'allintitle:\S+',
        'allinurl': r'allinurl:\S+',
        'allintext': r'allintext:\S+',
        'around': r'\w+\s*AROUND\(\d+\)\s*\w+',
        'author': r'author:\S+',
        'before': r'before:\S+',
        'cache': r'cache:\S+',
        'contains': r'contains:\S+',
        'define': r'define:\S+',
        'filetype': r'filetype:\S+',
        'inanchor': r'inanchor:\S+',
        'index_of': r'index\s*of:\S+',
        'info': r'info:\S+',
        'intext': r'intext:\S+',
        'intitle': r'intitle:\S+',
        'inurl': r'inurl:\S+',
        'link': r'link:\S+',
        'location': r'location:\S+',
        'safesearch': r'safesearch:\S+',
        'source': r'source:\S+',
        'site': r'site:\S+',
        'stock': r'stock:\S+',
        'weather': r'weather:\S+'
    }

    for key, pattern in patterns.items():
        matches = re.findall(pattern, user_input)
        if matches:
            if key in ['numrange', 'logical_or', 'around']:
                params[key] = tuple(matches[0].split())
            else:
                params[key] = matches[0].strip(patterns[key][:3])

    # The main query is the remaining part after extracting all known patterns
    params['query'] = re.sub('|'.join(patterns.values()), '', user_input).strip()

    return params

def create_search_query(params):
    query_parts = []

    for key, value in params.items():
        if key == 'query':
            query_parts.append(value)
        elif key == 'group' and value:
            query_parts.append(f"({value})")
        elif key == 'wildcard' and value:
            query_parts.append(f"{value}*")
        elif key == 'exact' and value:
            query_parts.append(f'"{value}"')
        elif key == 'numrange' and value[0] and value[1]:
            query_parts.append(f"{value[0]}..{value[1]}")
        elif key == 'exclude' and value:
            for word in re.split(r'\s*,\s*', value):
                query_parts.append(f"-{word.strip()}")
        elif key == 'include' and value:
            for word in re.split(r'\s*,\s*', value):
                query_parts.append(f"+{word.strip()}")
        elif key == 'logical_or' and value[0] and value[1]:
            query_parts.append(f"{value[0]} | {value[1]}")
        elif key == 'synonym' and value:
            query_parts.append(f"~{value}")
        elif key == 'social' and value:
            query_parts.append(f"@{value}")
        elif key == 'after' and value:
            query_parts.append(f"after:{value}")
        elif key == 'allintitle' and value:
            query_parts.append(f"allintitle:{value}")
        elif key == 'allinurl' and value:
            query_parts.append(f"allinurl:{value}")
        elif key == 'allintext' and value:
            query_parts.append(f"allintext:{value}")
        elif key == 'around' and value[0] and value[1] and value[2]:
            query_parts.append(f"{value[0]} AROUND({value[1]}) {value[2]}")
        elif key == 'author' and value:
            query_parts.append(f"author:{value}")
        elif key == 'before' and value:
            query_parts.append(f"before:{value}")
        elif key == 'cache' and value:
            query_parts.append(f"cache:{value}")
        elif key == 'contains' and value:
            query_parts.append(f"contains:{value}")
        elif key == 'define' and value:
            query_parts.append(f"define:{value}")
        elif key == 'filetype' and value:
            query_parts.append(f"filetype:{value}")
        elif key == 'inanchor' and value:
            query_parts.append(f"inanchor:{value}")
        elif key == 'index_of' and value:
            query_parts.append(f"index of:{value}")
        elif key == 'info' and value:
            query_parts.append(f"info:{value}")
        elif key == 'intext' and value:
            query_parts.append(f"intext:{value}")
        elif key == 'intitle' and value:
            query_parts.append(f"intitle:{value}")
        elif key == 'inurl' and value:
            query_parts.append(f"inurl:{value}")
        elif key == 'link' and value:
            query_parts.append(f"link:{value}")
        elif key == 'location' and value:
            query_parts.append(f"location:{value}")
        elif key == 'safesearch' and value:
            query_parts.append(f"safesearch:{value}")
        elif key == 'source' and value:
            query_parts.append(f"source:{value}")
        elif key == 'site' and value:
            query_parts.append(f"site:{value}")
        elif key == 'stock' and value:
            query_parts.append(f"stock:{value}")
        elif key == 'weather' and value:
            query_parts.append(f"weather:{value}")

    return " ".join(query_parts)

def perform_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(search_url)
    print(Fore.RED + f"Search URL: {search_url}")

def main():
    print_logo()
    print(Fore.RED + "Type 'help' for a list of search parameters and their usage.")
    user_input = input("Enter your search query: ")

    if user_input.lower() == 'help':
        print_help()
        return

    params = parse_input(user_input)
    query = create_search_query(params)
    perform_search(query)

if __name__ == "__main__":
    main()
