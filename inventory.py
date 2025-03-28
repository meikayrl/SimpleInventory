# (c) 2025 Full Name 
# A program to parse and manage a CSV file. 
 
import os 
import csv 


def write_to_file(filepath, data=[]): 
    with open(filepath, "w", newline="") as file: 
        writer = csv.writer(file) 
        writer.writerows(data)
        
def read_file(filepath): 
    with open(filepath, "r", newline="") as file: 
        records = csv.reader(file) 
        return [record for record in records]
        
def main(): 
    datapath = "data" 
    os.makedirs(datapath, exist_ok=True)
    
    filepath = f"{datapath}/inventory.csv" 
    if not os.path.exists(filepath): 
        write_to_file(filepath)

    records = read_file(filepath) 
    count = len(records) 
    
    print("[Inventory Recorder]") 
    print(f"You have {count} items in your inventory.") 
    print("\nNOTE: Hit <Enter> w/o input to end the program.")
    
    while True: 
        item = input("\nEnter a new item: ").strip() 
        if item == "": 
            break 
 
        price = float(input(f"Enter '{item}' price (P): ")) 
        quantity = float(input(f"Enter '{item}' stock on hand: ")) 
 
        records.append([item, price, quantity])
        
    print("\nSaving to file...") 
    write_to_file(filepath, records) 
     
    print("\n[Inventory]") 
    print("Item\tPrice\tQuantity") 
    print("----\t-----\t--------") 
    for record in records: 
        print("\t".join(map(str, record))) 
        
if __name__ == "__main__": 
    main()