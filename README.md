# Goork - Advanced Google Dorking Tool

Goork is a command-line tool designed for performing advanced Google searches using various search parameters. It allows users to construct complex search queries and retrieve specific information from Google search results.

## Features

- Supports a wide range of Google search operators.
- User-friendly CLI interface for entering search parameters.
- Displays search results with titles, links, and snippets.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install the required libraries using pip:

```bash
pip install requests
pip install beautifulsoup4
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/VVoiddd/Goork.git
cd Goork
```

2. Run the tool:

```bash
python goork.py
```

## Usage

### Using Goork

Goork allows you to build complex search queries by combining various search parameters. Here are the available search parameters:

- **Query**: The main search term.
- **Group**: Grouping search terms.
- **Wildcard**: Use of wildcard `*` in searches.
- **Exact**: Search for an exact phrase.
- **Number Range**: Specify a range of numbers.
- **Exclude**: Exclude specific words or phrases.
- **Include**: Include specific words or phrases.
- **Logical OR**: Use logical OR for multiple terms.
- **Synonym**: Search for synonyms using the tilde `~`.
- **Social**: Search social media content.
- **After**: Search for content published after a specific date.
- **Allintitle**: Search for pages with titles containing all terms.
- **Allinurl**: Search for pages with URLs containing all terms.
- **Allintext**: Search for pages with text containing all terms.
- **Around**: Search for terms within a certain proximity of each other.
- **Author**: Search for content written by a specific author.
- **Before**: Search for content published before a specific date.
- **Cache**: Find the cached version of a page.
- **Contains**: Search for specific file types or media.
- **Define**: Get the definition of a term.
- **Filetype**: Search for specific file types.
- **Inanchor**: Search for terms in anchor text.
- **Index Of**: Find directory listings.
- **Info**: Get information about a page.
- **Intext**: Search for terms in the text of a page.
- **Intitle**: Search for terms in the title of a page.
- **Inurl**: Search for terms in the URL of a page.
- **Link**: Search for pages that link to a URL.
- **Location**: Search for content from a specific location.
- **Safesearch**: Enable or disable SafeSearch.
- **Source**: Search for content from a specific source.
- **Site**: Limit search to a specific site or domain.
- **Stock**: Search for stock information.
- **Weather**: Search for weather information.

### Example Usage

1. To search for pages containing "open source" but excluding "proprietary":

   ```
   Enter query: open source
   Enter words to exclude (optional): proprietary
   ```

2. To search for PDFs related to Python programming:

   ```
   Enter query: Python programming
   Enter filetype (optional): pdf
   ```

### Running the Tool

1. Enter the relevant search parameters when prompted.
2. The tool constructs the search query based on your inputs.
3. Results are displayed with titles, links, and snippets.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
