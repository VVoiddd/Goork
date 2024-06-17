import requests
from bs4 import BeautifulSoup

def create_search_query(params):
    query = params['query']
    
    if params['group']:
        query += f" ({params['group']})"
    if params['wildcard']:
        query += f" {params['wildcard']} *"
    if params['exact']:
        query += f' "{params['exact']}"'
    if params['numrange']:
        query += f" {params['numrange'][0]}..{params['numrange'][1]}"
    if params['exclude']:
        query += f" -{params['exclude']}"
    if params['include']:
        query += f" +{params['include']}"
    if params['logical_or']:
        query += f" {params['logical_or'][0]} | {params['logical_or'][1]}"
    if params['synonym']:
        query += f" ~{params['synonym']}"
    if params['social']:
        query += f" @{params['social']}"
    if params['after']:
        query += f" after:{params['after']}"
    if params['allintitle']:
        query += f" allintitle:{params['allintitle']}"
    if params['allinurl']:
        query += f" allinurl:{params['allinurl']}"
    if params['allintext']:
        query += f" allintext:{params['allintext']}"
    if params['around']:
        query += f" {params['around'][0]} AROUND({params['around'][1]}) {params['around'][2]}"
    if params['author']:
        query += f" author:{params['author']}"
    if params['before']:
        query += f" before:{params['before']}"
    if params['cache']:
        query += f" cache:{params['cache']}"
    if params['contains']:
        query += f" contains:{params['contains']}"
    if params['define']:
        query += f" define:{params['define']}"
    if params['filetype']:
        query += f" filetype:{params['filetype']}"
    if params['inanchor']:
        query += f" inanchor:{params['inanchor']}"
    if params['index_of']:
        query += f" index of:{params['index_of']}"
    if params['info']:
        query += f" info:{params['info']}"
    if params['intext']:
        query += f" intext:{params['intext']}"
    if params['intitle']:
        query += f" intitle:{params['intitle']}"
    if params['inurl']:
        query += f" inurl:{params['inurl']}"
    if params['link']:
        query += f" link:{params['link']}"
    if params['location']:
        query += f" location:{params['location']}"
    if params['safesearch']:
        query += f" safesearch:{params['safesearch']}"
    if params['source']:
        query += f" source:{params['source']}"
    if params['site']:
        query += f" site:{params['site']}"
    if params['stock']:
        query += f" stock:{params['stock']}"
    if params['weather']:
        query += f" weather:{params['weather']}"
    
    return query

def perform_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for g in soup.find_all('div', class_='g'):
        title = g.find('h3').text if g.find('h3') else 'No title'
        link = g.find('a')['href']
        snippet = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else 'No snippet'
        results.append((title, link, snippet))
    
    return results

def main():
    params = {}
    params['query'] = input("Enter query: ")
    params['group'] = input("Enter group (optional): ")
    params['wildcard'] = input("Enter wildcard (optional): ")
    params['exact'] = input("Enter exact phrase (optional): ")
    numrange_start = input("Enter number range start (optional): ")
    numrange_end = input("Enter number range end (optional): ")
    params['numrange'] = (numrange_start, numrange_end) if numrange_start and numrange_end else None
    params['exclude'] = input("Enter words to exclude (optional): ")
    params['include'] = input("Enter words to include (optional): ")
    logical_or1 = input("Enter first logical OR term (optional): ")
    logical_or2 = input("Enter second logical OR term (optional): ")
    params['logical_or'] = (logical_or1, logical_or2) if logical_or1 and logical_or2 else None
    params['synonym'] = input("Enter synonym (optional): ")
    params['social'] = input("Enter social handle (optional): ")
    params['after'] = input("Enter after date (optional): ")
    params['allintitle'] = input("Enter allintitle (optional): ")
    params['allinurl'] = input("Enter allinurl (optional): ")
    params['allintext'] = input("Enter allintext (optional): ")
    around1 = input("Enter first AROUND term (optional): ")
    around2 = input("Enter AROUND proximity (optional): ")
    around3 = input("Enter second AROUND term (optional): ")
    params['around'] = (around1, around2, around3) if around1 and around2 and around3 else None
    params['author'] = input("Enter author (optional): ")
    params['before'] = input("Enter before date (optional): ")
    params['cache'] = input("Enter cache (optional): ")
    params['contains'] = input("Enter contains (optional): ")
    params['define'] = input("Enter define (optional): ")
    params['filetype'] = input("Enter filetype (optional): ")
    params['inanchor'] = input("Enter inanchor (optional): ")
    params['index_of'] = input("Enter index of (optional): ")
    params['info'] = input("Enter info (optional): ")
    params['intext'] = input("Enter intext (optional): ")
    params['intitle'] = input("Enter intitle (optional): ")
    params['inurl'] = input("Enter inurl (optional): ")
    params['link'] = input("Enter link (optional): ")
    params['location'] = input("Enter location (optional): ")
    params['safesearch'] = input("Enter safesearch (optional): ")
    params['source'] = input("Enter source (optional): ")
    params['site'] = input("Enter site (optional): ")
    params['stock'] = input("Enter stock (optional): ")
    params['weather'] = input("Enter weather (optional): ")
    
    query = create_search_query(params)
    results = perform_search(query)
    
    for title, link, snippet in results:
        print(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n")

if __name__ == "__main__":
    main()
