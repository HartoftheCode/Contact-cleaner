# Contact List Cleaner

This Python script processes a CSV file containing contact information. It:

- Removes any duplicate entries based on email addresses (case-insensitive).
- Sorts the cleaned contact list alphabetically by **Last Name**.
- Saves the cleaned file as `cleaned_contacts.csv` in the same directory as the original.
- Displays a summary showing the number of unique contacts processed.

## Expected CSV Format

The input CSV should have a header row and contain the following columns:

```
First Name,Last Name,Email
```

Each row should represent a contact. Example input:

```
First Name,Last Name,Email
Alice,Smith,alice@example.com
Bob,Johnson,bob@example.com
Carol,Smith,carol@example.com
Dave,Adams,dave@example.com
Eve,Johnson,eve@example.com
Bob,Johnson,bob@example.com
```

## How to Use

1. Run the script using Python 3.
2. When prompted, paste the full path to your CSV file.
3. After the script runs, check the same folder for the file `cleaned_contacts.csv`.

## Example

### Input: `contacts.csv`

```
First Name,Last Name,Email
Alice,Smith,alice@example.com
Bob,Johnson,bob@example.com
Carol,Smith,carol@example.com
Dave,Adams,dave@example.com
Eve,Johnson,eve@example.com
Bob,Johnson,bob@example.com
```

### Output: `cleaned_contacts.csv`

```
First Name,Last Name,Email
Dave,Adams,dave@example.com
Bob,Johnson,bob@example.com
Eve,Johnson,eve@example.com
Carol,Smith,carol@example.com
Alice,Smith,alice@example.com
```
