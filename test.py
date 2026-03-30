# import requests
# import time
# import os
# from json import dumps
# from dotenv import load_dotenv

# load_dotenv()

# # Trigger your workflow (already done, but here for context)
# url_trigger = "https://api.mindpal.io/api/v2/workflow/run?workflow_id=6914b3a9e2c54943480cbc97"
# headers = {
#     "accept": "application/json",
#     "x-api-key": os.getenv("MINDPAL_API"),
#     "Content-Type": "application/json"
# }

# # Use the run_id from your previous output
# run_id = "69ca2fd8cc8393c9e0ba2cc2" 

# # Correct polling URL
# url_result = f"https://api.mindpal.io/api/workflow-run-result/retrieve-by-id?run_id={run_id}"

# print(f"Waiting for workflow {run_id} to complete...")

# while True:
#     response = requests.get(url_result, headers=headers)
#     data = response.json()
    
#     # Check current status
#     status = data.get('status', 'processing')
#     outputs = data.get('workflow_run_output', [])
    
#     print(f"Status: {status} | Completed Nodes: {len(outputs)}")

#     if status == 'completed':
#         print("\n🎉 WORKFLOW COMPLETE!")
#         # Print the final output (the last node is usually the final result)
#         if outputs:
#             final_result = outputs[-1]['content']
#             print("--- FINAL OUTPUT ---")
#             print(final_result)
#         break
#     elif status == 'failed':
#         print("❌ Workflow failed.")
#         print(data)
#         break
#     else:
#         # Wait before checking again
#         time.sleep(5)





text = ""

with open('data.txt', 'r', encoding="utf-8") as f:
    for line in f:
        text+=line

print(text)