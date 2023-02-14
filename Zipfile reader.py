# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:51:17 2023

@author: KirthikRoshan
"""

import zipfile
import re

def extract_jobs_completed(zip_file):
    # Open the zip file
    with zipfile.ZipFile(zip_file, 'r') as z:
        # Extract the names of all files in the zip file
        filenames = z.namelist()

        # Keep a running sum of the total jobs completed
        total_jobs = 0

        # Loop through each file in the zip file
        for filename in filenames:
            # Read the contents of the file
            with z.open(filename) as f:
                content = f.read().decode('utf-8')
                # Split the contents of the file into lines
                lines = content.splitlines()

                # Loop through each line in the file
                for line in lines:
                    # Check if the line starts with "Jobs Completed"
                    if line.startswith("Jobs Completed"):
                        # Extract the number associated with this line
                        match = re.search(r'\d+', line)
                        if match:
                            jobs = int(match.group())
                            total_jobs += jobs
    return total_jobs

# Call the function with the name of the zip file
total = extract_jobs_completed("Jobs_Completed_log.zip")

# Print the total number of jobs completed
print("Total Jobs Completed:", total)
