import pandas as pd
import os

# Read CSV file
data = pd.read_csv("/storage/emulated/0/CODE/drug_data.csv")
history_file = "search_history.csv"

if os.path.exists(history_file):
    history = pd.read_csv(history_file)
else:
    history = pd.DataFrame(columns=["Drug", "Severity"])

# ------------------ SEARCH DRUG ------------------

def search_drug():
    global history
    drug = input("\nEnter Drug Name: ")

    result = data[data["Drug"].str.lower() == drug.lower()]

    if result.empty:
        print("\nDrug not found.")
        return

    severity = input("Enter Severity (All/Mild/Moderate/Severe/Rare): ").capitalize()

    if severity != "All":
        result = result[result["Severity"] == severity]

    if result.empty:
        print("\nNo ADR found with this severity.")
        return

    print("\n========== ADR SEARCH RESULT ==========")
    print("Drug :", drug.title())
    print("---------------------------------------")

    count = 1
    for index, row in result.iterrows():
        print(f"{count}. ADR      : {row['ADR']}")
        print(f"   Severity : {row['Severity']}")
        print()
        count += 1

    print("Total ADRs Found:", len(result))
    print("=======================================")
    global history

    new_record = pd.DataFrame({
        "Drug": [drug],
        "Severity": [severity]
    })

    history = pd.concat([history, new_record], ignore_index=True)
    history.to_csv(history_file, index=False)
    new_record = pd.DataFrame({
        "Drug": [drug],
        "Severity": [severity]
    })

    history = pd.concat([history, new_record],       ignore_index=True)
    history.to_csv(history_file, index=False)

# ------------------ VIEW ALL DRUGS ------------------

def view_all_drugs():

    print("\n========== DRUG DATABASE ==========\n")
    print(data.to_string(index=False))
    print("\nTotal Records:", len(data))


# ------------------ DRUG STATISTICS ------------------

def drug_statistics():

    print("\n========== DRUG STATISTICS ==========\n")

    print("Total Drugs :", data["Drug"].nunique())
    print("Total ADR Records :", len(data))

    print("\nADR Severity Count:\n")
    print(data["Severity"].value_counts())

    print("\n====================================")
def view_search_history():

    print("\n========== SEARCH HISTORY ==========\n")

    if history.empty:
        print("No search history found.")
    else:
        print(history.to_string(index=False))

# ------------------ MAIN MENU ------------------

while True:

    print("\n======================================")
    print(" AI PHARMACOVIGILANCE SYSTEM")
    print("======================================")
    print("1. Search Drug ADR")
    print("2. View All Drugs")
    print("3. View Drug Statistics")
    print("4. View Search History")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        search_drug()

    elif choice == "2":
        view_all_drugs()

    elif choice == "3":
        drug_statistics()

    elif choice == "4":
        view_search_history()

    elif choice == "5":
        print("\nThank you for using the system.")
        break
       
        

    else:
        print("\nInvalid Choice!")