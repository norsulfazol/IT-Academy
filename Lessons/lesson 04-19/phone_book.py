book = {}

def get_book():
    return book

def add(first, last, phone):
    global book
    if (first, last) in book:
        if not phone in book[(first, last)]:
            book[(first, last)].append(phone)
    else:
        book[(first, last)] = [phone]

def delete(first, last, phone):
    global book
    if (first, last) in book:
        if phone in book[(first, last)]:
            book[(first, last)].remove(phone)
            if not book[(first, last)]:
                del book[(first, last)]

def find(token):
    result = []

    for contact, phones in book.items():
        if token in contact[0] or token in contact[1]:
            result.append((contact, phones))
        else:
            for p in phones:
                if token in p:
                    result.append((contact, phones))
    
    return result
