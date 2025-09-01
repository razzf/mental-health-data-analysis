def categorize_gender(comment):
    """Categorize gender based on keywords in the comment."""
    comment = str(comment).lower()
    
    female_keywords = ['female', 'woman', 'girl', 'femme', 'femmina']
    male_keywords = ['male', 'masculino', 'masculine']
    non_binary_keywords = ['non-binary', 'nonbinary', 'bigender', 'non binary', 'queer', 
                          'gender fluid', 'fluid', 'genderfluid', 'agender', 'they', 'them', 'both']

    if any(keyword in comment for keyword in non_binary_keywords):
        return 'non-binary'
    elif any(keyword in comment for keyword in female_keywords):
        return 'female'
    elif any(keyword in comment for keyword in male_keywords):
        return 'male'
    else:
        return 'other'
