# Anonfiles Hunter

This code is used to query the Anonfiles API and check the status of files on Anonfiles. Here are the main things it does:

 1. It verifies the TOR network is enabled by making a request to check.torproject.org. This is done to ensure requests go through the TOR network for anonymity.

 2. It makes a request to anonfiles.com to check the server status.

 3. It makes an API request to the Anonfiles API at https://api.anonfiles.com to check the API status and status code.

 4. It defines a function get_file_info_api() to make a request to the Anonfiles API and get information about a file with a given file ID.

 5. It defines a function check_file_exists() to check if a file with a given file ID exists on Anonfiles using the get_file_info_api() function.

 6. It defines a function generate_ids() to generate random file IDs of a given length.

 7. It defines a main() function that:

 - Parses command line arguments to get a file ID or output file.
 - Checks if a file with the given file ID exists.
 - Generates 100 random file IDs and checks which exist, writing the existing IDs to the output file.

 So in summary, this code acts as a tool to check the status of Anonfiles servers, API and files. It can be used to find existing files on Anonfiles by their ID, or generate random file IDs to discover new files.
 
The probability of catching the right link is small, but still it is

# Installation

```
git clone https://github.com/Superdecrypt/anonfiles-hunter
```
```
cd anonfiles-hunter
```
```
pip install -r requirements.txt
```
# Usage

how you can use this tool from the command line:

1- Check the status of a single file ID:

`python script.py -t <file_id>`

This will check if a file with the given file ID exists on Anonfiles and print the file details if it exists.

Example:
```
python script.py -t abcdefghij
File name: myimage.png  
File size: 512 KB
File URL: http://anonfiles.com/abcdefghij
```

2- Generate file IDs and check which exist:

`python script.py -o results.txt`

This will generate 100 random 10 character file IDs and check which exist on Anonfiles, writing the existing file IDs to `results.txt`.

Example:
```
File ID abcdefghij exists on Anonfiles
File ID zyxwvutsrq does not exist on Anonfiles 
...
...
```

The `results.txt` file will contain a list of existing file IDs:

```
abcdefghij
mnopqrxyz1
...
```

You can modify the number and length of generated file IDs by passing arguments to the `generate_ids()` function.

So in summary, you can pass either:

- A `-t` argument to check a single file ID 
- An `-o` argument to generate and check multiple file IDs, writing the existing ones to an output file.
