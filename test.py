
#participant only on last and never participated before

participation_data=[['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
     ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'] 
     ,['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'], 
     ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'], 
     ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
     ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam','Amit']]

all_participants = participation_data[-1]
single_participants = set()
for day_participants in participation_data[:-1]:
        # all_participants.update(day_participants)
        for participant in day_participants:
            if participant in all_participants:
                all_participants.remove(participant)
            else:
                single_participants.add(participant)
print(all_participants)