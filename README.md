

# Goork: Advanced Google Dorking Tool

Goork is a Python script that enables advanced Google search queries, known as Google dorks, with various search parameters. It constructs complex search queries based on user inputs and opens the search results directly in your default web browser.

## Features

- **Flexible Query Construction**: Construct complex Google search queries using multiple parameters like wildcards, exact phrases, number ranges, logical OR, synonyms, and more.
- **Advanced Search Operators**: Utilize Google's advanced search operators like `allintitle`, `allinurl`, `allintext`, `AROUND()`, and others to refine your search.
- **Exclusion and Inclusion**: Exclude specific words (`-word1, -word2`) or include specific words (`+word1, +word2`) in your search results.
- **Open Search Results**: Directly open the search results in your default web browser for quick access.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VVoiddd/Goork.git
   cd Goork
   ```

2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

3. Run the script:
   ```bash
   python Main.py
   ```

## Usage

1. **Run the Script**: Open a terminal or command prompt, navigate to the Goork directory, and run `Main.py`.
   ```bash
   python Main.py
   ```

2. **Enter Search Parameters**: Follow the prompts to enter various search parameters. Leave inputs blank for optional parameters.
   - Enter query: Enter your main search query.
   - Enter group (optional): Specify a group or category.
   - Enter wildcard (optional): Use a wildcard for more flexible searching (e.g., `*`).
   - ...

3. **View Results**: The script constructs the Google search query based on your inputs and opens the search results in your default web browser.

4. **Refine Queries**: Adjust parameters as needed to refine your search results or explore different query combinations.

## Example

Suppose you want to search for software vulnerabilities but exclude mentions of cheats, fakes, and irrelevant results:

- Enter query: `software vulnerabilities`
- Enter words to exclude: `cheat, fake, irrelevant`

The script will construct a query that excludes the specified words and opens the search results in your browser.

## Contributing

Contributions are welcome! If you have ideas for improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

