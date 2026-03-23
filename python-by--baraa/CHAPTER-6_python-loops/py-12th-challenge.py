file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
seen = []
for file in file_list:
    if file in seen:
        print("Duplicate found.")
    seen.append(file)
    break
else:
    print("All files are unique.")