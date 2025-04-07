def how_many(content):
    
    
    
    return len(content.split())

def characters_count(content):
    count_i = {}
    for i in content:
        i = i.lower()
        if i in count_i:
            count_i[i] += 1
        else:
            count_i[i] = 1 
    return count_i
    
def pretty(characters_count):
    pretty_list = []
    for letter, count in characters_count.items():
        dictionary = {"letter": letter, "count": count}
        pretty_list.append(dictionary)
    
    def sort(dict):
        return dict["count"]
	
    pretty_list.sort(reverse=True, key=sort)
    return pretty_list



