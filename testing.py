
def get_every_day_participants(participation_data):
    # Initialize a set with the first day participants
    every_day_participants = set(participation_data[0])
    
    # Iterate through each subsequent day's participants
    for day_participants in participation_data[1:]:
        every_day_participants.append(day_participants)
    
    return list(every_day_participants)

def get_only_once_participants(participation_data):
    all_participants = set()
    single_participants = set()
    
    # Collect all participants and       identify single-time participants
    for day_participants in participation_data:
        all_participants.update(day_participants)
        for participant in day_participants:
            if participant in all_participants:
                all_participants.remove(participant)
            else:
                single_participants.add(participant)
    
    return list(single_participants)

def get_first_day_only_participants(participation_data):
    first_day_participants = set(participation_data[0])
    
    # Remove participants who appear on any subsequent day
    for day_participants in participation_data[1:]:
        first_day_participants.difference_update(day_participants)
    
    return list(first_day_participants)
quiz_participation = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole'],
    ['Brad', 'Walter', 'Sam', 'Krish', 'Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer', 'Desmond', 'Harry', 'Nicole', 'Sam']
]
# Example usage:
every_day = get_every_day_participants(quiz_participation)
only_once = get_only_once_participants(quiz_participation)
first_day_only = get_first_day_only_participants(quiz_participation)

print("Participants who participated every day:", every_day)
print("Participants who participated only once:", only_once)
print("Participants who participated on the first day and never participated again:", first_day_only)
