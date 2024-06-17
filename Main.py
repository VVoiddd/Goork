import webbrowser
import requests
from bs4 import BeautifulSoup

def create_search_query(params):
    query_parts = []

    query_parts.append(params['query'])

    if params['group']:
        query_parts.append(f"({params['group']})")
    if params['wildcard']:
        query_parts.append(f"{params['wildcard']}*")
    if params['exact']:
        query_parts.append(f'"{params["exact"]}"')
    if params['numrange']:
        query_parts.append(f"{params['numrange'][0]}..{params['numrange'][1]}")
    if params['exclude']:
        excluded_words = params['exclude'].split(',')
        for word in excluded_words:
            query_parts.append(f"-{word.strip()}")
    if params['include']:
        included_words = params['include'].split(',')
        for word in included_words:
            query_parts.append(f"+{word.strip()}")
    if params['logical_or']:
        query_parts.append(f"{params['logical_or'][0]} | {params['logical_or'][1]}")
    if params['synonym']:
        query_parts.append(f"~{params['synonym']}")
    if params['social']:
        query_parts.append(f"@{params['social']}")
    if params['after']:
        query_parts.append(f"after:{params['after']}")
    if params['allintitle']:
        query_parts.append(f"allintitle:{params['allintitle']}")
    if params['allinurl']:
        query_parts.append(f"allinurl:{params['allinurl']}")
    if params['allintext']:
        query_parts.append(f"allintext:{params['allintext']}")
    if params['around']:
        query_parts.append(f"{params['around'][0]} AROUND({params['around'][1]}) {params['around'][2]}")
    if params['author']:
        query_parts.append(f"author:{params['author']}")
    if params['before']:
        query_parts.append(f"before:{params['before']}")
    if params['cache']:
        query_parts.append(f"cache:{params['cache']}")
    if params['contains']:
        query_parts.append(f"contains:{params['contains']}")
    if params['define']:
        query_parts.append(f"define:{params['define']}")
    if params['filetype']:
        query_parts.append(f"filetype:{params['filetype']}")
    if params['inanchor']:
        query_parts.append(f"inanchor:{params['inanchor']}")
    if params['index_of']:
        query_parts.append(f"index of:{params['index_of']}")
    if params['info']:
        query_parts.append(f"info:{params['info']}")
    if params['intext']:
        query_parts.append(f"intext:{params['intext']}")
    if params['intitle']:
        query_parts.append(f"intitle:{params['intitle']}")
    if params['inurl']:
        query_parts.append(f"inurl:{params['inurl']}")
    if params['link']:
        query_parts.append(f"link:{params['link']}")
    if params['location']:
        query_parts.append(f"location:{params['location']}")
    if params['safesearch']:
        query_parts.append(f"safesearch:{params['safesearch']}")
    if params['source']:
        query_parts.append(f"source:{params['source']}")
    if params['site']:
        query_parts.append(f"site:{params['site']}")
    if params['stock']:
        query_parts.append(f"stock:{params['stock']}")
    if params['weather']:
        query_parts.append(f"weather:{params['weather']}")

    return " ".join(query_parts)

def perform_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    return search_url

def main():
    print("--- Welcome to Goork: Advanced Google Dorking Tool ---")
    print("Enter search parameters or leave blank for optional ones.")

    params = {
        'query': input("Enter query: "),
        'group': input("Enter group (optional): "),
        'wildcard': input("Enter wildcard (optional, e.g., *): "),
        'exact': input("Enter exact phrase (optional): "),
        'numrange': (input("Enter number range start (optional): "), input("Enter number range end (optional): ")),
        'exclude': input("Enter words to exclude, separated by commas (optional): "),
        'include': input("Enter words to include, separated by commas (optional): "),
        'logical_or': (input("Enter first logical OR term (optional): "), input("Enter second logical OR term (optional): ")),
        'synonym': input("Enter synonym (optional): "),
        'social': input("Enter social handle (optional): "),
        'after': input("Enter after date (optional): "),
        'allintitle': input("Enter allintitle (optional): "),
        'allinurl': input("Enter allinurl (optional): "),
        'allintext': input("Enter allintext (optional): "),
        'around': (input("Enter first AROUND term (optional): "), input("Enter AROUND proximity (optional): "), input("Enter second AROUND term (optional): ")),
        'author': input("Enter author (optional): "),
        'before': input("Enter before date (optional): "),
        'cache': input("Enter cache (optional): "),
        'contains': input("Enter contains (optional): "),
        'define': input("Enter define (optional): "),
        'filetype': input("Enter filetype (optional): "),
        'inanchor': input("Enter inanchor (optional): "),
        'index_of': input("Enter index of (optional): "),
        'info': input("Enter info (optional): "),
        'intext': input("Enter intext (optional): "),
        'intitle': input("Enter intitle (optional): "),
        'inurl': input("Enter inurl (optional): "),
        'link': input("Enter link (optional): "),
        'location': input("Enter location (optional): "),
        'safesearch': input("Enter safesearch (optional): "),
        'source': input("Enter source (optional): "),
        'site': input("Enter site (optional): "),
        'stock': input("Enter stock (optional): "),
        'weather': input("Enter weather (optional): ")
    }

    query = create_search_query(params)
    search_url = perform_search(query)
    print("\nOpening your default browser with search results...")
    webbrowser.open_new_tab(search_url)

if __name__ == "__main__":
    main()
