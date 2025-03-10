"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_address_ind_mp = {}

        new_ind_address_mp = {}

        dummy = Node(-1)

        temp = head

        ind = 0

        while temp :

            old_address_ind_mp[temp] = ind

            ind += 1

            temp = temp.next
        
        temp = head

        prev = dummy

        ind = 0

        while temp:

            new_node = Node(temp.val)

            new_ind_address_mp[ind] = new_node

            ind += 1

            if prev :

                prev.next = new_node

            prev = new_node

            temp = temp.next
        
        temp = head

        new_temp = dummy.next

        while temp:

            if temp.random == None:

                new_temp.random = None
            
            else:

                
                pos = old_address_ind_mp[temp.random]

                new_random_node_add = new_ind_address_mp[pos]

                new_temp.random = new_random_node_add
            
            temp = temp.next
        
            new_temp = new_temp.next
        
        copy_head = dummy.next

        return copy_head


        







