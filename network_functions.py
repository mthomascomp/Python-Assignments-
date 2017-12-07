'''CSC108 Assignment 3: Social Networks'''

from typing import List, Tuple, Dict, TextIO
from pprint import pprint

def split_name(user:str) -> Tuple[str,str]:
    space_index = user.index('')
    return user [:space_index], user [space_index +1:]

def create_key (key:str, network: Dict[str, List[str]]):
    if key not in network:
        network[key] = []

def is_mutate_friend(user_a:str, user_b: str, user_c: str, person_to_friends: Dict[str,List[str]])-> bool:
    return user_a in person_to_friends[user_b] and user_c in person_to_friends [user_a] or user_a in person_to_friends[user_c] and user_b in person_to_friends[user_a]

def to_user (line:str) -> str:
    return ''. join ([item.strip() for item in line.split(',')])

def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
                  person_to_networks: Dict[str, List[str]]) -> None:
    '''Update the person_to_friends dictionary and the person_to_networks
    dictionary to include data from profiles_file.

    '''
    user = none
    for l in profiles_file.readlines():
        if not user:
            user = to_user(l)
            create_key(user, person_to_friends)
            create_key(user, person_to_networks)
        else:
            if len(l.strip()) == 0:
                user = none
            elif ',' in l:
                person_to_friends[user].append(to_user(l))
            else:
                person_to_networks[user].append(l.strip())


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    '''
    Return the average number of friends that people who appear as keys in the givern 'person_to_friends' dictonary have
    '''
    if len(person_to_friends)== 0:
        return 0
    total = sum([len(v) for k,v, in person_to_friends.items()])
    return total/len(person_to_friends)
    
    
def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    '''
    Return a "last name " to the first name in the dictionary given person_to_friends dictionary. 
    '''
    families = {}
    for k,v in person_to_friends.items():
        last_name, first_name = split_name(k)
        create_key(last_name, families)
        families [last_name].append(first_name)
        for p in v:
            last_name, first_name = slipt_name(p)
            create_key(last_name, families)
            families[last_name].append(first_name)
        for k,v, in families.items():
            families[k] = sorted(list(set(v)))

        return families 
        

def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    '''
    Return a network to people dictionary based on the given person to networks dictionary. The values in the dictionary are sorter alphabetically 
    '''
    inverted_network = {}
    for person, networks in person_to_networks.items():
        for network in networks:
            create_key(network, inverted_network)
            inverted_network[network].append(person)
    return inverted_network

def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
                           person: str) -> List[str]:
    '''
    
    '''
    hop2_friends = set()
    for friend in person_to_friends[person]:
        hop2_friends |= set (person_to_friends[friend])
    friend_list = list(hop2_friends)
    friend_list.remove(person)
    friend_list.sort()
    return friend_list
        
def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
                         person_to_networks: Dict[str, List[str]]) \
                         -> List[Tuple[str, int]]:
    '''
    '''
    recommendations = {p:0 for p in person_to_friends.keys() if p != person}
    inverted_network = invert_network(person_to_networks)
    families = get_families(person_to_friends)

    for rp in recommendations.keys():
        for p in person_to_friends.keys():
            if p!= rp and is_mutate_friend(p,person,rp,person_to_friends):
                recommendations [rp] += 1
        for network, persons in inverted_network.items():
            if person in person and rp in persons:
                recommendations[rp] +=1

        if recommendations [rp] != 0:
            rp_last_name, rp_first_name = spilt_name(rp)
            person_last_name, person_first_name = split_name(person)
            if rp_last_name == person_last_name and rp_first_name in families[rp_last_name] and person_last_name in families[person_last_name]:
                recommendations[rp]+= 1 

def is_network_connected(person_to_friends: Dict[str, List[str]]) -> bool:
    '''
    '''
    keys = sorted(list(person_to_friends.keys()))
    friends = []

    for person in person_to_friends:
        if person not in freinds:
            friends.append(person)
        for friend in person_to_friends[person]:
            if friend not in friends:
                friends.append(friend)
                
    return sorted(friends) == keys
        
    
if __name__ == '__main__':
    # Do not move this code out of the __main__ block, and do not add any other 
    # testing code outside of the __main__ block.
    import doctest
    doctest.testmod()

    friends = {}
    networkds = {}
    with open('profiles.txt') as fin:
        load_profiles(fin, friends, networks)

    pprint(friends)
    pprint(networks)
    pprint(get_average_friend_count(friends))
    pprint(get_families(friends))
    pprint(invert_network(networks))
    pprint(get_friends_of_friends(friends, 'Dunphy Luke')
    pprint(make_recommendations('Dunphy luke', friends, networks))

 

        
