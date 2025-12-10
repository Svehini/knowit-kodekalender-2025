


def main():
    
    with open("track.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    current_energy = 3000
    total_length = 0
    last_two_actions = [0,0]    # Keep track of energy used last two actions, so we can add this back with pepperkake
    for line in lines:
        for action in line:    
            last_two_actions_sum = sum(last_two_actions)
            last_two_actions.pop(0)
            
            match chr(action):
                case 'S':
                    current_energy -= 5
                    last_two_actions.append(5)
                case 'B':
                    current_energy -= 10
                    last_two_actions.append(10)
                case 'D':
                    current_energy -= 15
                    last_two_actions.append(15)
                case 'P':
                    current_energy += last_two_actions_sum
                    last_two_actions.append(0)
                case 'I':
                    last_two_actions.append(0)
            
            
            # if action == 'S':
            #     current_energy -= 5
            #     last_two_actions.append(5)
            # elif action == 'B':
            #     current_energy -= 10
            #     last_two_actions.append(10)
            # elif action == 'D':
            #     current_energy -= 15
            #     last_two_actions.append(15)
            # elif action == "P":
            #     current_energy += last_two_actions_sum
            #     last_two_actions.append(0)
            # else:
            #     last_two_actions.append(0)
            if current_energy <= 0:
                print(f"Nissen klarte: {total_length} meter")
                return
            total_length += 10
main()