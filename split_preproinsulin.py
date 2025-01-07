# Read the cleaned sequence
with open("preproinsulin-seq-clean.txt", "r") as file:
    sequence = file.read()

# Define segments
lsinsulin = sequence[:24]  # Amino acids 1-24
binsulin = sequence[24:54]  # Amino acids 25-54
cinsulin = sequence[54:89]  # Amino acids 55-89
ainsulin = sequence[89:]  # Amino acids 90-110

# Write each segment to its respective file
with open("lsinsulin-seq-clean.txt", "w") as file:
    file.write(lsinsulin)

with open("binsulin-seq-clean.txt", "w") as file:
    file.write(binsulin)

with open("cinsulin-seq-clean.txt", "w") as file:
    file.write(cinsulin)

with open("ainsulin-seq-clean.txt", "w") as file:
    file.write(ainsulin)

# Print confirmation
print("Segments saved:")
print(f"  - lsinsulin: {len(lsinsulin)} characters")
print(f"  - binsulin: {len(binsulin)} characters")
print(f"  - cinsulin: {len(cinsulin)} characters")
print(f"  - ainsulin: {len(ainsulin)} characters")