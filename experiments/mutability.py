filename = ["1.raw_data.txt" , "2.raw_good.txt", "3.raw_collection.txt"]

for filename in filename:
    filename = filename.replace('.' , '-' , 1)
    print(filename)
