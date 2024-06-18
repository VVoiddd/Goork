# Goork: Advanced Google Dorking Tool

Goork is a Python-based tool designed to help you perform advanced Google searches (Google dorking) with ease. This tool allows you to build complex search queries using various parameters and opens the results in your default web browser.

## Features

- Create complex Google search queries with various parameters.
- Supports exclusion, inclusion, exact phrases, number ranges, and more.
- Automatically opens search results in your default web browser.
- User-friendly input prompts to build search queries interactively.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/VVoiddd/Goork.git
    cd Goork
    ```

2. **Install required packages:**

    This script requires the `requests` and `beautifulsoup4` libraries. You can install them using pip:

    ```sh
    pip install requests beautifulsoup4
    ```

## Usage

Run the script using Python:

```sh
python Main.py
```

You will be prompted to enter various search parameters. If you leave a prompt blank, that parameter will not be included in the search query.

### Example Usage

When prompted, you can enter values like these:

- **Enter query:** `python programming`
- **Enter group (optional):** `developers`
- **Enter wildcard (optional):** `*programming*`
- **Enter exact phrase (optional):** `"python tutorial"`
- **Enter words to exclude, separated by commas (optional):** `java, c++`
- **Enter words to include, separated by commas (optional):** `python, programming`

### Full List of Parameters

- `query`: Main search term.
- `group`: Group terms.
- `wildcard`: Wildcard terms.
- `exact`: Exact phrases.
- `numrange`: Number range (start and end).
- `exclude`: Words to exclude (comma-separated).
- `include`: Words to include (comma-separated).
- `logical_or`: Logical OR terms.
- `synonym`: Synonyms.
- `social`: Social handle.
- `after`: Date after.
- `allintitle`: All in title.
- `allinurl`: All in URL.
- `allintext`: All in text.
- `around`: AROUND term (term1, proximity, term2).
- `author`: Author name.
- `before`: Date before.
- `cache`: Cache.
- `contains`: Contains.
- `define`: Define.
- `filetype`: File type.
- `inanchor`: In anchor.
- `index_of`: Index of.
- `info`: Info.
- `intext`: In text.
- `intitle`: In title.
- `inurl`: In URL.
- `link`: Link.
- `location`: Location.
- `safesearch`: Safe search.
- `source`: Source.
- `site`: Site.
- `stock`: Stock.
- `weather`: Weather.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
