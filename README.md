# Final project of the Python course by Chernihivske team (team 12)

## This repository contains a **Python-based assistant** bot that performs the following functions:

1. **Contact Management**: Allows you to store contacts with names, addresses, phone numbers, emails, and birthdays in a contact book.
2. **Birthday Tracking**: Displays a list of contacts whose birthdays are within a specified number of days from the current date.
3. **Data Validation**: Verifies the correctness of phone numbers and emails when creating or editing a contact, notifying the user in case of incorrect input.
4. **Contact Search**: Enables searching through the contacts in the contact book.
5. **Editing and Deleting Contacts**: Provides the ability to edit and delete entries in the contact book.
6. **Note Management**: Allows you to store, edit, and delete text-based notes.
7. **Note Search**: Offers functionality to search through saved notes. 

This bot is designed for efficient management of contacts and notes, focusing on user convenience and ensuring data accuracy.

## Project requirements

### GIT
```https://git-scm.com/```

### Python
```https://www.python.org/```

## Project setup guide

#### SSH
``git clone git@github.com:DmytroShirobokov92/final-project-team-12.git``

#### HTTPS
``git clone https://github.com/DmytroShirobokov92/final-project-team-12.git``

#### IMPORTANT Setup path for project
`` EXAMPLE: how to set correct path for project, markd main folder as Source Root, Resourse Root and Namespace package using PyCharm``
![img.png](img.png)``git clone https://github.com/DmytroShirobokov92/final-project-team-12.git``

## Bot commands description

#### Start bot
```hello```

#### Add new contact 
```ДОПОЛНИТЬ ПОСЛЕ ЗАВЕРШЕНИЯ ЗАДАЧИ ДОБАВЛЕНИЯ ЮЗЕРА.```

#### Change contact info
```ДОПОЛНИТЬ ПОСЛЕ ЗАВЕРШЕНИЯ ЗАДАЧИ ДОБАВЛЕНИЯ ЮЗЕРА.```

#### Show user phone
```phone {user_name}```

#### Show all users list
```all```

#### Add birthday to user
```add-birthday {user_name} {birthday_date}```

#### Show user birthday date
```show-birthday {user_name}```

#### Show upcoming users birthdays related days ahead 
```birthdays {days_related}```

``F.E. if today 13.08 -- (birthdays 5) return users birthdays list 13.08-18.08 dates in format '13.08': 'foo, bar', '14.08': 'user_3'``

#### Modify or create new note
```add-note | modify-note```

#### Shows list of all notes
```all-notes```

#### Search note by anu word on title or body
```search-note```

#### Remove note by note title
```remove-note```

#### Exit
```close | exit```

#### The bot automatically saves data on your system