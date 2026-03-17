full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):

    if type(character_name) != str:
        return "The character name should be a string" 
    elif len(character_name) == 0:
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    elif " " in character_name:
        return "The character name should not contain spaces"
    elif type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma <  1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    elif (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"
    else:
        
        strength_full_dot = strength * full_dot
        strength_empty_dot = (10 - strength) * empty_dot
        strength_dot = strength_full_dot + strength_empty_dot
        
        
        intelligence_full_dot = intelligence * full_dot
        intelligence_empty_dot = (10 - intelligence) * empty_dot
        intelligence_dot = intelligence_full_dot + intelligence_empty_dot

        charisma_full_dot = charisma * full_dot
        charisma_empty_dot = (10 - charisma) * empty_dot
        charisma_dot = charisma_full_dot + charisma_empty_dot

        return f"{character_name}\nSTR {strength_dot}\nINT {intelligence_dot}\nCHA {charisma_dot}"


print(create_character("ren", 4, 2, 1))
