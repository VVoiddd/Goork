# Goork: Advanced Google Dorking Tool

Goork is a Python-based tool designed to facilitate advanced Google searches (Google dorking) with ease. This tool enables users to construct intricate search queries using various parameters and view the results directly in their default web browser.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Parameters](#parameters)
  - [Main Parameters](#main-parameters)
  - [Advanced Parameters](#advanced-parameters)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

<details>
  <summary>Expand for Installation Instructions</summary>

1. **Clone the repository:**

    ```sh
    git clone https://github.com/VVoiddd/Goork.git
    cd Goork
    ```

2. **Install required packages:**

    Goork requires the `requests` and `beautifulsoup4` libraries. Install them using pip:

    ```sh
    pip install requests beautifulsoup4
    ```

</details>

## Usage

<details>
  <summary>Expand for Usage Instructions</summary>

### Running the Script

To execute the script, use Python:

```sh
python Main.py
```

You will be prompted to input various search parameters. Leaving a prompt blank excludes that parameter from the search query.

### Example Usage

Sample input values:

- **Enter query:** `python programming`
- **Enter group (optional):** `developers`
- **Enter wildcard (optional):** `*programming*`
- **Enter exact phrase (optional):** `"python tutorial"`
- **Enter number range start (optional):** `1`
- **Enter number range end (optional):** `100`
- **Enter words to exclude, separated by commas (optional):** `java, c++`
- **Enter words to include, separated by commas (optional):** `python, programming`
- **Enter first logical OR term (optional):** `python`
- **Enter second logical OR term (optional):** `javascript`
- **Enter synonym (optional):** `~python`
- **Enter social handle (optional):** `@python`
- **Enter after date (optional):** `2022-01-01`
- **Enter allintitle (optional):** `python tutorial`
- **Enter allinurl (optional):** `python.org`
- **Enter allintext (optional):** `python documentation`
- **Enter first AROUND term (optional):** `python`
- **Enter AROUND proximity (optional):** `5`
- **Enter second AROUND term (optional):** `javascript`
- **Enter author (optional):** `John Doe`
- **Enter before date (optional):** `2022-01-01`
- **Enter cache (optional):** `cache:python`
- **Enter contains (optional):** `contains:python`
- **Enter define (optional):** `define:python`
- **Enter filetype (optional):** `filetype:pdf`
- **Enter inanchor (optional):** `inanchor:python`
- **Enter index of (optional):** `index of:python`
- **Enter info (optional):** `info:python`
- **Enter intext (optional):** `intext:python`
- **Enter intitle (optional):** `intitle:python`
- **Enter inurl (optional):** `inurl:python.org`
- **Enter link (optional):** `link:python.org`
- **Enter location (optional):** `location:usa`
- **Enter safesearch (optional):** `safesearch:on`
- **Enter source (optional):** `source:python.org`
- **Enter site (optional):** `site:python.org`
- **Enter stock (optional):** `stock:python`
- **Enter weather (optional):** `weather:usa`

</details>

## Parameters

### Main Parameters

<details>
  <summary>Expand for Main Parameters</summary>

- **Query**: Primary search term.
  - Example: `python programming`
  
- **Group**: Group terms.
  - Example: `developers`
  
- **Wildcard**: Wildcard terms.
  - Example: `*programming*`
  
- **Exact**: Exact phrases.
  - Example: `"python tutorial"`
  
- **Numrange**: Number range (start and end).
  - Example: `1` (start), `100` (end)

</details>

### Advanced Parameters

<details>
  <summary>Expand for Advanced Parameters</summary>

- **Exclude**: Words to exclude (comma-separated).
  - Example: `java, c++`
  
- **Include**: Words to include (comma-separated).
  - Example: `python, programming`
  
- **Logical OR**: Logical OR terms.
  - Example: `python` (first term), `javascript` (second term)
  
- **Synonym**: Synonyms.
  - Example: `~python`
  
- **Social**: Social handle.
  - Example: `@python`
  
- **After**: Date after.
  - Example: `2022-01-01`
  
- **Allintitle**: All in title.
  - Example: `python tutorial`
  
- **Allinurl**: All in URL.
  - Example: `python.org`
  
- **Allintext**: All in text.
  - Example: `python documentation`
  
- **Around**: AROUND term (term1, proximity, term2).
  - Example: `python` (first term), `5` (proximity), `javascript` (second term)
  
- **Author**: Author name.
  - Example: `John Doe`
  
- **Before**: Date before.
  - Example: `2022-01-01`
  
- **Cache**: Cache.
  - Example: `cache:python`
  
- **Contains**: Contains.
  - Example: `contains:python`
  
- **Define**: Define.
  - Example: `define:python`
  
- **Filetype**: File type.
  - Example: `filetype:pdf`
  
- **Inanchor**: In anchor.
  - Example: `inanchor:python`
  
- **Index of**: Index of.
  - Example: `index of:python`
  
- **Info**: Info.
  - Example: `info:python`
  
- **Intext**: In text.
  - Example: `intext:python`
  
- **Intitle**: In title.
  - Example: `intitle:python`
  
- **Inurl**: In URL.
  - Example: `inurl:python.org`
  
- **Link**: Link.
  - Example: `link:python.org`
  
- **Location**: Location.
  - Example: `location:usa`
  
- **Safesearch**: Safe search.
  - Example: `safesearch:on`
  
- **Source**: Source.
  - Example: `source:python.org`
  
- **Site**: Site.
  - Example: `site:python.org`
  
- **Stock**: Stock.
  - Example: `stock:python`
  
- **Weather**: Weather.
  - Example: `weather:usa`

</details>

## Examples

<details>
  <summary>Expand for Examples</summary>

Here are some example queries you can execute using Goork:

1. **Basic Query:**
    ```sh
    python programming
    ```

2. **Exclude Words:**
    ```sh
    python programming -java -c++
    ```

3. **Include Words:**
    ```sh
    python programming +tutorial +guide
    ```

4. **Number Range:**
    ```sh
    python programming 1..100
    ```

5. **Exact Phrase:**
    ```sh
    "python tutorial"
    ```

6. **Logical OR:**
    ```sh
    python | javascript
    ```

7. **Synonym:**
    ```sh
    ~python
    ```

8. **Social Handle:**
    ```sh
    @python
    ```

9. **Date Range:**
    ```sh
    after:2022-01-01 before:2023-01-01
    ```

10. **Filetype:**
    ```sh
    filetype:pdf
    ```

</details>

## Contributing

<details>
  <summary>Expand for Contribution Guidelines</summary>

Contributions are welcome! Please feel free to submit a Pull Request.

</details>

## License

<details>
  <summary>Expand for License Information</summary>

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

</details>
