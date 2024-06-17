# Goork - Google Dorking Tool

Goork is a user-friendly command-line interface (CLI) tool designed for Google Dorking. It allows users to perform advanced Google searches with various search parameters to retrieve specific information from the web.

## Features

- Supports various advanced Google search operators
- Easy-to-use CLI interface
- Displays search results with title, link, and snippet

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the necessary libraries using the following commands:

```bash
pip install requests
pip install beautifulsoup4
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/goork.git
cd goork
```

2. Run the tool:

```bash
python goork.py
```

## Usage

### Running the Tool

When you run the tool, a graphical interface will appear where you can enter your search parameters.

### Search Parameters

The tool supports a variety of Google search operators that can be combined to refine your search:

- **Query**: The main search term.
- **Group**: Group the search terms.
- **Wildcard**: Use a wildcard `*` in your search.
- **Exact**: Search for an exact phrase by enclosing it in quotes.
- **Number Range**: Specify a range of numbers (e.g., 10..20).
- **Exclude**: Exclude certain words from the search.
- **Include**: Include certain words in the search.
- **Logical OR**: Use logical OR in your search (e.g., term1 OR term2).
- **Synonym**: Search for synonyms by using the tilde `~`.
- **Social**: Search social media content.
- **After**: Search for content published after a specific date.
- **Allintitle**: Search for pages with titles containing all the terms.
- **Allinurl**: Search for pages with URLs containing all the terms.
- **Allintext**: Search for pages with text containing all the terms.
- **Around**: Use the AROUND operator to find terms within a certain number of words of each other.
- **Author**: Search for content written by a specific author.
- **Before**: Search for content published before a specific date.
- **Cache**: Find the cached version of a page.
- **Contains**: Search for pages containing specific file types or media.
- **Define**: Get the definition of a term.
- **Filetype**: Search for specific file types.
- **Inanchor**: Search for terms in anchor text.
- **Index Of**: Find directory listings.
- **Info**: Get information about a page.
- **Intext**: Search for terms in the text of the page.
- **Intitle**: Search for terms in the title of the page.
- **Inurl**: Search for terms in the URL of the page.
- **Link**: Search for pages that link to a URL.
- **Location**: Search for content from a specific location.
- **Safesearch**: Enable or disable SafeSearch.
- **Source**: Search for content from a specific source.
- **Site**: Limit search to a specific site or domain.
- **Stock**: Search for stock information.
- **Weather**: Search for weather information.

### Instructions

1. **Enter Search Parameters**: Fill in the search parameters in the respective input fields.
2. **Perform Search**: Click the "Search" button to execute the search.
3. **View Results**: The search results will be displayed in the results area with the title, link, and snippet of each result.

### Example Usage

1. To search for pages containing the phrase "open source" and excluding the term "proprietary", you would:
   - Enter `open source` in the **Query** field.
   - Enter `proprietary` in the **Exclude** field.
   - Click the **Search** button.

2. To search for PDFs related to Python programming:
   - Enter `Python programming` in the **Query** field.
   - Enter `pdf` in the **Filetype** field.
   - Click the **Search** button.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the Goork License.

