# Open and read the original file
with open("preproinsulin-seq.txt", "r") as file:
    data = file.read()

# Remove unwanted characters using regex
import re
cleaned_data = re.sub(r'(ORIGIN|\d+|//|\s)', '', data)

# Write the cleaned sequence to a new file
with open("preproinsulin-seq-clean.txt", "w") as output:
    output.write(cleaned_data)

# Print confirmation and the number of characters
print(f"Cleaned sequence written to preproinsulin-seq-clean.txt with {len(cleaned_data)} characters.")