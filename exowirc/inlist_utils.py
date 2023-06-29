import configparser
import ast

def parse_inlist(file):
	config = configparser.ConfigParser()
	config.optionxform = str
	config.read(file)
	params = {}
	for section in config.sections():
		params[section] = {}
		for key, value in config.items(section):
			try:
				params[section][key] = ast.literal_eval(value)
			except (SyntaxError, ValueError):
				params[section][key] = value  # keep as string if can't be parsed
		
	return params