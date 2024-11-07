import json

# Read the content of the text file
with open('quotes.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content into individual quotes
quotes = content.strip().split('\n\n')

# Create a list to hold the structured quotes
quotes_list = []

# Process each quote block
for quote_block in quotes:
    lines = quote_block.split('\n')
    if len(lines) == 3:
        quote, author, source = lines
        quotes_list.append({
            'quote': quote,
            'author': author,
            'source': source
        })

# Convert the list to JSON format
quotes_json = json.dumps(quotes_list, indent=4)

# Save the JSON to a file
with open('quotes.json', 'w') as json_file:
    json_file.write(quotes_json)

print("Quotes have been converted to JSON format and saved to quotes.json")