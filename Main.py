import tkinter as tk
from tkinter import ttk, scrolledtext
import webbrowser
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

def on_search():
    params = {
        'query': query_var.get(),
        'group': group_var.get(),
        'wildcard': wildcard_var.get(),
        'exact': exact_var.get(),
        'numrange': (numrange_start_var.get(), numrange_end_var.get()) if numrange_start_var.get() and numrange_end_var.get() else None,
        'exclude': exclude_var.get(),
        'include': include_var.get(),
        'logical_or': (logical_or_var1.get(), logical_or_var2.get()) if logical_or_var1.get() and logical_or_var2.get() else None,
        'synonym': synonym_var.get(),
        'social': social_var.get(),
        'after': after_var.get(),
        'allintitle': allintitle_var.get(),
        'allinurl': allinurl_var.get(),
        'allintext': allintext_var.get(),
        'around': (around_var1.get(), around_var2.get(), around_var3.get()) if around_var1.get() and around_var2.get() and around_var3.get() else None,
        'author': author_var.get(),
        'before': before_var.get(),
        'cache': cache_var.get(),
        'contains': contains_var.get(),
        'define': define_var.get(),
        'filetype': filetype_var.get(),
        'inanchor': inanchor_var.get(),
        'index_of': index_of_var.get(),
        'info': info_var.get(),
        'intext': intext_var.get(),
        'intitle': intitle_var.get(),
        'inurl': inurl_var.get(),
        'link': link_var.get(),
        'location': location_var.get(),
        'safesearch': safesearch_var.get(),
        'source': source_var.get(),
        'site': site_var.get(),
        'stock': stock_var.get(),
        'weather': weather_var.get(),
    }
    
    query = create_search_query(params)
    results = perform_search(query)
    display_results(results)

def display_results(results):
    results_text.configure(state='normal')
    results_text.delete(1.0, tk.END)
    
    for title, link, snippet in results:
        results_text.insert(tk.END, f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n\n")
    
    results_text.configure(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Goork - Google Dorking Tool")
root.geometry("800x800")

# Create input fields
ttk.Label(root, text="Query:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
query_var = tk.StringVar()
ttk.Entry(root, textvariable=query_var, width=50).grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Group:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
group_var = tk.StringVar()
ttk.Entry(root, textvariable=group_var, width=50).grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Wildcard:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
wildcard_var = tk.StringVar()
ttk.Entry(root, textvariable=wildcard_var, width=50).grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Exact:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
exact_var = tk.StringVar()
ttk.Entry(root, textvariable=exact_var, width=50).grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="Number Range:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
numrange_start_var = tk.StringVar()
numrange_end_var = tk.StringVar()
ttk.Entry(root, textvariable=numrange_start_var, width=24).grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
ttk.Entry(root, textvariable=numrange_end_var, width=24).grid(row=4, column=1, padx=10, pady=5, sticky=tk.E)

ttk.Label(root, text="Exclude:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
exclude_var = tk.StringVar()
ttk.Entry(root, textvariable=exclude_var, width=50).grid(row=5, column=1, padx=10, pady=5)

ttk.Label(root, text="Include:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
include_var = tk.StringVar()
ttk.Entry(root, textvariable=include_var, width=50).grid(row=6, column=1, padx=10, pady=5)

ttk.Label(root, text="Logical OR:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
logical_or_var1 = tk.StringVar()
logical_or_var2 = tk.StringVar()
ttk.Entry(root, textvariable=logical_or_var1, width=24).grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)
ttk.Entry(root, textvariable=logical_or_var2, width=24).grid(row=7, column=1, padx=10, pady=5, sticky=tk.E)

ttk.Label(root, text="Synonym:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
synonym_var = tk.StringVar()
ttk.Entry(root, textvariable=synonym_var, width=50).grid(row=8, column=1, padx=10, pady=5)

ttk.Label(root, text="Social:").grid(row=9, column=0, sticky=tk.W, padx=10, pady=5)
social_var = tk.StringVar()
ttk.Entry(root, textvariable=social_var, width=50).grid(row=9, column=1, padx=10, pady=5)

ttk.Label(root, text="After:").grid(row=10, column=0, sticky=tk.W, padx=10, pady=5)
after_var = tk.StringVar()
ttk.Entry(root, textvariable=after_var, width=50).grid(row=10, column=1, padx=10, pady=5)

ttk.Label(root, text="Allintitle:").grid(row=11, column=0, sticky=tk.W, padx=10, pady=5)
allintitle_var = tk.StringVar()
ttk.Entry(root, textvariable=allintitle_var, width=50).grid(row=11, column=1, padx=10, pady=5)

ttk.Label(root, text="Allinurl:").grid(row=12, column=0, sticky=tk.W, padx=10, pady=5)
allinurl_var = tk.StringVar()
ttk.Entry(root, textvariable=allinurl_var, width=50).grid(row=12, column=1, padx=10, pady=5)

ttk.Label(root, text="Allintext:").grid(row=13, column=0, sticky=tk.W, padx=10, pady=5)
allintext_var = tk.StringVar()
ttk.Entry(root, textvariable=allintext_var, width=50).grid(row=13, column=1, padx=10, pady=5)

ttk.Label(root, text="Around:").grid(row=14, column=0, sticky=tk.W, padx=10, pady=5)
around_var1 = tk.StringVar()
around_var2 = tk.StringVar()
around_var3 = tk.StringVar()
ttk.Entry(root, textvariable=around_var1, width=16).grid(row=14, column=1, padx=10, pady=5, sticky=tk.W)
ttk.Entry(root, textvariable=around_var2, width=16).grid(row=14, column=1, padx=10, pady=5)
ttk.Entry(root, textvariable=around_var3, width=16).grid(row=14, column=1, padx=10, pady=5, sticky=tk.E)

ttk.Label(root, text="Author:").grid(row=15, column=0, sticky=tk.W, padx=10, pady=5)
author_var = tk.StringVar()
ttk.Entry(root, textvariable=author_var, width=50).grid(row=15, column=1, padx=10, pady=5)

ttk.Label(root, text="Before:").grid(row=16, column=0, sticky=tk.W, padx=10, pady=5)
before_var = tk.StringVar()
ttk.Entry(root, textvariable=before_var, width=50).grid(row=16, column=1, padx=10, pady=5)

ttk.Label(root, text="Cache:").grid(row=17, column=0, sticky=tk.W, padx=10, pady=5)
cache_var = tk.StringVar()
ttk.Entry(root, textvariable=cache_var, width=50).grid(row=17, column=1, padx=10, pady=5)

ttk.Label(root, text="Contains:").grid(row=18, column=0, sticky=tk.W, padx=10, pady=5)
contains_var = tk.StringVar()
ttk.Entry(root, textvariable=contains_var, width=50).grid(row=18, column=1, padx=10, pady=5)

ttk.Label(root, text="Define:").grid(row=19, column=0, sticky=tk.W, padx=10, pady=5)
define_var = tk.StringVar()
ttk.Entry(root, textvariable=define_var, width=50).grid(row=19, column=1, padx=10, pady=5)

ttk.Label(root, text="Filetype:").grid(row=20, column=0, sticky=tk.W, padx=10, pady=5)
filetype_var = tk.StringVar()
ttk.Entry(root, textvariable=filetype_var, width=50).grid(row=20, column=1, padx=10, pady=5)

ttk.Label(root, text="Inanchor:").grid(row=21, column=0, sticky=tk.W, padx=10, pady=5)
inanchor_var = tk.StringVar()
ttk.Entry(root, textvariable=inanchor_var, width=50).grid(row=21, column=1, padx=10, pady=5)

ttk.Label(root, text="Index Of:").grid(row=22, column=0, sticky=tk.W, padx=10, pady=5)
index_of_var = tk.StringVar()
ttk.Entry(root, textvariable=index_of_var, width=50).grid(row=22, column=1, padx=10, pady=5)

ttk.Label(root, text="Info:").grid(row=23, column=0, sticky=tk.W, padx=10, pady=5)
info_var = tk.StringVar()
ttk.Entry(root, textvariable=info_var, width=50).grid(row=23, column=1, padx=10, pady=5)

ttk.Label(root, text="Intext:").grid(row=24, column=0, sticky=tk.W, padx=10, pady=5)
intext_var = tk.StringVar()
ttk.Entry(root, textvariable=intext_var, width=50).grid(row=24, column=1, padx=10, pady=5)

ttk.Label(root, text="Intitle:").grid(row=25, column=0, sticky=tk.W, padx=10, pady=5)
intitle_var = tk.StringVar()
ttk.Entry(root, textvariable=intitle_var, width=50).grid(row=25, column=1, padx=10, pady=5)

ttk.Label(root, text="Inurl:").grid(row=26, column=0, sticky=tk.W, padx=10, pady=5)
inurl_var = tk.StringVar()
ttk.Entry(root, textvariable=inurl_var, width=50).grid(row=26, column=1, padx=10, pady=5)

ttk.Label(root, text="Link:").grid(row=27, column=0, sticky=tk.W, padx=10, pady=5)
link_var = tk.StringVar()
ttk.Entry(root, textvariable=link_var, width=50).grid(row=27, column=1, padx=10, pady=5)

ttk.Label(root, text="Location:").grid(row=28, column=0, sticky=tk.W, padx=10, pady=5)
location_var = tk.StringVar()
ttk.Entry(root, textvariable=location_var, width=50).grid(row=28, column=1, padx=10, pady=5)

ttk.Label(root, text="Safesearch:").grid(row=29, column=0, sticky=tk.W, padx=10, pady=5)
safesearch_var = tk.StringVar()
ttk.Entry(root, textvariable=safesearch_var, width=50).grid(row=29, column=1, padx=10, pady=5)

ttk.Label(root, text="Source:").grid(row=30, column=0, sticky=tk.W, padx=10, pady=5)
source_var = tk.StringVar()
ttk.Entry(root, textvariable=source_var, width=50).grid(row=30, column=1, padx=10, pady=5)

ttk.Label(root, text="Site:").grid(row=31, column=0, sticky=tk.W, padx=10, pady=5)
site_var = tk.StringVar()
ttk.Entry(root, textvariable=site_var, width=50).grid(row=31, column=1, padx=10, pady=5)

ttk.Label(root, text="Stock:").grid(row=32, column=0, sticky=tk.W, padx=10, pady=5)
stock_var = tk.StringVar()
ttk.Entry(root, textvariable=stock_var, width=50).grid(row=32, column=1, padx=10, pady=5)

ttk.Label(root, text="Weather:").grid(row=33, column=0, sticky=tk.W, padx=10, pady=5)
weather_var = tk.StringVar()
ttk.Entry(root, textvariable=weather_var, width=50).grid(row=33, column=1, padx=10, pady=5)

# Search button
ttk.Button(root, text="Search", command=on_search).grid(row=34, column=1, pady=20)

# Results display
results_text = scrolledtext.ScrolledText(root, width=90, height=20, state='disabled')
results_text.grid(row=35, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
