import argparse
import webbrowser

def create_search_query(args):
    query = args.query
    
    # Group multiple terms or operators
    if args.group:
        query = f"({args.group})"
    
    # Wildcard
    if args.wildcard:
        query = f"{args.wildcard} * {query}"
    
    # Exact match
    if args.exact:
        query = f'"{args.exact}"'
    
    # Number range
    if args.numrange:
        query = f"{args.numrange[0]}..{args.numrange[1]}"
    
    # Exclude terms
    if args.exclude:
        query += f" -{args.exclude}"
    
    # Include terms
    if args.include:
        query += f" +{args.include}"
    
    # Logical OR
    if args.logical_or:
        query = f"{args.logical_or[0]} | {args.logical_or[1]}"
    
    # Synonyms
    if args.synonym:
        query = f"~{args.synonym}"
    
    # Social media
    if args.social:
        query = f"@{args.social}"
    
    # After date
    if args.after:
        query += f" after:{args.after}"
    
    # All in title
    if args.allintitle:
        query = f"allintitle:{args.allintitle}"
    
    # All in URL
    if args.allinurl:
        query = f"allinurl:{args.allinurl}"
    
    # All in text
    if args.allintext:
        query = f"allintext:{args.allintext}"
    
    # Around
    if args.around:
        query = f"{args.around[0]} AROUND({args.around[1]}) {args.around[2]}"
    
    # Author
    if args.author:
        query = f"author:{args.author}"
    
    # Before date
    if args.before:
        query += f" before:{args.before}"
    
    # Cached version
    if args.cache:
        query = f"cache:{args.cache}"
    
    # Contains filetype
    if args.contains:
        query += f" contains:{args.contains}"
    
    # Define word
    if args.define:
        query = f"define:{args.define}"
    
    # Filetype
    if args.filetype:
        query = f"filetype:{args.filetype}"
    
    # In anchor
    if args.inanchor:
        query = f"inanchor:{args.inanchor}"
    
    # Index of
    if args.index_of:
        query = f"index of:{args.index_of}"
    
    # Information about site
    if args.info:
        query = f"info:{args.info}"
    
    # In text
    if args.intext:
        query = f"intext:{args.intext}"
    
    # In title
    if args.intitle:
        query = f"intitle:{args.intitle}"
    
    # In URL
    if args.inurl:
        query = f"inurl:{args.inurl}"
    
    # Links
    if args.link:
        query = f"link:{args.link}"
    
    # Location
    if args.location:
        query = f"location:{args.location}"
    
    # Safe search
    if args.safesearch:
        query += f" safesearch:{args.safesearch}"
    
    # Source
    if args.source:
        query = f"source:{args.source}"
    
    # Site
    if args.site:
        query = f"site:{args.site}"
    
    # Stock
    if args.stock:
        query = f"stock:{args.stock}"
    
    # Weather
    if args.weather:
        query = f"weather:{args.weather}"
    
    return query

def main():
    parser = argparse.ArgumentParser(description="Goork: A tool for Google Dorking")
    parser.add_argument('--query', type=str, required=True, help='Main search query')
    parser.add_argument('--group', type=str, help='Group multiple terms or operators')
    parser.add_argument('--wildcard', type=str, help='Wildcard match')
    parser.add_argument('--exact', type=str, help='Exact match')
    parser.add_argument('--numrange', type=int, nargs=2, help='Number range')
    parser.add_argument('--exclude', type=str, help='Exclude terms')
    parser.add_argument('--include', type=str, help='Include terms')
    parser.add_argument('--logical_or', type=str, nargs=2, help='Logical OR operator')
    parser.add_argument('--synonym', type=str, help='Synonyms search')
    parser.add_argument('--social', type=str, help='Social media search')
    parser.add_argument('--after', type=str, help='Documents published after a date')
    parser.add_argument('--allintitle', type=str, help='All in title')
    parser.add_argument('--allinurl', type=str, help='All in URL')
    parser.add_argument('--allintext', type=str, help='All in text')
    parser.add_argument('--around', type=str, nargs=3, help='Words around n words apart')
    parser.add_argument('--author', type=str, help='Search articles by author')
    parser.add_argument('--before', type=str, help='Documents published before a date')
    parser.add_argument('--cache', type=str, help='Search cached version of a site')
    parser.add_argument('--contains', type=str, help='Search documents linking to filetype')
    parser.add_argument('--define', type=str, help='Define a word')
    parser.add_argument('--filetype', type=str, help='Search specific filetype')
    parser.add_argument('--inanchor', type=str, help='Search in anchors')
    parser.add_argument('--index_of', type=str, help='Search for index of')
    parser.add_argument('--info', type=str, help='Search for site information')
    parser.add_argument('--intext', type=str, help='Search in text')
    parser.add_argument('--intitle', type=str, help='Search in title')
    parser.add_argument('--inurl', type=str, help='Search in URL')
    parser.add_argument('--link', type=str, help='Search documents linking to keyword')
    parser.add_argument('--location', type=str, help='Search based on location')
    parser.add_argument('--safesearch', type=str, help='Exclude adult content')
    parser.add_argument('--source', type=str, help='Search on a specific news site')
    parser.add_argument('--site', type=str, help='Search on a specific site')
    parser.add_argument('--stock', type=str, help='Search for stock information')
    parser.add_argument('--weather', type=str, help='Search for weather information')
    
    args = parser.parse_args()
    
    query = create_search_query(args)
    print(f"Search Query: {query}")
    
    webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    main()
