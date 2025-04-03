import os
import subprocess
import shlex

def process_file(input_filename, output_filename):
    try:
        # Step 1: Read the content of the input file
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()

        # Step 2: Separate each word by space
        words = content.split()

        # Step 3 & 4: Read each <word>.hamnosys file and concatenate their content
    # Open the output file once before writing
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            # Step 1: Append the initial quote
            output_file.write("\"")
            # Step 2: Iterate through the words and write each one with a space before it
            first_word = True  # Flag to check if it's the first word
            for word in words:
                hamnosys_filename = f"hamnosys/{word}.hamnosys"
                if os.path.exists(hamnosys_filename):
                    with open(hamnosys_filename, 'r', encoding='utf-8') as hamnosys_file:
                        hamnosys_content = hamnosys_file.read().strip()
                        # Only add a space before appending if it's not the first word
                        if not first_word:
                            output_file.write(" ")
                        # Write the content from the hamnosys file
                        output_file.write(hamnosys_content)
                        first_word = False  # After the first word, we add spaces before subsequent words
            # Step 3: Append the original content enclosed in ""
            output_file.write("\"")
            if not first_word:  # Make sure we don't start with a space
               output_file.write(" ")
            
            output_file.write(f'"{content}"')
        
        print(f"Processing completed. Output written to {output_filename}")


        #Step 6: Read output file and pass content to another script
        with open(output_filename, 'r', encoding='utf-8') as output_file:
            output_content = output_file.read().strip()
        print(f"content: {output_content}")
        #./HamNoSys2SiGML/Original/HamNoSys2SiGML.py
        
        #Call another script with the output content as an argument
        cur_dir = os.getcwd()
        os.chdir("HamNoSys2SiGML/Original/")
        os.system(f"python HamNoSys2SiGML.py {output_content} > ../../sigml/abc.sigml")
        os.chdir(cur_dir)
        #command=["python", "HamNoSys2SiGML/Original/HamNoSys2SiGML.py", f"{output_content}", f'"{content}"']
        #print(f"command {command}")
        #result = subprocess.run(["python", "./HamNoSys2SiGML/Original/HamNoSys2SiGML.py", print(f"{output_content}")], capture_output=True, text=True)
        
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_filename = "demo/input.txt"  # Change to your actual input file
output_filename = "demo/input_to_h2s"  # Change to your desired output file
process_file(input_filename, output_filename)

