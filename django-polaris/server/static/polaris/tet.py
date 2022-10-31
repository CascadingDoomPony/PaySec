import toml

#toml_dict = toml.loads(toml_string)  # Read from a string

input_file_name = "local-stellar.toml"
with open(input_file_name) as toml_file:
    toml_dict = toml.load(toml_file)

print(toml_dict)