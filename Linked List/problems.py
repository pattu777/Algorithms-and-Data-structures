from linkedlist import LinkedList, Node

def merge_lists(ll1, ll2):
    '''Merge two sorted linked lists.'''
    if ll1.get_head() is None:
        return ll2
    elif ll2.get_head() is None:
        return ll1
    else:
        head1 = ll1.get_head()
        head2 = ll2.get_head()
        ll = LinkedList()

        while head1 is not None and head2 is not None:
            if head1 is not None and head1.data < head2.data:
                ll.insert_at_head(head1.data)
                head1 = head1.next_node
            elif head2 is not None and head1.data > head2.data:
                ll.insert_at_head(head2.data)
                head2 = head2.next_node

        return ll