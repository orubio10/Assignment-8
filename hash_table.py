
class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None  

class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size  

    
    def hash_function(self, key: str) -> int:
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size


    def insert(self, key: str, number: str):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

      
        if self.data[index] is None:
            self.data[index] = new_node
            return

        
        current = self.data[index]
        while current:
           
            if current.key == key:
                current.value.number = number
                return
            if current.next is None:
                break
            current = current.next

        
        current.next = new_node

    
    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  

    
    def print_table(self):
        for i in range(self.size):
            current = self.data[i]
            if not current:
                print(f"Index {i}: Empty")
            else:
                chain = []
                while current:
                    chain.append(str(current.value))
                    current = current.next
                print(f"Index {i}: " + " - ".join(chain))



if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()
    print()


    table.insert("John", "909-876-1234")
    table.insert("Marc", "111-555-0002")
    table.print_table()
    print()

    
    contact = table.search("John")
    print("Search result:", contact)
    print()

    
    table.insert("Evan", "111-222-3333")
    table.insert("Michael", "222-333-1111")  
    table.print_table()
    print()

    
    table.insert("Marc", "999-444-9999")
    table.print_table()
    print()

   
    print("Search result:", table.search("Chase"))

(""" The hash table is the right structure for this contact management system because it allows fast searches using a hash function. Instead of checking every name one by one, the hash function quickly finds where a contact belongs in the table. This makes it efficient, because it avoids unnecessary looping or searching like a list would. The speed of a hash table comes from how it directly maps keys to indexes in the array.

To handle collisions, I used separate chaining. Each index of the hash table can hold a small linked list if multiple names hash to the same index. When that happens, a new node is simply added to the chain. If a contact with the same name already exists, the system just updates that persons phone number instead of adding a duplicate. This  keeps the table organized and prevents data from being overwritten incorrectly.

An engineer would choose a hash table when fast access is more important than keeping data in order. Its best for systems that need to search or update information quickly, like phone directories, caches, or databases. However, if the data needs to stay sorted, like in alphabetical order or by rank, a list or tree would work better. Overall, the hash table gives speed and efficiency where organization order doesnt matter as much.
 """)