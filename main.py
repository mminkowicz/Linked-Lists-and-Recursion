from linked_list import LinkedList

if __name__ == "__main__":

    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert sample employee IDs
    ll.insert_at_front(101)
    ll.insert_at_front(202)
    ll.insert_at_front(303)
    ll.insert_at_end(404)

    # 3) Display the list
    print("Linked List:")
    ll.display()

    # 4) Recursive sum
    total = ll.recursive_sum()
    print(f"\nSum of all IDs: {total}")

    # 5) Recursive search
    search_target = 202
    found = ll.recursive_search(search_target)
    print(f"\nSearch for {search_target}: {'Found' if found else 'Not Found'}")

    missing_target = 999
    found_missing = ll.recursive_search(missing_target)
    print(f"Search for {missing_target}: {'Found' if found_missing else 'Not Found'}")

    # 6) Recursive reverse
    ll.recursive_reverse()
    print("\nReversed Linked List:")
    ll.display()
