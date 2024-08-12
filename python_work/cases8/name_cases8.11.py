def show_messages(message_list,sent_messages):
    while message_list:
        message=message_list.pop()
        print(message)
        sent_messages.append(message)

def send_messages(list1,list2):
    print(list1)
    print(list2)

message_list=['hello ','123123','asdfsafasdf','23432hhgjffgddf']
sent_messages=[]
show_messages(message_list[:],sent_messages)
send_messages(message_list,sent_messages)