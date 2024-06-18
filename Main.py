import webbrowser
import requests
from bs4 import BeautifulSoup
import re

def create_search_query(params):
    query_parts = []

    query_parts.append(params['query'])

    for key, value in params.items():
        if key == 'group':
            if value:
                query_parts.append(f"({value})")
        elif key == 'wildcard':
            if value:
                query_parts.append(f"{value}*")
        elif key == 'exact':
            if value:
                query_parts.append(f'"{value}"')
        elif key == 'numrange':
            if value[0] and value[1]:
                query_parts.append(f"{value[0]}..{value[1]}")
        elif key == 'exclude':
            if value:
                excluded_words = re.split(r'\s*,\s*', value)
                for word in excluded_words:
                    query_parts.append(f"-{word.strip()}")
        elif key == 'include':
            if value:
                included_words = re.split(r'\s*,\s*', value)
                for word in included_words:
                    query_parts.append(f"+{word.strip()}")
        elif key == 'logical_or':
            if value[0] and value[1]:
                query_parts.append(f"{value[0]} | {value[1]}")
        elif key == 'synonym':
            if value:
                query_parts.append(f"~{value}")
        elif key == 'social':
            if value:
                query_parts.append(f"@{value}")
        elif key == 'after':
            if value:
                query_parts.append(f"after:{value}")
        elif key == 'allintitle':
            if value:
                query_parts.append(f"allintitle:{value}")
        elif key == 'allinurl':
            if value:
                query_parts.append(f"allinurl:{value}")
        elif key == 'allintext':
            if value:
                query_parts.append(f"allintext:{value}")
        elif key == 'around':
            if value[0] and value[1] and value[2]:
                query_parts.append(f"{value[0]} AROUND({value[1]}) {value[2]}")
        elif key == 'author':
            if value:
                query_parts.append(f"author:{value}")
        elif key == 'before':
            if value:
                query_parts.append(f"before:{value}")
        elif key == 'cache':
            if value:
                query_parts.append(f"cache:{value}")
        elif key == 'contains':
            if value:
                query_parts.append(f"contains:{value}")
        elif key == 'define':
            if value:
                query_parts.append(f"define:{value}")
        elif key == 'filetype':
            if value:
                query_parts.append(f"filetype:{value}")
        elif key == 'inanchor':
            if value:
                query_parts.append(f"inanchor:{value}")
        elif key == 'index_of':
            if value:
                query_parts.append(f"index of:{value}")
        elif key == 'info':
            if value:
                query_parts.append(f"info:{value}")
        elif key == 'intext':
            if value:
                query_parts.append(f"intext:{value}")
        elif key == 'intitle':
            if value:
                query_parts.append(f"intitle:{value}")
        elif key == 'inurl':
            if value:
                query_parts.append(f"inurl:{value}")
        elif key == 'link':
            if value:
                query_parts.append(f"link:{value}")
        elif key == 'location':
            if value:
                query_parts.append(f"location:{value}")
        elif key == 'afesearch':
            if value:
                query_parts.append(f"safesearch:{value}")
        elif key == 'ource':
            if value:
                query_parts.append(f"source:{value}")
        elif key == 'ite':
            if value:
                query_parts.append(f"site:{value}")
        elif key == 'tock':
            if value:
                query_parts.append(f"stock:{value}")
        elif key == 'weather':
            if value:
                query_parts.append(f"weather:{value}")

    return " ".join(query_parts)

def perform_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    return search_url

def main():
    print("--- Welcome to Goork: Advanced Google Dorking Tool ---")
    print("Enter search parameters or leave blank for optional ones.")

    query = input("Enter query (e.g., 'python programming'): ")
    group = input("Enter group (optional, e.g., 'python developers'): ")
    wildcard = input("Enter wildcard (optional, e.g., '*python*'): ")
    exact = input("Enter exact phrase (optional, e.g., '\"python tutorial\"'): ")
    numrange_start = input("Enter number range start (optional, e.g., '1'): ")
    numrange_end = input("Enter number range end (optional, e.g., '10'): ")
    exclude = input("Enter words to exclude, separated by commas (optional, e.g., 'java, c++'): ")
    include = input("Enter words to include, separated by commas (optional, e.g., 'python, programming'): ")
    logical_or_term1 = input("Enter first logical OR term (optional, e.g., 'python'): ")
    logical_or_term2 = input("Enter second logical OR term (optional, e.g., 'javascript'): ")
    synonym = input("Enter synonym (optional, e.g., '~python'): ")
    social = input("Enter social handle (optional, e.g., '@python'): ")
    after = input("Enter after date (optional, e.g., '2022-01-01'): ")
    allintitle = input("Enter allintitle (optional, e.g., 'python tutorial'): ")
    allinurl = input("Enter allinurl (optional, e.g., 'python.org'): ")
    allintext = input("Enter allintext (optional, e.g., 'python documentation'): ")
    around_term1 = input("Enter first AROUND term (optional, e.g., 'python'): ")
    around_proximity = input("Enter AROUND proximity (optional, e.g., '5'): ")
    around_term2 = input("Enter second AROUND term (optional, e.g., 'javascript'): ")
    author = input("Enter author (optional, e.g., 'John Doe'): ")
    before = input("Enter before date (optional, e.g., '2022-01-01'): ")
    cache = input("Enter cache (optional, e.g., 'cache:python'): ")
    contains = input("Enter contains (optional, e.g., 'contains:python'): ")
    define = input("Enter define (optional, e.g., 'define:python'): ")
    filetype = input("Enter filetype (optional, e.g., 'filetype:pdf'): ")
    inanchor = input("Enter inanchor (optional, e.g., 'inanchor:python'): ")
    index_of = input("Enter index of (optional, e.g., 'index of:python'): ")
    info = input("Enter info (optional, e.g., 'info:python'): ")
    intext = input("Enter intext (optional, e.g., 'intext:python'): ")
    intitle = input("Enter intitle (optional, e.g., 'intitle:python'): ")
    inurl = input("Enter inurl (optional, e.g., 'inurl:python.org'): ")
    link = input("Enter link (optional, e.g., 'link:python.org'): ")
    location = input("Enter location (optional, e.g., 'location:usa'): ")
    safesearch = input("Enter safesearch (optional, e.g., 'afesearch:on'): ")
    source = input("Enter source (optional, e.g., 'ource:python.org'): ")
    site = input("Enter site (optional, e.g., 'ite:python.org'): ")
    stock = input("Enter stock (optional, e.g., 'tock:python'): ")
    weather = input("Enter weather (optional, e.g., 'weather:usa'): ")

    params = {
        'query': query,
        'group': group,
        'wildcard': wildcard,
        'exact': exact,
        'numrange': (numrange_start, numrange_end),
        'exclude': exclude,
        'include': include,
        'logical_or': (logical_or_term1, logical_or_term2),
        'synonym': synonym,
        'ocial': social,
        'after': after,
        'allintitle': allintitle,
        'allinurl': allinurl,
        'allintext': allintext,
        'around': (around_term1, around_proximity, around_term2),
        'author': author,
        'before': before,
        'cache': cache,
        'contains': contains,
        'define': define,
        'filetype': filetype,
        'inanchor': inanchor,
        'index_of': index_of,
        'info': info,
        'intext': intext,
        'intitle': intitle,
        'inurl': inurl,
        'link': link,
        'location': location,
        'afesearch': safesearch,
        'ource': source,
        'ite': site,
        'tock': stock,
        'weather': weather
    }

    query = create_search_query(params)
    search_url = perform_search(query)
    print("\nOpening your default browser with search results...")
    webbrowser.open_new_tab(search_url)

if __name__ == "__main__":
    main()