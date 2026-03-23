# MOST powerful data structure
# # DICTIONARY

# we store one piece of information at a time in (list, tuple, set)
# describing a entity
# everything in one place --> DICTIONARY

# DICTIONARY
# has two parts
# 1. key -> what the data means
# 2. value -> holds actual data


print("*" * 30)
# ------------------------------
# Data structures has these 4 character
# ------------------------------

# ----DICTIONARY----
# Ordered
# Duplicates
# Indexed
# Mutable

my_dict = {
    'a': 10,
    'b': 20,
    'c': 30
}

print(my_dict)  # Ordered

print("*" * 30)
my_dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a': 40
}

print(my_dict)  # duplicate value changed
# key must be unique
# value allow duplicate


print("*" * 30)
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30
}

# print(my_dict[1]) # NOT indexed
# we use keys inorder to access value
print(my_dict['b']) # dict is keyed


print("*" * 30)
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30
}


my_dict['c'] = 80
print(my_dict) # Mutable


#------------------------------------
# Usage cases
#------------------------------------

# user case 1: Representing a single row form a Database or API
# returned records are stored as dictionaries where column names are keys and the rows values are the dictonary values
row = {
    "id" : 101,
    "name" : "John",
    "age" : 29,
    "status" : "active"
}

# user case 2: Mapping Translations to Friendly values
# grest for converting technical codes into friendly labels.
status_map = {
    "01" : "Open",
    "02" : "In Progress",
    "03" : "Done"
}

# user case 3: Mapping Abbreviations
# turning short abbreviations into full readable names
country_map = {
    "DE" : "Germany",
    "FR" : "France",
    "IN" : "India"
}

# user case 4: Config and Environment Data
# store system settings like host, port, and usernames in one clear place.
system_conn = {
    "DB_HOST" : "prod-db.company.com",
    "DB_PORT" : 5432,
    "DB_USER" : "admin_user",
    "DB_NAME" : "analytics_warehouse"
}


# user case 5: ETL and Pipeline Settings
# great for storing run parameters and controlling how your ETL pipelne loads data
etl_config = {
    "DEBUG_MODE": False,                       # Turn verbose loging on/off
    "BATCH_SIZE": 500,                         # How many rows to process per batch
    "LOG_LEVEL" : "INFO",                      # Logging verbosity
    "SOURCE_PATH" : "/data/bronze/",           # Where raw files live
    "TARGET_PATH" : "/data/silver/",           # Where cleaned files go
    "RETRY_COUNT" : 3,                         # How many times to retry a failed extraction
    "FAIL_ON_ERROR" : False,                   # Keep going or stop the job
    "VALIDATION_SCHEMA" : True,                # Enforce schema checking
    "SUPPORTED_FORMATS" : ["csv", "parquet"],  # Allowed file extension
    "RUN_ENV" : "production"                   # dev / test / production
}

# use case 6: Metadata
# Data about your data
table_metadata = {
    "table_name" : "customers",
    "columns" : {
        "id" : {"type": "integer", "nullable": False},
        "name" : {"type": "string", "nullable": True},
        "age" : {"type" : "integer", "nullable": True},
        "country": {"type": "string", "nullable": True}
    },
    "row_count" : 105320,
    "file_format" : "parquet",
    "last_updated" : "2024-10-01T12:45:00Z",
    "partition_by" : ["country"],
    "tags" : ["pii", "customer-data"]
}