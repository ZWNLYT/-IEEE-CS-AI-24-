def condi_proy():
    event_a = input("Enter event A (separated by commas): ")
    event_a = [int(x) for x in event_a.split(",")]
    event_b = input("Enter event B (separated by commas): ")
    event_b = [int(x) for x in event_b.split(",")]
    if len(event_a) != len(event_b):
        print("Error: Both events must have the same number of occurrences.")
        return None
    both_events = sum([a and b for a, b in zip(event_a, event_b)])
    event_a_occurs = sum(event_a)
    if event_a_occurs == 0:
        print("Error: Event A never occurs.")
        return None
    else:
        cond_prob = both_events / event_a_occurs
    return cond_prob
print(condi_proy())