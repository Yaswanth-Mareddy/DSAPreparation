import random

# used idea from: https://towardsdatascience.com/python-linked-lists-c3622205da81
# Every node has data and next pointer to another node
class Node:
    
    # constructor
    def __init__(self,data):
        self._data=data
        self._next=None
    
    # setter mutator for data
    def set_data(self,data):
	    self._data=data
	    
    # getter accessor for data
    def get_data(self):
	    return self._data

    # setter mutator for next
    def set_next(self,next):
	    self._next=next
	    
    # getter accessor for next
    def get_next(self):
	    return self._next
	    
# used idea from: https://towardsdatascience.com/python-linked-lists-c3622205da81	    
# LinkedList has head and tail nodes
class LinkedList:
    
    # constructor
    def __init__(self):
        self._head=None
        self._tail=None
        
    # setter mutator for head 
    def set_head(self,head):
        self._head=head
    
    # getter accessor for head
    def get_head(self):
        # if linked list is empty return -1
        if(self.is_empty()):
            return Node(-1)
        return self._head
        
    # setter mutator for tail
    def set_tail(self,tail):
        self._tail=tail
    
    # getter accessor for tail
    def get_tail(self):
        # if linked list is empty return -1
        if(self.is_empty()):
            return Node(-1)
        return self._tail
        
    # method to append node to linked list
    def append_node(self,node):
        # if linked list is empty then add new node to head and tail
        if(self.is_empty()):
            self._head=node
            self._tail=node
        #if linked list contains some nodes then append new node to tail node
        else:
            self._tail.set_next(node)
            # move tail node to updated list tail node
            self._tail=self._tail.get_next()
        
    # method to iterate all nodes in the linked list
    def get_list(self):
        # check if linked list head is empty, if yes return "No items"
        if(self.is_empty()): 
            return "No items"
        # else get all elements from head node as string
        str_get_list=""
        head_node=self._head
        # iterate from head node till head node next is None
        while(head_node!=None):
            str_get_list+=str(head_node.get_data())
            str_get_list+=" "
            head_node=head_node.get_next()
        return str_get_list[:-1]
        

    # method to check if linked list is empty or not
    def is_empty(self):
        # if linked list is empty i.e head is None return true else false
        return self._head==None
    
    # used idea from: https://www.programiz.com/dsa/selection-sort    
    # method to sort linked list using selection sort algorithm    
    def sort_list(self):
        # sort list starting from head till end
        current_node=self._head
        while(current_node!=None):
            # for every iteration, initially current_node will be minimum_node
            minimum_node=current_node
            # for every iteration select minimum_node from the current_node right sub list
            right_node=current_node.get_next()
            while(right_node!=None):
                # if current minimum_node data is greater than current_node data then update minimum_node with current_node
                if(minimum_node.get_data()>right_node.get_data()):
                    minimum_node=right_node;
                right_node=right_node.get_next()
            # swap current_node data with minimum_node
            self.swap_node_data(current_node,minimum_node)
            current_node=current_node.get_next()
            
            
    #a function to swap two nodes data using temporary variable 
    def swap_node_data(self,node1,node2):
        temp=node1.get_data()
        node1.set_data(node2.get_data())
        node2.set_data(temp)

# used idea from: https://www.programiz.com/python-programming/user-defined-exception      
# class for InvalidNumber custom exception
class InvalidNumber(Exception):
    pass

# main solution class for the problem statement
class Solution:
    # method to create linked list with random values and sort it
	def main(self):
	    # read input from console
		user_input=input("Please, enter the number of nodes: ")
		# validate user_input, if user_input is invalid then read valid user_input
		user_input=self.validate_user_input(user_input)
		# generate linked_list with random values
		linked_list=self.generate_linked_list(user_input)
		# display linked_list values
		print("Unsorted list: "+linked_list.get_list())
		# display linked_list head node data 
		print("Head data: ",linked_list.get_head().get_data())
		# display linked_list tail node data
		print("Tail data: ",linked_list.get_tail().get_data())
		# sort linked_list using selection sort algorithm
		linked_list.sort_list()
		# display sorted linked_list values
		print("Sorted list: "+linked_list.get_list())
		# display sorted linked_list head node data
		print("Head data: ",linked_list.get_head().get_data())
		#display sorted linked_list tail node data
		print("Tail data: ",linked_list.get_tail().get_data())
	
	# method to generate linked list with random values
	def generate_linked_list(self,user_input):
	    # create linked_list 
	    linked_list=LinkedList()
	    # generate user_input number of random values
	    for random_number in range(user_input):
	        # generate random_number within(0,100) using random library, randint function
	        random_number=random.randint(0,100)
	        # generate random_node with random_number as data
	        random_node=Node(random_number)
	        # append random_number to linked_list
	        linked_list.append_node(random_node)
	    return linked_list
    
    # method to validate whether user_input is a valid positive number
	def validate_user_input(self,user_input):
	    # run until user_input is valid
		while(type(user_input)!=int):
		    # try to convert user_input to int, if conversion is failed then raise ValueError
		    try:
		        user_input=int(user_input)
		        # if user_input is invalid number i.e negative number raise InvalidNumber exception
		        if(user_input<0):
		            raise InvalidNumber()
		    except ValueError:
		        # read input again from console
		        user_input=input("Please, enter correct value for number of nodes: ")
		    except InvalidNumber:
		        # read input again from console
		        user_input=input("Please, enter correct value for number of nodes: ")
		return user_input

# create object for solution		
solution=Solution()
# run main method of solution
solution.main()
