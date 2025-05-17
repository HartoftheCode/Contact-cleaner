import csv
import os

# Prompt user for input file path
input_file = input("Enter the full path to the CSV file you want to clean: ").strip()

# Generate output file path in the same directory
folder = os.path.dirname(input_file)
output_file = os.path.join(folder, 'cleaned_contacts.csv')

# Read data from CSV and remove duplicates
unique_emails = set()
cleaned_rows = []

with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = row['Email'].strip().lower()
        if email not in unique_emails:
            unique_emails.add(email)
            cleaned_rows.append(row)

# Sort by Last Name
cleaned_rows.sort(key=lambda x: x['Last Name'].lower())

# Write to new CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['First Name', 'Last Name', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)

# Print summary
print(f"Cleaned list saved to {output_file}")
print(f"{len(unique_emails)} unique contacts written.")