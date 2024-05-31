import pandas as pd
from django.shortcuts import render
import os
import random as random
import time
def index(request):
    # Get the absolute path to the CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'conn.csv')

    # Check if the file exists
    res=[]
    if os.path.exists(csv_file_path):
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        x=df.iloc[0].tolist()[5:]
        

        for i in range(0,20,2):
            ans=[]
            ans.append(x[i])
            ans.append(x[i+1])
            timestamp = int(random.randint(0, 100))
            print(timestamp)

            # Create the Unsplash URL with the timestamp
            image_url = f"https://source.unsplash.com/300x200/?newsa&{timestamp}"
            ans.append(image_url)
            res.append(ans)
            

        # Print the first few rows (for debugging)
    else:
        print("CSV file not found at:", csv_file_path)

    print(type(res[0]))

    context = {
        'DATA':  res,
        'userid':df.iloc[0].tolist()[1],
        'name':df.iloc[0].tolist()[2],
        'email':df.iloc[0].tolist()[3],
        'interests':df.iloc[0].tolist()[4]

    }

    return render(request, 'home.html', context)
